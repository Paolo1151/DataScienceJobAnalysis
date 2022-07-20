import os
import re
from enum import Enum

import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from config import settings

class Page(Enum):
    INTRODUCTION = 1
    ANALYSIS = 2
    CONCLUSION = 3


class Renderer():
    def __init__(self):
        self.df = pd.read_csv(os.path.join(settings.DATA_PATH, 'ds_salaries_processed.csv'))
        self.iso_cc = pd.read_csv(os.path.join(settings.DATA_PATH, 'iso_cc.csv'))
        self.df = self.df.merge(self.iso_cc, how='left', left_on='employee_residence', right_on='Code')
        self.netrender = NetworkRenderer(self.df)

    def render(self, page_str: str):
        page = Page[page_str.upper()]
        if page == Page.INTRODUCTION:
            self._render_home()
        elif page == Page.ANALYSIS:
            self._render_analysis()
        elif page == Page.CONCLUSION:
            self._render_conclusion()
        else:
            raise Exception("Unknown page")

    def _render_home(self):
        st.title("An Analysis of Data Science Jobs and Data Scientist Migration Patterns")
        with open(os.path.join(settings.CONTENT_PATH, "background.md"), "r") as f:
            md = f.read().split(r"{METHOD PICTURE}")
        st.markdown(md[0])
        
        method = Image.open(os.path.join(settings.IMAGE_PATH, "method.jpg"))
        st.image(method, width=600)

        st.markdown(md[1])

    def _render_analysis(self):
        st.title("Analysis")

        with open(os.path.join(settings.CONTENT_PATH, "analysis.md"), "r") as f:
            md = re.split(r"{Interactive Data Explorer \d}", f.read())

        st.markdown(md[0])
        eda = Image.open(os.path.join(settings.IMAGE_PATH, 'q1.jpg'))
        st.image(eda)
        st.markdown(md[1])
        self._render_dataexplorer_2()
        st.markdown(md[2])

    def _render_dataexplorer_2(self):
        unique_residence = self.df['Country Name'].unique().tolist()
        
        is_reverse = st.checkbox("Generate Network going to a Country?", value=False)

        residence = st.selectbox(
            'Employee Residence',
            unique_residence
        )

        iso_cc_residence = self.iso_cc[self.iso_cc['Country Name'] == residence]['Code'].values[0]
        
        if is_reverse:
            title = f"Network of Migration of Data Scientists to {residence} from other Countries"
        else:
            title = f"Network of Migration of Data Scientists from {residence} to other Countries"

        curr_fig = self.netrender.graph_network(
            iso_cc_residence,
            title, 
            reverse=is_reverse
        )
        
        st.pyplot(fig=curr_fig)


    def _render_conclusion(self):
        st.title("Conclusion")

        with open(os.path.join(settings.CONTENT_PATH, "conclusion.md"), "r") as f:
            st.markdown(f.read())

    @staticmethod
    def get_page_list():
        return list(map(lambda x: x.name.capitalize(), Page))


class NetworkRenderer():
    def __init__(self, df):
        self._create_graph_dict(df)
        self._create_reverse_graph_dict(df)

    def _create_graph_dict(self, df):
        init_residence = dict(zip(df['employee_residence'].unique(), [dict() for i in range(df['employee_residence'].nunique())]))
        for i, row in df.iterrows():
            if row['company_location'] in init_residence[row['employee_residence']]:
                init_residence[row['employee_residence']][row['company_location']] += 1
            else:
                init_residence[row['employee_residence']][row['company_location']] = 1

        to_delete = []
        residence_seqs = {}
        for employee_residence, counts in init_residence.items():
            total_cnts = sum(counts.values())

            if total_cnts == 1:
                to_delete.append(employee_residence)

            for country, count in counts.items():
                counts[country] = count / total_cnts
            residence_seqs[employee_residence] = counts

        self.residence_seq = residence_seqs

    def _create_reverse_graph_dict(self, df):
        init_residence = dict(zip(df['company_location'].unique(), [dict() for i in range(df['company_location'].nunique())]))
        for i, row in df.iterrows():
            if row['employee_residence'] in init_residence[row['company_location']]:
                init_residence[row['company_location']][row['employee_residence']] += 1
            else:
                init_residence[row['company_location']][row['employee_residence']] = 1

        to_delete = []
        residence_seqs = {}
        for employee_residence, counts in init_residence.items():
            total_cnts = sum(counts.values())

            if total_cnts == 1:
                to_delete.append(employee_residence)

            for country, count in counts.items():
                counts[country] = count / total_cnts
            residence_seqs[employee_residence] = counts

        self.reverse_residence_seq = residence_seqs
    
    def graph_network(self, residence, title, reverse=False):
        fig = plt.figure(figsize=(6, 6))

        graph_dict = self.reverse_residence_seq if reverse else self.residence_seq 

        G = nx.Graph()
        destinations = graph_dict[residence]
        edge_labels = {}
        for i, (country, prob) in enumerate(destinations.items()):
            if reverse:
                G.add_edge(country, residence, weight=prob)
                edge_labels[(country, residence)] = prob
            else:
                G.add_edge(residence, country, weight=prob)
                edge_labels[(residence, country)] = prob
        node_sizes = []
        node_colors = []
        for u, ddict in G.nodes(data=True):
            if u == residence:
                node_colors.append('r')
            else:
                node_colors.append('b')
            node_sizes.append(500)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size=node_sizes, node_color=node_colors, font_color='white', with_labels=True)
        for u, v, ddict in G.edges(data=True):
            node1_x, node1_y = pos[u]
            node2_x, node2_y = pos[v]
            x_mid = (node1_x + node2_x) / 2
            y_mid = (node1_y + node2_y) / 2
            plt.text(x_mid, y_mid, str(round(ddict['weight'],4)), bbox=dict(facecolor='white', edgecolor='black'), ha='center', va='center')
        
        plt.title(title)

        return fig



