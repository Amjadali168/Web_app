import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# config
st.set_page_config(
    layout="wide",
    page_title=" Netflix-EDA App",
    page_icon="🧊",
)
st.subheader("Welcome to Entertainment World (Movies & TV Show)",divider='red')
# st.image("https://i.pcmag.com/imagery/reviews/05cItXL96l4LE9n02WfDR0h-5.fit_scale.size_760x427.v1582751026.png")
st.title("Netflix-Exploratory Data Analysis App")
st.image("https://i.pcmag.com/imagery/reviews/05cItXL96l4LE9n02WfDR0h-5.fit_scale.size_760x427.v1582751026.png")

st.write("""
Welcome to the Netflix Data Analysis App! This app allows you to explore and analyze Netflix data.

    This Netflix Dataset has information about TV Shows and Movies available on Netflix till 2021.
    This Dataset is available on Kaggle website for free.

**Here are some quick insights:**
- Total Number of Titles: 8709
- Number of data present in the dataframe: 148053
- Total Number of Columns: 12
- Total Number of Rows: 8709
- Types of content on Netflix: Movies and TV Shows
         
""")
st.write("""
**How to use this app:**
- Explore the sample data.
- Use the sidebar to navigate to different analysis sections.
- Enjoy your data exploration!
""")


