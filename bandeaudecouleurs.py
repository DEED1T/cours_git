import tkinter as tk
import random as r

#bandeau de couleurs
couleurs = ["blue","red","green"]
bandeau = [1,2,1,3,3,2,1,1,2,3]
coord = []

#creation de fenetre
window = tk.Tk()
window.title("Bandeau de couleurs")

#canvas
cv = tk.Canvas(window,width = 900,height = 100)
cv.pack()
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

#events
def callclick(event) :
    for c in coord :
        if c[0]<event.x<=c[1] :
            cv.create_rectangle(c[0],0,c[1],100,fill="yellow")


def tri(event) :
    print("ici")
    l = sorted(bandeau)
    create_bandeau(l)

#attribution des events 
cv.bind("<Button-1>", callclick) 
cv.bind("<Return>",tri)  



#affiche de la fenetre
window.mainloop()
