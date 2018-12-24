#Imports
import pprint as p
import numpy as np
import re
from string import ascii_lowercase

#Variables
values_list = []
output_list = []
output = 99999
removed_unit = 'a'

#Functions
def annihilates(str_1, str_2):
    output = False
    temp = str_1.swapcase()
    if temp == str_2: output = True
    return output

def annihilationOutput(value):
    count = 0
    destruction = True
    skip = False
    #While loop to test if any more can be destroyed
    while destruction:
        #Set some helpful variables
        count += 1
        temp_str = ""
        end_str = value[len(value)-1]
        destruction = False
        skip = False
        #Itterate through text
        for i in range( len(value) - 1 ):
            if skip:
                skip = False
            else:
                str_1 = value[i]
                str_2 = value[i + 1]
                boom = annihilates(str_1, str_2)
                if boom:
                    skip = True
                    destruction = True
                    if i == len(value)-2: end_str = ""
                else:
                    temp_str += str_1
                    temp_str_2 = str_2
        #if count > 0 and count < 10: print("---" + value[len(value)-20:len(value)] + "---")
        value = temp_str + end_str
    return value


#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_05/"
text_file = open(folder_path + "input.txt", "r")
input_str = text_file.read()
text_file.close()

#Create a list of values with each unit type removed
for abc in ascii_lowercase:
    AB = abc.upper()
    values_list.append(re.sub(abc+"|"+AB, "", input_str))

#Create a list of removed Units
for val in values_list:
    output_list.append(annihilationOutput(val))

#Find lowest count
i = 0
for out in output_list:
    if len(out) < output:
        output = len(out)
        removed_unit = ascii_lowercase[i]
    i += 1

#Print out value
print("amount in original list: " + str(len(input_str)))
print("amount in new list: " + str(output))
print("Unit removed: " + removed_unit)
