#Starting frequency
frequency = 0

#Create array from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_01/"
text_file = open(folder_path + "input.txt", "r")
frequencys = text_file.read().split('\n')

#Iterate across array
for freq in frequencys:
    if freq.strip() != "":
        val = float(freq.strip())
        frequency = frequency + val

#Find value.
print(frequency)
