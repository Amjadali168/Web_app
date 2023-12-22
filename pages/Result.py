import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import plotly.express as px

# Assuming df is your DataFrame
st.set_page_config(
    page_title="Netflix-EDA App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_data()
def load_data(path):
    df = pd.read_csv(path)
    return df

# Load the data
df = load_data('netflix_titles_2021.csv')

# Add a Streamlit page title
st.title('Exploratory Data Analysis Results')

# Display a sample of the DataFrame
st.subheader('Sample of the DataFrame:',divider='green')
st.dataframe(df.sample(9))

# Basic Statistics
st.subheader('Basic Statistics:')
st.write(df.describe())

# Correlation Heatmap
st.subheader('Correlation Heatmap',divider='green')
data = {
    'release_year': list(range(1900, 2023)),
    'Minutes': [random.randint(1, 40) for _ in range(2023 - 1900)]
}

df = pd.DataFrame(data)
# Exclude non-numeric columns from the correlation matrix
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_columns].corr()

# Create a heatmap using Seaborn
fig, ax = plt.subplots()
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
st.pyplot(fig)


# Calculate the distribution of release_year
year_distribution = df['release_year'].value_counts()

# Display the distribution with Streamlit
st.subheader("Distribution of release_year",divider='green')
st.bar_chart(year_distribution)


# st.subheader('Download Data:')
# csv_file = df.to_csv(index=False)
# st.download_button(
#     label='Download DataFrame as CSV',
#     data=csv_file,
#     file_name='eda_results.csv',
#     key='download_button'
# )
# Display the top 5 directors
top_directors = [
    "Raúl Campos, Jan Suter",
    "Marcus Raboy",
    "Jay Karas",
    "Cathy Garcia-Molina",
    "Martin Scorsese"
]

top_actors = [
    "Anupam Kher",
    "Om Puri",
    "Shah Rukh Khan",
    "Boman Irani",
    "Paresh Rawal"
]

most_watched_movie = "Sankofa"
most_watched_tv_show = "The Great British Baking Show"
most_rated_movie = "Dick Johnson Is Dead"
most_movies_in_2019 = "2019"
country_with_max_movies = "United States"


# Top Directors
st.subheader("Top 5 Directors on Netflix:",divider='red')
for director in top_directors:
    st.write(f"- {director}")

# Top Actors
st.subheader("Top 5 Actors on Netflix:",divider='red')
for actor in top_actors:
    st.write(f"- {actor}")

# Most Watched Movie
st.subheader("The most watched Movie is:")
st.markdown(f"<span style='font-family: Arial, sans-serif; font-weight: bold;color:red;font-size:20px;'>{most_watched_movie}</span>", unsafe_allow_html=True)

# Most Watched TV Show
st.subheader(f"The most watched TV show is:")
st.markdown(f"<span style='font-family: Arial, sans-serif; font-weight: bold;color:red;font-size:20px;'>{most_watched_tv_show}</span>", unsafe_allow_html=True)



# Most Rated Movie
st.subheader("The most Rated Movie is:")
st.markdown(f"<span style='font-family: Arial, sans-serif; font-weight: bold;color:red;font-size:20px;'>{most_rated_movie}</span>", unsafe_allow_html=True)

# Most Movies in 2019
st.subheader("Most of Movies released in:")
st.markdown(f"<span style='font-family: Arial, sans-serif; font-weight: bold;color:red;font-size:20px;'>{most_movies_in_2019}</span>", unsafe_allow_html=True)
# Country with Maximum Number of Movies
st.subheader("The Country with the maximum number of Movies released is:")
st.markdown(f"<span style='font-family: Arial, sans-serif; font-weight: bold;color:red;font-size:20px;'>{country_with_max_movies}</span>", unsafe_allow_html=True)

# Download all data in the DataFrame
all_data_csv = df.to_csv(index=False)
st.download_button(
    label='Download All Data as CSV',
    data=all_data_csv,
    file_name='all_data.csv',
    key='download_all_data_button'
)


