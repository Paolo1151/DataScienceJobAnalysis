import typing

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

from analysis.analytics import AnalyticsObject
from analysis.analytics import AnalyticsProcessorFactory
from analysis.analytics import AnalyticsAnalyzer
from analysis.analytics import AnalyticsGrapher


class MarkovObject(AnalyticsObject):
    def __init__(self):
        super().__init__("Markov")

    def fit(self, df: pd.DataFrame) -> None:
        init_residence = dict(zip(df['employee_residence'].unique(), [dict() for i in range(df['employee_residence'].nunique())]))
        for i, row in df.iterrows():
            if row['company_location'] in init_residence[row['employee_residence']]:
                init_residence[row['employee_residence']][row['company_location']] += 1
            else:
                init_residence[row['employee_residence']][row['company_location']] = 1

        to_delete = []
        self.residence_seqs = {}
        for employee_residence, counts in init_residence.items():
            total_cnts = sum(counts.values())

            if total_cnts == 1:
                to_delete.append(employee_residence)

            for country, count in counts.items():
                counts[country] = count / total_cnts
            self.residence_seqs[employee_residence] = counts

        super().fit()


class MarkovProcessorFactory(AnalyticsProcessorFactory):
    def __init__(self, bounded_object: MarkovObject):
        super().__init__("Markov", bounded_object, MarkovObject)

    def create_analyzer(self):
        return MarkovAnalyzer(self.name, self.bounded_object)

    def create_grapher(self):
        return MarkovGrapher(self.name, self.bounded_object)


class MarkovAnalyzer(AnalyticsAnalyzer):
    def __init__(self, name, bounded_object: MarkovObject):
        super().__init__(name, bounded_object, MarkovObject)

    def analyze(self):
        pass


class MarkovGrapher(AnalyticsGrapher):
    def __init__(self, name, bounded_object: MarkovObject):
        super().__init__(name, bounded_object, MarkovObject)

    def graph(self, residence: str):
        self._create_graph(residence)

    def _create_graph(self, residence: str):
        G = nx.DiGraph()
        destinations = self.bounded_object.residence_seqs[residence]
        edge_labels = {}
        for i, (country, prob) in enumerate(destinations.items()):
            G.add_edge(residence, country, weight=prob)
            edge_labels[(residence, country)] = prob
        self._visualize_graph(G, edge_labels)


    def _visualize_graph(self, G: nx.Graph, edge_labels: typing.Dict[tuple, float]):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        for u, v, ddict in G.edges(data=True):
            node1_x, node1_y = pos[u]
            node2_x, node2_y = pos[v]
            x_mid = (node1_x + node2_x) / 2
            y_mid = (node1_y + node2_y + (0.3 * int(u == v))) / 2
            plt.text(x_mid, y_mid, str(round(ddict['weight'],4)), bbox=dict(facecolor='red', alpha=0.8), ha='center', va='center')
        plt.show()


