from pathlib import Path
import time, random
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


def readFromSocket(con, manager):
    while 1:
        manager[0] = con.recv(1024)
        print(manager[0].decode('utf-8'))


def designe(studentName, currentLesson, con, serverLocation, var):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("assets")


    def buttonAction():
        mensahe = studentName + " присутствует."
        con.sendto((mensahe).encode('utf-8'), serverLocation)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("300x500")
    window.configure(bg="#F5F5F5")

    canvas = Canvas(
        window,
        bg="#F5F5F5",
        height=500,
        width=300,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        86.0,
        13.0,
        anchor="nw",
        text="Привет, " + studentName + "!",
        fill="#000000",
        font=("Roboto", 18 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=buttonAction,
        relief="flat"
    )
    button_1.place(
        x=86.0,
        y=383.0,
        width=140.0,
        height=30.0
    )

    canvas.create_text(
        5.0,
        56.0,
        anchor="nw",
        text="Текущий урок: " + currentLesson,
        fill="#000000",
        font=("Roboto", 13 * -1)
    )

    canvas.create_text(
        5.0,
        123.0,
        anchor="nw",
        text="Преподаватель: Александр Дмитревич",
        fill="#000000",
        font=("Roboto", 13 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets('image_1.png'))
    image_1 = canvas.create_image(
        156.0,
        280.0,
        image=image_image_1
    )

    window.resizable(False, False)
    window.mainloop()

#random.randint(300, 600)

def timer(con, serverLocation):
    timing = time.time()
    while True:
        answer = ""
        if time.time() - timing > 10:
            timing = time.time()
            answer = messagebox.showinfo(
                "Вопрос",
                "Ты тут?")
            if answer == "ok":
                con.sendto(("Привет").encode('utf-8'), serverLocation)
