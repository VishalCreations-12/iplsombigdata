## IPL Deliveries Anomaly Detection with SOM (Bash Script)

This script installs dependencies, runs the Python script, and organizes outputs.

**Requirements:**

* Linux system with bash shell
* `pip` installed

**Steps:**

1. **Clone or Download Project:** Replace `<project_url>` with the actual project URL.

```bash
git clone <project_url>
```

2. **Install Dependencies:**

```bash
cd IPL_Deliveries_SOM  # Change directory to project folder
pip install -r requirements.txt
```

3. **Run Script and Generate Outputs:**

```bash
python src/main.py

mv som_u_matrix_deliveries.png visuals/  # Move visualization to visuals folder
mv som_with_anomalies_deliveries.png visuals/
```

**Explanation:**

* This script assumes the project is cloned or downloaded into a folder named `IPL_Deliveries_SOM`.
* `pip install -r requirements.txt` installs all necessary libraries listed in the `requirements.txt` file.
* `python src/main.py` executes the main Python script located in the `src` folder.
* The `mv` commands move the generated visualization files (`som_u_matrix_deliveries.png` and `som_with_anomalies_deliveries.png`) to a folder named `visuals`. 

