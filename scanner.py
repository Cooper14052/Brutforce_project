import socket
import threading

HOST = '...'
THREADS_NUM = 30


def find_ports(host, ports):
    for port in ports:
        client = socket.socket()
        result = client.connect_ex((host, port))
        if result == 0:
            print(f'Порт {port} открыт')

        client.close()


checked_ports = [i for i in range(1, 65536)]

threads_list = list()

one_thread_check_count = len(checked_ports) // THREADS_NUM

for i in range(1, len(checked_ports) + 1, one_thread_check_count):
    threads_list.append(threading.Thread(
        target=find_ports,
        args=[HOST, checked_ports[i:(i + one_thread_check_count)]]
    ))

for i_thread in threads_list:
    i_thread.start()

for i_thread in threads_list:
    i_thread.join()
