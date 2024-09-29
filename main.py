import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

# Load the dataset
data = pd.read_csv('dataset/deliveries.csv')

# Select relevant features
som_data = data[['over', 'ball', 'batsman_runs', 'extra_runs', 'total_runs', 'is_wicket']]

# Scale the data using Min-Max Scaler
scaler = MinMaxScaler()
som_data_scaled = scaler.fit_transform(som_data)

# Create a Self-Organizing Map (SOM)
som = MiniSom(x=10, y=10, input_len=som_data_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(som_data_scaled)
som.train_random(som_data_scaled, 500)

# Visualize the SOM U-Matrix
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar()
plt.title('SOM U-Matrix for IPL Deliveries')
plt.savefig('som_u_matrix_deliveries.png')
plt.show()

# Detect anomalies using Local Outlier Factor (LOF)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outliers = lof.fit_predict(som_data_scaled)

# Visualize the SOM with anomaly detection
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar()

# Plot points on SOM grid with anomalies
for i, x in enumerate(som_data_scaled):
    w = som.winner(x)
    if outliers[i] == -1:  # Outlier points
        plt.plot(w[0] + 0.5, w[1] + 0.5, 'rx', markersize=12, markeredgewidth=2)
    else:  # Normal points
        plt.plot(w[0] + 0.5, w[1] + 0.5, 'bo', markersize=12, markeredgewidth=2)

plt.title('SOM with Anomaly Detection on IPL Deliveries')
plt.savefig('som_with_anomalies_deliveries.png')
plt.show()
