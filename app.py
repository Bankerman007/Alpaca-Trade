import streamlit as st
import pandas as pd
from api_calls import get_profits
from python_to_postgres import get_data

st.sidebar.write("Trade Bot")
option = st.sidebar.selectbox("Trade or Profit History?", ("Trade History", "Profit/Loss History"),1)
st.header(option)
if option == "Trade History":
    st.subheader("TSLA")
    dataframe1 = get_data()
    st.dataframe(dataframe1)

if option == "Profit/Loss History":
    st.subheader("TSLA")
    profit_history= get_profits()
    st.bar_chart(profit_history)
    print(profit_history)

    



