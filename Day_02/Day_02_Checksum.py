#Imports
import pprint as p

#Variables
checksum = 0
value_list = [0,0]

#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_02/"
text_file = open(folder_path + "input.txt", "r")
box_ids = text_file.read().split('\n')
text_file.close()

#Iterate through list
for box_id in box_ids:
    test_list = [False,False]
    #Iterate through each box_id
    for char in box_id:
        #Test if box_id has a char repeating 2 or 3 times
        temp = box_id.count(char)
        if temp == 2: test_list[0] = True
        if temp == 3: test_list[1] = True
    #Add value to correct item
    if test_list[0]: value_list[0] += 1
    if test_list[1]: value_list[1] += 1

#Create checksum
checksum = value_list[0] * value_list[1]

#Print out value
p.pprint(value_list)
print("Checksum: " + str(checksum))
