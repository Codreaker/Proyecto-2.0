from tkinter import *
from tkinter.ttk import Progressbar
from random import *
from PIL import Image, ImageTk, ImageSequence
from threading import Thread
import time


Nave = 3
puntaje = 0
nombre = ""
minutos=0
minutos_nivel_dos = 0
minutos_nivel_tres = 0
parar = True
xspeed = 1 
yspeed = 4

# clase donde estara el juego con ambas ventanas
class Pantalla_principal:
    def __init__(self, master):
        self.master = master
        self.master_seg = master
        self.master_ter = master
        self.canvas = Canvas(master, width=796, height=500, highlightthickness=0, relief='ridge', bg="black")
        self.canvas.place(x=0, y=0)
        self.pantallaInicio()

    def pantallaInicio(self):
        self.canvas = Canvas(self.master, width=796, height=500, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)

        # Label en la parte superior para texto de bienvenido
        self.bienvenido = Label(self.canvas, text="GLOW IN THE DARK", font=("Helvetica", 12), fg="#f55cdf", bg="#190F3B")
        self.bienvenido.place(x=200,y=30)
        #Label para indicar escribir el nombre
        self.name_please = Label(self.canvas, text="Digite su nombre:", fg="#f55cdf", bg="#1A1153")
        self.name_please.place(x=200,y=155,width=100,height=30)

        #entrada de texto para el nombre
        self.player_name = Entry(self.canvas)
        self.player_name.place(x=300,y=155,width=100,height=30)

        #Radiobotton con el primer nivel
        self.level_2 = Radiobutton(self.canvas,text="2",variable=valorRango, value=2,bg="#b4b0f7")
        self.level_2.place(x=275,y=186,width=50,height=20)

        #Radiobotton con el segundo nivel
        self.level_1 = Radiobutton(self.canvas,text="1", variable=valorRango,value=1,bg="#b4b0f7")
        self.level_1.place(x=200,y=186,width=50,height=20)

        self.level_3 = Radiobutton(self.canvas,text="3",  variable=valorRango,value=3,bg="#b4b0f7")
        self.level_3.place(x=350,y=186,width=50,height=20)

        # boton jugar para llamar al metodo que hace las validaciones
        self.boton_jugar = Button(self.canvas, text="Jugar", font=("Times New Roman", 16),bg="#1d2086", command=self.validaciones)
        self.boton_jugar.place(x=250,y=250,width=100,height=30)

        self.button_mostrar = Button(self.canvas, text ="Creditos", fg="black", bg="#6e67ed", command = self.creditos)
        self.button_mostrar.place(x=0,y=470,width=100,height=30)
        self.button_mostrar = Button(self.canvas, text ="Puntajes", fg="black", bg="#b4b0f7", command = self.puntajes)
        self.button_mostrar.place(x=500,y=470,width=100,height=30)
        
    #ventana de puntajes
    def puntajes(self):
        self.canvas = Canvas(self.master, width=796, height=800, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        self.score = Label(self.canvas, text="Puntaje: ", font=("Helvetica", 15), fg="#f55cdf", bg="#1d2086")
        self.score.place(x=200,y=30)
        self.boton_back_punt = Button(self.canvas, text="Back",font=("Times New Roman", 18),bg="#1d2086",command=self.pantallaInicio)
        self.boton_back_punt.place(x=250,y=470,width=100,height=30)

   
    #ventana about con labels que muestran informacion importante
    def creditos(self):
        self.canvas = Canvas(self.master, width=796, height=500, relief='ridge',bg="#1d2086")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)

        self.info1 = Label(self.canvas, text="Costa Rica", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info1.place(x=0,y=30)

        self.info2 = Label(self.canvas, text="Instituto Tecnologico de Costa Rica", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info2.place(x=0, y=55)

        self.info3 = Label(self.canvas, text="Ingeniería en Computadores", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info3.place(x=0, y=85)

        self.info4 = Label(self.canvas, text="CE 1102-Taller de Programación", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info4.place(x=0, y=105)

        self.info5 = Label(self.canvas, text="Grupo 4", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info5.place(x=0, y=135)

        self.info6 = Label(self.canvas, text="Año: 2021", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info6.place(x=0, y=165)

        self.info7 = Label(self.canvas, text="Profesor: Luis Alonso Artavia Barboza", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info7.place(x=0, y=195)

        self.info8 = Label(self.canvas, text="Versión del Juego 1.2", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info8.place(x=0, y=225)

        self.info9 = Label(self.canvas, text="Autores: Luis Morera Cortes and Cristopher Blanco Fallas", font=("Times New Roman", 15),fg="green",bg="#1d2086")
        self.info9.place(x=0, y=255)

        self.info10 = Label(self.canvas, text="Importante:", font=("Times New Roman", 15),fg="red",bg="#1d2086")
        self.info10.place(x=0, y=285)

        self.info11 = Label(self.canvas, text="1.Use las flechas arriba,abajo,derecha,izquierda para mover la nave", font=("Comic Sans MS", 13),fg="green",bg="#1d2086")
        self.info11.place(x=0, y=315)

        self.info11 = Label(self.canvas, text="2.Use la tecla 1 para disparar ", font=("Comic Sans MS", 15),fg="green",bg="#1d2086")
        self.info11.place(x=0, y=345)
        
        self.boton_back_c = Button(self.canvas, text="Back",font=("Times New Roman", 15),bg="#1d2086",command=self.pantallaInicio)
        self.boton_back_c.place(x=250,y=470,width=100,height=30)
   

    # valida que el entry para nombre no este vacío y si hay un radiobutton seleccionado o no
    def validaciones(self):
        global nombre
        
        if self.player_name.get() != "":
            nombre +=self.player_name.get()
            if valorRango.get() == 1 or valorRango.get() == 0:
                self.primerNivel()
                self.nombreJugador_N1.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label   
            if valorRango.get() == 2:
                self.segundoNivel()
                self.nombreJugador_N2.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label
            if valorRango.get() == 3:
                self.tercerNivel()
                self.nombreJugador_N3.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label

    # primer nivel del juego 
    def primerNivel(self):
        global parar
        global Nave
        self.canvas = Canvas(self.master, width=796, height=500, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.boton_retorno1 = Button(self.canvas, text="back",font=("Comic Sans MS", 9),bg="#1d2086")
        self.boton_retorno1.place(x=0,y=218, width=100, height=30)
        
        self.vidanave = Label(self.canvas, text="Vida: ", font=("Helvetica", 9), fg="#f55cdf", bg="#1d2086")
        self.vidanave.place(x=0, y=130)
        
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'zafkiel.gif'))]
        self.image = self.canvas.create_image(400,250, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)
        #tiempo nivel 1
        self.tiempo_nivel1 = Label(self.canvas, text="tiempo",font=("Comic Sans MS", 9),fg="red",bg="#1d2086")
        self.tiempo_nivel1.place(x=0, y=172)

        #muestra el puntaje
        self.puntaje_N1 = Label(self.canvas, text="puntaje: 0",font=("Comic Sans MS", 9),fg="red",bg="#1d2086")
        self.puntaje_N1.place(x=0, y=150)

        #nombre del jugador nivel 1
        self.nombreJugador_N1 = Label(self.canvas, text="", font=("Comic Sans MS", 9),fg="red",bg="#1d2086")
        self.nombreJugador_N1.place(x=0, y=195)

        #boton de retorno a la pantalla de inicio
        self.boton_retorno1 = Button(self.canvas, text="back",font=("Comic Sans MS", 9),bg="#1d2086",command=self.retorno)
        self.boton_retorno1.place(x=0,y=218, width=100, height=30)

        #importa y coloca la img de la nave
        self.Nave=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N1 = self.canvas.create_image(250,402,image=self.Nave, anchor=NW)

        self.vidanave = Label(self.canvas, text="Vida: " + str(Nave), font=("Helvetica", 9), fg="#f55cdf", bg="#1d2086")
        self.vidanave.place(x=0, y=130)
        
        self.enemiga = ImageTk.PhotoImage(Image.open("enemigo.png"))
        
        
        #importa img de la bala de la nave
        self.bala_nave=ImageTk.PhotoImage(Image.open("Fire1.gif"))
        
        self.enemigo=ImageTk.PhotoImage(Image.open("enemigo.png"))
        
        progress = Progressbar(window, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progress.place(x=0,y=250)
        #varible y llamada a la función de cronometro
        self.segundos=0

        #cronometro 
        def cronometro_N1():
            global minutos
            if self.segundos == 60:
                minutos+=1
                self.segundos=0
                self.tiempo_nivel1.configure(text="tiempo: "+ str(minutos)+":"+str(self.segundos))#actualiza el tiempo
                return self.jefe_derrotado()
            self.tiempo_nivel1.configure(text="tiempo: "+str(minutos)+":"+ str(self.segundos))#actualiza el tiempo
            self.segundos += 1
            self.canvas.after(1000,cronometro_N1)#repite la funcion cada segundo
        cronometro_N1()
        def rebotedebalas():
            
            #crea las balas
            enemigo = self.canvas.create_image(600, 0,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(500, 0,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(400, 0,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(300, 0,image=self.enemiga, anchor=NW)
            enemigocinco = self.canvas.create_image(200, 0,image=self.enemiga, anchor=NW)
            
            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo)
            rebotedebalas_aux(enemigodos)
            rebotedebalas_aux(enemigotres)
            rebotedebalas_aux(enemigocuatro)
            rebotedebalas_aux(enemigocinco)
            #self.canvas.after(100,rebotedebalas)

        def rebotedebalas_aux(enemigo):
            global xspeed
            global yspeed
            self.canvas.move(enemigo, xspeed, yspeed)
            #obtiene coordenadas del enemigo en el eje x,y
            x = self.canvas.coords(enemigo)[0]
            y = self.canvas.coords(enemigo)[1]
            
            if self.canvas.coords(enemigo)[0] > 760 or self.canvas.coords(enemigo)[0] < 0: # y range
                    xspeed = -xspeed
            if self.canvas.coords(enemigo)[1] > 450 or self.canvas.coords(enemigo)[1] < 0: # x range
                    yspeed = -yspeed
            
            self.canvas.after(10, rebotedebalas_aux,enemigo)

        rebotedebalas()


        def colision_n1():
            global Nave
            #daño caja nave
            Caja_nave = self.canvas.bbox(self.nave_N1)
            #daño caja boss
            daño_cajabo = self.canvas.bbox(self.enemigo)
            if daño_cajabo[2]>daño_cajana[0]>daño_cajabo[0] and daño_cajabo[2]<daño_cajana[3]<daño_cajabo[3]:
               global Nave
               Nave-=10
               self.vidanave.config(text="Nave: " + str(Nave))
    

        #verifica las teclas y realiza el movimiento de la nave
        def movimiento_nave(mover):
            if mover.keysym=='Right' and self.canvas.coords(self.nave_N1)[0]<745:#derecha
                self.canvas.move(self.nave_N1, 8, 0)
            if mover.keysym=='Left' and self.canvas.coords(self.nave_N1)[0]>0:#izquierda
                self.canvas.move(self.nave_N1, -8, 0)   
            if mover.keysym=='Down' and self.canvas.coords(self.nave_N1)[1]<405:#abajo
                self.canvas.move(self.nave_N1, 0, 8)
            if mover.keysym=='Up' and self.canvas.coords(self.nave_N1)[1]>0:#arriba
                self.canvas.move(self.nave_N1, 0, -8)
        self.master.bind("<KeyPress>", movimiento_nave)#para evento continuo de teclas
        
        #verifica la tecla presionada
        def disparo_nave(tecla):
            if tecla.keysym == 'f':
                #obtiene las coordenadas de la nave y crea la bala en esa posicion
                self.x = self.canvas.coords(self.nave_N1)[0]
                self.y = self.canvas.coords(self.nave_N1)[1]
                bala_nave = self.canvas.create_image(self.x+10,self.y,image=self.bala_nave, anchor=NW)
                disparo_nave_aux(bala_nave)#llama a la funcion de movimiento de la bala de la nave

        self.master.bind("<KeyRelease>", disparo_nave)#para evento discontinuo de teclas
        #realiza el movimiento de la bala
        def disparo_nave_aux(bala_nave):
            if self.canvas.coords(bala_nave)[1] > 0:
                self.canvas.move(bala_nave, 0, -10)
                self.canvas.after(20,disparo_nave_aux,bala_nave)
            else:
                self.canvas.delete(bala_nave)#elimina la bala cuando llega al limite superior
      
        def barra_de_progreso():
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite):
                time.sleep(1)
                progress["value"]+=(speed/Limite)*100
                Tiempo+=speed
                window.update_idletasks()
        t1 = Thread(target= barra_de_progreso)
        t1.start()

    #segundo nivel del juego
    def segundoNivel(self):
        global puntaje
        self.canvas = Canvas(self.master, width=796, height=500, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'clockword.gif'))]
        self.image = self.canvas.create_image(400,250, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)


        #boton de retorno a la pantalla de inicio
        self.boton_retorno2 = Button(self.canvas, text="back",font=("Comic Sans MS", 8),bg="#1d2086",command=self.retorno)
        self.boton_retorno2.place(x=0,y=218, width=100, height=30)

        #label para mostrar la vida de la nave
        self.vidanave2= Label(self.canvas,text="vida: 3",font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.vidanave2.place(x=0, y=130)

        #nombre del jugador nivel 2
        self.nombreJugador_N2 = Label(self.canvas, text="", font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.nombreJugador_N2.place(x=0, y=195)

        #label para mostrar el puntaje
        self.puntaje_N2 = Label(self.canvas, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.puntaje_N2.place(x=0, y=150)

        #label para mostrar el tiempo
        self.tiempo_nivel2 = Label(self.canvas, text="tiempo",font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.tiempo_nivel2.place(x=0, y=172)

        #importa img de la nave
        self.Nave2=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N2 = self.canvas.create_image(250,402,image=self.Nave2, anchor=NW)

        #importa img de las balas de la nave y el enemigo
        self.bala_nave2=ImageTk.PhotoImage(Image.open("Fire1.gif"))
        progreso = Progressbar(window, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progreso.place(x=0,y=250)

        #variable y llamada a la funcion de cronometro
        self.segundos2=0
        

        #llama a la funcion de colision
  

        #cronometro 
        def iniciar2():
            global minutos_nivel_dos
            if self.segundos2 == 60:
                minutos_nivel_dos += 1
                self.segundos2=0
                self.tiempo_nivel2.configure(text="tiempo: "+ str(minutos_nivel_dos)+":"+str(self.segundos2))#actualiza el tiempo
                return self.jefe_derrotado()
            self.tiempo_nivel2.configure(text="tiempo: "+ str(minutos_nivel_dos)+":"+str(self.segundos2))#actualiza el tiempo
            self.segundos2 +=1
            self.canvas.after(1000,iniciar2)#repite el proceso cada segundo
        iniciar2()        

        
        #verifica la tecla presionada
        def disparo_nave_2(tecla):
            if tecla.keysym == 'f':
                #obtiene las coordenadas de la nave y crea la bala en esa posicion
                self.x = self.canvas.coords(self.nave_N2)[0]
                self.y = self.canvas.coords(self.nave_N2)[1]
                bala_nave_N2 = self.canvas.create_image(self.x+15,self.y,image=self.bala_nave2, anchor=NW)
                disparar_aux2(bala_nave_N2)
        self.master.bind("<KeyRelease>", disparo_nave_2)#para evento discontinuo de teclas
        #realiza el movimiento de la bala
        def disparar_aux2(bala_nave2):
            if self.canvas.coords(bala_nave2)[1] > 0:
                self.canvas.move(bala_nave2, 0, -10)
                self.canvas.after(20, disparar_aux2,bala_nave2)
            else:
                self.canvas.delete(bala_nave2)#elimina la bala cuando llega al limite superior
                
        #verifica las teclas y realiza el movimiento de la nave
        def mover_nave_2(mover):
            if mover.keysym=='Right' and self.canvas.coords(self.nave_N2)[0]<745:#derecha
                self.canvas.move(self.nave_N2, 15, 0)
            if mover.keysym=='Left' and self.canvas.coords(self.nave_N2)[0]>0:#izquierda
                self.canvas.move(self.nave_N2, -15, 0)   
            if mover.keysym=='Down' and self.canvas.coords(self.nave_N2)[1]<405:#abajo
                self.canvas.move(self.nave_N2, 0, 15)
            if mover.keysym=='Up' and self.canvas.coords(self.nave_N2)[1]>0:#arriba
                self.canvas.move(self.nave_N2, 0, -15)
        self.master.bind("<KeyPress>",mover_nave_2)#para evento continuo de teclas
        def barra_de_progreso_2():
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite):
                time.sleep(1)
                progreso['value']+=(speed/Limite)*100
                Tiempo+=speed
                window.update_idletasks()
        t2 = Thread(target= barra_de_progreso_2)
        t2.start()

    def tercerNivel(self):
        global puntaje
        global no_dispare#global para detener el disparo del enemigo
        self.canvas = Canvas(self.master, width=796, height=500, relief='ridge',bg="#1d2086")
        self.canvas.place(x=0, y=0)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'wow.gif'))]
        self.image = self.canvas.create_image(400,250, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(120, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)


        #boton para regresar a pantalla de inicio
        self.boton_retorno3 = Button(self.canvas, text="back",font=("Times New Roman", 8),command=self.retorno)
        self.boton_retorno3.place(x=0,y=218, width=100, height=30)

        #nombre del jugador nivel 3
        self.nombreJugador_N3 = Label(self.canvas, text="", font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.nombreJugador_N3.place(x=0, y=195)

        #vida de la nave nivel 3
        self.vidanave3 = Label(self.canvas, text="vida: 3", font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.vidanave3.place(x=0, y=130)

        #muestra el puntaje
        self.puntaje_N3 = Label(self.canvas, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.puntaje_N3.place(x=0, y=150)

        #label que muestra el tiempo
        self.tiempo_N3 = Label(self.canvas, text="tiempo ",font=("Comic Sans MS", 8),fg="red",bg="#1d2086")
        self.tiempo_N3.place(x=0, y=172)

        #importa imagen de la nave del nivel 3
        self.nave_N3_img=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N3 = self.canvas.create_image(250,405,image=self.nave_N3_img, anchor=NW)#coloca la imagen en la ventana


        self.bala_nave_3 = ImageTk.PhotoImage(Image.open("Fire1.gif"))#importa imagen de la bala de la nave
        #variable y llamada al cronometro
        self.segundos_N3=0
        progresoo = Progressbar(window, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progresoo.place(x=0,y=250)
        


        

        #cuenta el tiempo
        def cronometro_N3():
            global minutos_nivel_tres
            if self.segundos_N3 == 60:#verifica si se llego a 60 segundos
                minutos_nivel_tres +=1#aumenta en 1 los minutos
                self.segundos_N3=0
                self.tiempo_N3.configure(text="tiempo "+ str(minutos_nivel_tres)+":"+str(self.segundos_N3))#actualiza los minutos y segundos
                return self.jefe_derrotado()
            self.tiempo_N3.configure(text="tiempo "+ str(minutos_nivel_tres)+":"+str(self.segundos_N3))#actualiza los segundos
            self.segundos_N3 +=1
            self.canvas.after(1000,cronometro_N3)#repite la funcion cada 1 segundo
        cronometro_N3()
        #verifica la tecla de disparo
        def disparo_nave3(tecla):
            if tecla.keysym == '1':
            #crea la bala de la nave y obtiene la posicion de la nave
                self.x = self.canvas.coords(self.nave_N3)[0]
                self.y = self.canvas.coords(self.nave_N3)[1]
                bala_nave_3 = self.canvas.create_image(self.x+15,self.y,image=self.bala_nave_3, anchor=NW)#crea la bala en la posicion de la nave
                disparo_nave_aux_N3(bala_nave_3)

        self.master.bind("<KeyRelease>", disparo_nave3)#realiza el evento de varias pulsaciones de tecla
        #realiza el movimiento de la bala
        def disparo_nave_aux_N3(bala_nave_3):
            if self.canvas.coords(bala_nave_3)[1] > 0:
                self.canvas.move(bala_nave_3, 0, -10)
                self.canvas.after(20,disparo_nave_aux_N3,bala_nave_3)
            else:
                self.canvas.delete(bala_nave_3)#elimina la bala cuando llega al limite superior
                
        def mover_nave3(mover):
            if mover.keysym=='Right' and self.canvas.coords(self.nave_N3)[0]<745:#se mueve a la derecha hasta el limite
                self.canvas.move(self.nave_N3, 8, 0)
            if mover.keysym=='Left' and self.canvas.coords(self.nave_N3)[0]>0:#se mueve a la izquierda hasta el limite
                self.canvas.move(self.nave_N3, -8, 0)   
            if mover.keysym=='Down' and self.canvas.coords(self.nave_N3)[1]<405:#se mueve abajo hasta el limite
                self.canvas.move(self.nave_N3, 0, 8)
            if mover.keysym=='Up' and self.canvas.coords(self.nave_N3)[1]>0:#se mueve arriba hasta el limite
                self.canvas.move(self.nave_N3, 0, -8)
        self.master.bind("<KeyPress>", mover_nave3)#realiza el evento de mantener pulsada las teclas
        def barra_de_progreso_3():
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite):
                time.sleep(1)
                progresoo['value']+=(speed/Limite)*100
                Tiempo+=speed
                window.update_idletasks()
        t3 = Thread(target= barra_de_progreso_3)
        t3.start()


    #verifica cuando el enemigo es derrotado y pasa al siguiente nivel
    def jefe_derrotado(self):
        global Nave
        global nombre
        global minutos
        global minutos_nivel_dos
        global minutos_nivel_tres
        
        if minutos == 1:#verifica el nivel 1
            self.bonus()
            time.sleep(1)
            self.canvas.destroy()
            self.segundoNivel()
            self.nombreJugador_N2.configure(text=nombre)
     
        if minutos_nivel_dos == 1:#verifica el nivel 2
            self.bonus()
            self.canvas.destroy()
            time.sleep(1)
            self.tercerNivel()
            self.nombreJugador_N3.configure(text=nombre)
            
        if minutos_nivel_tres == 1:#verifica el nivel 3
            self.bonus()
            self.canvas.destroy()
            time.sleep(1)
            self.retorno()

    #verifica si se cumplen las condiciones para el bonus del puntaje
    def bonus(self):
        global minutos
        global puntaje
        global Nave
        global minutos_nivel_dos
        global minutos_nivel_tres
        if minutos_nivel_tres==0:
            puntaje +=20
        if minutos_nivel_dos==0:
            puntaje +=20
        if minutos==0:
            puntaje +=20
        if Nave==3:
            puntaje +=10 
            
     


    #verifica cuando la vida de la nave llega a 0 y llama a la función de retorno
    def juego_perdido(self):
        global Nave
        Nave=3
        self.retorno()

    #retorna a la pantalla principal desde cualquier ventana
    def retorno(self):
        global Nave
        global puntaje
        global minutos
        global nombre
        global minutos_nivel_dos
        global minutos_nivel_tres
        
        
        if Nave < 3: #verifica y restablece la vida de la nave
            Nave=3
        puntaje=0#restablece el puntaje
        minutos_nivel_dos = 0
        minutos_nivel_tres = 0
        minutos=0
        nombre=""
        self.canvas.destroy()
        self.pantallaInicio()



window = Tk()
valorRango = IntVar()
window.config(cursor="pirate")
ventana_principal = Pantalla_principal(window)
window.title("space")
window.minsize(800, 500)
window.resizable(False, False)
window.mainloop()


