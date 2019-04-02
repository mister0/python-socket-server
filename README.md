# This repository contains a simple socket server written in python
## The server receives events and write them to comma separated file 

Before running this application you need to make sure : 

* You have python3 installed [here](https://realpython.com/installing-python/)
* You have `pip3` installed [here](https://pypi.org/project/pip/)
* You have google proto buffer python package installed using the command 
`pip3 install protobuf`

#### To run the server, in the server folder use the terminal to run `python3 socket-server.py`
##### If you want to verify the server is running correctly you can run the sample client from terminal using `python3 socket-client.py`
##### Observe how the server appends the data to `events.csv` file