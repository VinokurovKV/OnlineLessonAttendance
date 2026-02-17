import multiprocessing as mp
from _thread import start_new_thread
import socket

#Настройки программы
host = "192.168.1.12"
port = 25565
clients = []

def callStudent(sock):  #Функция обращению к клиенту
    command = b'aGVsbG8='
    sock.send(command)

def serverStartUp():        #Функция запуска сервера
    def threaded(connection):   #Создание потоков для каждого отдельного клиента
        while True:
            data = connection.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                print('Bye')
                break
            connection.send(data)
            connection.send(b'hello')
        connection.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print("Сервер запущен!")

    while True:
        sock, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])
        global clients
        if sock not in clients:
            clients.append(sock)
        start_new_thread(threaded, (sock,))

def main():
    global clients
    server = mp.Process(target=serverStartUp)
    server.start()


if __name__=='__main__':
    main()