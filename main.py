#Anime/Manga Generator using PySimpleGUI and JikanPy, SECOND EVER GITHUB PROJECT!
import PySimpleGUI as sg
from jikanpy import Jikan
import subprocess
import random

jikan = Jikan()

sg.theme('Dark Grey 13') # The theme I used for the GUI

Layout = [              # The layout for the Main Menu
    [sg.Text('Type the number in the input box below!')],
    [sg.Text('0. Random Top Anime')],
    [sg.Text('1. Random Anime')],
    [sg.Text('2. Random Top Manga')],
    [sg.Text('3. Random Manga')],
    [sg.Input()],
    [sg.B("Submit")],
    [sg.B("Quit")]
]

window = sg.Window("Anime/Manga Generator", Layout, margins=(300, 300) , grab_anywhere=True, finalize=True) # Creates the window

while True:         # Event Loop
    event, values = window.Read()
    if event in (None, 'Quit'):         # Checks if user presses 'Quit'
        exit()
    elif event == "Submit":             # Checks if user presses 'Submit' to redirect him to a new GUI
        if values[0] == "0":
            break
        if values[0] == "1":
            break
        if values[0] == "2":
            break
        if values[0] == "3":
            break
        if values[0] == "4":
            break
        if values[0] == "5":
            break


window.close()      # Closes the window

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

if values[0] == "0":   
    r0= random.randint(1, 5)
    top=jikan.top(type='anime', page=r0)['top']
    url=[i['url'] for i in top] #sorts only urls
    Layout0 = [
    [sg.T("Press the 'Random' Button to get a random from the top 250 Anime")],
    [sg.B("Random")],
    [sg.B("Quit")]
    ]
    x = random.choice(url)
    window0 = sg.Window("Random Top Anime", Layout0, margins=(300, 300) , grab_anywhere=True, finalize=True)
    while True:         # Event Loop
        event, values = window0.Read()
        if event in (None, 'Quit'):         # Checks if user presses 'Quit'
            exit()
        elif event == "Random":             # Gives a random anime
            window0.close()
            Layout69 = [
                        [sg.Text(x)],
                        [sg.B("Copy")],
                        [sg.B("Quit")]
            ]        
            window69 = sg.Window("Random Top Anime Result: " + x, Layout69, margins=(100, 50) , grab_anywhere=True, finalize=True)
            while True:         # Event Loop
                event, values = window69.Read()
                if event in (None, 'Quit'):         # Checks if user presses 'Quit'
                    exit()
                if event == "Copy":                 # Checks if user wants to copy the url
                    copy2clip(x)
elif values[0] == "1":
    completerandopage = random.randint(0, 300)
    completerando=jikan.top(type='anime', page=completerandopage)['top']
    url=[i['url'] for i in completerando] #sorts only urls
    Layout1 = [
    [sg.T("Press the 'Random' Button to get a completly random Anime")],
    [sg.B("Random")],
    [sg.B("Quit")]
    ]
    x = random.choice(url)
    window1 = sg.Window("Random Anime", Layout1, margins=(300, 300) , grab_anywhere=True, finalize=True)
    while True:         # Event Loop
        event, values = window1.Read()
        if event in (None, 'Quit'):         # Checks if user presses 'Quit'
            exit()
        elif event == "Random":             # Gives a random anime
            window1.close()
            Layout11 = [
                        [sg.Text(x)],
                        [sg.B("Copy")],
                        [sg.B("Quit")]
            ]        
            window1 = sg.Window("Random Anime Result: " + x, Layout11, margins=(100, 50) , grab_anywhere=True, finalize=True)
            while True:         # Event Loop
                event, values = window1.Read()
                if event in (None, 'Quit'):         # Checks if user presses 'Quit'
                    exit()
                if event == "Copy":                 # Checks if user wants to copy the url
                    copy2clip(x)

    
elif values[0] == "2":
    r2= random.randint(1, 5)
    top2=jikan.top(type='manga', page=r2)['top']
    url=[i['url'] for i in top2] #sorts only urls
    Layout2 = [
    [sg.T("Press the 'Random' Button to get a random Manga from the top 250 Mangas")],
    [sg.B("Random")],
    [sg.B("Quit")]
    ]
    x = random.choice(url)
    window2 = sg.Window("Random Top Manga", Layout2, margins=(300, 300) , grab_anywhere=True, finalize=True)
    while True:         # Event Loop
        event, values = window2.Read()
        if event in (None, 'Quit'):         # Checks if user presses 'Quit'
            exit()
        elif event == "Random":             # Gives a random anime
            window2.close()
            Layout22 = [
                        [sg.Text(x)],
                        [sg.B("Copy")],
                        [sg.B("Quit")]
            ]        
            window22 = sg.Window("Random Top Manga Result: " + x, Layout22, margins=(100, 50) , grab_anywhere=True, finalize=True)
            while True:         # Event Loop
                event, values = window22.Read()
                if event in (None, 'Quit'):         # Checks if user presses 'Quit'
                    exit()
                if event == "Copy":                 # Checks if user wants to copy the url
                    copy2clip(x)    

elif values[0] == "3":
    completerandopage2 = random.randint(0, 300)
    completerando2=jikan.top(type='manga', page=completerandopage2)['top']
    url=[i['url'] for i in completerando2] #sorts only urls
    Layout1 = [
    [sg.T("Press the 'Random' Button to get a completly random Manga")],
    [sg.B("Random")],
    [sg.B("Quit")]
    ]
    x = random.choice(url)
    window1 = sg.Window("Random Manga", Layout1, margins=(300, 300) , grab_anywhere=True, finalize=True)
    while True:         # Event Loop
        event, values = window1.Read()
        if event in (None, 'Quit'):         # Checks if user presses 'Quit'
            exit()
        elif event == "Random":             # Gives a random anime
            window1.close()
            Layout11 = [
                        [sg.Text(x)],
                        [sg.B("Copy")],
                        [sg.B("Quit")]
            ]        
            window1 = sg.Window("Random Manga Result: " + x, Layout11, margins=(100, 50) , grab_anywhere=True, finalize=True)
            while True:         # Event Loop
                event, values = window1.Read()
                if event in (None, 'Quit'):         # Checks if user presses 'Quit'
                    exit()
                if event == "Copy":                 # Checks if user wants to copy the url
                    copy2clip(x)