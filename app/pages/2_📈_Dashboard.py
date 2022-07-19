import os

import streamlit as st
import pandas as pd

from config import settings

def dashboard():
    df = settings.DASHBOARD.get_df()

    with st.sidebar:
        st.header("Mode")
        mode = st.selectbox("Mode", settings.DASHBOARD.get_modes())

        st.markdown("----")
        st.header("Filters")

        if mode == "Table":
            selected_year = st.multiselect("Year: ", df['work_year'].unique().tolist() + ['All'], default='All')
            selected_experience = st.multiselect("Experience Level: ", df['experience_level'].unique().tolist() + ['All'], default='All')
            selected_employment_type = st.multiselect("Employment Type: ", df['employment_type'].unique().tolist() + ['All'], default='All')
            selected_employee_res = st.multiselect("Employee Residence: ", df['employee_residence'].unique().tolist() + ['All'], default='All')
            selected_company_loc = st.multiselect("Company Location: ", df['company_location'].unique().tolist() + ['All'], default='All')
            selected_company_size = st.multiselect("Company Size: ", df['company_size'].unique().tolist() + ['All'], default='All')
            selected_arrangement_type = st.multiselect("Arrangement Type: ", df['arrangement_type'].unique().tolist() + ['All'], default='All')
            selected_field = st.multiselect("Field: ", df['field'].unique().tolist() + ['All'], default='All')
            selected_brain_drain = st.multiselect("Brain Drain: ", df['brain_drain'].unique().tolist() + ['All'], default='All')

            filter_dict = dict(
                zip(
                    ['work_year', 'experience_level', 'employment_type', 'employee_residence', 'company_location', 'company_size', 'arrangement_type', 'field', 'brain_drain'],
                    [selected_year, selected_experience, selected_employment_type, selected_employee_res, selected_company_loc, selected_company_size, selected_arrangement_type, selected_field, selected_brain_drain]
                )
            )
        elif mode == "Chart":
            selected_experience = st.multiselect("Experience Level: ", df['experience_level'].unique().tolist() + ['All'], default='All')
            selected_employment_type = st.multiselect("Employment Type: ", df['employment_type'].unique().tolist() + ['All'], default='All')
            selected_employee_res = st.multiselect("Employee Residence: ", df['employee_residence'].unique().tolist() + ['All'], default='All')
            selected_company_loc = st.multiselect("Company Location: ", df['company_location'].unique().tolist() + ['All'], default='All')
            selected_company_size = st.multiselect("Company Size: ", df['company_size'].unique().tolist() + ['All'], default='All')
            selected_arrangement_type = st.multiselect("Arrangement Type: ", df['arrangement_type'].unique().tolist() + ['All'], default='All')
            selected_brain_drain = st.multiselect("Brain Drain: ", df['brain_drain'].unique().tolist() + ['All'], default='All')

            filter_dict = dict(
                zip(
                    ['experience_level', 'employment_type', 'employee_residence', 'company_location', 'company_size', 'arrangement_type', 'field', 'brain_drain'],
                    [selected_experience, selected_employment_type, selected_employee_res, selected_company_loc, selected_company_size, selected_arrangement_type, "All", selected_brain_drain]
                )
            )
        else:
            raise ValueError("Mode not supported!")



    settings.DASHBOARD.render(filter_dict, mode)

st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout='wide',
    initial_sidebar_state='auto'
)

dashboard()