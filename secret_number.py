secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Ayo tebak angka berapakah aku : '))
    guess_count += 1
    if guess == secret_number:
        print('Yeayy kamu menang !')
        break
else :
    print("Maaf, kamu gagal :(")