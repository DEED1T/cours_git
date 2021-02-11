import tkinter as tk
import random as r

#bandeau de couleurs
couleurs = ["white","blue","red","green","yellow","pink","orange","black"]
bandeau = [[0 for i in range(50)] for j in range(50)]
bandeau_base = [[0 for i in range(50)] for j in range(50)]
coord = []

#pencil
pen = ["yellow",4]

#events
#pencils change
def pen_black() :
    global pen
    pen = ["black",7]
    
def pen_yellow() :
    global pen
    pen = ["yellow",4]
    
def pen_pink() :
    global pen
    pen = ["pink",5]

def pen_orange() :
    global pen
    pen = ["orange",6]
    
def motif1() :
    for i in range(len(bandeau)) :
        for j in range(len(bandeau[0])) :
            if i%2 == 0 :
                bandeau[i][j] = 7
    
    create_bandeau(bandeau)

def motif2() :
    for i in range(len(bandeau)) :
        for j in range(len(bandeau[0])) :
            if j%2 == 0 :
                bandeau[i][j] = 7
    
    create_bandeau(bandeau)
        

    
#clicks/bind event
def callclick(event) :
    global bandeau
    for c in coord :
        xL,yL,(i,j) = c
        if (xL[0]<event.x<=xL[1]) and (yL[0]<event.y<=yL[1]) :
            cv.create_rectangle(xL[0],yL[0],xL[1],yL[1],fill=pen[0])
            bandeau[i][j] = pen[1]

def reset() :
    global bandeau,bandeau_base
    create_bandeau(bandeau_base)

def tri(event) :
    global bandeau,bandeau_base
    l = sorted(bandeau)
    create_bandeau(l)

#creation de fenetre
window = tk.Tk()
window.title("Bandeau de couleurs")

#canvas
cv = tk.Canvas(window,width = 900,height = 900)
cv.pack()

#buttons
frame1 = tk.Frame(window,borderwidth=2)
frame1.pack(side="top", fill="both", ipadx=10, ipady=10, expand=0)
button1 = tk.Button(window,text="jaune", command=pen_yellow,background="yellow").pack(side="right", padx=10, pady=10)
button2 = tk.Button(window,text="rose", command=pen_pink,background="pink").pack(side="right", padx=10, pady=10)
button3 = tk.Button(window,text="orange", command=pen_orange,background="orange").pack(side="right", padx=10, pady=10)
button4 = tk.Button(window,text="RESET", command=reset,background="red").pack(side="left", padx=10, pady=10)
button5 = tk.Button(window,text="black", command=pen_black).pack(side="right", padx=10, pady=10)
button6 = tk.Button(window,text="MOTIF1", command=motif1,background="green").pack(side="left", padx=10, pady=10)
button7 = tk.Button(window,text="MOTIF2", command=motif2,background="green").pack(side="left", padx=10, pady=10)



#creation du bandeau
def create_bandeau(list) :
    x=0
    y=0
    for i in range(len(list)) :
        for j in range(len(list[0])) :
            x1 = x
            x2 = x+25
            y1 = y
            y2 = y + 25
            cv.create_rectangle(x1,y1,x2,y2, fill=couleurs[list[i][j]],outline="black")
            coord.append([(x1,x2),(y1,y2),(i,j)])
            x+=25
        x = 0
        y+=25

create_bandeau(bandeau)


#attribution des events 
cv.bind("<Button-1>", callclick) 
window.bind("<space>",tri)  



#affiche de la fenetre
window.mainloop()
