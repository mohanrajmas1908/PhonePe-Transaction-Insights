import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
#Load the combined CSV file (case1_combined.csv)
trend_combined_df = pd.read_csv('C:/DataScience/Projects/PhonePe Transaction Insights/BusinessUseCases/Trend_Ana_case_combined.csv')

# Centered, Large, Bold Title in Streamlit using custom HTML and Markdown.
st.image("C:/DataScience/Projects/PhonePe-Logo.png", width=250)
st.markdown(
    """
    <h1 style='text-align: center; color: #9B59B6; font-size: 40px; font-weight: bold;'>
    🎢Trend Analysis-PhonePe
    </h1>
    """,
    unsafe_allow_html=True
)

#######################################################################################
# Case Study 1: User_Engagement-Device Brand-wise App Engagement
st.subheader("Anticipate Demand Fluctuations")
# Filter for Query 3
df3 = trend_combined_df[trend_combined_df['query'] == 'query1']

df3['Time'] = df3['Year'].astype(str) + ' Q' + df3['Quarter'].astype(str)

df3['Time'] = pd.Categorical(df3['Time'], ordered=True, categories=sorted(df3['Time'].unique()))

# Create a barplot

fig, ax = plt.subplots(figsize=(10, 5))
pivot = df3.pivot(index='Year', columns='Quarter', values='Total_Amount_Billion')
sns.heatmap(pivot, annot=True, fmt=".2f", cmap='YlGnBu')

#sns.lineplot(data=df3, x='Time', y='total_amount_Billion', marker='o', ax=ax)

ax.set_title("📈 Yearly & Quarterly Trend Analysis", fontsize=16)
ax.set_xlabel("Quarter")
ax.set_ylabel("Yearly")
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
plt.tight_layout()
st.pyplot(fig) 
    
