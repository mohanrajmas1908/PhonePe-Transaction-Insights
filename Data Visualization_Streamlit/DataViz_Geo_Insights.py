import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as plotly
import json
import requests
import plotly.express as px

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.
  
st.image("C:/DataScience/Projects/PhonePe-Logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    🌏Geographical Insights
    </h1>
    """,
    unsafe_allow_html=True
)
sb = st.selectbox(
    'Geographical Analysis',
    ["Transaction Amount Vs States", 'Transaction Amount Vs Districts'],
    index=0
)
if sb == "Transaction Amount Vs States":
    
# Case Study 1: Geographical Insights - Transaction Amount Vs State (Top States from 2018–2024)
    st.subheader("📍 Transaction Amount Across Indian States")

#  Load the combined CSV file
    Geo_combined_df = pd.read_csv("C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/Geo_combined.csv")

#  Filter for Query 1
    df2 = Geo_combined_df[Geo_combined_df['query'] == 'query1']

#  Load GeoJSON for India states
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    india_geojson = requests.get(geojson_url).json()

#  Extract state names from GeoJSON
    geo_states = [f["properties"]["ST_NM"] for f in india_geojson["features"]]
    df_geo = pd.DataFrame({"State_cleaned": geo_states})

#  Merge with transaction data
    df_merged = df_geo.merge(df2, on="State_cleaned", how="left").fillna(0)

#  Plot choropleth map
    fig = px.choropleth(
        df_merged,
        geojson=india_geojson,
        featureidkey="properties.ST_NM",
        locations="State_cleaned",
        color="Total_Amount_Trillion",
        color_continuous_scale="Turbo",
        title="💸 Total Transactions Across Indian States"
    )
    fig.update_geos(fitbounds="locations", visible=False)

#  Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
#####################################################################
if sb == "Transaction Amount Vs Districts":
### Case Study 2:Geographical Insights - Transaction Amount Vs Districts (Top States from 2018 -2024)

    st.subheader("📍 Transaction Amount Across Indian Districts")

#  Load the combined CSV file
    Geo_combined_df = pd.read_csv("C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/Geo_combined.csv")

# Filter and sort the DataFrame
    filtered_df = (Geo_combined_df[Geo_combined_df['query'] == 'query2']
        .sort_values(by="Total_Amount_Trillion", ascending=False)
    )

# Create a barplot
    fig = plt.figure(figsize=(10 ,5))
    ax = sns.barplot(x="districts", y="Total_Amount_Trillion",data=filtered_df, palette="Accent")

    unique_brands = filtered_df['districts'].unique()
    ax.legend(unique_brands, title="districts", loc="upper right", fontsize=5, title_fontsize=5)
    
    plt.title("Districts Vs Transaction Amount_Top10", fontsize=20)
    plt.xlabel("Districts", fontsize=20)
    plt.ylabel("Total_Amount_Trillion", fontsize=20)
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig) 