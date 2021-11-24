name = input('Masukan namamu : ')
if len(name) < 3:
    print("Nama harus lebih dari 3 karakter")
elif len(name) > 50:
    print("Nama tidak boleh lebih dari 50 karakter")
else :
    print("Nama yang bagus !!")
#tebak angka
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Ayo tebak!! angka berapakah aku? : '))
    guess_count += 1
    if guess == secret_number:
        print(f"Yeayy {name} kamu menang :)")
        break
else :
    print(f"Maaf, {name} Kamu kalah :(")
