# taxfix-event-validator
A Program to validate events schema and count the number of event objects present in the input JSON file.

# How to run

Dependencies:
Python 3.8
JsonSchema 4.3.2

Create Virtual Environment
python -m venv env

Activate virtual environment:
source env/bin/activate

Install Packages
pip install -r requirements.txt

Run program
python taxfix.py

# Approach

The program has two functionalities:
1) validates the schema of the JSON objects from the input file
2) counts the number of events occuring for on each date.
3) We are to assume the input json file has infinite events and cannot be loaded at once in memory.

## Schema Validation
- For schema validation I'm using the **jsonschema** module in python. 
- We define a schema specification against which we will compare the schema of each of our input JSON objects.

## Events Count
The count of number of events per date is as follows:
- I'm maintaining a dictionary which will have a structure as follows:
     {'date' : { 'eventName' : count_of_event } }
- First I check whether a date is already in my dictionary if not then I insert it in the dictionary and initialize its values with name of the event and count as 1
- If date is already in the event_count dictionary, I check whether an event is already present against the date in the dictonary and if not then it is inserted for that date with count as 1.
- if event is already present for the given date then count for that event is just incremented.
- Lastly we just print the counts for each event for each date.

## Opening infinitly large files
To tackle this issue, we are using **python iterators**. Since the file is very big we can not open and load it all at once in memory. The open method in python is iterable and also an iterator which yeilds one line at a time. It creates a fileobject on the given file which can then be used to traverse the file. This comes in handy to read very large files that can't fit in memory.

