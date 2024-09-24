correct_logins = ["743"]
correct_passwords = ["cf"]


print("--------------------------\nДобро пожаловать\n--------------------------")

count = 0
while count < 3:
    login = input("Введите логин: ")
    print("--------------------------")
    password = input("Введите пароль: ")
    print("--------------------------")
    if login == correct_logins and password == correct_passwords:
        print("Вы вошли в систему! 743!")
        print("--------------------------")
        break
    else:
        print("Неверный логин или пароль! Повторите попытку")
        print("--------------------------")
        count += 1
        if count == 3:
            print("Вы исчерпали все попытки! До свидания!")
            print("--------------------------")
            break