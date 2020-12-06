file = open('Day6PuzzleInput.txt','r')
lines = file.readlines()

validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

currentCount = 0
groupAnswer = ""

amountGroupAnswers = []

# Day 6.1

for line in lines:
    if line != "\n":
        groupAnswer += line[:-1]
    else:
        for letter in validLetters:
            if letter in groupAnswer:
                currentCount += 1
        amountGroupAnswers.append(currentCount)
        currentCount = 0
        groupAnswer = ""

#check for last group (no newline at the end)
for letter in validLetters:
    if letter in groupAnswer:
        currentCount += 1
amountGroupAnswers.append(currentCount)

result = sum(amountGroupAnswers)
print(result)