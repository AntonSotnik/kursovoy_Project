import os

def repoz():
    while True:
        os.system('cd /tmp')
        os.system('wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb')
        os.system('sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb')
        break
    menu()


def install():
    os.system('sudo apt update')
    os.system('sudo apt install -y mysql-server')
    menu()

def service():
    os.system('sudo systemctl status mysql')
    menu()

def command():
    while True:
        print("==========\n1 - Запустить MySQL\n2 - Остановить MySQL\n3 - Рестарт MySQL\n4 - Перезагрузить MySQL\n0 - Вернуться в меню")
        b = input('Введите цифру - ').strip()
        if b == "1":
            os.system('sudo systemctl start mysql')
            print("!!!!!!!!!!\nВы запустили MySQL\n!!!!!!!!!!")
        if b == "2":
            os.system('sudo systemctl stop mysql')
            print("!!!!!!!!!!\nВы остановили MySQL\n!!!!!!!!!!")
        if b == "3":
            os.system('sudo systemctl restart mysql')
            print("!!!!!!!!!!\nВы перезагрузили MySQL\n!!!!!!!!!!")
        if b == "4":
            os.system('sudo systemctl reload mysql')
            print("!!!!!!!!!!\nВы перезапустили MySQL\n!!!!!!!!!!")
        if b == "0":
            menu()
        else:
            print("Вы ввели некоректное значение", '"',b,'"')

def secure():
    os.system('sudo mysql_secure_installation')
    menu()

def work():
    os.system('mysql -u root -p')
    menu()


def menu():
    while True:
        print("==========\n1 - Добавить репозиторий MySQL\n2 - Установка и настройка БД MySQL\n3 - Проверить состояние служб MySQL\n4 - Управление БД MySQL\n5 - Настройка безопасности MySQL\n6 - Работа с БД MySQL\n7 - Закрыть программу")
        a = input('Введите цифру - ').strip()
        if a == "1":
            repoz()
        if a == "2":
            install()
        if a == "3":
            service()
        if a == "4":
            command()
        if a == "5":
            secure()
        if a == "6":
            work()
        if a == "7":
            exit("33333333333333\n---|||  Goodbye, user!   |||---\n33333333333333")
        else:
            print("Вы ввели некоректное значение",'"',a,'"')

print("*******\nПривет, это программа создана для автомазиции БД MySQL, здесь ты сможешь установить и настроить свою Базу Данных\n*******")
menu()


