import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as plotly
import json
import requests
import plotly.express as px
# Step 1: Load the combined CSV file (case1_combined.csv)
combined_df = pd.read_csv("C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/case1_combined.csv")

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.
st.image("C:/DataScience/Projects/PhonePe-Logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    🧑‍📱Customer Segmentation
    </h1>
    """,
    unsafe_allow_html=True
)

sb = st.selectbox(
    'CustomerSegmentation',
    ["Transaction_Type Vs Transaction _Count(2018-2014)", 'Transaction_Amount Vs Year(2018-2014)'],
    index=0
)
#######################################################################################
if sb == "Transaction_Type Vs Transaction _Count(2018-2014)":
# Case Study 1: CustomerSegmentation - Transaction_Type Vs Transaction_Count(2018-2024)
    
# Filter for Query 1
    df1 = combined_df[combined_df['query'] == 'query1']

# Create a barplot
    fig = plt.figure(figsize=(12, 8))
    ax = sns.barplot(x="Transaction_type", y="Total_count_Crore",data=df1, palette="Pastel1")

# Format Y-axis
    import matplotlib.ticker as ticker
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

    plt.title("Transaction Type vs Count", fontsize=18)
    plt.xlabel("Transaction Type", fontsize=14)
    plt.ylabel("Total_count_Crore", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig) 


#########################################
if sb == "Transaction_Amount Vs Year(2018-2014)":
# Filter for Query 2
    df1 = combined_df[combined_df['query'] == 'query2']

# Create the line plot
    fig = px.line(
        df1,
        x="Year",
        y="Total_amount_Trillion",
        markers=True,
        title="📈 Transaction Trend Over Years",
        labels={"Amount_Tr": "Amount (₹ Trillions)", "Year": "Year"},
        line_shape="linear"
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))
# Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
