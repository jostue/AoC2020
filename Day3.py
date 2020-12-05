
file = open('Day3PuzzleInput.txt','r')
lines = file.readlines()

##Day3.1

pattern = [1,3]
modifiedLines = []

for line in lines:
    line = line.rstrip("\n")
    modifiedLines.append(line)

totalLines = len(modifiedLines)
lineLength = len(modifiedLines[0])

currentLine = 0
currentColumn = 0

treeCount = 0

while currentLine < totalLines:
    currentObject = modifiedLines[currentLine][currentColumn]
    if(currentObject == "#"):
        treeCount += 1
    currentLine += pattern[0]
    currentColumn += pattern[1]
    if currentColumn >= lineLength:
        currentColumn -= lineLength

print(treeCount)

## Days 3.2

patterns = ([1,1],[1,3],[1,5],[1,7],[2,1])
modifiedLines = []

for line in lines:
    line = line.rstrip("\n")
    modifiedLines.append(line)

totalLines = len(modifiedLines)
lineLength = len(modifiedLines[0])

totalTrees = 1

for pattern in patterns:
    treeCount = 0
    currentLine = 0
    currentColumn = 0
    while currentLine < totalLines:
        currentObject = modifiedLines[currentLine][currentColumn]
        if(currentObject == "#"):
            treeCount += 1
        currentLine += pattern[0]
        currentColumn += pattern[1]
        if currentColumn >= lineLength:
            currentColumn -= lineLength
    totalTrees *= treeCount
    print(treeCount)

print(totalTrees)