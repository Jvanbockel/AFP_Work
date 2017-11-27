rainfall = []

values = input("Enter the average rainfall in your area"
                 " for each month. Separate values with commas: ")

rainFall = values.split(',')
print(rainFall)

print("Max rainfall is: ",max(rainFall))
print("Min rainfall is: ",min(rainFall))

total = 0
for x in rainFall:
    total += int(x)

for i in range(len(rainFall)):
    len = int(rainFall[i])

average = total / len
print("The average rainfall is: ",round(average,2))
print("The total rainfall is: ",total)



