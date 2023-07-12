import secrets

flag = False
pwd = ""

while flag != True:
    pwd_length = input("input password length between 6 - 12 = ")

    try:
        pwd_length = int(pwd_length)
    except ValueError:
        print("Input valid ")
        continue

    if pwd_length < 6 or pwd_length > 12:
        print("Input number between 6 - 12 ")
        continue

    for i in range(0, pwd_length):
        pwd += secrets.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
        )
    print(pwd)
    break
