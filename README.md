# Backend Challenge

Race Average  
Assumptions: Start time is 8:00 AM, DAY 1. Finish times in same timezone as start time. If empty list is provided return -1.  

average_minutes(list_of_finish_times:[]) returns the average race time given a list of finish times(strings).  

get_minutes_per_race(race_time: str) returns the total minutes taken for a single race given a finish time.   
 
parse_date(race_time: str) returns each component of the given race time.  

round_average(average: float) rounds the average race times appropriately (since Python's round() does not always round up on .5)   

## Usage
The program takes a string of finish times separated by pipes (' | ') where each finish time is formatted as follows: hh:mm xM, DAY n. 


Sample input:  
$ python race_average.py "02:00 PM, DAY 19|02:00 PM, DAY 20|01:58 PM, DAY 20"

Setup:  
python3 -m venv env
source env/bin/activate  
pip install pytest 


To run:   
python race_average.py "input string"

To run tests:  
pytest race_average_test.py
 