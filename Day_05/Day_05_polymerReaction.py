#Imports
import pprint as p
import numpy as np

#Variables
claims_list =[]
max_area = [9999,9999,0,0] #[left, top, right, bottom]
value = []

#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_03/"
text_file = open(folder_path + "input.txt", "r")
input_list = text_file.read().split('\n')
text_file.close()


#Print out value
p.pprint(value) #Note: The id (value) can not include '#' when submitted
