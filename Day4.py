
file = open('Day4PuzzleInput.txt','r')
lines = file.readlines()

entriesDict = {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False,'cid':False}
entryOptionalDict = {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False,'cid':True}

def ResetDict(dict):
    for dictEntry in dict:
        dict[dictEntry] = False
    return dict

def checkCondition(key, value):
    result = False
    if key == 'byr':
        result = (len(value) == 4) and (int(value) >= 1920) and (int(value) <= 2002)
    elif key == 'iyr':
        result = (len(value) == 4) and (int(value) >= 2010) and (int(value) <= 2020)
    elif key == 'eyr':
        result = (len(value) == 4) and (int(value) >= 2020) and (int(value) <= 2030)
    elif key == 'hgt':
        result = (value[-2:] == "in") or (value[-2:] == "cm")
        if result:
            try:
                int(value[0:-2])
                if (value[-2:] == "in"):
                    result = (int(value[:-2]) >= 59) and (int(value[:-2]) <= 76)
                if (value[-2:] == "cm"):
                    result = (int(value[:-2]) >= 150) and (int(value[:-2]) <= 193)
            except ValueError:
                result = False
    elif key == 'hcl':
        result = (value[0] == "#") and (len(value) == 7)
        if result:
            validSymbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f',]
            for letter in value[1:]:
                if letter not in validSymbols:
                    result = False
                    break
    elif key == 'ecl':
        validColours = ['amb','blu','brn','gry','grn','hzl','oth']
        result = value in validColours
    elif key == 'pid':
        result = (len(value) == 9)
        if result:
            try:
                int(value)
            except ValueError:
                result = False
    else:
        result = True

    return result


# Day 4.1 & Day 4.2

amountOfLines = len(lines)

newEntry = True
validPassports = 0

for line in lines:
    entryFound = []
    if newEntry:
        ResetDict(entriesDict)
        newEntry = False
    
    splitLine = line.split()
    if line == "\n":
        # Check Entries
        newEntry = True
        passportValidity = True
        for currentDictEntry in entriesDict:
            if not(entriesDict[currentDictEntry] or entryOptionalDict[currentDictEntry]):
                passportValidity = False
        if passportValidity:
            validPassports += 1
    else:
        for entryInLine in splitLine:
            entryKey , entryValue = entryInLine.split(":")
            entriesDict[entryKey] = checkCondition(entryKey, entryValue)

print(validPassports)