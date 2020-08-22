# Program-a-GUI

#Impor packages
import tkinter as tk
from tkinter import font
import requests

#Setting height and width
HEIGHT = 500
WIDTH = 800

#define function which takes entry
def test_function(entry):
    print("This is the entry:", entry)

 

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information ! '

    return final_str

def get_weather(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='pink', bd=5)# html color picker website
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='pink', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="This is a label", font = ('Courier', 18), bg='yellow', anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth=1, relheight=1)



root.mainloop()
