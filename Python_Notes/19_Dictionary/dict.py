'''
Dictionary: Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

dct = {"Name": "Ryomen Sukuna", 
       "Section": "CD", 
       "Course": "Btech"}
print(dct, type(dct))
print(dct["Name"])
print(dct["Section"])
print(dct["Course"])