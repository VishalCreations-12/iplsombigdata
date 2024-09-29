Self Organizing Map And Anomalies Detection Using Neural Networks On IPL Deliveries Dataset Overview This project implements a Self-Organizing Map (SOM) using neural networks on the IPL Deliveries dataset.
The tool visualizes the results and identifies anomalies in the dataset.

Hardware Requirements To run this project effectively, ensure that your system meets the following hardware specifications:

Processor: Dual-core processor (Intel i3 or equivalent) 
RAM: Minimum 4GB Disk Space: At least 500MB for the dataset and environment 
Operating System: Windows, macOS, or any Linux distribution Software Requirements

Ensure you have the following software installed:

Python Version: Python 3.8 or higher Required Libraries The following libraries are required for the project. 

Install them using the provided requirements.txt file:

numpy
pandas
matplotlib 
scikit-learn
minisom 
   
Installation Steps Follow these steps to set up the environment and execute the project:

Install Required Libraries Open a terminal and run the following command to install the necessary libraries:

pip install -r requirements.txt Run the Main Script Navigate to the directory where the main.py file is located and execute the script:

python src/main.py Output Files Upon successful execution of the program, you will find two visual output files generated in the visuals folder:

som_u_matrix_deliveries.png: This file contains the visual representation of the Self-Organizing Map. som_with_anomalies_deliveries.png: This file highlights the identified anomalies in the dataset.