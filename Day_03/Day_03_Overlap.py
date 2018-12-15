#Imports
import pprint as p

#Variables


#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_03/"
text_file = open(folder_path + "input.txt", "r")
input_list = text_file.read().split('\n')
text_file.close()

#Create better claims_list from input_list
claims_list = input_list


#Print out value
p.pprint(claims_list)
