from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from yt import vidInfo, mp3
import json
from subprocess import call

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def search():
    query = entry_1.get()
    i = vidInfo(query)
    data = {
        'id': i['id'],
        'thumbnail': i['thumbnail'],
        'title': i['title']
        }
    print(data)
    with open('current.json', 'w') as f:
        json.dump(data, f)
    call(['python3', 'downloader.py'])
    

def download():
    query = entry_1.get()
    mp3(query)

window = Tk()

window.geometry("1200x700")
window.configure(bg = "#2D2D2D")
window.wm_attributes('-type', 'splash')

canvas = Canvas(
    window,
    bg = "#2D2D2D",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    623.0,
    57.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    615.0,
    176.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    536.0,
    177.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=308.0,
    y=159.0,
    width=456.0,
    height=34.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    cursor='hand2',
    command=lambda: search(),
    relief="flat"
)
button_1.place(
    x=805.0,
    y=158.0,
    width=167.0,
    height=37.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    376.0,
    401.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    811.0,
    401.0,
    image=image_image_4
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    cursor='hand2',
    command=lambda: window.iconify(),
    relief="flat"
)
button_2.place(
    x=1146.0,
    y=5.0,
    width=20.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    cursor='hand2',
    command=lambda: window.destroy(),
    relief="flat"
)
button_3.place(
    x=1172.0,
    y=5.0,
    width=20.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
