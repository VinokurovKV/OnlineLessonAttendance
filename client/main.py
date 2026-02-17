import json
import os.path
import multiprocessing as mp
import socket

import build.gui
import second

# Настройки
server = '127.0.0.1', 25565  # Сервер
file_path = "settings.json"  # Путь до файла с данными ученика
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Серверная часть
connection.connect(server)


def main():
    if os.path.exists(file_path):  # Проверка существования файла с настрйками
        with open(file_path, 'r') as f:
            userSettings = json.load(f)
        manager = mp.Manager()
        var = manager.list()
        var.append(' ')
        sC = mp.Process(target=build.gui.readFromSocket, args=(connection, var))
        gui = mp.Process(target=build.gui.designe, args=(userSettings['name'], "Математика", connection, server, var))
        timer = mp.Process(target=build.gui.timer, args=(connection, server))
        sC.start()
        gui.start()
        timer.start()
        timer.join()
        gui.join()
        sC.kill()
        timer.kill()
    else:
        second.userSetup(file_path)  # Запуск системы в режиме настройки
        exit()


if __name__ == '__main__':
    main()
