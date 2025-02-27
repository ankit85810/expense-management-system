import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_by_month_tab():
    response = requests.get(f"{API_URL}/analytics_month")
    response = response.json()
    df = pd.DataFrame(response)
    
    df_sorted = df.sort_values(by= "month_name", ascending=False)

    st.title('Expense Breakdown by Month')

    st.bar_chart(data=df_sorted.set_index("month_name")["total_spent"])
    st.table(df_sorted)
    