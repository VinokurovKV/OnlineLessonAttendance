from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import server

def guiStart():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("200x300")
    window.configure(bg = "#F0FFFF")


    canvas = Canvas(
        window,
        bg = "#F0FFFF",
        height = 300,
        width = 200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        30.0,
        66.0,
        anchor="nw",
        text="Список детей на уроке",
        fill="#000000",
        font=("RobotoRoman SemiBold", 12 * -1)
    )

    canvas.create_text(
        21.0,
        12.0,
        anchor="nw",
        text="Добро пожаловать Александр Дмитревич",
        fill="#000000",
        font=("RobotoRoman SemiBold", 12 * -1)
    )

    canvas.create_rectangle(
        21.0,
        115.0,
        180.0,
        287.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=server.callStudent(),
        relief="flat"
    )
    button_1.place(
        x=21.0,
        y=129.0,
        width=159.0,
        height=15.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=21.0,
        y=142.0,
        width=159.0,
        height=15.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=21.0,
        y=114.0,
        width=159.0,
        height=15.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=21.0,
        y=157.0,
        width=159.0,
        height=15.0
    )
    window.resizable(False, False)
    window.mainloop()
