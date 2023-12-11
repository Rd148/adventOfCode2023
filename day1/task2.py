numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
with open('input', 'r') as file:
    lines = file.readlines()

substring = ''
finalSum = 0
found = False

for line in lines:
    print(line)
    for char in line:
        if not found:
            if char.isdigit():
                finalSum += 10 * int(char)
                print(char)
                found = True
            else:
                substring += char
                for number in numbers:
                    if substring.find(number) != -1:
                        finalSum += 10 * numbers[number]
                        print(numbers[number])
                        found = True

    found = False                
    substring = ''
    line = line[::-1]
    for char in line:
        if not found:
            if char.isdigit():
                finalSum += int(char)
                print(char)
                found = True
            else:
                substring += char
                for number in numbers:
                    if substring.find(number[::-1]) != -1:
                        finalSum += numbers[number]
                        print(numbers[number])
                        found = True
    found = False
    substring = ''
print(finalSum)
