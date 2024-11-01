import streamlit as st
import pandas as pd
import plotly.express as px
# Load the dataset
data = pd.read_csv("vehicles_us.csv")

# Display a sample of the dataset (optional for testing)
st.write(data.head())
st.header("Exploratory Data Analysis of US Vehicles")
# Create and display a histogram for vehicle prices
fig_hist_price = px.histogram(data, x="price", title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist_price)
# Create and display a scatter plot for odometer vs. price
fig_scatter_odometer_price = px.scatter(
    data,
    x="odometer",
    y="price",
    color="condition",
    title="Price vs Odometer Reading by Vehicle Condition"
)
st.plotly_chart(fig_scatter_odometer_price)
# Add a checkbox to filter data based on odometer readings
if st.checkbox("Show only vehicles with an odometer reading less than 100,000 miles"):
    filtered_data = data[data["odometer"] < 100000]

    # Display a filtered histogram for vehicle prices
    fig_hist_filtered = px.histogram(filtered_data, x="price", title="Distribution of Vehicle Prices (Filtered)")
    st.plotly_chart(fig_hist_filtered)

    # Display the filtered data (optional)
    st.write("Filtered Data (vehicles with odometer < 100,000 miles):")
    st.write(filtered_data)

