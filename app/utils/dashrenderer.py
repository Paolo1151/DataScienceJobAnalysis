import os
import typing
from enum import Enum

import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import plotly.graph_objects as go

from config import settings

class DashMode(Enum):
    CHART = 1
    TABLE = 2


class Dashboard():
    def __init__(self):
        self.df = pd.read_csv(os.path.join(settings.DATA_PATH, 'ds_salaries_processed.csv'))

    def render(self, filters: typing.Dict[str, typing.List[object]], mode: str):
        mode = DashMode[mode.upper()]
        if mode == DashMode.TABLE:
            self._render_table(filters)
        elif mode == DashMode.CHART:
            self._render_chart(filters)
        else:
            raise Exception("Unknown mode")

    def _render_table(self, filters: typing.Dict[str, typing.List[object]]):
        st.title("Data Science Salaries Table View")
        st.dataframe(Dashboard._apply_filters(self.df, filters))

    def _render_chart(self, filters: typing.Dict[str, typing.List[object]]):
        st.title("Data Science Salaries Chart View")

        first_row = st.columns([2.5, 1])

        with first_row[0]:
            st.header("Data Scientist Attributes throughout the Years")
            sel_col = st.selectbox("Column to view", self.df.drop(columns=['work_year']).columns)
            curr_df = Dashboard._apply_filters(self.df, filters)
            fig_top = self._render_column_dash(curr_df, sel_col)
            st.plotly_chart(fig_top, use_container_width=True)

        with first_row[1]:
            st.header("Network of Data Scientist Residences to Company Locations")
            with open(os.path.join(settings.CONTENT_PATH, "pyvis_graph.html"), "r") as f:
                html = f.read()
            stc.html(html, height=500)
            
        # Generate Line Plot
        fig = go.Figure()
        for field in self.df['field'].unique():
            temp_filters = filters.copy()
            temp_filters.update({'field': [field]})
            curr_df = Dashboard._apply_filters(self.df, temp_filters)
            curr_df = curr_df.groupby(['work_year']).mean().reset_index()
            fig.add_trace(
                go.Scatter(x=curr_df['work_year'], y=curr_df['salary_in_usd'], mode='lines+markers', name=field)
            )
        fig.update_xaxes(range=[2020, 2022], dtick=1)

        st.header("Changes in Salary by Field")

        # Update Layout
        fig.update_layout(
            xaxis=dict(
                showline=False,
                showgrid=False
            ),
            yaxis=dict(
                showgrid=False,
                showline=False
            )
        )

        st.plotly_chart(fig, use_container_width=True)



    def _render_column_dash(self, df, sel_col, override_type=None):
        if df[sel_col].dtype == object or override_type == object:
            fig_top = go.Figure()
            for year in sorted(df['work_year'].unique().tolist()):
                fig_top.add_trace(
                    go.Bar(
                        y=self.df[self.df['work_year']==year][sel_col].unique(),
                        x=df[df['work_year']==year][sel_col].value_counts().values,
                        name=str(year),
                        orientation='h',
                        # To add Marker
                    )
                )
            fig_top.update_layout(barmode='stack')
            max_value_g = self.df[sel_col].value_counts().max()
            fig_top.update_xaxes(range=[0, max_value_g])
        else:
            fig_top = go.Figure()
            for year in sorted(df['work_year'].unique().tolist()):
                fig_top.add_trace(
                    go.Histogram(
                        x=df[df['work_year']==year][sel_col],
                        name=str(year)
                    )
                )
            
        return fig_top


    def get_df(self):
        return self.df

    @staticmethod
    def get_modes():
        return list(map(lambda x: x.name.capitalize(), DashMode))

    @staticmethod
    def _apply_filters(df, filters):
        for column, values in filters.items():
            df = df[df[column].isin(df[column].unique() if 'All' in values else values)]
        return df

        

