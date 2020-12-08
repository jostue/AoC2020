
colorCodes = {}

def prepareData():
    # key:"color1 color2", value: [["colorX colorY", i], ..., ["colorV colorW", j]]
    for line in lines:
        currentBagCode, containedBags = line.split("contain")
        containedBags = containedBags.split(",")

        currentBagCode1, currentBagCode2, _ = currentBagCode.split()

        bagColorCode = currentBagCode1 + " " + currentBagCode2

        modifidyContainedBags = []
        if "no other bags" not in containedBags[0]:
            for containedBag in containedBags:
                amount, color1, color2, _ = containedBag.split()
                modifidyContainedBags.append([color1 + " " + color2, amount])

        # Save if already ran through and if goldes bag found inside
        colorCodes[bagColorCode] = {"containedBags":modifidyContainedBags, "checked":False, "containsGolden":False}

def checkColor(key, checkedKeys):
    if (key not in checkedKeys) and (colorCodes[key]["checked"] == False):
        checkedKeys.append(key)
        currentBagData = colorCodes[key]
        if key == "shiny gold":
            for checkedKey in checkedKeys:
                colorCodes[checkedKey]["checked"] = True
                colorCodes[checkedKey]["containsGolden"] = True

        else:
            for containedBag in currentBagData["containedBags"]:
                checkedKeys = []
                checkColor(containedBag[0], checkedKeys)
                colorCodes[key]["checked"] = True
                if colorCodes[containedBag[0]]["containsGolden"]:
                    colorCodes[key]["containsGolden"] = True


### MAIN ####
file = open('Day7PuzzleInput.txt','r')
lines = file.readlines()

prepareData()
for colorCode in colorCodes:
    checkedKeys = []
    checkColor(colorCode, checkedKeys)

#print(colorCodes)

amountWithGolden = 0
for colorCode in colorCodes:
    print(colorCode)
    print(colorCodes[colorCode])
    if colorCodes[colorCode]["containsGolden"] and (colorCode != "shiny gold"):
        amountWithGolden += 1

print(amountWithGolden)




