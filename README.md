# A small flask API to recolt and format logs from various python processes

*Destined initially to collect logs from jupyterhub sessions. If you want to use this service for this usage, you have to modify the jupyter notebook source code to send the log messages to the API: follow the commits from the [APHP version of notebook](https://github.com/EDS-APHP/notebook/commits/master).*

+ The [root_listen.py](https://github.com/strayMat/logs_api/blob/master/root_listen.py) file is the model of the API with configurable ip, port and formatting.
+ The [send_logs.py](https://github.com/strayMat/logs_api/blob/master/root_listen.py) file shows the code to be added to python services that we want to record the activity.

## Usage 

1- Launch the API as a service from the collector user with `python root_listen`

2- Launch the command `python send_logs.py` to send an example log to the api

3- The logs are recorded in a newly created `record` directory (instanced in the same folder as the two other .py file). 

