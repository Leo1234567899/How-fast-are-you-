
from words import words
from tkinter import *
import random
from tkinter import messagebox

# Funktion för tidtagning, resultat och att messagebox kommer upp när spelet är slut.                                                                                                                                                                  
def time():
    global timer,score,miss
    if timer>11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer>0:
        timer -=1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000,time)
    else:
        result.configure(text='Rätt = {} | Fel = {} | Totala poängen = {}'
                                  .format(score,miss,score-miss))
        rr= messagebox.askretrycancel('Meddelande','Vill du spela igen!!!!')
        if rr==True:
            score=0
            miss=0
            timer=60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)
# Funktion som räknar ord man har skrivit in samt rättar dem och ger endast poäng när det är rätt stavat.
def startgame(event):
    global score, miss
    if timer==60:
        time()

    if wordentry.get()== wordlabel['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)


# Här är själva Tkinter rutan samt hur stor den ska vara och färg på bakgrund.
screen= Tk()
screen.geometry('800x600')
screen.configure(bg='black')
screen.title("Roligt spel")
score=0
miss=0
timer=60
count=0

# Visar random ord från andra filen 
random.shuffle(words)
wordlabel=Label(screen,text=words[0],bg='black',font=('airal',45),justify='center',fg='magenta')
wordlabel.place(x=300,y=240)

# Texten som visar hur många ord man har skrivit
scorelabel=Label(screen,text='Ord:',bg='black',font=('arial',25),fg='blue')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(screen,text=score,bg='black',font=('arial',25),fg='blue')
scorelabelcount.place(x=150,y=180)

# Texten och timern som visar hur mcket tid man har kvar
timerlabel=Label(screen,text='Tid kvar:',bg='black',font=('arial',25),fg='red')
timerlabel.place(x=600,y=100)

timerlabelcount=Label(screen,text=timer,bg='black',font=('arial',25,),fg='red')
timerlabelcount.place(x=600,y=180)


# Resultatet som visas när spelet är över
result= Label(screen,bg='black',font=('arial',20),fg='light green')
result.place(x=110,y=500)

# Rutan där man skriver orden
wordentry= Entry(screen,font=('Helvetica',25,),justify='center')
wordentry.place(x=205,y=330)
wordentry.focus_set()

screen.bind('<Return>',startgame)
screen.mainloop()
