import tkinter
import time 
from random import *
from threading import Thread
from tkinter import *
from PIL import ImageTk, Image


Livesnave = 50
Livesnave1 = 50
Livesnave2 = 50
Lives3 = 50
Lives2 = 40
Lives = 30
score = 0
proceso = 0
proceso1 = 0
proceso2 = 0
pro = 0
seguir = True
seguir2 = True
seguir3 = True

class Ventana_Principal:
    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(self.master, width=350, height=450, highlightthickness=0, relief='ridge', bg="gray")
        self.canvas.place(x=0,y=0)
        self.ventana_Principal()
    #Esta es la ventana principal
    def ventana_Principal(self):
        #Se abre la imagen 
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        #Texto de biembenida
        self.minombre = Label(self.canvas, text="Welcome soldier mission save Undertale", font=("Helvetica", 15), fg="purple", bg="gray")
        self.minombre.place(x=0,y=30)
        #Texto de digite su nombre
        self.label_nombre = Label(self.canvas, text="Digite su nombre:", fg="purple", bg="gray")
        self.label_nombre.place(x=30,y=155,width=100,height=30)
        #Caja donde se ingresa el nombre
        self.entrada_nombre = Entry(self.canvas)
        self.entrada_nombre.place(x=130,y=155,width=100,height=30)
        #Botton de jugar
        self.button_mostrar = Button(self.canvas, text ="Jugar", fg="purple", bg="gray", command = lambda:self.seleccion())
        self.button_mostrar.place(x=130,y=250,width=100,height=30)
        #lugares de seleccion de nivel
        self.uno = Radiobutton(self.canvas,text="1", variable=r, value=1,bg="purple")
        self.uno.place(x=110,y=186,width=50,height=20)

        self.dos = Radiobutton(self.canvas,text="2", variable=r, value=2,bg="blue")
        self.dos.place(x=160,y=186,width=50,height=20)

        self.tres = Radiobutton(self.canvas,text="3", variable=r, value=3,bg="red")
        self.tres.place(x=210,y=186,width=50,height=20)
        #Boton para ir a creditos
        self.button_mostrar = Button(self.canvas, text ="Creditos", fg="purple", bg="gray", command = lambda:self.cambiar_creditos())
        self.button_mostrar.place(x=0,y=420,width=100,height=30)
        self.button_mostrar = Button(self.canvas, text ="Puntajes", fg="purple", bg="gray", command = lambda:self.cambia_pun())
        self.button_mostrar.place(x=250,y=420,width=100,height=30)
        print("este codigo es una mierda")
    # lugar donde se ejecuta la seleccion y redirecciona al nivel seleccionado 
    def seleccion(self):
        if r.get()==1:
            self.cambia1(self.entrada_nombre.get())
        elif r.get()==2:
            self.cambia2(self.entrada_nombre.get())
        elif r.get()==3:
            self.cambia3(self.entrada_nombre.get())
        else:
            self.cambia1(self.entrada_nombre.get())
            
    #Funcion para ir a creditos
    def cambiar_creditos(self):
        self.destruir_widgets(self.canvas.place_slaves())
        self.Creditos()
        
    def destruir_widgets(self,lista_widgets):
        if lista_widgets == []:
            return 0
        else:
            lista_widgets[0].destroy()
            return self.destruir_widgets(lista_widgets[1:])
    def Creditos(self):
        #Se abre la imagen de fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        #Informacion y creditos
        self.ava = Label(self.canvas, text="Welcome soldier mission save Undertale", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=30)
        
        self.ava = Label(self.canvas, text="Pais: Costa Rica", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=55)
        
        self.ava = Label(self.canvas, text="Universidad: Tecnologico de Costarica ", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=85)
        
        self.ava = Label(self.canvas, text="Carrera: Ing.Computadores", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=115)
        
        self.ava = Label(self.canvas, text="Curso: Taller de programacion", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=145)
        
        self.ava = Label(self.canvas, text="Año: 2021,Grupo 4", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=175)
        
        self.ava = Label(self.canvas, text="Profesor: LUIS BARBOZA ARTAVIA", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=205)
        
        self.ava = Label(self.canvas, text="Autor: Cristopher Blanco Fallas", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=235)
        
        self.ava = Label(self.canvas, text="Recuerda nadie es perfecto", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=265)
        
        self.ava = Label(self.canvas, text="este juego TAMPOCO lo es", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=295)
        
        self.ava = Label(self.canvas, text="Disfruta(version de python 3.9.2)", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=325)
        #Boton para volver
        self.button_mostrar = tkinter.Button(self.canvas, text ="Volver", fg="purple", bg="gray", command = self.cambiar_principal)
        self.button_mostrar.place(x=110,y=400,width=100,height=30)
    #funcion para volver ala ventana principal
    def cambiar_principal(self):
        self.destruir_widgets1(self.canvas.place_slaves())
        self.ventana_Principal()
    #funcion para ir ala pantalla de juego 1  
    def cambia1(self,nom):
        if self.entrada_nombre.get() != "":
            self.destruir_widgets(self.canvas.place_slaves())
            self.juego1(nom)
        
    def destruir_widgets1(self,lista_widgets):
        if lista_widgets == []:
            return 0
        else:
            lista_widgets[0].destroy()
            return self.destruir_widgets(lista_widgets[1:])




    def puntuacion(self):
        #Se abre la imagen de fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        self.ava = Label(self.canvas, text="Puntaje: ", font=("Helvetica", 15), fg="purple", bg="gray")
        self.ava.place(x=0,y=30)
        self.button_mostrar = tkinter.Button(self.canvas, text ="Volver", fg="purple", bg="gray", command = self.cambiar_principal)
        self.button_mostrar.place(x=110,y=400,width=100,height=30)
        
    def cambia_pun(self):
        self.destruir_widgets1(self.canvas.place_slaves())
        self.puntuacion()
        
    def destruir_widgets1(self,lista_widgets):
        if lista_widgets == []:
            return 0
        else:
            lista_widgets[0].destroy()
            return self.destruir_widgets1(lista_widgets[1:])
    
    #pantalla de juego 1
    def juego1(self,nom):
        #lugar donde se llaman las varibles globales de la vida,score,vida,vida del jefe y crono
        global score
        global Livesnave
        global Lives
        global proceso
        global seguir
        #Lugar para abrir la imagen de fondo
        self.imagen = ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0,0,image=self.imagen, anchor=NW)
        #Lugar para abrir la imagen del jefe
        self.jefe=ImageTk.PhotoImage(Image.open("jefe.png"))
        self.boss = self.canvas.create_image(10,0,image=self.jefe, anchor=NW)
        #Lugar para abrir la imagen de la nave     
        self.Nave=ImageTk.PhotoImage(Image.open("Nave.png"))
        self.ships = self.canvas.create_image(125,400,image=self.Nave, anchor=NW)
        #definicion de segundos y minutos
        self.s = 0
        self.m = 0
        #Lugar donde se muestra el relog
        self.time = Label(self.canvas,text=""  , width=5, font=("Helvetica", 9),fg="purple",bg="gray")
        self.time.place(x=0,y=170)
        #Lugar para abrir la imagen de la bala
        self.Bala_nave=ImageTk.PhotoImage(Image.open("balita.png"))
        #Lugar donde se muestra la vida del jefe
        self.livesLabel=Label(self.canvas, text="Livesboss: " + str(Lives) , font=("Helvetica", 9), fg="purple",bg="gray")
        self.livesLabel.place(x=0,y=108.5)
        #Boton para volver
        self.button_mostrar = Button(self.canvas, text ="volver", fg="purple", bg="gray", command = lambda:volver() )
        self.button_mostrar.place(x=0,y=218,width=40,height=15)
        #Lugar donde se muestra en nombre del jugador
        self.mostrarnombre=Label(self.canvas, text="Hola: "+nom, font=("Helvetica", 9), fg="purple",bg="gray")
        self.mostrarnombre.place(x=0,y=195)
        #Lugar donde se muestra el puntaje
        self.scoreLabel=Label(self.canvas, text="score: " + str(score), font=("Helvetica", 9), fg="purple",bg="gray")
        self.scoreLabel.place(x=0,y=150)
        #Lugar donde se muestra la vida de la nave
        self.LivesnaveLabel=Label(self.canvas, text="Livesnave: " + str(Livesnave), font=("Helvetica", 9), fg="purple",bg="gray")
        self.LivesnaveLabel.place(x=0,y=130)
        #funcion para velver ala pantalla principal
        def volver():
            score = 0
            Livesnave = 50
            Lives = 30
            proceso = 0
            seguir = False
            self.cambiar_principal()
        #evento donde se ejecuta la para disparar
        def disparo(evento):
            if evento.keysym=='g':
                if seguir == True:
                    disparar()
        self.master.bind("<KeyRelease>", disparo)
        #evento donde se usa el awsd para mover la nave
        def presion_tecla(evento):
            if self.canvas.coords(self.ships)[0]<280:
                if evento.keysym=='d':
                    self.canvas.move(self.ships, 10, 0)
            if self.canvas.coords(self.ships)[0]>0:
                if evento.keysym=='a':
                    self.canvas.move(self.ships, -10, 0)
            if self.canvas.coords(self.ships)[1]<400:
                if evento.keysym=='s':
                    self.canvas.move(self.ships, 0, 10)
            if self.canvas.coords(self.ships)[1]>0:
                if evento.keysym=='w':
                    self.canvas.move(self.ships, 0, -10)
        self.master.bind("<KeyPress>", presion_tecla)
        #funcion de disparo de la nave
        def disparar():
            x = self.canvas.coords(self.ships)[0]
            y = self.canvas.coords(self.ships)[1]
            Bala_nave = self.canvas.create_image(x+25,y,image=self.Bala_nave, anchor=NW)
            if seguir == True:
                disparar_aux(Bala_nave)
        
        def disparar_aux(Bala_nave):
            global Lives
            
            #daño caja Bala
            #daño caja boss
            daño_cajaBa = self.canvas.bbox(Bala_nave)
            daño_cajbo = self.canvas.bbox(self.boss)
                
            if daño_cajbo[2]>daño_cajaBa[0]>daño_cajbo[0] and daño_cajbo[1]<daño_cajaBa[3]<daño_cajbo[3]:
                global Lives
                Lives-=1
                puntuacion()
                self.canvas.delete(Bala_nave)
                self.livesLabel.configure(text="Livesboss: " + str(Lives))
                
            else:
                self.livesLabel.configure(text="Livesboss: " + str(Lives))
            
            if self.canvas.coords(Bala_nave) != []:
                    if self.canvas.coords(Bala_nave)[1]<0:
                        self.canvas.delete(Bala_nave)
                    else:
                        self.canvas.move(Bala_nave, 0, -10)
                        self.canvas.after(35,disparar_aux,Bala_nave)
            if Lives == 0:
                seguir = False
                bonificasion()
                self.cambia2(nom)

        #funcion para el relog
        def cronometro():
            global proceso
            if self.s >= 60:
                self.s=0
                self.m+=1
                if self.m >= 60:
                    self.m=0
            self.time.configure(text = str(self.m)+":"+str(self.s))
            self.s+=1
            if seguir == True:
                proceso=self.canvas.after(1000,cronometro)
        cronometro()
        #funcion para el movimiento del jefe
        def moverse_jefe(x):
            global livesnave
                
            if self.s%3==0: 
                ran = randint(1,10)
                time.sleep(1)
                if ran%3 == 0:
                    if seguir == True:
                        embestida()
                        try:
                            return moverse_jefe(x)
                        except:
                            return moverse_jefe(x)
            if self.canvas.coords(self.boss)[0]>=250:
                self.canvas.move(self.boss,-5,0)
                time.sleep(0.1)
                return moverse_jefe(-5)
            elif self.canvas.coords(self.boss)[0]<=0:
                self.canvas.move(self.boss,5,0)
                time.sleep(0.1)
                return moverse_jefe(5)
            else:
                self.canvas.move(self.boss,x,0)
                time.sleep(0.1)
                return moverse_jefe(x)
            
        t1 = Thread(target= moverse_jefe, args=(5,))
        if seguir == True:
            t1.start()
        #funcion para guardar la puntuacion
        def puntuacion():
            global score
            global Livesnave
            if Lives<30:
                score=score + 10
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
        def bonificasion():
            global score
            if Livesnave == 50:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
            if self.s <= 30:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
        #funcion para cuando el jefe choca con la nave
        def colicion():
            global Livesnave
            #daño caja nave
            daño_cajana = self.canvas.bbox(self.ships)
            #daño caja boss
            daño_cajabo = self.canvas.bbox(self.boss)
            if daño_cajabo[2]>daño_cajana[0]>daño_cajabo[0] and daño_cajabo[2]<daño_cajana[3]<daño_cajabo[3]:
                global Livesnave
                Livesnave-=10
                self.LivesnaveLabel.config(text="Livesnave: " + str(Livesnave))
        #funcion para la embestida del jefe
        def embestida():
            global Livesnave
            if self.canvas.coords(self.boss)[1]<375:
                self.canvas.move(self.boss,0,30)
                colicion()
                time.sleep(0.1)
                if seguir == True:
                    return embestida()
            else:
                self.LivesnaveLabel.configure(text="Livesnave: " + str(Livesnave))
                if seguir == True:
                    return regreso()
        #funcion para cuando termina la embestida para que vuelva
        def regreso():
            if self.canvas.coords(self.boss)[1]==0:
                global Lives
                Lives-=1
                self.livesLabel.configure(text="Livesboss: " + str(Lives))
            if self.canvas.coords(self.boss)[1]>0:
                self.canvas.move(self.boss,0,-30)
                time.sleep(0.1)
                if seguir == True:
                    return regreso()

    def cambia2(self,nom):
        if self.entrada_nombre.get() != "":
            self.destruir_widgets(self.canvas.place_slaves())
            self.juego2(nom)
        
    def destruir_widgets2(self,lista_widgets):
        if lista_widgets == []:
            return 0
        else:
            lista_widgets[0].destroy()
            return self.destruir_widgets(lista_widgets[1:])
        
    def juego2(self,nom):
        #lugar donde se llaman las varibles globales de la vida,score,vida,vida del jefe y crono
        global score
        global Livesnave1
        global Lives2
        global proceso1
        global seguir2
        #Lugar donde se abre la imagen de fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0,0,image=self.imagen, anchor=NW)
        #Lugar donde se abre la imagen del jefe
        self.jefe=ImageTk.PhotoImage(Image.open("jefe.png"))
        self.Uboss = self.canvas.create_image(10,0,image=self.jefe, anchor=NW)
        #Lugar donde se abre la imagen de la nave   
        self.Nave=ImageTk.PhotoImage(Image.open("Nave.png"))
        self.ships = self.canvas.create_image(125,400,image=self.Nave, anchor=NW)
        #definicion de segundos y minutos
        self.sd = 0
        self.mt = 0
        #label para mostrar el tiempo
        self.tienpo = Label(self.canvas,text="" , width=5, font=("Helvetica", 9),fg="purple",bg="gray")
        self.tienpo.place(x=0,y=170)
        #Label para mostrar el nombre del jugador
        self.mostrarnombre=Label(self.canvas, text="Hola: "+nom, font=("Helvetica", 9), fg="purple",bg="gray")
        self.mostrarnombre.place(x=0,y=195)
        #boton para volver ala pantalla principal 
        self.button_mostrar = Button(self.canvas, text ="volver", fg="purple", bg="gray", command = self.cambiar_principal)
        self.button_mostrar.place(x=0,y=218,width=40,height=15)
        #selfs para abrir la imgen de la bala de la nave y del jefe 
        self.Bala_nave2=ImageTk.PhotoImage(Image.open("balita.png"))

        self.Bala_jefe=ImageTk.PhotoImage(Image.open("balote.png"))
        #Labels para mostrar la vida del jefe,nave,puntaje=score
        self.lives2Label=Label(self.canvas, text="Livesboss: " + str(Lives2), font=("Helvetica", 9), fg="purple",bg="gray")
        self.lives2Label.place(x=0,y=108.5)
        self.scoreLabel=Label(self.canvas, text="score: " + str(score), font=("Helvetica", 9), fg="purple",bg="gray")
        self.scoreLabel.place(x=0,y=150)
        self.Livesnave1Label=Label(self.canvas, text="Livesnave: " + str(Livesnave1), font=("Helvetica", 9), fg="purple",bg="gray")
        self.Livesnave1Label.place(x=0,y=130)
        #Funcion para el disparo de la nave
        def disparo(evento):
            if evento.keysym=='g':
                if seguir2 == True:
                    disparar()
        self.master.bind("<KeyRelease>",disparo)        
        def presion_tecla(evento):
            if self.canvas.coords(self.ships)[0]<280:
                if evento.keysym=='d':
                    self.canvas.move(self.ships, 10, 0)
            if self.canvas.coords(self.ships)[0]>0:
                if evento.keysym=='a':
                    self.canvas.move(self.ships, -10, 0)
            if self.canvas.coords(self.ships)[1]<400:
                if evento.keysym=='s':
                    self.canvas.move(self.ships, 0, 10)
            if self.canvas.coords(self.ships)[1]>0:
                if evento.keysym=='w':
                    self.canvas.move(self.ships, 0, -10)
        self.master.bind("<KeyPress>",presion_tecla)
        #Funcion del cronometro
        def cronometro():
            global proceso1,seguir2
            if self.sd >= 60:
                self.sd = 0
                self.mt+=1
                if self.mt >= 60:
                    self.mt = 0
            self.tienpo.configure(text = str(self.mt)+":"+str(self.sd))
            self.sd+=1
            if seguir2 == True:
                proceso1 = self.canvas.after(1000,cronometro)
        cronometro()
        #Funcion para el disparo de la nave
        def disparar():
            x = self.canvas.coords(self.ships)[0]
            y = self.canvas.coords(self.ships)[1]
            Bala_nave2 = self.canvas.create_image(x+25,y,image= self.Bala_nave2, anchor=NW)
            disparar_aux(Bala_nave2)

        def disparar_aux(Bala_nave2):
            global seguir2
            #daño caja Bala
            #daño caja boss
            daño_cajaBa = self.canvas.bbox(Bala_nave2)
            daño_cajbo = self.canvas.bbox(self.Uboss)
                
            if daño_cajbo[2]>daño_cajaBa[0]>daño_cajbo[0] and daño_cajbo[1]<daño_cajaBa[3]<daño_cajbo[3]:
                global Lives2
                Lives2-=1
                puntaje2()
                self.canvas.delete(Bala_nave2)
                self.lives2Label.configure(text="Livesboss: " + str(Lives2))
                
            else:
                self.lives2Label.configure(text="Livesboss: " + str(Lives2))
            if self.canvas.coords(Bala_nave2) != []:
                if seguir2 == True:
                    if self.canvas.coords(Bala_nave2)[1]<0:
                        self.canvas.delete(Bala_nave2)
                    else:
                        self.canvas.move(Bala_nave2, 0, -20)
                        self.canvas.after(35,disparar_aux,Bala_nave2)
            if Lives2 <= 0:
                seguir2 = False
                bonificasion2()
                self.cambia3(nom)
        #Funcion para el disparo del jefe
        def disparar_jefe1():
            global seguir
            x = self.canvas.coords(self.Uboss)[0]
            y = self.canvas.coords(self.Uboss)[1]
            Bala_jefe = self.canvas.create_image(x,y+75,image=self.Bala_jefe, anchor=NW)
            Bala_jefe1 = self.canvas.create_image(x+35,y+75,image=self.Bala_jefe, anchor=NW)
            Bala_jefe2 = self.canvas.create_image(x+70,y+75,image=self.Bala_jefe, anchor=NW)
            
            t2 = Thread(target=disparar_jefe_aux, args=(Bala_jefe, ))
            t2.start()
            t3 = Thread(target=disparar_jefe_aux,args=(Bala_jefe1, ))
            t3.start()
            t4 = Thread(target=disparar_jefe_aux,args=(Bala_jefe2, ))
            t4.start()
            if seguir2 == True:
                self.canvas.after(1500,disparar_jefe1)
        t5 = Thread(target=disparar_jefe1)
        t5.start()
        def disparar_jefe_aux(Bala_jefe):
            global Livesnave1
            #daño caja Bala
            #daño caja nave
            daño_cajaBa = self.canvas.bbox(Bala_jefe)
            daño_cajna = self.canvas.bbox(self.ships)
    
            #bbox de la primera bala  
            if daño_cajna[2]>daño_cajaBa[0]>daño_cajna[0] and daño_cajna[1]<daño_cajaBa[3]<daño_cajna[3]:
                Livesnave1-=3
                self.canvas.delete(Bala_jefe)
                self.Livesnave1Label.configure(text="Livesnave: " + str(Livesnave1))
                

            #movimiento de las balas   
            if self.canvas.coords(Bala_jefe) != []:
                #primer disparo
                if self.canvas.coords(Bala_jefe)[1]<400:
                    self.canvas.move(Bala_jefe, 0, 5)
                    self.canvas.after(30,disparar_jefe_aux,Bala_jefe)
                else:
                    self.canvas.delete(Bala_jefe)
        #Funcion para el teletransporte del jefe
        def mover_boss(ejex = 0):
            global Livesnave2
            if self.sd%2==0:
                ejex = randint(0,250)
            self.canvas.coords(self.Uboss,ejex,0)
            if seguir2 == True:
                self.canvas.after(1000,mover_boss)
            #self.Livesnave1Label.config(text="Livesnave: " + str(Livesnave1))
        t06 = Thread(target=mover_boss)
        t06.start()
        #Funcion para el puntaje 
        def puntaje2():
            global Livesnave1
            global score
            if Lives<40:
                score=score + 10
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
        def bonificasion2():
            global score
            if Livesnave1 == 50:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
            if self.sd <= 30:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
    #Funcion para cambiar al tercer nivel
    def cambia3(self,nom):
        if self.entrada_nombre.get() != "":
            self.destruir_widgets3(self.canvas.place_slaves())
            self.juego3(nom)
     
    def destruir_widgets3(self,lista_widgets):
        if lista_widgets == []:
            
            return 0
        else:
            lista_widgets[0].destroy()
         
            return self.destruir_widgets3(lista_widgets[1:])
    
    #Funcion para el tercer nivel           
    def juego3(self,nom):
    
        global score
        global Livesnave2
        global Lives3
        global pro
        global seguir3


        #Lugar para la creacion y abre la imagen del fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0,0,image=self.imagen, anchor=NW)
        #Lugar para la creacion y abre la imagen del jefe
        self.jefe=ImageTk.PhotoImage(Image.open("jefe.png"))
        self.Iboss = self.canvas.create_image(10,0,image=self.jefe, anchor=NW)
        #Lugar para la creacion y abre la imagen dela nave
        self.Nave=ImageTk.PhotoImage(Image.open("Nave.png"))
        self.ships = self.canvas.create_image(125,400,image=self.Nave, anchor=NW)
        #Lugar donde segundos y minutoscson iguales a 0
        self.ss = 0
        self.ms = 0
        #label para mostrar el tiempo
        self.ti = Label(self.canvas,text="" , width=5, font=("Helvetica", 9),fg="purple",bg="gray")
        if seguir3 == True:
            self.ti.place(x=0,y=170)
        #Label para mostrar el nombre del jugador
        self.mostrarnombre=Label(self.canvas, text="Hola: "+nom, font=("Helvetica", 9), fg="purple",bg="gray")
        if seguir3 == True:
            self.mostrarnombre.place(x=0,y=230)
        
        self.button_mostrar = Button(self.canvas, text ="volver", fg="purple", bg="gray", command = self.cambiar_principal)
        self.button_mostrar.place(x=0,y=218,width=40,height=15)
        #Lugar donde se abre la imagen de la bala de la nave
        self.Bala_nave=ImageTk.PhotoImage(Image.open("balita.png"))
        #Lugar donde se abre la imagen de la bala del jefe
        self.Bala_jefe01 = ImageTk.PhotoImage(Image.open("balote.png"))
        #Labals para mostrar la vida del jefe,nave,puntaje=score
        self.Lives3Label=Label(self.canvas, text="Livesboss: " + str(Lives3), font=("Helvetica", 9), fg="purple",bg="gray")
        self.Lives3Label.place(x=0,y=195)
        
        self.scoreLabel=Label(self.canvas, text="score: " + str(score), font=("Helvetica", 9), fg="purple",bg="gray")
        self.scoreLabel.place(x=0,y=150)
        
        self.Livesnave2Label=Label(self.canvas, text="Livesnave: " + str(Livesnave2), font=("Helvetica", 9), fg="purple",bg="gray")
        self.Livesnave2Label.place(x=0,y=130)
        #enevento para que la funcion de disparo funciones cuando se preciona la g
        def disparo(evento):
            if evento.keysym=='g':
                if seguir3 == True:
                    disparar()
        self.master.bind("<KeyRelease>",disparo)
        #evento para que la nave se mueva con el awsd
        def presion_tecla(evento):
            if self.canvas.coords(self.ships)[0]<280:
                if evento.keysym=='d':
                    self.canvas.move(self.ships, 10, 0)
            if self.canvas.coords(self.ships)[0]>0:
                if evento.keysym=='a':
                    self.canvas.move(self.ships, -10, 0)
            if self.canvas.coords(self.ships)[1]<400:
                if evento.keysym=='s':
                    self.canvas.move(self.ships, 0, 10)
            if self.canvas.coords(self.ships)[1]>0:
                if evento.keysym=='w':
                    self.canvas.move(self.ships, 0, -10)
        self.master.bind("<KeyPress>", presion_tecla)
        #Funcion para el disparo de la nave
        def disparar():
            x = self.canvas.coords(self.ships)[0]
            y = self.canvas.coords(self.ships)[1]
            Bala_nave = self.canvas.create_image(x+25,y,image=self.Bala_nave, anchor=NW)  
            disparar_aux(Bala_nave)

        def disparar_aux(Bala_nave):
            global Lives3
            #daño caja Bala
            #daño caja boss
            daño_cajaBa = self.canvas.bbox(Bala_nave)
            daño_cajbo = self.canvas.bbox(self.Iboss)
                
            if daño_cajbo[2]>daño_cajaBa[0]>daño_cajbo[0] and daño_cajbo[1]<daño_cajaBa[3]<daño_cajbo[3]:
                Lives3-=1
                puntuacion()
                self.canvas.delete(Bala_nave)
                self.Lives3Label.configure(text="Livesboss: " + str(Lives3))

            if self.canvas.coords(Bala_nave) != []:
                if seguir3 == True:
                    if self.canvas.coords(Bala_nave)[1]<0:
                        self.canvas.delete(Bala_nave)
                    else:
                        self.canvas.move(Bala_nave, 0, -10)
                        self.canvas.after(35,disparar_aux,Bala_nave)
            
            #self.m = 0
            #self.s = 0
        #Funcion para el relog
        def crocro():
            global pro
            if self.ss >= 60:
                self.ss = 0
                self.ms +=1
                if self.ms >= 60:
                    self.ms = 0
            self.ti.configure(text = str(self.ms)+":"+str(self.ss))
            self.ss+=1
            if seguir3 == True:
                pro = self.canvas.after(1000,crocro)
        crocro()
        #Funcion para el movimiento del jefe de isquierda a derecha
        def mover_jefe1(x):
            
            if self.ss%6==0: 
                ran = randint(1,10)
                time.sleep(0.9)
                if seguir3 == True:
                    if ran%3 == 0:
                        embestidon()
                        return mover_jefe1(x)
                    
            if self.canvas.coords(self.Iboss)[0]>250:
                self.canvas.move(self.Iboss,-5,0)
                time.sleep(0.1)
                return mover_jefe1(-5)
            elif self.canvas.coords(self.Iboss)[0]<0:
                self.canvas.move(self.Iboss,5,0)
                time.sleep(0.1)
                return mover_jefe1(5)
            else:
                self.canvas.move(self.Iboss,x,0)
                time.sleep(0.1)
                return mover_jefe1(x)
        t99 = Thread(target=mover_jefe1, args=(5,))
        if seguir3 == True:
            t99.start()
        #Funcion para el disparo del jefe
        def disparar_jefe():
            x = self.canvas.coords(self.Iboss)[0]
            y = self.canvas.coords(self.Iboss)[1]
            Bala_jefe05 = self.canvas.create_image(x,y+75,image=self.Bala_jefe01, anchor=NW)
            Bala_jefe06 = self.canvas.create_image(x+35,y+75,image=self.Bala_jefe01, anchor=NW)
            Bala_jefe07 = self.canvas.create_image(x+70,y+75,image=self.Bala_jefe01, anchor=NW)
            
            t05 = Thread(target=disparar_jefe_aux1, args=(Bala_jefe05, ))
            t05.start()
            t06 = Thread(target=disparar_jefe_aux1,args=(Bala_jefe06, ))
            t06.start()
            t07 = Thread(target=disparar_jefe_aux1,args=(Bala_jefe07, ))
            t07.start()
            self.canvas.after(1000,disparar_jefe)
       
        t98 = Thread(target=disparar_jefe)
        if seguir3 == True:
            t98.start()
        def disparar_jefe_aux1(Bala_jefe01):
            global Livesnave2
            #daño caja Bala
            #daño caja nave
            daño_cajaBa = self.canvas.bbox(Bala_jefe01)
            daño_cajna = self.canvas.bbox(self.ships)
    
            #bbox de la primera bala
            if daño_cajna[2]>daño_cajaBa[0]>daño_cajna[0] and daño_cajna[1]<daño_cajaBa[3]<daño_cajna[3]:
                Livesnave2-=3
                self.canvas.delete(Bala_jefe01)
                self.Livesnave2Label.configure(text="Livesnave: " + str(Livesnave2))
                

            #movimiento de las balas   
            if self.canvas.coords(Bala_jefe01) != []:
                #primer disparo
                if self.canvas.coords(Bala_jefe01)[1]<400:
                    self.canvas.move(Bala_jefe01, 0, 5)
                    self.canvas.after(30,disparar_jefe_aux1,Bala_jefe01)
                else:
                    self.canvas.delete(Bala_jefe01)
            if Lives3 == 0:
                seguir3 = False
                
                
                
        #Funcion para la puntuacion
        def puntuacion():
            global score
            if Lives3<50:
                score=score + 10
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
        def bonificasion3():
            global score
            if Livesnave2 == 50:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
                return  bonificasion3()
            if self.ss <= 30:
                score=score + 30
                self.scoreLabel.configure(text="score: " + str(score))
            else:
                self.scoreLabel.configure(text="score: " + str(score))
        #Funcion para el daño de la embestida
        def colicion2():
            global Livesnave2
            #daño caja nave
            daño_cajana = self.canvas.bbox(self.ships)
            #daño caja boss
            daño_cajabo = self.canvas.bbox(self.Iboss)
            if daño_cajabo[2]>daño_cajana[0]>daño_cajabo[0] and daño_cajabo[2]<daño_cajana[3]<daño_cajabo[3]:
                global Livesnave2
                print("gj")
                Livesnave2-=10
                self.Livesnave2Label.config(text="Livesnave: " + str(Livesnave2))
        #Funcion para la embestida
        def embestidon():
            if self.canvas.coords(self.Iboss)[1]<375:
                self.canvas.move(self.Iboss,0,30)
                colicion2()
                time.sleep(0.1)
                return embestidon()
            else:
                return regresesame()
        #Funcion para el regreso del jefe despues de la embestida
        def regresesame():
            if self.canvas.coords(self.Iboss)[1]>0:
                ron = randint(1,2)
                ranx = randint(0,250)
                if ron == 1:
                    self.canvas.coords(self.Iboss,0,0)
                    time.sleep(0.1)
                if ron == 2:
                    self.canvas.coords(self.Iboss,ranx,0)                
                    time.sleep(0.1)
                    return embestidon()
                return regresesame()
window = tkinter.Tk()
r = IntVar()
window.geometry("350x450")
window.title("Operation Undertale")
ventana_principal = Ventana_Principal(window)
window.mainloop()
