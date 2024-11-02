import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("vehicles_us.csv")


st.write(data.head())
st.header("Exploratory Data Analysis of US Vehicles")

fig_hist_price = px.histogram(data, x="price", title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist_price)

fig_scatter_odometer_price = px.scatter(
    data,
    x="odometer",
    y="price",
    color="condition",
    title="Price vs Odometer Reading by Vehicle Condition"
)
st.plotly_chart(fig_scatter_odometer_price)

if st.checkbox("Show only vehicles with an odometer reading less than 100,000 miles"):
    filtered_data = data[data["odometer"] < 100000]

    fig_hist_filtered = px.histogram(filtered_data, x="price", title="Distribution of Vehicle Prices (Filtered)")
    st.plotly_chart(fig_hist_filtered)

    st.write("Filtered Data (vehicles with odometer < 100,000 miles):")
    st.write(filtered_data)

