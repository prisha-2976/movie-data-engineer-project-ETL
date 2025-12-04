Automated Movie Data ETL Pipeline Using Airflow

📘 Project Overview

This project is a simple and  ETL (Extract–Transform–Load) pipeline built using:

1- TMDB API (for extracting movie data)

2- Pandas (for transforming and cleaning data)

3- Airflow (for scheduling and automating the workflow)

4- AWS EC2 (for running Airflow in the cloud)

5- The pipeline runs automatically every day and stores popular movie data in CSV format.

🚀 What This Project Does

* Extracts movie data from the TMDB API
* Transforms the raw JSON into a clean Pandas DataFrame
* Loads the final output as a CSV file
* Automates the entire pipeline using Apache Airflow
* Runs daily on an AWS EC2 instance


🛠 Technologies Used

Apache Airflow -	Workflow orchestration & scheduling
TMDB API -	Data source for movie information
Python -	ETL logic
Pandas -	Data cleaning & transformation
AWS EC2	Server - hosting the Airflow environment
Ubuntu -	OS for running Airflow
Virtual Environment (venv) -	Python environment isolation

📂 Project Structure
Movie_Data_Engineer_Project(ETL)

      ├── tmdb.py            # ETL logic
      └── tmdb_dag.py        # Airflow DAG for automation


🧩 How the Pipeline Works
1️ Extract

The pipeline calls the TMDB API to fetch the latest popular movie data.

2️ Transform

Using pandas, the raw JSON is cleaned and converted into a structured table (DataFrame).

3️ Load

The final DataFrame is saved as a CSV file inside the EC2 server.

4️ Automate

Airflow schedules and runs the ETL pipeline every day automatically.

## Airflow DAG Flow

* Start DAG

* Execute Python ETL function (run_tmdb_etl)

* Save CSV

* Task completes & waits for next scheduled run

## DAG Scheduling

The pipeline runs daily using Airflow’s schedule:


📌 Why This Project Is Useful

Shows understanding of ETL pipelines

Demonstrates skills with APIs, Python, Pandas, Airflow, and AWS

Reflects real-world Data Engineering workflow automation

🧑‍💻 Future Improvements

Push data into Amazon S3

Load into a data warehouse like Redshift or BigQuery

Add data quality checks

Add notifications on DAG success/failure

👩‍🎓 Made By

Prisha Verma
