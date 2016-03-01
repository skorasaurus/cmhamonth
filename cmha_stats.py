#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fnmatch import fnmatch
import agate 
import re
import datetime

julytable = agate.Table.from_csv('2.3-july.csv')

# selects which tables to use; lamba means this is a function that I'm just using once, throwing away, sorta. 
# new_table = julytable.where(lambda row: re.match('Served', row['Reservation Status']))

#CMHA by age ranges 

# youth = julytable.where(lambda row: 0 < row['age'] < 19)
# adult = julytable.where(lambda row: 18 < row['age'] < 54)
# elderly = julytable.where(lambda row: 55 < row['age'] < 180)



# this works; 
cmhatotal = julytable.aggregate(agate.Count('housing_other', 'CMHA'))
print "Total CMHA Clients served:", cmhatotal

# create table only of CMHA clients
cmhatable = julytable.where(lambda row: row['housing_other'] == 'CMHA')

# now filter this 
youth = cmhatable.where(lambda row: 0 < row['age'] < 19)
adult = cmhatable.where(lambda row: 18 < row['age'] < 54)
elderly = cmhatable.where(lambda row: 55 < row['age'] < 180)

CMHAelderlycount = len(elderly.rows)
CMHAadultcount = len(adult.rows)
CMHAyouthcount = len(youth.rows)

print "elderly clients this month",(CMHAelderlycount)
print "elderly clients this month",(CMHAadultcount)
print "Youth clients this month",(CMHAyouthcount)




# elderlycount = julytable.aggregate(agate.Count(elderly))
# print "CMHA seniors are:", elderlycount


# counts the number of houses for the households that were served; 
# sauce = julytable.aggregate(agate.Count('Reservation Status', 'Served'))

# totalppl = julytable.aggregate(agate.Count(new_table))

