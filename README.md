Overview

This project performs customer segmentation using the K-Means clustering algorithm. The goal is to group customers based on their Annual Income and Spending Score, which can help businesses understand customer behavior and create targeted marketing strategies.

Dataset

The dataset used is Mall_Customers.csv (or your dataset name), which contains:

Column	Description
CustomerID	Unique ID for each customer
Gender	Customer gender (Male/Female)
Age	Age of the customer
Annual Income (k$)	Customer income in thousand dollars
Spending Score (1-100)	Score assigned by the mall based on customer behavior
Steps in the Project

Import libraries: pandas, numpy, matplotlib, sklearn

Load dataset into a DataFrame

Select features (Annual Income, Spending Score)

Apply K-Means clustering with n_clusters=5

Visualize clusters using a scatter plot

Analyze clusters to understand different customer segments

Cluster Insights

Cluster 1 → “Big Spenders” (high income, high spending)

Cluster 2 → “Careful Savers” (high income, low spending)

Cluster 3 → “Moderate Customers” (middle income and spending)

Cluster 4 → “Bargain Hunters” (low income, high spending)

Cluster 5 → “Low Value Customers” (low income, low spending)

(You can adjust these labels based on your own analysis.)

How to Run


Install dependencies:

pip install -r requirements.txt


Run the script:

python kmeans_customer_segmentation.py

Libraries Used

pandas – data manipulation

numpy – numerical operations

matplotlib – data visualization

scikit-learn – machine learning (K-Means algorithm)
