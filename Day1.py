
file = open('Day1PuzzleInput.txt','r')
lines = file.readlines()

lines0 = [int(i) for i in lines]
lines1 = lines0
lines2 = lines0




## Day 1.1

key0 = 0
for idx0, line0 in enumerate(lines0):

    for idx1, line1 in enumerate(lines1):
        result1 = line0 + line1

        if (idx0 != idx1) and (result1 == 2020):
            key0 = line0 * line1
            break
    if key0 != 0:
        break

print(key0)

## Day 1.2

key1 = 0
for idx0, line0 in enumerate(lines0):

    for idx1, line1 in enumerate(lines1):
        result1 = line0 + line1

        for idx2, line2 in enumerate(lines2):
            result2 = result1 + line2

            if (idx0 != idx1) and (idx1 != idx2) and (idx1 != idx2) and (result2 == 2020):
                key1 = line0 * line1 * line2
                break
        if key1 != 0:
            break
    if key1 != 0:
        break

print(key1)