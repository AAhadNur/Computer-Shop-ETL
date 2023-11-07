    ███████╗████████╗██╗
    ██╔════╝╚══██╔══╝██║
    █████╗     ██║   ██║
    ██╔══╝     ██║   ██║
    ███████╗   ██║   ███████╗
    ╚══════╝   ╚═╝   ╚══════╝

# Automated Web Data Collection and ETL Workflow

The project involves scraping laptop data from 2 websites ( ryans.com and startech.com ) with Scrapy,
data manipulation with Pandas and regular expression, and data storage in PostgreSQL using SQLAlchemy.Powered by Apache Airflow, it streamlines the data pipeline for seamless insights.

## Architecture

![Architecture](https://github.com/AAhadNur/Computer-Shop-ETL/blob/main/resources/media/Laptop_Shop_Project_Architecture.png)

The project is organized into several key components:

- `ExtractingLaptopData`: This directory contains the web scraping scripts for extracting data from e-commerce websites. Spiders are defined for each website, and data is stored in JSON format.

- `TransformScripts`: In this directory, you'll find data cleaning and transformation scripts to prepare the scraped data for storage in the database.

- `LoadData`: The scripts here manage the insertion of cleaned data into a PostgreSQL database using SQLAlchemy.

- `database`: This directory defines the database schema and settings.

- `airflow_dags`: The Apache Airflow DAG that orchestrates the entire data pipeline is located here.

## Installation Guide

### Clone the repository to your local machine

```shell
git clone https://github.com/AAhadNur/Computer-Shop-ETL.git
```

### Set up a Python virtual environment and install project dependencies

```shell
cd Computer-Shop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Scrapy settings and Proxy Rotation Middleware with ScrapeOps

My project utilizes the ScrapeOps proxy rotation middleware to enhance web scraping by rotating through a pool of fake browser headers for each request. This section explains how to configure and enable this middleware.

#### Setting Up ScrapeOps API Key

1. Create a `.env` file in your project directory if you don't already have one.

2. Create an account in the [ScrapeOps](https://scrapeops.io/app/register/main) and collect you API key.

3. Add your ScrapeOps API key to the `.env` file using the following format:

```
SCRAPEOPS_API_KEY = your_api_key
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5
```

#### Middleware Configuration

The ScrapeOps proxy rotation middleware is already integrated and enabled by default into the project.If you wish to disable it, set the `SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED` to `False` in your Scrapy project settings.

### Configure your database settings in `LoadData/dbSettings.py`

1. Create a `.env` file in the project base directory.

2. Add your database credentials to the `.env` file using the following format:

```
username = your_database_username
password = your_database_user_password
host = 'localhost'
database_name = your_database_name
```

3. If you want to use another database server rather than PostgreSQL then you also need to change the `connection_string` in the `LoadData/dbSettings.py` file.

### Apache Airflow configuration

1. Open a terminal and navigate to the root directory of the project.

2. Create `AIRFLOW_HOME` variable in the shell by running the following command:

```shell
export $AIRFLOW_HOME = your_root_project_directory_full_path
```

for me your_root_project_directory_full_path is `/home/a_ahad/Desktop/Workshop/Computer-Shop/Computer-Shop`

3. Create Airflow Database by running:

```shell
airflow db init
```

4. Create a super user by running:

```shell
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```

5. Run the Airflow Webserver:

```shell
airflow webserver -p 8080
```

6. Run the Airflow Scheduler:

```shell
airflow scheduler
```

7. Trigger the dedicated dag:

```shell
airflow trigger_dag my_datapipeline_dag
```

## Contribution

We welcome contributions to this project, and we appreciate your help in making it even better. To contribute effectively, please follow these guidelines:

### Creating Issues

- Before working on a new feature or bug fix, check the project's issue tracker to see if there are related issues or feature requests.
- If you find a relevant issue, feel free to comment on it to express your interest in working on it. This helps coordinate efforts.
- If the issue doesn't exist, you can create a new one. Provide a clear and detailed description of the problem or feature you plan to address.

### Coding Style and Standards

- Follow the project's coding style and standards. These may include naming conventions, code formatting, and best practices specific to the project.
- Ensure that your code is well-documented with clear comments and docstrings. This makes it easier for others to understand and maintain your code.
- Keep your codebase clean by removing unnecessary comments, debugging statements, or unused code.

### Branching and Pull Requests

- Fork the repository and create your branch from the `main` branch.
- Use a descriptive branch name that reflects the purpose of your changes (e.g., `feature/new-feature` or `bugfix/issue-description`).
- Make small, focused commits with clear and concise commit messages.
- Test your changes thoroughly to ensure they do not introduce new issues.
- If you're addressing an existing issue, reference it in your commit message using the format `Fixes #issue-number` or `Closes #issue-number`.
- Submit a pull request to the `main` branch with a clear and brief description of your changes.

We value your contributions and will review your pull request as soon as possible. Thank you for helping improve the project!

## Author

- [Abdul Ahad Nur](https://github.com/AAhadNur)
- Contact: ahadnur0001@gmail.com

## Expectations

'Computer-Shop' is developed with the aim of simplifying web data extraction, cleaning, and storage. Here's what you can expect from this project:

- Efficient web scraping of laptop data from various e-commerce websites.
- Reliable data cleaning and transformation for structured information.
- Secure storage of cleaned data in a PostgreSQL database.
- Seamless orchestration of the entire data pipeline using Apache Airflow.

## Future Work

In the future, I plan to enhance and expand the 'Computer-Shop' project in the following ways:

- Add support for more e-commerce websites to extract a wider range of laptop data.
- Implement advanced data analysis and visualization features for deeper insights.
- Enhance the proxy rotation middleware for even more reliable web scraping.
- Develop user-friendly configuration and management tools for the project.

### Cloud Implementation

In the near future, we have plans to implement cloud-based features, including:

- Migrating data storage to cloud services for scalability and accessibility.
- Leveraging cloud computing resources to enhance data processing capabilities.
- Implementing automated deployment and scaling to accommodate increased workloads.

Stay tuned for updates on our cloud implementation efforts as we continue to evolve and improve the 'Computer-Shop' project.

## Project Video

[![Video](https://img.youtube.com/vi/LBU9KFj5-_o/0.jpg)](https://www.youtube.com/watch?v=LBU9KFj5-_o)
