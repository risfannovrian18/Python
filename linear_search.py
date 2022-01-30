myList = [1,5,10,20,25,30,2,6,8,9]
cari = int(input("Masukan Angka Yang Anda Cari : "))

#function
def searchNumber(list, search):
    counter = 0
    while counter != len(myList):
        if myList[counter] == search:
            result = counter
        counter += 1
    return result

try :
    hasil = searchNumber(myList, cari)
    if cari in myList :
        print(f"Number {cari} in index {hasil}")
except :
    print("Number Not Found !!!")