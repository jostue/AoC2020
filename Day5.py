
file = open('Day5PuzzleInput.txt','r')
lines = file.readlines()

# F = 0
# B = 1

# L = 0
# R = 1

replacedLines = [l.replace("F","0") for l in lines]
replacedLines = [l.replace("B","1") for l in replacedLines]
replacedLines = [l.replace("L","0") for l in replacedLines]
replacedLines = [l.replace("R","1") for l in replacedLines]

highestSeatId = 0


# Day 5.1

for currentLine in replacedLines:
    print(currentLine[:7])
    print(currentLine[7:])
    currentRow = int(currentLine[:7], 2)
    currentColumn = int(currentLine[7:],2)

    currentSeatId = currentRow * 8 + currentColumn

    if currentSeatId > highestSeatId:
        highestSeatId = currentSeatId

print(highestSeatId)


# Day 5.2

seatTaken =[[0 for col in range(8)] for row in range(128)]
mySeatId = 0

for currentLine in replacedLines:
    print(currentLine[:7])
    print(currentLine[7:])
    currentRow = int(currentLine[:7], 2)
    currentColumn = int(currentLine[7:],2)

    seatTaken[currentRow][currentColumn] = 1

for idx, row in enumerate(seatTaken):
    if (idx > 0) and (idx < 127):
        if (0 in row) and (seatTaken[idx-1][0] == 1) and (seatTaken[idx+1][0] == 1):
            mySeatId = idx * 8 + row.index(0)

print(mySeatId)