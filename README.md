# DLT
## About dlt
dlt is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets.
## Table of contents
* [Installation of dlt](#Installation-of-dlt)
* [Introduction to dlt](#Introduction-to-dlt)
* [Features](#Features)
* [Building data pipeline with dlt](#Building-data-pipeline-with-dlt)
* [First pipeline](#First-pipeline)
## Installation of dlt
The following installation method is for linux users(ubuntu OS):
* First install python. To install python use command  ``` sudo apt-get install python```
* After python is installed, next go for pip installation. To install pip use the command  ``` sudo apt-get install pip ```
* Check python and pip version to make sure its installed properly. Use the following commands to check the version of python and pip: ```python --version``` and ```pip --version```
* Create a virtual enviornment. Perfom the following steps:
  ```pip install virtualenv
     $ python<version> -m venv <virtual-environment-name>
     $ mkdir /home/project
     $ cd /home/project
     $ python3.10 -m venv env
     $ source env/bin/activate

  ```
* To install dlt, we have install dlt package. To install the package we have to run the command
   ``` pip install dlt```
## Introduction to dlt
* We don't need to start any backend server or containers for dlt. Just need to import ```dlt``` in our python script and write a pipeline. The below code will give an idea about dlt:

 ```
import dlt
from dlt.sources.helpers import requests
# Create a dlt pipeline that will load
# chess player data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name='chess_pipeline',
    destination='duckdb',
    dataset_name='player_data'
)
# Grab some player data from Chess.com API
data = []
for player in ['magnuscarlsen', 'rpragchess']:
    response = requests.get(f'https://api.chess.com/pub/player/{player}')
    response.raise_for_status()
    data.append(response.json())
# Extract, normalize, and load the data
pipeline.run(data, table_name='player')
```


* The above code load the chess game data from chess.com API and store in DuckDB.

## Features
* Automated maintenance - with schema inference and evolution and alerts, and with short declarative code, maintenance becomes simple.
* User-friendly, declarative interface that removes knowledge obstacles for beginners while empowering senior professionals.
* Consistent and verified data before loading.
* Adapts to growing data needs in production.
* Load only new or changed data and avoid loading old records again.
  
## Building data pipeline with dlt
* dlt provides extact and load process.
* dlt is a powerful tool that allows to move data from your Python code to a destination with a single function call. By defining a pipeline, you can easily load, normalize, and evolve your data schemas, enabling seamless data integration and analysis.
* Lets look into an example below:
```
import dlt
pipeline = dlt.pipeline(destination="duckdb", dataset_name="country_data")

data = [
     {'country': 'USA', 'population': 331449281, 'capital': 'Washington, D.C.'},
    {'country': 'Canada', 'population': 38005238, 'capital': 'Ottawa'},
    {'country': 'Germany', 'population': 83019200, 'capital': 'Berlin'}
]

info = pipeline.run(data, table_name="countries")

print(info)
```
* Copy the code and save it as ``` <filename>.py```
* To run the script use the command ```python3 <filename>.py```
* Run the above code which gives the following output:
```
Pipeline dlt_simple_pipe completed in 2.16 seconds
1 load package(s) were loaded to destination duckdb and into dataset country_data
The duckdb destination used duckdb:////home/antony/Documents/dlt_simple_pipe.duckdb location to store data
Load package 1698944103.788485 is LOADED and contains no failed jobs
```
* In the above example pipeline function is used to create a pipeline with the specified destination (DuckDB) and dataset name ("country_data").
* run method--> to load the data from a list of objects into the table named "countries".
* info method--> variable stores information about the loaded data, such as package IDs and job metadata.
* To configure data we have--> write_dispositions,replace,append and merge.
* The below example shows to configure how the data is loaded with ```merge``` option:
```
import dlt

data = [{'id': 1, 'name': 'John'}]

# open connection
pipeline = dlt.pipeline(
    destination='duckdb',
    dataset_name='raw_data'
)

# Upsert/merge: Update old records, insert new
load_info = pipeline.run(
    data,
    write_disposition="merge",
    primary_key="id",
    table_name="users"
)

```
* In the above code you can see we have used ```write_disposition="merge"```
* Similarly we have option to get alert if there ia any change in the schema.

## First pipeline
* Install dlt package. If not install package using command ```pip install dlt```
* Initalize project--> Create a new empty directory for your dlt in /home/<your_directory>
* To create directory use command ```mkdir weatherapi_duckdb``` and to move to that directory use the command ```cd weatherapi_duckdb```
* Start a dlt project with a pipeline template that loads data to DuckDB by running the command ```dlt init weatherapi duckdb```
* By running above command we get the following output:
  ```
  Looking up the init scripts in https://github.com/dlt-hub/verified-sources.git...
A verified source weatherapi was not found. Using a template to create a new source and pipeline with name weatherapi.
Do you want to proceed? [Y/n]: y

Your new pipeline weatherapi is ready to be customized!
* Review and change how dlt loads your data in weatherapi.py
* Add credentials for duckdb and other secrets in ./.dlt/secrets.toml
* requirements.txt was created. Install it with:
pip3 install -r requirements.txt
* Read https://dlthub.com/docs/walkthroughs/create-a-pipeline for more information
 ``` 
  
 
  
  
