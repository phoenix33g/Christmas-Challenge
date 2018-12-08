#Imports
import pprint as p

#Variables
checksum = 0
value_list = [0,0]

#Create array from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_02/"
text_file = open(folder_path + "input.txt", "r")
box_ids = text_file.read().split('\n')

#Print out value
p.pprint(box_ids)
