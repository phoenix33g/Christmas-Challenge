#Imports
import pprint as p
import numpy as np

#Variables
value = ""
destruction = True
skip = False
count = 0

#Functions
def annihilates(str_1, str_2):
    output = False
    temp = str_1.swapcase()
    if temp == str_2: output = True
    return output

#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_05/"
text_file = open(folder_path + "input.txt", "r")
input_str = text_file.read()
text_file.close()
value = input_str

#While loop to test if any more can be destroyed
while destruction:
    #Set some helpful variables
    count += 1
    temp_str = ""
    skip = False
    end_str = value[len(value)-1]
    destruction = False
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

#Print out value
#p.pprint(value)
print("amount in og: " + str(len(input_str)))
print("amount in new: " + str(len(value)))
