from fnmatch import fnmatch
import agate 
import re
import datetime


monthlytable = agate.Table.from_csv('2015-10-30.csv')

# selects which tables to use; lamba means this is a function that I'm just using once, throwing away, sorta. 
# new_table = monthlytable.where(lambda row: re.match('Served', row['Reservation Status']))


# tables separated by AGE
youth = monthlytable.where(lambda row: 0 < row['age'] < 18)
adult = monthlytable.where(lambda row: 17 < row['age'] < 59)
elderly = monthlytable.where(lambda row: 59 < row['age'])

# tables - now separate by gender
youthf = youth.where(lambda row: row['gender'] == 'F')
youthm = youth.where(lambda row: row['gender'] == 'M')

adultf = adult.where(lambda row: row['gender'] == 'F')
adultm = adult.where(lambda row: row['gender'] == 'M')

elderlyf = elderly.where(lambda row: row['gender'] == 'F')
elderlym = elderly.where(lambda row: row['gender'] == 'M')

# I could also use a pivot, but I'm being explicit, for the sake of learning 
# and ensuring I don't screw up
# http://agate.readthedocs.org/en/1.3.0/cookbook/transform.html

# aggregate the count for all
cmhayouthf = youthf.aggregate(agate.Count('housing_other', 'CMHA'))
cmhayouthm = youthm.aggregate(agate.Count('housing_other', 'CMHA'))

cmhaadultf = adultf.aggregate(agate.Count('housing_other', 'CMHA'))
cmhaadultm = adultm.aggregate(agate.Count('housing_other', 'CMHA'))

cmhaelderlyf = elderlyf.aggregate(agate.Count('housing_other', 'CMHA'))
cmhaelderlym = elderlym.aggregate(agate.Count('housing_other', 'CMHA'))


print("For CMHA clients")
print("Youth F clients this month:",(cmhayouthf))
print("Youth M clients this month:",(cmhayouthm))
print("adult F clients this month:",(cmhaadultf))
print("Youth M clients this month:",(cmhayouthm))
print("Elderly F clients this month",(cmhaelderlyf))
print("Elderly M clients this month:",(cmhaelderlym))


cmhatotalm = cmhayouthm + cmhaelderlym + cmhaadultm
print("Total CMHA - M clients",(cmhatotalm))

cmhatotalf = cmhayouthf + cmhaelderlyf + cmhaadultf
print("Total CMHA - F clients",(cmhatotalf))

#print(type(youthm))
#print(type(cmhayouthm))
	
print("Non-CMHA clients below:")

otheryouthf = ((youthf.aggregate(agate.Count()) - cmhayouthf))
otheryouthm = ((youthm.aggregate(agate.Count()) - cmhayouthm))
otheradultf = ((adultf.aggregate(agate.Count()) - cmhaadultf))
otheradultm = ((adultm.aggregate(agate.Count()) - cmhaadultm))
otherelderlyf = ((elderlyf.aggregate(agate.Count()) - cmhaelderlyf))
otherelderlym = ((elderlym.aggregate(agate.Count()) - cmhaelderlym))

print("NON-CMHA Youth females",(otheryouthf))

print("NON-CMHA Youth males",(otheryouthm))

print("NON-CMHA Adult females",(otheradultf))

print("NON-CMHA Adult males",(otheradultm))

print("NON-CMHA Elderly females",(otherelderlyf))

print("NON-CMHA Elderly males",(otherelderlym))


othertotalm = otheryouthm + otherelderlym + otheradultm
print("Total Non-CMHA - M clients",(othertotalm))

othertotalf = otheryouthf + otherelderlyf + otheradultf
print("Total NON-CMHA - F clients",(othertotalf))


# counts the number of houses for the households that were served; 
# sauce = monthlytable.aggregate(agate.Count('Reservation Status', 'Served'))

# totalppl = monthlytable.aggregate(agate.Count(new_table))

