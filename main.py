correct_login = "user"
correct_password = 5634


print("--------------------------\nДобро пожаловать\n--------------------------")

# Проверка логина и пароля пользователя

count = 0
while count < 3:
    login = input("Введите логин: ")
    print("--------------------------")
    password = int(input("Введите пароль: "))
    print("--------------------------")
    if login == correct_login and password == correct_password:
        print("Вы вошли в систему! user!")
        print("--------------------------")
        break
    elif login != correct_login or password != correct_password:
        print("Неверный логин или пароль! Повторите попытку")
        print("--------------------------")
        count += 1
        if count == 3:
            print("Вы исчерпали все попытки! До свидания!")
            print("--------------------------")
            break