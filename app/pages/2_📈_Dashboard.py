import os

import streamlit as st
import pandas as pd

from config import settings

def dashboard():
    st.title("Dashboard")

    # DataFrame
    df = pd.read_csv(os.path.join(settings.DATA_PATH, 'ds_salaries_processed.csv'))
    
    with st.sidebar:
        st.header("Mode")
        mode = st.selectbox("Mode", ["Table", "Chart"])

        st.markdown("----")

        st.header("Filters")

        selected_year = st.multiselect("Year: ", df['work_year'].unique().tolist() + ['All'], default='All', )
        selected_experience = st.multiselect("Experience Level: ", df['experience_level'].unique().tolist() + ['All'], default='All')
        selected_employment_type = st.multiselect("Employment Type: ", df['employment_type'].unique().tolist() + ['All'], default='All')
        selected_employee_res = st.multiselect("Employee Residence: ", df['employee_residence'].unique().tolist() + ['All'], default='All')
        selected_company_loc = st.multiselect("Company Location: ", df['company_location'].unique().tolist() + ['All'], default='All')
        selected_company_size = st.multiselect("Company Size: ", df['company_size'].unique().tolist() + ['All'], default='All')
        selected_arrangement_type = st.multiselect("Arrangement Type: ", df['arrangement_type'].unique().tolist() + ['All'], default='All')
        selected_field = st.multiselect("Field: ", df['field'].unique().tolist() + ['All'], default='All')
        selected_brain_drain = st.multiselect("Brain Drain: ", df['brain_drain'].unique().tolist() + ['All'], default='All')

    if mode == "Table":
        filt_df = df.copy()
        filt_df = filt_df[filt_df['work_year'].isin(df['work_year'].unique() if selected_year[0] == 'All' else selected_year)]
        filt_df = filt_df[filt_df['experience_level'].isin(df['experience_level'].unique() if selected_experience[0] == 'All' else selected_experience)]
        filt_df = filt_df[filt_df['employment_type'].isin(df['employment_type'].unique() if selected_employment_type[0] == 'All' else selected_employment_type)]
        st.dataframe(filt_df)
    elif mode == "Chart":
        st.title("TBD")
    else:
        raise Exception("Mode is not supported")

    

st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout='wide',
    initial_sidebar_state='auto'
)

dashboard()