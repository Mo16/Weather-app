from tkinter import *
import requests

firstclick = True


def on_entry_click(event):
    global firstclick
    if firstclick:
        firstclick = False
        entry.delete(0, "end")


def get_weather(country):
    api_key = 'b1e6aa1735fe02c21d6feeeeaacda497'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather = response.json()
    try:
        label["text"] = format_weather(weather)
    except KeyError:
        label["text"] = "Try again"


def format_weather(weather):
    name = weather["name"]
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    country = weather['sys']['country']
    return f'City: {name}, {country}\nDescription: {desc}\nTemperature: {temp}'


# Tkinter Start

root = Tk()

canvas = Canvas(root, height=600, width=800,bg="#d7e69a")
canvas.pack()

frame = Frame(root, bg='#9abf9a', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = Entry(frame, fg="grey", bg="#a6b895", font=40)
entry.insert(0, 'Enter City...')
entry.bind('<FocusIn>', on_entry_click)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Search", font=40, bg="#a6b895", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bd=10, bg='#826a6b')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = Label(lower_frame, font=('Courier', 20), text="", bg='#826a6b', justify="left", anchor="nw")
label.place(relwidth=1, relheight=1)

root.mainloop()
