from pathlib import Path
from tkinter import *
import requests
from io import BytesIO
from PIL import Image, ImageTk
import json
from yt import mp3, mp4

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Assets/downloader")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main():
    
    with open('current.json', 'r') as f:
    # Load the JSON data from the file
        data = json.load(f)
    
    window = Tk()

    window.geometry("1100x641")
    window.configure(bg = "#2D2D2D")
    window.wm_attributes('-type', 'splash')

    #Thumbnail
    image_url = data['thumbnail']
    image_byt = requests.get(image_url).content
    image = Image.open(BytesIO(image_byt))
    
    canvas = Canvas(
        window,
        bg = "#2D2D2D",
        height = 641,
        width = 1100,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 =ImageTk.PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        550.0,
        57.0,
        image=image_image_1
    )
    
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        command=lambda: window.iconify(),
        relief="flat"
    )
    button_1.place(
        x=1054.0,
        y=5.0,
        width=20.0,
        height=20.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        command=lambda: window.destroy(),
        relief="flat"
    )
    button_2.place(
        x=1080.0,
        y=5.0,
        width=20.0,
        height=20.0
    )
    resized_image= image.resize((336,188), Image.ANTIALIAS)
    image_image_2 = ImageTk.PhotoImage(resized_image)
    image_2 = canvas.create_image(
        259.0,
        294.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        784.0,
        389.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        656.0,
        516.0,
        image=image_image_4
    )

    canvas.create_text(
        526.0,
        216.0,
        anchor="nw",
        text= data['title'],
        fill="#FFFFFF",
        font=("BreeSerif Regular", 24 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        command=lambda: mp4(data['id']),
        relief="flat"
    )
    button_3.place(
        x=541.0,
        y=486.984619140625,
        width=212.0,
        height=59.015380859375
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        938.0,
        516.0,
        image=image_image_5
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        cursor='hand2',
        command=lambda: mp3(data['id']),
        relief="flat"
    )
    button_4.place(
        x=822.0,
        y=486.984619140625,
        width=212.0,
        height=59.015380859375
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        805.0,
        443.0,
        image=image_image_6
    )
    window.resizable(False, False)
    window.mainloop()

main()