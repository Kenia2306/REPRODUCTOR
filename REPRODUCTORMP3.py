from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk,Image
import os



pygame.init()#iniciamos modulo de pygame
#funcion boton abrir cancion
def OpenFileSong():
    cancion=filedialog.askopenfilename()#Guardar el nombre o cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def PlaySong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()
    
def VolumenUP():
    volumenLevel=pygame.mixer.music.get_volume()+ 0.5
    print(volumenLevel)
    pygame.mixer.music.set_volume(volumenLevel)
    
def VolumenDOWN():
    volumenLeve2=pygame.mixer.music.get_volume()- 0.5
    print(volumenLeve2)
    pygame.mixer.music.set_volume(volumenLeve2)



    


raiz=Tk()
raiz.title("REPRODUCTOR MP3 - KENINI")
#raiz.iconbitmap("disk-jockey.ico")
raiz.geometry("540x500")
raiz.resizable(0,0)

#crear Frame
framePrincipal=Frame(raiz, bg="black")
framePrincipal.pack(fill="both",expand=1)

#Titulo Reproductot
tituloReproductor= Label(framePrincipal,text="REPRODUCTOR MP3 - KENINI",font=("PowerMax",15,"bold"),bg="black",fg="pink")
tituloReproductor.place(relx=0.25,rely=0.02)

#Boton Open Song
botonOpenSong=Button(framePrincipal,text="Open Song",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=OpenFileSong)
botonOpenSong.place(relx=0.02,rely=0.5)

imagenchi=Image.open("KENINI.ico")
imagenReproductor=imagenchi.resize((150,150))
img= ImageTk.PhotoImage(imagenReproductor)

TituloImagen=Label(framePrincipal,image=img)
TituloImagen.place(relx=0.4,rely=0.1)

#Boton Play Song
botonPlaySong=Button(framePrincipal,text="Play Song",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=PlaySong)
botonPlaySong.place(relx=0.22,rely=0.5, )

#Boton Stop Song
botonStopSong=Button(framePrincipal,text="Stop Song",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=stopSong)
botonStopSong.place(relx=0.42,rely=0.5)

#Boton Resume
botonresumeSong=Button(framePrincipal,text="Resume",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=resumeSong)
botonresumeSong.place(relx=0.62,rely=0.5)

#Boton Pause
botonPause=Button(framePrincipal,text="Pause",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1, command=pauseSong)
botonPause.place(relx=0.82,rely=0.5)

#Boton VolumenUP
botonVolumenUP=Button(framePrincipal,text="Volumen+",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=VolumenUP)
botonVolumenUP.place(relx=0.22,rely=0.6)

#Boton VolumenDOWN
botonVolumenDOWN=Button(framePrincipal,text="Volumen-",bg="pink",fg="black",font=("Roboto",12,"bold"),width=8,height=1,command=VolumenDOWN)
botonVolumenDOWN.place(relx=0.62,rely=0.6)


raiz.mainloop()