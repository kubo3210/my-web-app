# US Vehicles Data Analysis Dashboard

# Render URL
https://my-web-app-ywlq.onrender.com

## Project Description
This project is a web application built using Streamlit that allows users to perform exploratory data analysis on a dataset containing information about vehicles in the US. The app includes interactive visualizations such as histograms and scatter plots, providing insights into vehicle prices, conditions, odometer readings, and more.

## Features
- **Interactive Histogram**: Visualize the distribution of vehicle prices.
- **Scatter Plot**: Explore the relationship between odometer readings and vehicle prices, categorized by vehicle condition.
- **Interactive Checkbox**: Filter data to show only vehicles with specific odometer readings.

## Methods and Libraries Used
- **Streamlit**: Used for creating the web app interface and interactive components.
- **Pandas**: Used for data manipulation and loading the CSV dataset.
- **Plotly Express**: Used for creating interactive and customizable charts.

## How to Run the Code
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\\Scripts\\activate'
   ```

3. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter notebook**:
   ```bash
   jupyter notebook
   ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
