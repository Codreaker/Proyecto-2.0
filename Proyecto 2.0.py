from tkinter import *
import pygame
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
pasa = True

# clase donde estara el juego con ambas ventanas
class Pantalla_principal:
    def __init__(self, master):
        self.master = master
        self.master_seg = master
        self.master_ter = master
        self.canvas = Canvas(master, width=1200, height=700, highlightthickness=0, relief='ridge', bg="black")
        self.canvas.place(x=0, y=0)
        self.pantallaInicio()

    def pantallaInicio(self):
 
        
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)

        # Label en la parte superior para texto de bienvenido
        self.bienvenido = Label(self.canvas, text="CLOCKWORK PLANET", font=("Helvetica", 12), fg="#c44387", bg="#27433a")
        self.bienvenido.place(x=510,y=30)
        #Label para indicar escribir el nombre
        self.name_please = Label(self.canvas, text="Digite su nombre:", fg="#c44387", bg="#27433a")
        self.name_please.place(x=450,y=155,width=100,height=30)


        pygame.init()
        pygame.mixer.music.load("Musica.ogg")
        pygame.mixer.music.play(4)

        global paused
        paused = False
        def parar_o_reanudar_musica(is_paused):
            global paused
            paused = is_paused
            if paused:
                pygame.mixer.music.unpause()
                paused = False
            else:
                pygame.mixer.music.pause()
                paused = True

        self.mute = Button(self.canvas, text="Mute",font=("Comic Sans MS", 5),bg="#b4b0f7",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=550,y=670, width=80, height=30)
        
        #entrada de texto para el nombre
        self.player_name = Entry(self.canvas)
        self.player_name.place(x=550,y=155,width=100,height=30)

        #Radiobotton con el primer nivel
        self.level_2 = Radiobutton(self.canvas,text="Intermedio",variable=valorRango, value=2,bg="#b4b0f7")
        self.level_2.place(x=560,y=186,width=80,height=20)

        #Radiobotton con el segundo nivel
        self.level_1 = Radiobutton(self.canvas,text="Facil", variable=valorRango,value=1,bg="#b4b0f7")
        self.level_1.place(x=480,y=186,width=70,height=20)

        self.level_3 = Radiobutton(self.canvas,text="Dificil",  variable=valorRango,value=3,bg="#b4b0f7")
        self.level_3.place(x=650,y=186,width=70,height=20)

        # boton jugar para llamar al metodo que hace las validaciones
        self.boton_jugar = Button(self.canvas, text="Jugar", font=("Times New Roman", 16),bg="#b4b0f7", command=self.validaciones)
        self.boton_jugar.place(x=550,y=210,width=100,height=30)

        self.button_mostrar = Button(self.canvas, text ="Creditos", fg="black", bg="#6e67ed", command = self.creditos)
        self.button_mostrar.place(x=3,y=670,width=100,height=30)
        self.button_mostrar = Button(self.canvas, text ="Puntajes", fg="black", bg="#b4b0f7", command = self.puntajes)
        self.button_mostrar.place(x=1100,y=670,width=100,height=30)
        
        
    #ventana de puntajes
    def puntajes(self):
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="#b4b0f7")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        self.score = Label(self.canvas, text="Puntaje: ", font=("Helvetica", 15), fg="#f55cdf", bg="#b4b0f7")
        self.score.place(x=200,y=30)
        self.boton_back_punt = Button(self.canvas, text="Back",font=("Times New Roman", 18),bg="#b4b0f7",command=self.pantallaInicio)
        self.boton_back_punt.place(x=350,y=520, width=80, height=30)

   
    #ventana about con labels que muestran informacion importante
    def creditos(self):
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="#b4b0f7")
        self.canvas.place(x=0, y=0)
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)

        self.info1 = Label(self.canvas, text="Costa Rica", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info1.place(x=3,y=30)

        self.info2 = Label(self.canvas, text="Instituto Tecnologico de Costa Rica", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info2.place(x=3, y=55)

        self.info3 = Label(self.canvas, text="Ingeniería en Computadores", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info3.place(x=3, y=85)

        self.info4 = Label(self.canvas, text="CE 1102-Taller de Programación", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info4.place(x=3, y=105)

        self.info5 = Label(self.canvas, text="Grupo 4", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info5.place(x=3, y=135)

        self.info6 = Label(self.canvas, text="Año: 2021", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info6.place(x=3, y=165)

        self.info7 = Label(self.canvas, text="Profesor: Luis Alonso Artavia Barboza", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info7.place(x=3, y=195)

        self.info8 = Label(self.canvas, text="Versión del Juego 1.2", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info8.place(x=3, y=225)

        self.info9 = Label(self.canvas, text="Autores: Luis Morera Cortes and Cristopher Blanco Fallas", font=("Times New Roman", 15),fg="green",bg="#b4b0f7")
        self.info9.place(x=3, y=255)

        self.info10 = Label(self.canvas, text="Importante:", font=("Times New Roman", 15),fg="red",bg="#b4b0f7")
        self.info10.place(x=3, y=285)

        self.info11 = Label(self.canvas, text="1.Use las flechas arriba,abajo,derecha,izquierda para mover la nave", font=("Comic Sans MS", 13),fg="green",bg="#b4b0f7")
        self.info11.place(x=3, y=315)

        self.boton_back_c = Button(self.canvas, text="Back",font=("Times New Roman", 15),bg="#b4b0f7",command=self.pantallaInicio)
        self.boton_back_c.place(x=350,y=520, width=80, height=30)
   

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
        self.canvas = Canvas(self.master, width=1200, height=650, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)
 
        
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'wow.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)


        pygame.init()
        pygame.mixer.music.load("MarieNoChouzetsuGikou-KarinNakanoSatoshiHono-5036166.mp3")
        pygame.mixer.music.play(4)
        
        

        
         #boton de retorno a la pantalla de inicio
        self.boton_retorno = Button(self.canvasdos, text="back",font=("Comic Sans MS", 8),fg="red",bg="black",command=self.retorno)
        self.boton_retorno.place(x=1149,y=3, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.vidanave.place(x=103, y=3)

        #nombre del jugador nivel 2
        self.nombreJugador_N1 = Label(self.canvasdos, text="", font=("Comic Sans MS", 8),fg="red",bg="black")
        self.nombreJugador_N1.place(x=275, y=3)

        #label para mostrar el puntaje
        self.puntaje = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="black")
        self.puntaje.place(x=147, y=3)

        #label para mostrar el tiempo
        self.tiempo_nivel1 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.tiempo_nivel1.place(x=207, y=3)

        #importa img de las balas de la nave y el enemigo
        progress = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progress.place(x=0,y=3)
        global paused
        paused = False
        def parar_o_reanudar_musica(is_paused):
            global paused
            paused = is_paused
            if paused:
                pygame.mixer.music.unpause()
                paused = False
            else:
                pygame.mixer.music.pause()
                paused = True
     
        self.mute = Button(self.canvasdos, text="Mute or UnMute",font=("Comic Sans MS", 5),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)
   

        #importa y coloca la img de la nave
        self.Nave=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N1 = self.canvas.create_image(550,555,image=self.Nave, anchor=NW)


        
        self.enemiga = ImageTk.PhotoImage(Image.open("enemigo.png"))
        
        
        

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

        def sonido_choque():
            sonido_choque = pygame.mixer.Sound("golpe.mp3")
            sonido_choque.play()
            
        
        def rebotedebalas():
            ran = randint(0,795)
            randos = randint(0,795)
            rantres = randint(0,795)
            rancuatro = randint(0,795)
            rancinco = randint(0,790)
           
            #crea las balas
            enemigo = self.canvas.create_image(ran, 100,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(randos, 170,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(rantres, 300,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(rancuatro, 450,image=self.enemiga, anchor=NW)
            enemigocinco = self.canvas.create_image(rancinco, 30,image=self.enemiga, anchor=NW)
            
            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo,1,7)
            rebotedebalas_aux(enemigodos,1,7)
            rebotedebalas_aux(enemigotres,1,7)
            rebotedebalas_aux(enemigocuatro,1,7)
            rebotedebalas_aux(enemigocinco,1,7)
    

        def rebotedebalas_aux(enemigo, x , y):

            area_nave = self.canvas.bbox(self.nave_N1)
            #daño caja boss
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                if self.canvas.coords(enemigo)[0] > 1140 or self.canvas.coords(enemigo)[0] < 0: # y range
                        x = -x

                        
                        t5 = Thread(target= sonido_choque)
                        t5.start()

                        
                if self.canvas.coords(enemigo)[1] > 610 or self.canvas.coords(enemigo)[1] < 0: # x range
                        y = -y
                        

                        t5 = Thread(target= sonido_choque)
                        t5.start()

                if (area_nave[2]>area_Misil[0]>area_nave[0]) and (area_nave[1]<area_Misil[3]<area_nave[3]):
                        self.canvas.delete(enemigo)
                        global Nave
                        Nave-=1
                        self.vidanave.config(text="vida: " + str(Nave))
                        if Nave <= 0:
                            return self.juego_perdido()
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.delete(enemigo)

            self.canvas.after(10,lambda:rebotedebalas_aux(enemigo,x,y))
        rebotedebalas()


        #verifica las teclas y realiza el movimiento de la nave
        def movimiento_nave(mover):
            try:
                if mover.keysym=='Right' and self.canvas.coords(self.nave_N1)[0]<1140:#derecha
                    self.canvas.move(self.nave_N1, 15, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N1)[0]>0:#izquierda
                    self.canvas.move(self.nave_N1, -15, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N1)[1]<565:#abajo
                    self.canvas.move(self.nave_N1, 0, 15)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N1)[1]>0:#arriba
                    self.canvas.move(self.nave_N1, 0, -15)
            except IndexError:#controla el error y elimina la bala del enemigo
                self.canvas.move(self.nave_N1, 15, 0)
        self.master.bind("<KeyPress>", movimiento_nave)#para evento continuo de teclas
        
      
        def barra_de_progreso():
            global pasa
            pasa = True
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite and pasa):
                time.sleep(1)
                progress["value"]+=(speed/Limite)*100
                Tiempo+=speed
                window.update_idletasks()
        t1 = Thread(target= barra_de_progreso)
        t1.start()

        
    #segundo nivel del juego
    def segundoNivel(self):
        global puntaje
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'clockword.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)

        pygame.init()
        pygame.mixer.music.load("JitaiKyuuhen-KarinNakanoSatoshiHono-5036133.mp3")
        pygame.mixer.music.play(4)

        
        #boton de retorno a la pantalla de inicio
        self.boton_retorno2 = Button(self.canvasdos, text="back",font=("Comic Sans MS", 8),fg="red",bg="black",command=self.retorno)
        self.boton_retorno2.place(x=1149,y=3, width=50, height=20)
        self.mute = Button(self.canvasdos, text="Mute",font=("Comic Sans MS", 5),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave2= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.vidanave2.place(x=103, y=3)

        #nombre del jugador nivel 2
        self.nombreJugador_N2 = Label(self.canvasdos, text="", font=("Comic Sans MS", 8),fg="red",bg="black")
        self.nombreJugador_N2.place(x=275, y=3)

        #label para mostrar el puntaje
        self.puntaje_N2 = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="black")
        self.puntaje_N2.place(x=147, y=3)

        #label para mostrar el tiempo
        self.tiempo_nivel2 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.tiempo_nivel2.place(x=207, y=3)

        #importa img de la nave
        self.Nave2=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N2 = self.canvas.create_image(550,555,image=self.Nave2, anchor=NW)

        #importa img de las balas de la nave y el enemigo
        progreso = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progreso.place(x=0,y=3)

        #variable y llamada a la funcion de cronometro
        self.segundos2=0
        
        self.enemiga=ImageTk.PhotoImage(Image.open("enemigo.png"))
        #llama a la funcion de colision

        global paused
        paused = False
        def parar_o_reanudar_musica(is_paused):
            global paused
            paused = is_paused
            if paused:
                pygame.mixer.music.unpause()
                paused = False
            else:
                pygame.mixer.music.pause()
                paused = True
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

        

                
        #verifica las teclas y realiza el movimiento de la nave
        def mover_nave_2(mover):
            try:
                if mover.keysym=='Right' and self.canvas.coords(self.nave_N2)[0]<1140:#derecha
                    self.canvas.move(self.nave_N2, 15, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N2)[0]>0:#izquierda
                    self.canvas.move(self.nave_N2, -15, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N2)[1]<565:#abajo
                    self.canvas.move(self.nave_N2, 0, 15)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N2)[1]>0:#arriba
                    self.canvas.move(self.nave_N2, 0, -15)
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.move(self.nave_N2, 15, 0)
        self.master.bind("<KeyPress>",mover_nave_2)#para evento continuo de teclas
        def barra_de_progreso_2():
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite):
                time.sleep(1)
                progreso['value']+=(speed/Limite)*100
                Tiempo+=speed
                self.canvasdos.update_idletasks()
        t2 = Thread(target= barra_de_progreso_2)
        t2.start()
        def rebotedebalas():
            ran = randint(0,795)
            randos = randint(0,795)
            rantres = randint(0,795)
            rancuatro = randint(0,795)
            rancinco = randint(0,790)
            ranseis = randint(0,795)
            ransiete = randint(0,790)
            ranocho = randint(0,795)
          
           
            #crea las balas
            enemigo = self.canvas.create_image(ran, 100,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(randos, 170,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(rantres, 300,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(rancuatro, 450,image=self.enemiga, anchor=NW)
            enemigocinco = self.canvas.create_image(rancinco, 10,image=self.enemiga, anchor=NW)
            enemigoseis = self.canvas.create_image(ranseis, 240,image=self.enemiga, anchor=NW)
            enemigosiete = self.canvas.create_image(ransiete, 190,image=self.enemiga, anchor=NW)
            enemigoocho = self.canvas.create_image(ranocho, 500,image=self.enemiga, anchor=NW)
         
            
            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo,1,7)
            rebotedebalas_aux(enemigodos,1,7)
            rebotedebalas_aux(enemigotres,1,6)
            rebotedebalas_aux(enemigocuatro,1,3)
            rebotedebalas_aux(enemigocinco,1,8)
            rebotedebalas_aux(enemigoseis,1,6)
            rebotedebalas_aux(enemigosiete,1,7)
            rebotedebalas_aux(enemigoocho,1,10)
           
            #self.canvas.after(100,rebotedebalas)

        def rebotedebalas_aux(enemigo, x , y):
            area_nave = self.canvas.bbox(self.nave_N2)
            #daño caja boss
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                if self.canvas.coords(enemigo)[0] > 1140 or self.canvas.coords(enemigo)[0] < 0: # y range
                        x = -x
                if self.canvas.coords(enemigo)[1] > 610 or self.canvas.coords(enemigo)[1] < 0: # x range
                        y = -y
                if (area_nave[2]>area_Misil[0]>area_nave[0]) and (area_nave[1]<area_Misil[3]<area_nave[3]):
                        self.canvas.delete(enemigo)
                        global Nave
                        Nave-=1
                        self.vidanave2.config(text="vida: " + str(Nave))
                        if Nave <= 0:
                            return self.juego_perdido()
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.delete(enemigo)
            self.canvas.after(10,lambda:rebotedebalas_aux(enemigo,x,y))
        rebotedebalas()

    def tercerNivel(self):
        global puntaje
        global no_dispare#global para detener el disparo del enemigo
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="#1d2086")
        self.canvas.place(x=0, y=0)
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'zafkiel.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(120, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)



        pygame.init()
        pygame.mixer.music.load("ElectronicWarfare-KarinNakanoSatoshiHono-5036030.mp3")
        pygame.mixer.music.play(4)



        #importa imagen de la nave del nivel 3
        self.nave_N3_img=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N3 = self.canvas.create_image(550,555,image=self.nave_N3_img, anchor=NW)#coloca la imagen en la ventana

        

        #boton de retorno a la pantalla de inicio
        self.boton_retorno3 = Button(self.canvasdos, text="back",font=("Comic Sans MS", 8),fg="red",bg="black",command=self.retorno)
        self.boton_retorno3.place(x=1149,y=3, width=50, height=20)
        self.mute = Button(self.canvasdos, text="Mute",font=("Comic Sans MS", 5),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave3= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.vidanave3.place(x=103, y=3)

        #nombre del jugador nivel 2
        self.nombreJugador_N3 = Label(self.canvasdos, text="", font=("Comic Sans MS", 8),fg="red",bg="black")
        self.nombreJugador_N3.place(x=275, y=3)

        #label para mostrar el puntaje
        self.puntaje_N3 = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="black")
        self.puntaje_N3.place(x=147, y=3)

        #label para mostrar el tiempo
        self.tiempo_N3 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.tiempo_N3.place(x=207, y=3)



        #importa img de las balas de la nave y el enemigo
        progresoo = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progresoo.place(x=0,y=3)
        self.enemiga=ImageTk.PhotoImage(Image.open("enemigof.png"))
        self.segundos_N3=0

        global paused
        paused = False
        def parar_o_reanudar_musica(is_paused):
            global paused
            paused = is_paused
            if paused:
                pygame.mixer.music.unpause()
                paused = False
            else:
                pygame.mixer.music.pause()
                paused = True

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

                
        def mover_nave3(mover):
            try:
                if mover.keysym=='Right' and self.canvas.coords(self.nave_N3)[0]<1140:#se mueve a la derecha hasta el limite
                    self.canvas.move(self.nave_N3, 15, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N3)[0]>0:#se mueve a la izquierda hasta el limite
                    self.canvas.move(self.nave_N3, -15, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N3)[1]<565:#se mueve abajo hasta el limite
                    self.canvas.move(self.nave_N3, 0, 15)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N3)[1]>0:#se mueve arriba hasta el limite
                    self.canvas.move(self.nave_N3, 0, -15)
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.move(self.nave_N3, 15, 0)
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
        def rebotedebalas():
            ran = randint(0,700)
            randos = randint(0,700)
            rantres = randint(0,565)
            rancuatro = randint(0,735)
            rancinco = randint(0,770)
            ranseis = randint(0,715)
            ransiete = randint(0,725)
            ranocho = randint(0,775)
            rannueve = randint(0,725)
            randies = randint(0,700)
           
            #crea las balas
            enemigo = self.canvas.create_image(ran, 20,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(randos, 70,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(rantres, 150,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(rancuatro, 450,image=self.enemiga, anchor=NW)
            enemigocinco = self.canvas.create_image(rancinco, 10,image=self.enemiga, anchor=NW)
            enemigoseis = self.canvas.create_image(ranseis, 260,image=self.enemiga, anchor=NW)
            enemigosiete = self.canvas.create_image(ransiete, 400,image=self.enemiga, anchor=NW)
            enemigoocho = self.canvas.create_image(ranocho, 100,image=self.enemiga, anchor=NW)
            enemigonueve = self.canvas.create_image(rannueve, 200,image=self.enemiga, anchor=NW)
            enemigodies = self.canvas.create_image(randies, 300,image=self.enemiga, anchor=NW)
            
            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo,1,7)
            rebotedebalas_aux(enemigodos,1,6)
            rebotedebalas_aux(enemigotres,1,5)
            rebotedebalas_aux(enemigocuatro,1,3)
            rebotedebalas_aux(enemigocinco,1,2)
            rebotedebalas_aux(enemigoseis,1,8)
            rebotedebalas_aux(enemigosiete,1,5)
            rebotedebalas_aux(enemigoocho,1,4)
            rebotedebalas_aux(enemigonueve,1,6)
            rebotedebalas_aux(enemigodies,1,4)
            #self.canvas.after(100,rebotedebalas)

        def rebotedebalas_aux(enemigo, x , y):
            area_nave = self.canvas.bbox(self.nave_N3)
            #daño caja boss
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                if self.canvas.coords(enemigo)[0] > 1140 or self.canvas.coords(enemigo)[0] < 0: # y range
                        x = -x
                if self.canvas.coords(enemigo)[1] > 610 or self.canvas.coords(enemigo)[1] < 0: # x range
                        y = -y
                if (area_nave[2]>area_Misil[0]>area_nave[0]) and (area_nave[1]<area_Misil[3]<area_nave[3]):
                        self.canvas.delete(enemigo)
                        global Nave
                        Nave-=1
                        self.vidanave3.config(text="vida: " + str(Nave))
                        if Nave <= 0:
                            return self.juego_perdido()
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.delete(enemigo)
            self.canvas.after(10,lambda:rebotedebalas_aux(enemigo,x,y))
        rebotedebalas()


    #verifica cuando el enemigo es derrotado y pasa al siguiente nivel
    def jefe_derrotado(self):
        global pasa
        global Nave
        global nombre
        global minutos
        global minutos_nivel_dos
        global minutos_nivel_tres
        
        if minutos == 1:#verifica el nivel 1
            self.bonus()
            pasa = False
            pygame.mixer.stop()
            time.sleep(1)
            self.canvas.destroy()
            self.segundoNivel()
            self.nombreJugador_N2.configure(text=nombre)
     
        if minutos_nivel_dos == 1:#verifica el nivel 2
            self.bonus()
            pygame.mixer.stop()
            self.canvas.destroy()
            time.sleep(1)
            self.tercerNivel()
            self.nombreJugador_N3.configure(text=nombre)
            
        if minutos_nivel_tres == 1:#verifica el nivel 3
            self.bonus()
            pygame.mixer.stop()
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
        global pausa
        global minutos_nivel_dos
        global minutos_nivel_tres
        
        
        if Nave < 3: #verifica y restablece la vida de la nave
            Nave=3
        pausa = False
        puntaje=0#restablece el puntaje
        minutos_nivel_dos = 0
        minutos_nivel_tres = 0
        minutos=0
        nombre=""
        pygame.mixer.stop
        self.canvas.destroy()
        self.pantallaInicio()



window = Tk()

valorRango = IntVar()
window.config(cursor="pirate")
ventana_principal = Pantalla_principal(window)
window.title("space")
window.configure(bg="red")
window.minsize(1200, 700)
window.resizable(False, False)
window.mainloop()


