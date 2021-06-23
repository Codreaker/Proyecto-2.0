from tkinter import *
import pygame
from tkinter.ttk import Progressbar
from random import *
from PIL import Image, ImageTk, ImageSequence
from threading import Thread
import time


Nave = 3 # Vida de la nave
puntaje = 0 # Puntaje
nombre = "" # Nombre
minutos=0 #Minutos del nivel 1
minutos_nivel_dos = 0  #Minutos del nivel 2
minutos_nivel_tres = 0  #Minutos del nivel 3
pasa = True  #Bandera 

# clase donde estara el juego con ambas ventanas
class Pantalla_principal:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=1200, height=700, highlightthickness=0, relief='ridge', bg="black")
        self.canvas.place(x=0, y=0)
        self.pantallaInicio()

    def pantallaInicio(self):
 
        
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        
        # Aqui se carga la imagen de fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)

        # Label en la parte superior para texto de bienvenido
        self.bienvenido = Label(self.canvas, text="CLOCKWORK PLANET", font=("Helvetica", 12), fg="#c44387", bg="#27433a")
        self.bienvenido.place(x=510,y=30)
        #Label para indicar escribir el nombre
        self.name_please = Label(self.canvas, text="Digite su nombre:", fg="#c44387", bg="#27433a")
        self.name_please.place(x=450,y=155,width=100,height=30)

        # Lugar donde se reproduce la muisca de fondo
        pygame.init()
        pygame.mixer.music.load("Musica.ogg")
        pygame.mixer.music.play(4)
        
        # Funcion para el boton de silenciar
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

        # Boton para silenciar
        self.mute = Button(self.canvas, text="Mute",font=("Comic Sans MS", 10),bg="#b4b0f7",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=550,y=670, width=80, height=30)
        
        #entrada de texto para el nombre
        self.player_name = Entry(self.canvas)
        self.player_name.place(x=550,y=155,width=100,height=30)

        #Radiobotton con el primer nivel 1
        self.level_2 = Radiobutton(self.canvas,text="Intermedio",variable=valorRango, value=2,bg="#b4b0f7")
        self.level_2.place(x=560,y=186,width=80,height=20)

        #Radiobotton con el segundo nivel 2
        self.level_1 = Radiobutton(self.canvas,text="Facil", variable=valorRango,value=1,bg="#b4b0f7")
        self.level_1.place(x=480,y=186,width=70,height=20)
        
        #Radiobotton con el segundo nivel 3
        self.level_3 = Radiobutton(self.canvas,text="Dificil",  variable=valorRango,value=3,bg="#b4b0f7")
        self.level_3.place(x=650,y=186,width=70,height=20)

        # boton jugar para llamar al metodo que hace las validaciones
        self.boton_jugar = Button(self.canvas, text="Jugar", font=("Times New Roman", 16),bg="#b4b0f7", command=self.validaciones)
        self.boton_jugar.place(x=550,y=210,width=100,height=30)
        
        # Boton para mostrar los creditos
        self.button_mostrar = Button(self.canvas, text ="Creditos", fg="black", bg="#6e67ed", command = self.creditos)
        self.button_mostrar.place(x=3,y=670,width=100,height=30)
        # Boton para mostrar los puntajes
        self.button_mostrar = Button(self.canvas, text ="Puntajes", fg="black", bg="#b4b0f7", command = self.puntajes)
        self.button_mostrar.place(x=1100,y=670,width=100,height=30)
        

        
        
    #ventana de puntajes
    def puntajes(self):
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="#b4b0f7")
        self.canvas.place(x=0, y=0)
        # Aqui se carga la imagen de fondo
        self.imagen=ImageTk.PhotoImage(Image.open("gamef.png"))
        self.canvas.create_image(0, 0, image=self.imagen, anchor=NW)
        # Lugar donde se mostrara el puntaje
        self.score = Label(self.canvas, text="Puntaje: ", font=("Helvetica", 15), fg="#f55cdf", bg="#b4b0f7")
        self.score.place(x=580,y=30)
        # Boton para regresar ala pantalla principal
        self.boton_back_punt = Button(self.canvas, text="Back",font=("Times New Roman", 18),bg="#b4b0f7",command=self.pantallaInicio)
        self.boton_back_punt.place(x=550,y=520, width=80, height=30)

        #abre el archivo .txt
        def abrir_puntajes(): 
            archivo= open("archivo.txt","r") 
            nombres = archivo.readlines() #guarda los nombres y puntajes en una variable
            archivo.close() 
            separar(nombres)#llama a la funcion para separar los nombres y puntajes
            
        quicksort_L = Thread(target= abrir_puntajes) 
        quicksort_L.start()


        def separar(lista):
                i = 0 #contador
                print(lista)
                nombres=[]
                puntaje=[]
                while i != 7:  
                    divisor = lista[0].split(";")#separa el nombre y el puntaje y los convierte en lista
                    puntaje += [int(divisor[1])]#guarda el puntaje en la variable como una lista
                    nombres += [divisor[0]]#guarda el nombre en la variable como una lista
                    i += 1 # aumenta el contador en 1
                    lista = lista[1:]#corta la lista para ir al siguiente elemento
                jugadores(nombres)
                puntos(puntaje)

        #funcion para mostrar los puntajes en pantalla
        def puntos(puntajes):
            ordenado = quicksort(puntajes)
            y1=120
            for linea in ordenado: #recorre la lista de puntajes
                #coloca  los puntajes en la pantalla
                self.mejores_puntajes= Label(self.canvas, text=linea, font=("Helvetica", 15), fg="black", bg="white").place(x=650,y=y1)
                y1=y1 + 50 #cambia la posicion en y en la que se muestran los puntajes 

        #funcion para mostrar los nombres en pantalla
        def jugadores(nombres):
            y1=120
            for linea in nombres:#recorre la lista de nombres
                #coloca  los nombres en la pantalla
                self.mejores= Label(self.canvas, text=linea, font=("Helvetica", 15), fg="black", bg="white").place(x=550,y=y1)
                y1=y1 + 50 #cambia la posicion en y en la que se muestran los nombres

        #funcion quicksort que acomoda los puntajes en una lista ordenada
        def quicksort(puntaje):
            if len(puntaje) < 2:#verifica que la lista de puntajes contenga más de 1 elemento
                return puntaje
            indicador,menor,mayor = partir(puntaje)#llama a la funcion que realiza el ordenamiento de la lista
            return quicksort(mayor) +[indicador]+ quicksort(menor)#suma las listas ordenadas de los numeros mayores al indicador,el indicador y los menores al indicador

        def partir(puntaje):
            indicador = puntaje[0]#obtiene el primer elemento de la lista que se utilizara para comparar con el resto de elementos
            menor = []
            mayor = []
            for i in range(1,len(puntaje)):#recorre la lista sin contar el primer elemento
                print(indicador,menor,mayor)
                if puntaje[i] < indicador:#compara el primer elemento con el resto de la lista
                    menor += [puntaje[i]]#guarda en una lista los elementos menores al indicador
                else:
                    mayor += [puntaje[i]]#guarda en una lista los elementos menores al indicador
            return indicador,menor,mayor#retorna la lista con los numeros menores, el inidcador , la lista con lo mayores
   
   
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
        global pasa
        if self.player_name.get() != "":
            nombre +=self.player_name.get()
            if valorRango.get() == 1 or valorRango.get() == 0:
                
                self.primerNivel()
                pasa = False
                self.nombreJugador_N1.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label   
            if valorRango.get() == 2:

                self.segundoNivel()
                pasa = False
                self.nombreJugador_N2.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label
            if valorRango.get() == 3:

                self.tercerNivel()
                pasa = False
                self.nombreJugador_N3.config(text=self.player_name.get())#obtiene el nombre del jugador y lo coloca en un label

    # primer nivel del juego 
    def primerNivel(self):
        global parar
        global Nave
        # Canvas donde de mostrara el gif,nave,enemigos
        self.canvas = Canvas(self.master, width=1200, height=650, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        # Canvas donde se mostrara la info como el puntaje,vida,tiempo.nombre
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)
 
        # Funcion para cargar el gif frame por frame y hacer su animacion
        self.sequence = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(r'wow.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)
        
        # Aqui se incia el reproductor de la musica de inicio
        pygame.init()
        pygame.mixer.music.load("MarieNoChouzetsuGikou-KarinNakanoSatoshiHono-5036166.mp3")
        pygame.mixer.music.play(4)
        

        
        #boton de retorno a la pantalla de inicio
        self.boton_retorno = Button(self.canvasdos, text="back",font=("Comic Sans MS", 8),fg="red",bg="black",command=self.puntaje_superado)
        self.boton_retorno.place(x=1149,y=3, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.vidanave.place(x=103, y=3)

        #nombre del jugador nivel 1
        self.nombreJugador_N1 = Label(self.canvasdos, text="", font=("Comic Sans MS", 8),fg="red",bg="black")
        self.nombreJugador_N1.place(x=275, y=3)

        #label para mostrar el puntaje
        self.puntaje = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 8),fg="red",bg="black")
        self.puntaje.place(x=147, y=3)

        #label para mostrar el tiempo
        self.tiempo_nivel1 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 8),fg="red",bg="black")
        self.tiempo_nivel1.place(x=207, y=3)

        #Funcion para mostrar la barra de progreso
        progress = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progress.place(x=0,y=3)
        
        # Funcion para el boton de silenciar
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
                
        # Boton para silenciar
        self.mute = Button(self.canvasdos, text="Mute or UnMute",font=("Comic Sans MS", 5),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)

        #importa y coloca la img de la nave
        self.Nave=ImageTk.PhotoImage(Image.open("nave.png"))
        
        self.nave_N1 = self.canvas.create_image(550,555,image=self.Nave, anchor=NW)
        #impor img de los enemigos
        self.enemiga = ImageTk.PhotoImage(Image.open("enemigo.png"))

        #varible y llamada a la función de cronometro
        self.segundos=0
        
        #cronometro 
        def cronometro_N1():
            global minutos
            global puntaje
            if self.segundos == 60:
                minutos+=1
                self.segundos=0
                self.tiempo_nivel1.configure(text="tiempo: "+ str(minutos)+":"+str(self.segundos))#actualiza el tiempo
                return self.Nivel_Completado()
            self.tiempo_nivel1.configure(text="tiempo: "+str(minutos)+":"+ str(self.segundos))#actualiza el tiempo
            self.segundos += 1
            puntaje += 1
            self.puntaje.configure(text="puntaje: " + str(puntaje))
            self.canvas.after(1000,cronometro_N1)#repite la funcion cada segundo
        cronometro_N1()
        
        # Funcion para que suene el choque de las balas
        def sonido_choque():
            sonido_choque = pygame.mixer.Sound("golpe.mp3")#LLama a la musica
            sonido_choque.play()# Reproduce
            
        # Funcion para el rebote de las balas
        def rebotedebalas():
            #Generacion aleatoria
            ran = randint(0,795)
            randos = randint(0,795)
            rantres = randint(0,795)
            rancuatro = randint(0,795)
 

            #crea las balas
            enemigo = self.canvas.create_image(ran, 0,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(randos, 0,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(rantres, 0,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(rancuatro, 0,image=self.enemiga, anchor=NW)

            #envia las balas creadas a la funcion que hace su movimiento 
            rebotedebalas_aux(enemigo,1,5)
            rebotedebalas_aux(enemigodos,1,6)
            rebotedebalas_aux(enemigotres,1,9)
            rebotedebalas_aux(enemigocuatro,1,7)

        def rebotedebalas_aux(enemigo, x , y):
            #daño caja de la nave
            area_nave = self.canvas.bbox(self.nave_N1)
            #daño caja del enemigo
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                # x es la gravedad
                # y es la velocidad
                
                #Borde de arriba
                if self.canvas.coords(enemigo)[1] < 0:
                        y = randint(5,7)
                        x = -randint(5,9)
                        t5 = Thread(target= sonido_choque)
                        t5.start()
                #Borde de abajo
                if self.canvas.coords(enemigo)[1] > 610: # x range
                        y = -randint(5,7)
                        x = randint(-5,9)
                        t5 = Thread(target= sonido_choque)
                        t5.start()
                #Borde de izquierda
                if self.canvas.coords(enemigo)[0] < 0:
                        x = randint(5,9)
                        y = randint(-5,7)
                        t5 = Thread(target= sonido_choque)
                        t5.start()
                #Borde de derecha
                if self.canvas.coords(enemigo)[0] > 1140: # y range
                        x = -randint(5,9)
                        y = randint(-5,7)
                        t5 = Thread(target= sonido_choque)
                        t5.start()
                
                #Detector de coliciones
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
                    self.canvas.move(self.nave_N1, 25, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N1)[0]>0:#izquierda
                    self.canvas.move(self.nave_N1, -25, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N1)[1]<565:#abajo
                    self.canvas.move(self.nave_N1, 0, 25)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N1)[1]>0:#arriba
                    self.canvas.move(self.nave_N1, 0, -25)
            except IndexError:#controla el error y elimina la bala del enemigo
                self.canvas.move(self.nave_N1, 25, 0)
        self.master.bind("<KeyPress>", movimiento_nave)#para evento continuo de teclas
        
        # Funcion para crear la barra de progreso
        def barra_de_progreso():
            Limite = 60
            Tiempo = 0
            speed = 1
<<<<<<< Updated upstream
            while(Tiempo < Limite and pasa):
=======
            while(Tiempo<Limite):
>>>>>>> Stashed changes
                time.sleep(1)
                progress['value']+=(speed/Limite)*100
                Tiempo+=speed
                self.canvasdos.update_idletasks()
        t001 = Thread(target= barra_de_progreso)
        t001.start()

        
    #segundo nivel del juego
    def segundoNivel(self):
        # Canvas donde de mostrara el gif,nave,enemigos
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        # Canvas donde se mostrara la info como el puntaje,vida,tiempo.nombre
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)

        # Funcion para cargar el gif frame por frame y hacer su animacion
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(Image.open(r'clockword.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(100, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)
  


        # Aqui se incia el reproductor de la musica de inicio
        pygame.init()
        pygame.mixer.music.load("JitaiKyuuhen-KarinNakanoSatoshiHono-5036133.mp3")
        pygame.mixer.music.play(4)
        
        #boton de retorno a la pantalla de inicio
        self.boton_retorno2 = Button(self.canvasdos, text="back",font=("Comic Sans MS", 10),fg="red",bg="black",command=self.puntaje_superado)
        self.boton_retorno2.place(x=1149,y=3, width=50, height=20)

        # Boton para silenciar
        self.mute = Button(self.canvasdos, text="Mute",font=("Comic Sans MS", 8),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave2= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 10),fg="red",bg="black")
        self.vidanave2.place(x=100, y=3)

        #nombre del jugador nivel 2
        self.nombreJugador_N2 = Label(self.canvasdos, text="", font=("Comic Sans MS", 10),fg="red",bg="black")
        self.nombreJugador_N2.place(x=400, y=3)

        #label para mostrar el puntaje
        self.puntaje_N2 = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 10),fg="red",bg="black")
        self.puntaje_N2.place(x=200, y=3)

        #label para mostrar el tiempo
        self.tiempo_nivel2 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 10),fg="red",bg="black")
        self.tiempo_nivel2.place(x=600, y=3)

        #importa img de la nave
        self.Nave2=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N2 = self.canvas.create_image(550,555,image=self.Nave2, anchor=NW)

        #Funcion para mostrar la barra de progresoo
        progreso = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progreso.place(x=0,y=3)

        #variable y llamada a la funcion de cronometro
        self.segundos2=0
        
        #impor img de los enemigos
        self.enemiga=ImageTk.PhotoImage(Image.open("enemigo.png"))

        
        # Funcion para el boton de silenciar
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
            global minutos_nivel_dos,puntaje
            if self.segundos2 == 60:
                minutos_nivel_dos += 1
                self.segundos2=0
                self.tiempo_nivel2.configure(text="tiempo: "+ str(minutos_nivel_dos)+":"+str(self.segundos2))#actualiza el tiempo
                return self.Nivel_Completado()
            self.tiempo_nivel2.configure(text="tiempo: "+ str(minutos_nivel_dos)+":"+str(self.segundos2))#actualiza el tiempo
            self.segundos2 +=1
            puntaje += 3
            self.puntaje_N2.configure(text="puntaje: " + str(puntaje))
            self.canvas.after(1000,iniciar2)#repite el proceso cada segundo
        iniciar2()        

                
        #verifica las teclas y realiza el movimiento de la nave
        def mover_nave_2(mover):
            try:
                if mover.keysym=='Right' and self.canvas.coords(self.nave_N2)[0]<1140:#derecha
                    self.canvas.move(self.nave_N2, 25, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N2)[0]>0:#izquierda
                    self.canvas.move(self.nave_N2, -25, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N2)[1]<565:#abajo
                    self.canvas.move(self.nave_N2, 0, 25)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N2)[1]>0:#arriba
                    self.canvas.move(self.nave_N2, 0, -25)
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.move(self.nave_N2, 25, 0)
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

         # Funcion para que suene el choque de las balas
        def sonido_choquedos():
            sonido_choquedos = pygame.mixer.Sound("golpe.mp3")#LLama ala musica
            sonido_choquedos.play()# Reproduce
            
        # Funcion para el rebote de las balas
        def rebotedebalas():
            #Generacion aleatoria
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
            enemigocinco = self.canvas.create_image(rancinco, 10,image=self.enemiga, anchor=NW)

            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo,1,7)
            rebotedebalas_aux(enemigodos,1,7)
            rebotedebalas_aux(enemigotres,1,6)
            rebotedebalas_aux(enemigocuatro,1,3)
            rebotedebalas_aux(enemigocinco,1,8)

        # Funcion para su movimiento aleatorio y la verificasion de colicion
        def rebotedebalas_aux(enemigo, x , y):
            area_nave = self.canvas.bbox(self.nave_N2)
            #daño caja boss
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                # x es la gravedad
                # y es la velocidad
                #Borde de arriba
                if self.canvas.coords(enemigo)[1] < 0:
                        y = randint(5,7)
                        x = -randint(5,9)
                        t01 = Thread(target= sonido_choquedos)
                        t01.start()
                #Borde de abajo
                if self.canvas.coords(enemigo)[1] > 610: # x range
                        y = -randint(5,7)
                        x = randint(-5,9)
                        t01 = Thread(target= sonido_choquedos)
                        t01.start()
                #Borde de izquierda
                if self.canvas.coords(enemigo)[0] < 0:
                        x = randint(5,9)
                        y = randint(-5,7)
                        t01 = Thread(target= sonido_choquedos)
                        t01.start()
                #Borde de derecha
                if self.canvas.coords(enemigo)[0] > 1140: # y range
                        x = -randint(5,9)
                        y = randint(-5,7)
                        t01 = Thread(target= sonido_choquedos)
                        t01.start()
                        
                        
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
        
    # Tercer nivel
    def tercerNivel(self):

        # Canvas donde de mostrara el gif,nave,enemigos
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="#1d2086")
        self.canvas.place(x=0, y=0)
        # Canvas donde se mostrara la info como el puntaje,vida,tiempo.nombre
        self.canvasdos = Canvas(self.master, width=1197, height=46, relief='ridge',bg="black")
        self.canvasdos.place(x=0, y=650)


        # Funcion para cargar el gif frame por frame y hacer su animacion
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(Image.open(r'zafkiel.gif'))]
        self.image = self.canvas.create_image(600,350, image=self.sequence[0])
        
        def animate(counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.canvas.after(120, lambda: animate((counter+1) % len(self.sequence)))
        animate(1)
        
        # Aqui se incia el reproductor de la musica de inicio
        pygame.init()
        pygame.mixer.music.load("ElectronicWarfare-KarinNakanoSatoshiHono-5036030.mp3")
        pygame.mixer.music.play(4)

        #importa imagen de la nave del nivel 3
        self.nave_N3_img=ImageTk.PhotoImage(Image.open("nave.png"))
        self.nave_N3 = self.canvas.create_image(550,555,image=self.nave_N3_img, anchor=NW)#coloca la imagen en la ventana


        #boton de retorno a la pantalla de inicio
        self.boton_retorno3 = Button(self.canvasdos, text="back",font=("Comic Sans MS", 10),fg="red",bg="black",command=self.puntaje_superado)
        self.boton_retorno3.place(x=1149,y=3, width=50, height=20)
        self.mute = Button(self.canvasdos, text="Mute",font=("Comic Sans MS", 8),fg="red",bg="black",command = lambda:parar_o_reanudar_musica(paused))
        self.mute.place(x=1149,y=20, width=50, height=20)

        #label para mostrar la vida de la nave
        self.vidanave3= Label(self.canvasdos,text="vida: 3",font=("Comic Sans MS", 10),fg="red",bg="black")
        self.vidanave3.place(x=100, y=3)

        #nombre del jugador nivel 3
        self.nombreJugador_N3 = Label(self.canvasdos, text="", font=("Comic Sans MS", 10),fg="red",bg="black")
        self.nombreJugador_N3.place(x=400, y=3)

        #label para mostrar el puntaje
        self.puntaje_N3 = Label(self.canvasdos, text="puntaje: " + str(puntaje),font=("Comic Sans MS", 10),fg="red",bg="black")
        self.puntaje_N3.place(x=200, y=3)

        #label para mostrar el tiempo
        self.tiempo_N3 = Label(self.canvasdos, text="tiempo",font=("Comic Sans MS", 10),fg="red",bg="black")
        self.tiempo_N3.place(x=600, y=3)



        #Funcion para mostrar la barra de progreso
        progresoo = Progressbar(self.canvasdos, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progresoo.place(x=0,y=3)

        #impor img de los enemigos
        self.enemiga=ImageTk.PhotoImage(Image.open("enemigof.png"))

        #varible y llamada a la función de cronometro
        self.segundos_N3=0


        # Funcion para el boton de silenciar
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
            global minutos_nivel_tres,puntaje
            if self.segundos_N3 == 60:#verifica si se llego a 60 segundos
                minutos_nivel_tres +=1#aumenta en 1 los minutos
                self.segundos_N3=0
                self.tiempo_N3.configure(text="tiempo "+ str(minutos_nivel_tres)+":"+str(self.segundos_N3))#actualiza los minutos y segundos
                return self.Nivel_Completado()
            self.tiempo_N3.configure(text="tiempo "+ str(minutos_nivel_tres)+":"+str(self.segundos_N3))#actualiza los segundos
            self.segundos_N3 +=1
            puntaje += 5
            self.puntaje_N3.configure(text="puntaje: " + str(puntaje))
            self.canvas.after(1000,cronometro_N3)#repite la funcion cada 1 segundo
        cronometro_N3()

                
        def mover_nave3(mover):
            try:
                if mover.keysym=='Right' and self.canvas.coords(self.nave_N3)[0]<1140:#se mueve a la derecha hasta el limite
                    self.canvas.move(self.nave_N3, 25, 0)
                if mover.keysym=='Left' and self.canvas.coords(self.nave_N3)[0]>0:#se mueve a la izquierda hasta el limite
                    self.canvas.move(self.nave_N3, -25, 0)   
                if mover.keysym=='Down' and self.canvas.coords(self.nave_N3)[1]<565:#se mueve abajo hasta el limite
                    self.canvas.move(self.nave_N3, 0, 25)
                if mover.keysym=='Up' and self.canvas.coords(self.nave_N3)[1]>0:#se mueve arriba hasta el limite
                    self.canvas.move(self.nave_N3, 0, -25)
            except IndexError:#controla el error y elimina la bala del enemigo
                 self.canvas.move(self.nave_N3, 15, 0)
        self.master.bind("<KeyPress>", mover_nave3)#realiza el evento de mantener pulsada las teclas

        # Funcion para crear la barra de progreso
        def barra_de_progreso_3():
            Limite = 60
            Tiempo = 0
            speed = 1
            while(Tiempo<Limite):
                time.sleep(1)
                progresoo['value']+=(speed/Limite)*100
                Tiempo+=speed # esto hace que avanse
                window.update_idletasks()
        t3 = Thread(target= barra_de_progreso_3)
        t3.start()

        # Funcion para que suene el choque de las balas
        def sonido_choquetres():
            sonido_choquetres = pygame.mixer.Sound("Tic_Tac.mp3")#LLama ala musica
            sonido_choquetres.play()# Reproduce


            
        # Funcion para el rebote de las balas
        def rebotedebalas():
            #Generacion aleatoria
            ran = randint(0,100)
            randos = randint(0,700)
            rantres = randint(0,565)
            rancuatro = randint(0,735)
            rancinco = randint(0,770)
            ranseis = randint(0,715)
         
            #crea las balas
            enemigo = self.canvas.create_image(ran, 20,image=self.enemiga, anchor=NW)
            enemigodos = self.canvas.create_image(randos, 70,image=self.enemiga, anchor=NW)
            enemigotres = self.canvas.create_image(rantres, 150,image=self.enemiga, anchor=NW)
            enemigocuatro = self.canvas.create_image(rancuatro, 450,image=self.enemiga, anchor=NW)
            enemigocinco = self.canvas.create_image(rancinco, 10,image=self.enemiga, anchor=NW)
            enemigoseis = self.canvas.create_image(ranseis, 260,image=self.enemiga, anchor=NW)

            #envia las balas creadas a la funcion que hace su movimiento
            rebotedebalas_aux(enemigo,1,7)
            rebotedebalas_aux(enemigodos,1,6)
            rebotedebalas_aux(enemigotres,1,5)
            rebotedebalas_aux(enemigocuatro,1,3)
            rebotedebalas_aux(enemigocinco,1,2)
            rebotedebalas_aux(enemigoseis,1,8)

        # Funcion para su movimiento aleatorio y la verificasion de colicion
        def rebotedebalas_aux(enemigo, x , y):
            area_nave = self.canvas.bbox(self.nave_N3)
            #daño caja boss
            area_Misil = self.canvas.bbox(enemigo)
            self.canvas.move(enemigo, x, y)
            #obtiene coordenadas del enemigo en el eje x,y
            try:
                # x es la gravedad
                # y es la velocidad
                #Borde de arriba
                if self.canvas.coords(enemigo)[1] < 0:
                        y = randint(5,7)
                        x = -randint(5,9)
                        t02 = Thread(target= sonido_choquetres)
                        t02.start()
                #Borde de abajo
                if self.canvas.coords(enemigo)[1] > 610: # x range
                        y = -randint(5,7)
                        x = randint(-5,9)
                        t02 = Thread(target= sonido_choquetres)
                        t02.start()
                #Borde de izquierda
                if self.canvas.coords(enemigo)[0] < 0:
                        x = randint(5,9)
                        y = randint(-5,7)
                        t02 = Thread(target= sonido_choquetres)
                        t02.start()
                #Borde de derecha
                if self.canvas.coords(enemigo)[0] > 1140: # y range
                        x = -randint(5,9)
                        y = randint(-5,7)
                        t02 = Thread(target= sonido_choquetres)
                        t02.start()
                        
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
    def Nivel_Completado(self):
        global pasa
        global Nave
        global nombre
        global minutos
        global minutos_nivel_dos
        global minutos_nivel_tres
        
        if minutos == 1:#verifica el nivel 1
            pasa = False
            pygame.mixer.stop()#detiene la musica
            time.sleep(1)
            self.canvas.destroy()
            self.segundoNivel()
            self.nombreJugador_N2.configure(text=nombre)
     
        if minutos_nivel_dos == 1:#verifica el nivel 2
            pygame.mixer.stop()#detiene la musica
            self.canvas.destroy()
            time.sleep(1)
            self.tercerNivel()
            self.nombreJugador_N3.configure(text=nombre)
            
        if minutos_nivel_tres == 1:#verifica el nivel 3
            pygame.mixer.stop()#detiene la musica
            self.canvas.destroy()
            time.sleep(1)
            self.puntaje_superado()
            
    #verifica cuando la vida de la nave llega a 0 y llama a la función de retorno
    def juego_perdido(self):
        global Nave
        Nave=3
        self.puntaje_superado()

    #pantalla que muestra el mensaje de si supero o no un puntaje del top 7
    def puntaje_superado(self):
        self.canvas.destroy()
        global nombre, puntaje
        self.canvas = Canvas(self.master, width=1200, height=700, relief='ridge',bg="black")
        self.canvas.place(x=0, y=0)
        self.posicion_obt = Label(self.canvas, text="No has conseguido superar ninguno de los mejores puntajes" ,font=("Comic Sans MS", 30),fg="red",bg="black")
        self.posicion_obt.place(x=50, y=100)
        self.retorno_p = Button(self.canvas, text="back",font=("Comic Sans MS", 14),fg="red",bg="black",command=self.retorno)
        self.retorno_p.place(x=550,y=500, width=100, height=50)
        self.abrir_txt(nombre,puntaje)

    #abre el archivo .txt
    def abrir_txt(self,persona,puntaje):#tiene como argumentos el nombre y puntaje del jugador que finalizo partida 
        archivo= open("archivo.txt","r") 
        nombres = archivo.readlines()#guarda los nombres y puntajes en una variable
        archivo.close() 
        self.comparador(nombres,"",persona,puntaje,0)#llama a la funcion que compara el puntaje con los del top 7 

    def comparador(self,lista, res , persona,puntaje,i):
        if i == 7: #contador que verifica que se revise hasta el 7 lugar
            return self.actualizar(res) 
        divisor = lista[0].split(";")#separa el nombre del puntaje y los guarda en una lista
        actualPunt = int(divisor[1])#obtiene el puntaje de la lista y lo convierte en entero
        
        if actualPunt < puntaje: #compara si el puntaje obtenido es mayor a uno del top 7
            
            res += persona + ";" + str(puntaje)+ "\n"#guarda el nombre y puntaje del jugador en el string de resultado
            
            #usando el contador +1 se obtiene la posición que consiguió y se muestra en un label junto con el puntaje
            self.posicion_obt.configure(text="Has obtenido la posición " + str(i+1)+" con un total de " + str(puntaje)+" puntos")
            return self.comparador(lista,res,persona,0,i+1)#cambia el valor del puntaje a 0 para no reemplazar los demas puntajes menores
        
        self.comparador(lista[1:],res+lista[0],persona,puntaje,i+1)#guarda los datos del top 7 cuando el puntaje del jugador no es superior a alguno de estos

    #funcion que obtiene la variable con los datos del nuevo top 7 y actualiza el archivo de texto con estos    
    def actualizar(self,nuevos):
        archivo = open("archivo.txt","w") 
        archivo.write(nuevos) 
        archivo.close()
    
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
        pasa = False
        puntaje=0#restablece el puntaje
        minutos_nivel_dos = 0
        minutos_nivel_tres = 0
        minutos=0
        nombre=""
        pygame.mixer.stop# Para la musica
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


