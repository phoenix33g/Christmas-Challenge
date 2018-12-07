#Starting frequency
frequency = 0
stepArr = [frequency]
i = 0
output = 0
quit = True

#Create array from input.txt file
folder_path = "D:/_SCRIPTING/_ScriptProjects/25DaysTillChristmas-GITHUB/Day_01/"
text_file = open(folder_path + "input.txt", "r")
frequencys = text_file.read().split('\n')

#While loop to find value
while quit:
    if i > len(frequencys)-1:
        i=0
    freq = frequencys[i]
    val = int(freq.strip())
    frequency = frequency + val
    #Create secondary array with all iterated values
    stepArr.append(frequency)

    #Find first repeated value in array
    count_val = stepArr.count(stepArr[-1])
    if count_val != 1:
        output = stepArr[-1]
        quit = False
    #for a in stepArr:
    #    count_val = stepArr.count(a)
    #    if count_val != 1:
    #        output = a
    #        quit = False
    #        break
    #print('PASS')
    i += 1

#Print value
print(output)
