Python script to obtain monthly statistics of our pantry for CMHA

wHY:
I need to calculate the number of people that live in CMHA (Cuyahoga Metropolitan Housing Authority) housing 
that our pantry serves within specific age ranges each month.

With a monthly file that I receive (see sample.csv for its structure and contents) from Pantrytrak, 
I specify the input file in cmhamonth.py, run it, and it returns the number of people who live in CMHA that we served and 
split by age ranges.

This could also provide some additional examples for people learning python and agate.

To run: `python cmhamonth.py`

This runs on python 2.7; has not been tested on python 3

You must also install the following packages before using; most recent version of these packages are fine. 

agate

re

fnmatch

datetime

