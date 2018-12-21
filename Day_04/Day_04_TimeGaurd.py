#Variables
time_list =[]
guard_list = []
guard_id = "0"
mins_asleep = 0
value = 0

#Functions
def search(name, search_for, search_list):
    return [element for element in search_list if element[name] == search_for]

def getCount(name, search_for, search_list):
    for i in range(len(search_list)):
        element = search_list[i]
        if element[name] == search_for:
            return i

#Create list from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_04/"
text_file = open(folder_path + "input.txt", "r")
input_list = text_file.read().split('\n')
text_file.close()
#Order input_list by time
input_list.sort()

#Create better time_list from input_list
for time in input_list:
    #Reworking dates to fit mold (Fixing guard starts work day before issue)
    temp_date = time.split("[")[1].split("]")[0]
    temp_info = time.split("]")[1].strip()
    temp_date_day = temp_date.split(" ")[0]
    temp_month = int(temp_date_day.split("-")[1])
    temp_day = int(temp_date_day.split("-")[2])
    temp_time = temp_date.split(" ")[1]
    temp_hr = int(temp_time.split(":")[0])
    temp_min = int(temp_time.split(":")[1])
    if temp_hr == 23:
        temp_min = 0
        temp_day += 1
    temp_ddate = str(temp_month) + "-" + str(temp_day)
    #Create list of dictionaries based off time
    starts_shift = bool(temp_info.find("Guard #")+1)
    asleep_bool = bool(temp_info.find("falls asleep")+1)
    awake_bool = bool(temp_info.find("wakes up")+1)
    if starts_shift:
        temp_id = int(temp_info.split("#")[1].split(" ")[0])
        temp_mins_list = []
        guard_dic = {
            'id': temp_id,
            'date': temp_ddate,
            'asleep_list': temp_mins_list
        }
        time_list.append(guard_dic)
    elif asleep_bool:
        time_list[-1].get("asleep_list").append(temp_min)
    elif awake_bool:
        start_sleep = time_list[-1]["asleep_list"][-1] + 1
        end_sleep = temp_min
        for i in range(start_sleep, end_sleep):
            time_list[-1].get("asleep_list").append(i)

#Create guard_list from time_list
for time in time_list:
    guard_exists = bool( len( search('id', time.get('id'), guard_list) ) )
    guard_mins_asleep = time.get('asleep_list')
    if guard_exists:
        i = getCount('id', time.get('id'), guard_list)
        guard_list[i]['mins_asleep'] += len(guard_mins_asleep)
        guard_list[i]['asleep_list'].extend(guard_mins_asleep)
    else:
        guard_dic = {
            'id': time.get('id'),
            'mins_asleep': len(guard_mins_asleep),
            'asleep_list': guard_mins_asleep
        }
        guard_list.append(guard_dic)

#Find Guard (guard_id) and minutes asleep (mins_asleep)
for guard in guard_list:
    temp_list = guard.get('asleep_list')
    temp_mins_asleep = guard.get('mins_asleep')
    if value < temp_mins_asleep:
        count = 0
        value = temp_mins_asleep
        guard_id = guard.get('id')
        for m in temp_list:
            temp_count = temp_list.count(m)
            if count < temp_count:
                mins_asleep = m
                count = temp_count


#Find value by multipling guard_id and mins_asleep
value = guard_id * mins_asleep

#Print out value
#p.pprint(input_list)
print("Guard ID: #" + str(guard_id))
print("Minutes Asleep: " + str(mins_asleep) + "mins")
print(value)
