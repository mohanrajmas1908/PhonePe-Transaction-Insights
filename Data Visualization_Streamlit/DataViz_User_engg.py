import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
# Step 1: Load the combined CSV file (case1_combined.csv)
User_engg_combined_df = pd.read_csv('C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/User_case_combined.csv')
# Step 2: Visualize the results in Streamlit

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.

#Background color B0E0E6    

st.image("C:/DataScience/Projects/PhonePe-Logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    📱User Engagement-PhonePe
    </h1>
    """,
    unsafe_allow_html=True
)

sb = st.selectbox(
    'User Engagement',
    ["Device Brand-wise App Engagement", 'Distribution of Registered Users Across Brands'],
    index=0
 )
#######################################################################################
if sb == "Device Brand-wise App Engagement":
# Case Study 1: User_Engagement-Device Brand-wise App Engagement
    st.subheader("App Usage Breakdown by Brand")

      # Filter and sort the DataFrame
    filtered_df = (
        User_engg_combined_df[User_engg_combined_df['query'] == 'query1']
        .sort_values(by="AppOpens_Billion", ascending=False)
    )

    # Create a barplot
    fig = plt.figure(figsize=(10, 5))
    ax = sns.barplot(x="Brand", y="AppOpens_Billion",data=filtered_df, palette="Dark2")

    unique_brands = filtered_df['Brand'].unique()
    ax.legend(unique_brands, title="Brands", loc="upper right", fontsize=6, title_fontsize=8)
    
    plt.title("Brand vs AppOpens", fontsize=18)
    plt.xlabel("Brand", fontsize=20)
    plt.ylabel("AppOpens_Billion", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig) 
    
###############################################
if sb == "Distribution of Registered Users Across Brands":
        # Case Study 2: User_Engagement-Distribution of Registered Users Across Brands
        st.subheader("Registered Users Breakdown by Brand")

        # Filter and sort the DataFrame
        filtered_df = (
            User_engg_combined_df[User_engg_combined_df['query'] == 'query2']
            .sort_values(by="RegisteredUsers_Billion", ascending=False)
        )

        # Create a barplot
        fig = plt.figure(figsize=(15, 8))
        ax = sns.barplot(x="Brand", y="RegisteredUsers_Billion",data=filtered_df, palette="tab20")
    # Create a color palette with unique colors for each brand
        unique_brands = filtered_df['Brand'].unique()
        ax.legend(unique_brands, title="Brands", loc="upper right", fontsize=9, title_fontsize=10)
        plt.title("Brand vs RegisteredUsers", fontsize=18)
        plt.xlabel("Brand", fontsize=20)
        plt.ylabel("RegisteredUsers_Billion", fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig) 