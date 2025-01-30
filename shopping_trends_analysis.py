# -*- coding: utf-8 -*-
"""Shopping Trends Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hq6MWXqs7tTjceZYazc3U_IxRsy21It3

:<div style="color: White; display: fill;
            border-radius: 5px;
            background-color: #123456;
            font-size: 100%;
            font-family: Verdana">

<p style="padding: 7px; color: Black;">
      <ul>  📌 <b>Customer ID</b> - Unique identifier for each customer.<br>
        📌 <b>Age</b> - Age of the customer.<br>
        📌 <b>Gender</b> - Gender of the customer (Male/Female).<br>
        📌 <b>Item Purchased</b> - The item purchased by the customer.<br>
        📌 <b>Category</b> - Category of the item purchased.<br>
        📌 <b>Purchase Amount (USD)</b> - The amount of the purchase in USD.<br>
        📌 <b>Location</b> - Location where the purchase was made.<br>
        📌 <b>Size</b> - Size of the purchased item.<br>
        📌 <b>Color</b> - Color of the purchased item.<br>
        📌 <b>Season</b> - Season during which the purchase was made.<br>
        📌 <b>Review Rating</b> - Rating given by the customer for the purchased item.<br>
        📌 <b>Subscription Status</b> - Indicates if the customer has a subscription (Yes/No).<br>
        📌 <b>Shipping Type</b> - Type of shipping chosen by the customer.<br>
        📌 <b>Discount Applied</b> - Indicates if a discount was applied to the purchase (Yes/No).<br>
        📌 <b>Promo Code Used</b> - Indicates if a promo code was used for the purchase (Yes/No).<br>
        📌 <b>Previous Purchases</b> - Number of previous purchases made by the customer.<br>
        📌 <b>Payment Method</b> - Customer's most preferred payment method.<br>
        📌 <b>Frequency of Purchases</b> - Frequency at which the customer makes purchases (e.g., Weekly, Fortnightly, Monthly).<br><br>
    <p style = "padding: 3px; color: Black;">
"""

# importing libraries
import numpy as np # Importing the numpy library for array operations and mathematical functions
import pandas as pd # Use for exploring the data
import seaborn as sns # it has also plot
import matplotlib.pyplot as plt # for some extra plot functions
import plotly.express as px # this library can makes interactive plots

# reading the data set
shop = pd.read_csv('shopping_trends_updated.csv')
shop.shape

shop.to_excel('shopping_trends_updated.xlsx')
shop.head()

shop.dtypes

# it shows the names of the columns
shop.columns

shop.info()

shop.isnull().sum()

print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")

"""## OBSERVATION:
Upon initial examination of the dataset, it is evident that we have a comprehensive and well-structured dataset with 3900 rows and 18 columns. The data is complete, with no missing values, which allows us to proceed confidently with our analysis.

Let's delve into the columns and their significance in understanding our custome      

-  **Customer ID:** This column serves as a unique identifier for each customer, enabling us to differentiate between individuals.
-  **Age:** The age column provides insights into the age demographics of our customers, helping us understand their preferences and behaviors.
-  **Gender:** This column showcases the gender of the customers, enabling us to analyze buying patterns based on gender.
-  **Item Purchased:** Here, we can identify the specific products that customers have bought, allowing us to gain an understanding of popular choices.
-  **Category:** The category column categorizes the products into different groups such as clothing, footwear, and more, aiding us in analyzing trends within specific product categories.
-  **Purchase Amount (USD):** This column reveals the amount customers spent on their purchases, providing insights into their spending habits.
-  **Location:** The location column indicates the geographical location of customers, which can help identify regional trends and preferences.
-  **Size:** This column denotes the size of the purchased products, assisting in understanding size preferences across different categories.
-  **Color:** Here, we can determine the color preferences of customers, aiding in analyzing color trends and their impact on purchasing decisions.
-  **Season:** The season column allows us to identify the season during which customers made their purchases, enabling us to explore seasonal shopping trends.
-  **Review Rating:** This column showcases the ratings given by customers, providing valuable feedback on product satisfaction and quality.
-  **Subscription Status:** This column indicates whether customers have opted for a subscription status, which can help us understand customer loyalty and engagement.
-  **Shipping Type:** Here, we can identify the different shipping methods used to deliver products to customers, shedding light on preferred shipping options.
-  **Discount Applied:** This column indicates whether a discount was applied to the purchased products, enabling us to analyze the impact of discounts on customer behavior.
-  **Promo Code Used:** Here, we can identify whether customers utilized promo codes during their purchases, helping us evaluate the effectiveness of promotional campaigns.
-  **Previous Purchases:** This column reveals the number of previous purchases made by customers, aiding in understanding customer loyalty and repeat business.
-  **Payment Method:** The payment method column showcases the various methods used by customers to make their purchases, allowing us to analyze preferred payment options.
-  **Frequency of Purchases:** This column provides insights into the frequency at which customers make purchases, helping us identify patterns and customer buying habits.

ustomer buying habits.
With this rich and diverse dataset, we are well-equipped to explore customer shopping trends, understand their preferences, and uncover valuable insights that can drive informed decision-making and enhance the overall customer experience. Let's embark on this exciting analysis journey!

## 1 What is the overall distribution of customer ages in the dataset?
"""

shop['Age'].value_counts()

shop['Age'].mean()

shop['Gender'].unique()

shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults', 'old'] )

fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()

"""## 2 How does the average purchase amount vary across different product categories?"""

shop['Category'].unique()

shop.groupby('Category')['Purchase Amount (USD)'].mean()

"""## 3 Which gender has the highest number of purchases?"""

sns.barplot(shop , x = 'Gender' , y = 'Purchase Amount (USD)')

"""## 4 What are the most commonly purchased items in each category?"""

shop.groupby('Category')['Item Purchased'].value_counts()

fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()

"""## 5 Are there any specific seasons or months where customer spending is significantly higher?"""

shop['Season'].unique()

shop[shop['Season'] == 'Summer'].value_counts().sum()

shop[shop['Season'] == 'Winter'].value_counts().sum()

shop[shop['Season'] == 'Spring'].value_counts().sum()

shop[shop['Season'] == 'Fall'].value_counts().sum()

fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )
fig.show()

"""## 6 What is the average rating given by customers for each product category?"""

shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()

fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()

"""## 7 Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?"""

shop['Subscription Status'].unique()

sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')

shop['Purchase Amount (USD)'].sum()

shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()

"""## 8 Which payment method is the most popular among customers?"""

shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)

shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()
fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()

sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')

"""## 9 Do customers who use promo codes tend to spend more than those who don't?"""

shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()

fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()

fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()

"""## 10 How does the frequency of purchases vary across different age groups?"""

shop[['Age' , 'Age_category']]

shop['Age_category'].unique()

shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()

px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')

"""## 11 Are there any correlations between the size of the product and the purchase amount?"""

shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()

fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()

"""## 12 Which shipping type is preferred by customers for different product categories?"""

shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)

shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2, 'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})

shop['Category'].unique()

shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})

"""## 13 How does the presence of a discount affect the purchase decision of customers?"""

shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()

px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')

fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')
fig.show()

"""## 14 Are there any specific colors that are more popular among customers?"""

px.histogram(shop , x = 'Color')

shop['Color'].value_counts().nlargest(5)

"""## 15 What is the average number of previous purchases made by customers?"""

shop['Previous Purchases'].mean()

"""## 16 Are there any noticeable differences in purchase behavior between different locations?"""

shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)

shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()

fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()

"""## 17 Is there a relationship between customer age and the category of products they purchase?"""

shop_group = shop.groupby('Category')['Age'].mean().reset_index()

fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()

"""## 18 How does the average purchase amount differ between male and female customers?"""

shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()

fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()

px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')