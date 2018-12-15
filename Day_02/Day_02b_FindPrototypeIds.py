#Imports
import pprint as p

#Variables
ids_list = []

#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_02/"
text_file = open(folder_path + "input.txt", "r")
box_ids = text_file.read().split('\n')
text_file.close()

#Iterate through list
for i in range(len(box_ids)-1):
    box_id = box_ids[i]
    #Iterate through remaining list
    for j in range(i+1, len(box_ids)):
        test_id = box_ids[j]
        test_value = 0
        temp_id = ""
        #Iterate through each box_id
        for x in range(len(box_id)):
            #Test difference between box_id and test_id
            if box_id[x] != test_id[x]:
                test_value += 1
            else:
                temp_id += box_id[x]
        #Find and append ids with specified characteristics to ids_list
        if test_value == 1: ids_list.append(temp_id)

#Print out value
p.pprint(ids_list)
