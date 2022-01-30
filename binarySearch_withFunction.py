yourList = [2,4,9,8,1,3,5,6,3,]
yourNumber = int(input("Insert Number to Search ? "))

#function
def searchNumber(Number, List) :
    found = False #untuk memberikan kondisi adanya angka
    List.sort() #binary search harus di urutkan terlebih dahulu
    firstIndex = 0 #index pertama
    lastIndex = len(List)-1 #index terakhir

    while firstIndex <= lastIndex and not found:
        middleIndex = (firstIndex + lastIndex) // 2
        if List[middleIndex] == Number :
            found = True
        else :
            if Number < List[middleIndex]:
                lastIndex = middleIndex - 1
            else :
                firstIndex = middleIndex + 1
            return found
#Pemanggilan fungsi ditandai dengan pemanggilan fungsi
result = searchNumber(yourNumber,yourList)
if result :
    print(f"Number {yourNumber} is Found in List")
else :
    print(f"Number {yourNumber} is Not Found in List")