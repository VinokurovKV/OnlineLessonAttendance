import server, gui
import multiprocessing as mp


# Настройки программы
host = "127.0.0.1"
port = 25565
client = 'hi'


def main():
    gui1 = mp.Process(target=gui.guiStart)
    sr = mp.Process(target=server.serverStartUp, args=(host, port))
    gui1.start()
    sr.start()
    gui1.join()
    sr.kill()


if __name__ == '__main__':
    main()
