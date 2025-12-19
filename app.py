import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -----------------------------
# App Title
# -----------------------------
st.title("Customer Segmentation using K-Means")
st.markdown("""
This app allows you to segment customers based on **Annual Income** and **Spending Score** using K-Means clustering.
""")

# -----------------------------
# Upload CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload your CSV file (Mall_Customers.csv)", type="csv")

if uploaded_file is not None:
    # Read dataset
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Select features
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

    # Number of clusters
    n_clusters = st.slider("Select number of clusters:", 2, 10, 5)

    # Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    data['Cluster'] = kmeans.fit_predict(X)

    # Show cluster summary
    st.subheader("Cluster Summary")
    cluster_summary = data.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()
    st.dataframe(cluster_summary)

    # -----------------------------
    # Plot clusters
    # -----------------------------
    st.subheader("Cluster Visualization")
    plt.figure(figsize=(8,5))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'orange', 'purple', 'brown', 'pink']

    for i in range(n_clusters):
        plt.scatter(
            X[data['Cluster'] == i].iloc[:, 0],
            X[data['Cluster'] == i].iloc[:, 1],
            s=50,
            c=colors[i],
            label=f'Cluster {i+1}'
        )

    # Plot centroids
    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s=200,
        c='black',
        marker='X',
        label='Centroids'
    )

    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.title("Customer Segments")
    plt.legend()
    st.pyplot(plt)

else:
    st.warning("Please upload a CSV file to run the app.")
