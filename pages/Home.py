import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns 
from matplotlib import pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting tools


# Set page config
st.set_page_config(
    page_title="Netflix-EDA App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
@st.cache_data()
def load_data(path):
    df = pd.read_csv('netflix_titles_2021.csv')
    return df

with st.spinner('Processing netflix Data'):
    df=load_data('netflix_titles_2021.csv')
with st.container():
    st.title('Netflix-Exploratory Data Analysis')
    st.image("/Users/bafel/Downloads/WhatsApp Image 2023-12-19 at 7.17.10 PM.jpeg",caption='Netflix Data Analysis')
    st.subheader("Data Summary",divider='red')
c1,c2,c3=st.columns(3)

total_typeShow=df.shape[0]
type_trend="Movie & TV Show"

#Main Heads
c1.metric("Total_type",total_typeShow)
c2.metric("Type",type_trend)
c3.image("https://qph.cf2.quoracdn.net/main-qimg-2a3b020be05348e551c313cd03871286-lq",width=400)
c1.subheader("Insight: ")
c1.text("""This app contains various analysis and
its graphs based on total 105684 number 
of data""")
st.subheader("Movies and TV Shows",divider='rainbow')
st.image("/Users/bafel/Downloads/marvel.jpg")
st.header("Netflix Data-Visualization",divider='rainbow')
st.sidebar.success("Select page above.")
#Visualization: Count of different types of content (movies, TV shows) in each country using a bar chart.
st.subheader('Types of Content(Movie & TV Show)in each country',divider='blue')
fig = px.bar(df, 
                   x='type',
                   y='country')
st.plotly_chart(fig,use_container_width=True)


st.subheader('Director Selection and Rating Analysis', anchor='director_selection',divider='green')
# --- STREAMLIT SELECTION
directors = df['director'].unique().tolist()
release_years = df['release_year'].unique().tolist()

release_years_selection = st.slider('Release Year:',
                                    min_value=min(release_years),
                                    max_value=max(release_years),
                                    value=(min(release_years), max(release_years)))

directors_selection = st.multiselect('Directors:',
                                      directors,
                                      default=directors[:10],
                                     format_func=lambda x: str(x)[:20])

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['release_year'].between(*release_years_selection)) & (df['director'].isin(directors_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['rating']).count()[['release_year']]
df_grouped = df_grouped.rename(columns={'release_year': 'Count'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='rating',
                   y='Count',
                   text='Count',
                   color_discrete_sequence=['#176BA0'] * len(df_grouped),
                   template='plotly_white')

# --- DISPLAY BAR CHART
st.plotly_chart(bar_chart)

#Visualization: Time series line plot to show the trend of content added over the years.
st.subheader('Time series line plot of content over years',divider='grey')
df['date_N'] = pd.to_datetime(df['date_added'], errors='coerce', infer_datetime_format=True)
c1,c2=st.columns(2)
fig2,ax=plt.subplots()
ax = sns.lineplot(
             data=df,
             x='date_N',
             y='release_year',
             hue='release_year',
            )
c1.pyplot(fig2)
c2.image('https://www.whats-on-netflix.com/wp-content/uploads/2022/10/whats-coming-to-netflix-in-november-2022.jpg')
plt.show()

# Add a Streamlit subheader
st.subheader('Box Plot: Distribution of Release Years for Movies and TV Shows', divider='green')
col1,col2=st.columns(2)
# Create a box plot using Seaborn
fig, ax = plt.subplots()
box_plot = sns.boxplot(
    data=df,
    x='type',
    y='release_year',
    palette='Set2', 
)

# Set labels and title
box_plot.set(xlabel='Content Type', ylabel='Release Year', title='Box Plot: Distribution of Release Years')

# Display the box plot
col1.pyplot(fig)
col2.image("https://actu.meilleurmobile.com/wp-content/uploads/2020/02/top-10-netflix.jpeg")
# Sample data
data = {
    'release_year': list(range(1900, 2023)),
    'Minutes': [random.randint(1, 40) for _ in range(2023 - 1900)]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Scatter Plot Visualization")
st.subheader('Scatter Plot: Release Year vs. Minutes',divider='red')
# Create two columns
col1, col2 = st.columns(2)

# Plot in the first column
fig, ax = plt.subplots()
scatter_plot = sns.scatterplot(
    data=df,
    x='release_year',
    y='Minutes',
    color='blue',
    alpha=0.7,
)
scatter_plot.set(xlabel='Release Year', ylabel='Minutes')
col1.pyplot(fig)

col2.image("https://docs.influxdata.com/img/influxdb/2-0-visualizations-scatter-example.png")



st.subheader("Exploring the Relationship Between Release Year and Minutes in a 3D Scatter Plot", divider='blue')

data = {
    'release_year': list(range(1900, 2023)),
    'Minutes': [random.randint(1, 40) for _ in range(2023 - 1900)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add 'year' column to DataFrame
df['year'] = pd.DatetimeIndex(df['release_year']).year

# Create a 3D scatter plot with Plotly Express
fig = px.scatter_3d(df, x='release_year', y='Minutes', z='year', color='release_year')

# Set labels and title
fig.update_layout(scene=dict(xaxis_title='Release Year', yaxis_title='Minutes', zaxis_title='Year'))
fig.update_layout(title_text='3D Scatter Plot: Release Year vs. Minutes')

# Display the 3D scatter plot
st.plotly_chart(fig)
