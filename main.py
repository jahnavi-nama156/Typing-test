from words import words
from tkinter import *
import random
from tkinter import messagebox

mainscreen = Tk()
mainscreen.geometry('800x600')
mainscreen.title("Typing Test by dataflair")
mainscreen.config(bg="skyblue")

score = 0
missed = 0
time = 60
count1 = 0
movingwords =''

def movingtext():
    global count1,movingwords
    floatingtext='Typing test by dataflair'
    if count1 >= len(floatingtext):
        count1 = 0
        movingwords=''
    movingwords += floatingtext[count1]
    count1 += 1
    fontlabel.configure(text=movingwords)
    fontlabel.after(150,movingtext)


def giventime():
    global time,score,missed
    if time > 11:
        pass
    else:
        timecount.configure(fg='red')
    if time>0:
        time -=1
        timecount.configure(text=time)
        timecount.after(1000,giventime)
    else:
        gameinstruction.configure(text='Hit={} | miss = {} | total score = {}'.format(score,missed,score-missed))
        rr = messagebox.askretrycancel('notification','do you want to play again?')
        if rr==True:
            score =0
            missed = 0
            time = 60
            timecount.configure(text=time)
            labelforward.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0,END)


def game(event):
    global score,missed
    if time == 60:
        giventime()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get() == labelforward.cget('text'):
        score += 1
        scorelabelcount.configure(text=score)
    else:
        missed +=1
    random.shuffle(words)
    labelforward.configure(text=words[0])
    wordentry.delete(0,END)


fontlabel = Label(mainscreen,text='',font = ('arial',25,'italic bold'),fg = 'purple',width=40)
fontlabel.place(x=10,y=10)
movingtext()


startlabel = Label(mainscreen,text='start typing',font=('arial',30,'italic bold'),bg = 'black',fg = 'white')
startlabel.place(x=275,y=50)

random.shuffle(words)
labelforward = Label(mainscreen,text=words[0],font=('arial',45,'italic bold'),fg = 'black')
labelforward.place(x=250,y=240)

scorelabel = Label(mainscreen,text='your score',font=('arial',25,'italic bold'),fg = 'orange')
scorelabel.place(x=10,y=100)


scorelabelcount = Label(mainscreen,text= score,font=('arial',25,'italic bold'),fg = 'green')
scorelabelcount.place(x=150,y=180)



labelfortimer = Label(mainscreen,text='time left',font=('arial',25,'italic bold'),fg = 'orange')
labelfortimer.place(x=600,y=100)


timecount = Label(mainscreen,text=time,font=('arial',30,'italic bold'),fg = 'black')
timecount.place(x=600,y=180)


gameinstruction = Label(mainscreen,text='press enter after typing the word',font=('arial',30,'italic bold'),fg = 'blue')
gameinstruction.place(x=150,y=550)

gameinstruction = Label(mainscreen,text='press Enter to start',font=('arial',30,'italic bold'),fg = 'blue')
gameinstruction.place(x=150,y=500)



wordentry = Entry(mainscreen,font=('arial',25,'italic bold'),bd = 10,justify='center')
wordentry.place(x=250,y=330)
wordentry.focus_set()

mainscreen.bind('<Return>',game)
mainloop()






















