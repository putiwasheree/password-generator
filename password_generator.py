import random
passcode = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") 
pass_length = int(input("Berapa karakter yang ingin digunakan?"))

password = ""
for i in range(pass_length):
    password += random.choice(passcode)

print(password)
