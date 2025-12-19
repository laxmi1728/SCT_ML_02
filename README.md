Customer Segmentation using K-Means Clustering

This project demonstrates customer segmentation using the K-Means clustering algorithm on the popular Mall Customers dataset.
It helps businesses understand customer behavior based on Annual Income and Spending Score, and visually explore different customer groups.

The project includes:

A machine learning script for clustering and visualization

An interactive Streamlit web app for real-time exploration

 Project Overview:

Customer segmentation is a key application of unsupervised machine learning.
In this project, customers are grouped into clusters based on:

Annual Income (k$)

Spending Score (1–100)

The K-Means algorithm is used to identify meaningful customer segments that can help in:

Targeted marketing

Business strategy planning

Customer behavior analysis
Project Structure
customer-segmentation-ml/
│
├── Mall_Customers.csv          # Dataset
├── customer_segmentation.py    # K-Means clustering + visualization
├── app.py                      # Streamlit web application
├── README.md                   # Project documentation

 Dataset Description:

File: Mall_Customers.csv

Column Name	Description
CustomerID	Unique customer identifier
Gender	Customer gender
Age	Customer age
Annual Income (k$)	Annual income in thousands
Spending Score (1-100)	Spending behavior score

 Technologies Used:

Python

Pandas – Data handling

Matplotlib – Data visualization

Scikit-learn – K-Means clustering

Streamlit – Web application

Machine Learning Approach:

Load and explore the dataset

Select relevant features:

Annual Income

Spending Score

Use the Elbow Method to determine optimal clusters

Apply K-Means clustering

Visualize customer segments and centroids

 How to Run the Project:
 
-> Clone the Repository
git clone https://github.com/your-username/customer-segmentation-ml.git
cd customer-segmentation-ml

-> Install Required Libraries
pip install pandas matplotlib scikit-learn streamlit

->Run the ML Script (Optional)
python customer_segmentation.py


This will:

Apply K-Means clustering

Display elbow method and cluster visualization

4️ Run the Streamlit App:
streamlit run app.py


📌 Upload Mall_Customers.csv when prompted in the app.

 Streamlit App Features:

CSV file upload

Interactive cluster selection (slider)

Dataset preview

Cluster-wise summary statistics

Real-time visualization of customer segments

Cluster centroids display

Output Visualization:

Scatter plot of customer clusters

Each cluster shown in a different color

Centroids marked clearly

Easy interpretation of customer groups

 Use Cases:

Market segmentation

Personalized marketing strategies

Business decision support

Beginner-friendly ML project for portfolios
