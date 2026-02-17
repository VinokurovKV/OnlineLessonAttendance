import multiprocessing as mp
from _thread import start_new_thread
import socket

sock123 = '1'

def callStudent():  # Функция обращению к клиенту
    command = b'aGVsbG8='
    print(command)
    global sock123
    if sock123 != '1':
        sock123.send(command)


def serverStartUp(host, port):  # Функция запуска сервера
    def threaded(connection):  # Создание потоков для каждого отдельного клиента
        while True:
            data = connection.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                print('Bye')
                break
            connection.send(data)
        connection.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print("Сервер запущен!")

    while True:
        sock, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])
        global sock123
        sock123 = sock
        start_new_thread(threaded, (sock,))


def main():
    server = mp.Process(target=serverStartUp)
    server.start()

if __name__ == '__main__':
    main()
