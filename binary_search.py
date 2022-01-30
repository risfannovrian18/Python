yourList = [2,4,9,8,1,3,5,6,3,]
yourNumber = int(input("Insert Number to Search ? "))
firstIndex = 0
lastIndex = len(yourList)-1
foundNumber = False
yourList.sort()
while firstIndex <= lastIndex and not foundNumber:
    middleIndex = (firstIndex + lastIndex) // 2
    if yourList[middleIndex] == yourNumber :
        foundNumber = True
    else :
        if yourNumber < yourList[middleIndex]:
            lastIndex = middleIndex - 1
        else :
            firstIndex = middleIndex + 1
if foundNumber :
    print(f"Number {yourNumber} is Found in List")
else :
    print(f"Number {yourNumber} is Not Found in List")