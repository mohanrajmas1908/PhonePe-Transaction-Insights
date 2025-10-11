import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

# Step 1: Load the combined CSV file (case1_combined.csv)
insu_top_combined_df = pd.read_csv('C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/insu_top_case_combined.csv')
# Step 2: Visualize the results in Streamlit

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.

#Background color B0E0E6    

st.image("C:/DataScience/Projects/PhonePe-Logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    🛡️💰Insurance_Insights-PhonePe
    </h1>
    """,
    unsafe_allow_html=True
)

sb = st.selectbox(
    'User Engagement',
    ["District-Level Insurance Financial Activity", 'State-Level Insurance Transaction Count'],
    index=0
 )
#######################################################################################
if sb == "District-Level Insurance Financial Activity":
# Case Study 1: Insurance_Insights Districts Vs Transaction Amount 
    st.subheader("Districts Vs Transaction Amount")

# Filter and sort the DataFrame
    filtered_df = (
        insu_top_combined_df[insu_top_combined_df['query'] == 'query1']
        .sort_values(by="Transactions_Count_Crore", ascending=False)
    )
# Create a barplot
    fig = plt.figure(figsize=(10 ,5))
    ax = sns.barplot(x="districts", y="Trans_Amount_Trillion",data=filtered_df, palette="colorblind")

    unique_brands = filtered_df['districts'].unique()
    ax.legend(unique_brands, title="districts", loc="upper right", fontsize=5, title_fontsize=5)
    
    plt.title("Districts Vs Transaction Amount_Top20", fontsize=20)
    plt.xlabel("Districts", fontsize=20)
    plt.ylabel("Trans_Amount_Trillion", fontsize=20)
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig) 
    
###############################################
if sb == "State-Level Insurance Transaction Count":
    st.subheader("🥧 Insurance Insights: State-wise Transaction Share")

# Filter and sort the DataFrame
    filtered_df = (
        insu_top_combined_df[insu_top_combined_df['query'] == 'query2']
        .sort_values(by="Transactions_Count_Crore", ascending=False)
    )
# Prepare data
    states = filtered_df['State'].tolist()
    transactions = filtered_df['Transactions_Count_Crore'].tolist()
    colors = sns.color_palette("plasma", len(states))  # Optional: add color

# Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

# Plot pie chart
    ax.pie(
        transactions,
        labels=states,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 7},
        wedgeprops={'alpha': 0.8},
        colors=colors
    )

# Title and layout
    ax.set_title("State-wise Share of Insurance Transactions-TOP 10", fontsize=12)
    ax.axis('equal')  # Ensures pie is circular

# Display in Streamlit
    st.pyplot(fig)
