import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

file_path = 'C:/Users/PC/PycharmProjects/Data_project/Data/supermarket_sales.csv'  # Replace this with the actual file path from Step 3
sales = pd.read_csv(file_path)
# Get basic summary statistics for numeric columns
print(sales.describe())
# Count the number of non-null values in each column
print(sales.count())

# Most used form of payment
payment_counts = sales['Payment'].value_counts()
print(payment_counts)
plt.figure(figsize=(8, 6))
sns.barplot(x=payment_counts.index, y=payment_counts.values)
plt.title('Most Used Payment Methods')
plt.xlabel('Payment')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
# From the figure we see that the most used payment method is ewallet and cash.


# Visualize sales trends over time using line plots or time series plots:
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Total', data=sales)
plt.title('Sales Trends over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# Segment customers based on their purchasing behavior:
customer_segments = sales.groupby('Invoice ID')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.histplot(customer_segments['Total'], bins=30)
plt.title('Customer Segments by Total Sales')
plt.xlabel('Total Price including tax')
plt.ylabel('Number of customers')
plt.show()

# Analyze product sales and identify popular products:
product_sales = sales.groupby('Product_line')['Quantity'].sum().reset_index()
top_products = product_sales.nlargest(10, 'Quantity')
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_line', y='Quantity', data=top_products)
plt.title('Top Products by Quantity Sold')
plt.xlabel('Product ID')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.show()
# Compare sales performance across different branches:
plt.figure(figsize=(8, 6))
sns.boxplot(x='Branch', y='Total', data=sales)
plt.title('Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

# Compare gross income performance across different branches:

plt.figure(figsize=(8, 6))
sns.boxplot(x='Branch', y='gross_income', data=sales)
plt.title('Gross income by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Gross income ')
plt.show()
# Feature Selection (use relevant columns as features)
features = sales[['Unit_price', 'Tax 5%', 'cost_of_goods_sold']]

# Target variable (total sales)
target = sales['Total']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model's performance using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
# Visualize the model's predictions
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', lw=2)  # Plot the ideal line
plt.xlabel('Actual Total Sales')
plt.ylabel('Predicted Total Sales')
plt.title('Model Prediction vs. Actual')
plt.show()

# the model is successful in predicting actual sales