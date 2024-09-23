correct_logins = ["user_743", "user_123", "admin"]
correct_passwords = ["cf63m", "pm5dw123", "py5en6"]

print("--------------------------")
login = input("Введите логин: ")
print("--------------------------")
password = input("Введите пароль: ")
print("--------------------------")

print("--------------------------")
if login == correct_logins[0] and password == correct_passwords[0]:
    print("Добро пожаловать, user_743!")
elif login == correct_logins[1] and password == correct_passwords[1]:
    print("Добро пожаловать, user_123!")
elif login == correct_logins[2] and password == correct_passwords[2]:
    print("Добро пожаловать, админ!")
else:
    print("Неправильный логин или пароль. Попробуйте еще раз.")
print("--------------------------")