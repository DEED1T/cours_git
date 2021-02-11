import tkinter as tk
import random as r

#bandeau de couleurs
couleurs = ["white"]
bandeau = [0,0,0,0,0,0,0,0,0,0]
coord = []

#pencil
pen = "black"

#events
#pencils change
def pen_black() :
    global pen
    pen = "black"
    
#clicks/bind event
def callclick(event) :
    for c in coord :
        if c[0]<event.x<=c[1] :
            canvas.create_rectangle(c[0],0,c[1],100,fill=pen)

#creation de fenetre
window = tk.Tk()
window.title("Bandeau de couleurs")

#canvas
canvas = tk.Canvas(window,width = 900,height = 100)
canvas.pack()

#buttons
frame1 = tk.Frame(window,borderwidth=2)
frame1.pack(side="top", fill="both", ipadx=10, ipady=10, expand=0)
button1 = tk.Button(window,text="noir", command=pen_black).pack(side="right", padx=10, pady=10)

#creation du bandeau
def create_bandeau(list) :
    x=0
    for i in range(len(list)) :
        x1 = x
        x2 = x+100
        canvas.create_rectangle(x1,0,x2,100, fill=couleurs[list[i]],outline="black")
        coord.append((x1,x2))
        x+=100 

create_bandeau(bandeau)

#attribution des events 
canvas.bind("<Button-1>", callclick) 

#affiche de la fenetre
window.mainloop()
