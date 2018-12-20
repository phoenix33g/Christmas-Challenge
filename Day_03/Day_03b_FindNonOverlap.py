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

#Create better claims_list from input_list
for claim in input_list:
    temp_id = claim.split("@")[0].strip()
    temp_location = claim.split("@")[1].strip().split(":")[0].strip().split(",")
    temp_location[0] = int(temp_location[0])
    temp_location[1] = int(temp_location[1])
    temp_size = claim.split("@")[1].strip().split(":")[1].strip().split("x")
    temp_size[0] = int(temp_size[0])
    temp_size[1] = int(temp_size[1])
    claim_dic = {
        'id': temp_id,
        'location': temp_location,
        'size': temp_size
    }
    claims_list.append(claim_dic)

    #Find min and max area (max_area)
    if max_area[0] > temp_location[0]: max_area[0] = temp_location[0]
    if max_area[1] > temp_location[1]: max_area[1] = temp_location[1]
    if max_area[2] < temp_location[0] + temp_size[0]: max_area[2] = temp_location[0] + temp_size[0]
    if max_area[3] < temp_location[1] + temp_size[1]: max_area[3] = temp_location[1] + temp_size[1]

#Create blank area_array using max_area
area_array = np.zeros( (max_area[3], max_area[2]) )

#Fill area array with claims
for claim in claims_list:
    height_start = claim.get('location')[1]
    height_end = claim.get('location')[1] + claim.get('size')[1]
    width_start = claim.get('location')[0]
    width_end = claim.get('location')[0] + claim.get('size')[0]
    area_array[height_start:height_end ,width_start:width_end] += 1

#Find claim that only contains 1's
for claim in claims_list:
    height_start = claim.get('location')[1]
    height_end = claim.get('location')[1] + claim.get('size')[1]
    width_start = claim.get('location')[0]
    width_end = claim.get('location')[0] + claim.get('size')[0]
    #Create an array per claim from area_array
    claim_array = area_array[height_start:height_end ,width_start:width_end]
    #Find values in claim_array that are greater than 1
    test = True
    for temp_array in claim_array:
        for i in temp_array:
            if i > 1: test = False
    #Append claim id to value for all non-overlaping clamis
    if test: value.append(claim.get('id'))

#Print out value
p.pprint(value) #Note: The id (value) can not include '#' when submitted
