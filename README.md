# DLT
## About dlt
dlt is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets.
## Table of contents
* [Installation of dlt](#Installation-of-dlt)
* [Introduction to dlt](#Introduction-to-dlt)
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
     $ source ./env/bin/activate
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
pipeline.run(data, table_name='player')```


* The above code load the chess game data from chess.com API and store in DuckDB.
 
  
  
