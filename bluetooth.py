# teeth = []
# n = int(input())
# for _ in range(n):
#     teeth.append(input().strip()) 

with open("input.txt") as file:
    teeth = file.read().strip().split("\n")[1:]
    print(teeth)
    # teeth = teeth[1:len(teeth)-1]

blue = "b"
missing = "m"

left = 0
right = 1
soup = 2

upperTeethRight = [str(n) + "+" for n in range(8,0, -1)]
upperTeethLeft = [ "+" + str(n) for n in range(1,9)]
lowerTeethRight = [ str(n) + "-" for n in range(8,0, -1)]
lowerTeethLeft = [ "-" + str(n)  for n in range(1,9)]
fullSetOfTeeth = set(upperTeethRight + upperTeethLeft + lowerTeethRight + lowerTeethLeft)
setOfTeeth = fullSetOfTeeth
missingTeeth = set()


def bluetooth(teeth):
    for tooth in teeth:
        if blue in tooth:
            if tooth[0] == "+" or tooth[0] == "-":
                setOfTeeth = fullSetOfTeeth.difference(set(lowerTeethLeft)).difference(set(upperTeethLeft))
                return(setOfTeeth)
            elif tooth[1] == "+" or tooth[1] == "-":
                setOfTeeth = fullSetOfTeeth.difference(set(lowerTeethRight)).difference(set(upperTeethRight))
                return(setOfTeeth)
            
haraldsTeeth = bluetooth(teeth)
for tooth in teeth:
    if missing in tooth and tooth in haraldsTeeth:
        tooth = tooth[0:2]
        haraldsTeeth.remove(tooth)


def chew(haraldsTeeth):
    if len(haraldsTeeth) < 3:
        return soup
    
    leftSide = []
    rightSide = []
    for tooth in haraldsTeeth:
        if tooth[0] == "+" or tooth[0] == "-":
            leftSide.append(tooth)
        elif tooth[1] == "+" or tooth[1] == "-":
            rightSide.append(tooth)

    upperJawLeft = set()
    lowerJawLeft = set()
    for tooth in leftSide:
        if "+" in tooth:
            upperJawLeft.add(tooth)
        elif "-" in tooth:
            lowerJawLeft.add(tooth)
    
    upperJawRight = set()
    lowerJawRight = set()
    for tooth in rightSide:
        if "+" in tooth:
            upperJawRight.add(tooth)
        elif "-" in tooth:
            lowerJawRight.add(tooth)
    
    tempUpperLeft = set()
    for tooth in upperJawLeft:
        tempUpperLeft.add(tooth.replace("+",""))
    
    tempLowerLeft = set()
    for tooth in lowerJawLeft:
        tempLowerLeft.add(tooth.replace("-",""))

    tempUpperRight= set()
    for tooth in upperJawRight:
        tempUpperRight.add(tooth.replace("+",""))
    
    tempLowerRight = set()
    for tooth in lowerJawRight:
        tempLowerLeft.add(tooth.replace("-",""))
    
    for tooth in tempUpperLeft:
        if tooth in tempLowerLeft:
            return left
    for tooth in tempUpperRight:
        if tooth in tempLowerRight:
            return right
    
    return soup

print(chew(haraldsTeeth))