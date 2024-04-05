import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df_DS_salaries = pd.read_csv('datasets/DataScience_salaries_2024.csv')


salary_in_usd_max = df_DS_salaries['salary_in_usd'].max()
salary_in_usd_min = df_DS_salaries['salary_in_usd'].min()
salary_in_usd_md = 400000



max_salary = st.sidebar.slider("Salary Data Science Range", salary_in_usd_min, salary_in_usd_max, salary_in_usd_md)


df_salaries = df_DS_salaries[df_DS_salaries['salary_in_usd'] <= max_salary]
df_salaries


fig = px.bar(df_salaries['salary_in_usd'].value_counts())
fig2 = px.histogram(df_salaries['work_year'])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)