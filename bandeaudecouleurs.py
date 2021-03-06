import tkinter as tk
import random as r

#bandeau de couleurs
couleurs = ["blue","red","green"]
bandeau = [1,2,1,3,3,2,1,1,2,3]
coord = []

#pencil
pen = "yellow"

#events
#pencils change
def pen_yellow() :
    global pen
    pen = "yellow"
    

def pen_pink() :
    global pen
    pen = "pink"

def pen_orange() :
    global pen
    pen = "orange"
    
#clicks/bind event
def callclick(event) :
    for c in coord :
        if c[0]<event.x<=c[1] :
            cv.create_rectangle(c[0],0,c[1],100,fill=pen)

def reset() :
    create_bandeau(bandeau)

def tri(event) :
    print("ici")
    l = sorted(bandeau)
    create_bandeau(l)

#creation de fenetre
window = tk.Tk()
window.title("Bandeau de couleurs")

#canvas
cv = tk.Canvas(window,width = 900,height = 100)
cv.pack()

#buttons
frame1 = tk.Frame(window,borderwidth=2)
frame1.pack(side="top", fill="both", ipadx=10, ipady=10, expand=0)
button1 = tk.Button(window,text="jaune", command=pen_yellow,background="yellow").pack(side="right", padx=10, pady=10)
button2 = tk.Button(window,text="rose", command=pen_pink,background="pink").pack(side="right", padx=10, pady=10)
button3 = tk.Button(window,text="orange", command=pen_orange,background="orange").pack(side="right", padx=10, pady=10)
button4 = tk.Button(window,text="RESET", command=reset,background="red").pack(side="left", padx=10, pady=10)



#creation du bandeau
def create_bandeau(list) :
    x=0
    for i in range(len(list)) :
        x1 = x
        x2 = x+100
        cv.create_rectangle(x1,0,x2,100, fill=couleurs[list[i]-1],outline="black")
        coord.append((x1,x2))
        x+=100 

create_bandeau(bandeau)


#attribution des events 
cv.bind("<Button-1>", callclick) 
window.bind("<space>",tri)  



#affiche de la fenetre
window.mainloop()
