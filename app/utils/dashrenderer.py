import os
import typing
from enum import Enum

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from config import settings



class DashMode(Enum):
    TABLE = 1
    CHART = 2


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
        
        columns = st.columns(3)
        
        for year, column in zip([2020, 2021, 2022], columns):
            with column:
                st.title(year)
                temp_filters = filters.copy()
                temp_filters.update({'work_year': [year]})
                curr_df = Dashboard._apply_filters(self.df, temp_filters)
                fig_top = self._render_column_dash(curr_df)
                st.plotly_chart(fig_top)

        # Generate Line Plot
        fig = go.Figure()
        for field in self.df['field'].unique():
            temp_filters = filters.copy()
            temp_filters.update({'field': [field]})
            curr_df = Dashboard._apply_filters(self.df, temp_filters)
            fig.add_trace(
                go.Scatter(x=["2020", "2021", "2022"], y=curr_df['salary_in_usd'], mode='lines+markers', name=field)
            )

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



    def _render_column_dash(self, df):
        fig_top = go.Figure(data=[go.Histogram(x=df['salary_in_usd'])])
        return fig_top
        
    def _render_main_line_chart(self, df):

        return fig


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

        

