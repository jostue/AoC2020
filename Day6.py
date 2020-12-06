file = open('Day6PuzzleInput.txt','r')
lines = file.readlines()

# Day 6.1

groupAnswer = ""
amountGroupAnswers = []

for line in lines:
    if line != "\n":
        strippedNewline = line.replace("\n","")
        groupAnswer += strippedNewline
    else:
        collectiveAnswers = "".join(set(groupAnswer))
        amountGroupAnswers.append(len(collectiveAnswers))
        groupAnswer = ""

#check for last group (no newline at the end)
collectiveAnswers = "".join(set(groupAnswer))
amountGroupAnswers.append(len(collectiveAnswers))

result = sum(amountGroupAnswers)
print(result)


# Day 6.2

currentGroupAnswers = []
amountGroupAnswers = []

for line in lines:
    if line != "\n":
        strippedNewline = line.replace("\n","")
        currentGroupAnswers.append(strippedNewline)
    else:
        tempResult = ""
        for idx, currentAnswer in enumerate(currentGroupAnswers):
            if idx > 0:
                for currentLetter in tempResult:
                    if currentLetter not in currentAnswer:
                        tempResult = tempResult.replace(currentLetter, "")
            else:
                tempResult = currentAnswer
        currentGroupAnswers = []
        amountGroupAnswers.append(len(tempResult))

#check for last group (no newline at the end)
tempResult = ""
for idx, currentAnswer in enumerate(currentGroupAnswers):
    if idx > 0:
        for currentLetter in tempResult:
            if currentLetter not in currentAnswer:
                tempResult = tempResult.replace(currentLetter, "")
    else:
        tempResult = currentAnswer
amountGroupAnswers.append(len(tempResult))

result = sum(amountGroupAnswers)
print(result)