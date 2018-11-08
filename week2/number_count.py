import re
list = []
file = open('regex_sum_81834.txt')
for line in file:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    #strings = strings.split()
    #print(num)
    for number in num:
        #print(number)
        if len(number) < 0:
            continue
        number = int(number)
        list.append(number)
total = sum(list)
print(total)