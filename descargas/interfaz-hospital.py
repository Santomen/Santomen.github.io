# -*- coding: utf-8 -*-
#Importing libraries tkinter and matploitlib
import matplotlib.pyplot as plt
import tkinter as tk
x=0

#Creating the father widget
raiz=tk.Tk()
raiz.title("Hospital")
#Here we create two frames, the first one, mFrame, is where labels will be placed to fill in the data base. The second frame (mFramemodi) is where the menu will be placed in order to modify the data.
mFrame=tk.Frame(raiz)
mFrame.config(width=1400,height=900)
mFrame.pack(side="top",anchor="w")
mFramemodi=tk.Frame(raiz)
mFramemodi.config(width=400,height=500,bg="pink")
mFramemodi.pack(side="top",anchor="w")

boton=tk.IntVar()
def Contenido_primer_Ingreso():
#Here we have set the first label with its correspondent entry so as to start filling in the data base, pressing the accept button, a method will be called so as to start the action.
  lblb=tk.Label(mFrame,text="Bienvenido a la base de datos:").grid(row=0,column=0)
  LbH=tk.Label(mFrame,text="Ingrese el nombre del hospital:").grid(row=1,column=0)
  Ehospital=tk.Entry(mFrame,textvariable=non)
  Ehospital.grid(row=1,column=1)
  non.set(Ehospital.get())
  Lnum=tk.Label(mFrame,text="Ingrese el número de médicos generales").grid(row=2,column=0)
  Enum=tk.Entry(mFrame,textvariable=num)
  Enum.grid(row=2,column=1)
  num.set(Enum.get())
  primerboton=tk.Button(mFrame,text="Aceptar",command=lambda:llenado_m_generales(int(Enum.get()),1,medicos_generales)).grid(row=3,column=0)
def otro():
    mFrame.pack_forget()
#Pink frame
    #Here is the menu that shows everything you can do to the previously stored information.
def Contenido_pestaña_modificar():
    La=tk.Label(mFramemodi,text="Modificar datos").grid(row=0,column=0)
    r1=tk.Radiobutton(mFramemodi,text="1. Médico General",value=1,variable=boton,command=botone).grid(row=1,column=0)
    r2=tk.Radiobutton(mFramemodi,text="2. Cirujano",value=2,variable=boton,command=botone).grid(row=2,column=0)
    r3=tk.Radiobutton(mFramemodi,text="3. Laboratorista",value=3,variable=boton,command=botone).grid(row=3,column=0)
    r4=tk.Radiobutton(mFramemodi,text="4. Comparación de datos",value=4,variable=boton,command=botone).grid(row=4,column=0)
    r5=tk.Radiobutton(mFramemodi,text="5. Salir",value=5,variable=boton,command=botone).grid(row=5,column=0)

def final(n):
    n.destoy()

#Build menu
barramenu=tk.Menu(raiz)
#Place menu
menubase=tk.Menu(barramenu)
menubase1=tk.Menu(barramenu)
# Create commands for the menu####################################################
menubase.add_command(label="Abrir",command= Contenido_primer_Ingreso)
menubase.add_separator
menubase.add_command(label="cerrar",command=otro)
menubase1.add_command(label="Abrir",command= Contenido_pestaña_modificar)
menubase1.add_separator
menubase1.add_command(label="cerrar",command=lambda:final(mFramemodi))

#Place menus in the setting bar
barramenu.add_cascade(label="Base de datos",menu=menubase)
barramenu.add_cascade(label="Modificar datos",menu=menubase1)
#Indicate in which window the setting bar will be
raiz.config(menu=barramenu)
#Special tkinter variables that reset entrys
botong=tk.IntVar()
non=tk.StringVar()
num=tk.IntVar()
nDoc=tk.StringVar()
su=tk.IntVar()
eda=tk.IntVar()
I=tk.StringVar()
ex=tk.BooleanVar()
op=tk.IntVar()
exito=tk.IntVar()
enfer=tk.IntVar()
numC=tk.IntVar()
numL=tk.IntVar()

# Here the classes are built, starting with the Medic Superclass, which will have a salary, age, antiquity, name, ID, Qualification, attributes that will be retained by the General Medical, Surgeon and Laboratory subclasses.
class Medico:
    def __init__ (self,sueldo,edad,nombre,antiguedad, calif,ID,disponible):
        self.sueldo=sueldo
        self.edad=edad
        self.nombre=nombre
        self.antiguedad= antiguedad
        self.calif=calif
        self.ID=ID
        self.disponible=disponible
        self.change=False
       
    def pagar(self,n):
        l=tk.Label(n,text="Se ha pagado a "+self.nombre+" la cantidad de $"+str(self.sueldo)+".").grid(row=0,column=0)
        b=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=0,column=1)
    def available (self,n):
        if self.disponible==True:
            l=tk.Label(n,text="El médico "+self.nombre+" se encuentra disponible.").grid(row=0,column=0)
        else:
            l=tk.Label(n,text="El médico se encuentra ocupado.").grid(row=0,column=0)
        b=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=0,column=1)
    def fun(self,c):
        if c==True:
                tk.messagebox.showinfo("Cambio Realizado","Ha comenzado exitosamente.")
                self.disponible=False
    def fu(self,c):      
        if c==True:
                tk.messagebox.showinfo("Cambio Realizado","Ha terminado exitosamente.")
                self.disponible=True            
    def estado (self,n):
        b=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=1,column=1)
        self.change=False
        if self.disponible==True:
            l=tk.Label(n,text="El médico se encuentra disponible, ¿desea asignarle un paciente?(1)").grid(row=0,column=0)
            e=tk.Entry(n)
            e.grid(row=0,column=1)
            self.change=bool(e.get())
            bg=tk.Button(n,text="Aceptar",command=lambda:self.fun(bool(e.get()))).grid(row=1,column=0)
           
        else:
            l=tk.Label(n,text="El médico no se encuentra disponible, ¿ha terminado su trabajo?(1)").grid(row=0,column=0)
            e=tk.Entry(n)
            e.grid(row=0,column=1)
            self.change=bool(e.get())
            bg=tk.Button(n,text="Aceptar",command=lambda:self.fu(bool(e.get()))).grid(row=1,column=0)
           
estudi=tk.IntVar()    
class Medico_General(Medico):
    def __init__ (self,sueldo,edad,nombre,antiguedad, calif,ID,disponible,pacientes):
        self.__key=0
        self.titulo="N/A"
        self.pacientes=pacientes
        super().__init__(sueldo,edad,nombre, antiguedad, calif,ID,disponible)
    def estudiar(self,n):
            b=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=2,column=0)
            l=tk.Label(n,text="1.-Premédica\n2.-Licenciatura\n3.-Especialización\n4.-Subespecialidad\n5.-Maestría\n6.-Doctorado\n7.-Posdoctorado").grid(row=0,column=0)
            l=tk.Label(n,text="Seleccione el título a estudiar:").grid(row=1,column=0)
            er=tk.Entry(n,textvariable=estudi)
            er.grid(row=1,column=1)
            bg=tk.Button(n,text="Aceptar",command=lambda:self.est(int(er.get()))).grid(row=1,column=3)
    def est(self,value):
            if (value<0) or (value>7):
                tk.messagebox.showwarning("ERROR","El número seleccionado no es válido.")
                estudi.set(0)
            elif value<self.__key:
                tk.messagebox.showwarning("ERROR","No puede estudiar un título previamente obtenido.")
            else:
                self.titulo=switch(value)
                self.__key=value
#Method that saves self.title, an exclusive atribute of General medic
def switch (value):
    switcher={1:"Premédica",
              2:"Licenciatura",
              3:"Especialización",
              4:"Subespecialidad",
              5:"Maestría",
              6:"Doctorado",
              7:"Posdoctorado"
            }
    return switcher.get(value)

sumando=tk.IntVar()
class Medico_Cirujano(Medico):
    def __init__ (self,sueldo,edad,nombre,antiguedad, calif,ID,disponible,operaciones,enfermeras):
        self.operaciones=operaciones
        self.enfermeras=enfermeras
        super().__init__(sueldo,edad,nombre, antiguedad,calif,ID,disponible)
   
    def registro (self,n):
            l=tk.Label(n,text="¿Con cuántas enfermeras cuenta el cirujano?").grid(row=0,column=0)
            s=tk.Entry(n,textvariable=sumando).grid(row=0,column=1)
            b=tk.Button(n,text="Aceptar",command=lambda:self.vo(int(sumando.get()))).grid(row=0,column=3)
            bt=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=1,column=0)
    def vo(self,so):
      if (so>=0) and (so<=4):
                self.enfermeras=int(sumando.get())
               
      else:
         tk.messagebox.showwarning("ERROR","El número ingresado de enfermeras no es válido.")
         sumando.set(0)
prue=tk.IntVar()
class Medico_Laboratorista(Medico):
    def __init__ (self,sueldo,edad,nombre,antiguedad, calif,ID,disponible,vacunas):
        self.prueba=0
        self.vacunas=vacunas
        super().__init__(sueldo,edad,nombre,antiguedad, calif, ID,disponible)
    def realizar_pruebas(self,n):
        l=tk.Label(n,text="¿Cuántas pruebas se realizaron").grid(row=0,column=0)
        s=tk.Entry(n,textvariable=prue).grid(row=0,column=1)
        b=tk.Button(n,text="Aceptar",command=lambda:self.va(int(prue.get()))).grid(row=0,column=3)
        by=tk.Button(n,text="OK",command=lambda:n.destroy()).grid(row=1,column=0)
    def va(self,sa):
        if sa<0 or sa>6:
            tk.messagebox.showwarning("Error","El número de pruebas ingresado es inválido")
            prue.set(0)
        else:
         self.prueba+=sa
         if self.prueba>=10:
            self.vacunas+=1
            self.prueba=0
            tk.messagebox.showinfo("Felicidades","¡Se ha creado un nueva vacuna!")
#estas son las listas donde se van a almazenar los objetos por el nombre.
medicos_generales=[]
medicos_cirujanos=[]
medicos_laboratoristas=[]

ng=tk.StringVar()

#The next three functions perform the same task which is to keep track of how much data will be requested from each doctor in addition to instantiating new objects by filling their corresponding parameters

def creador_obj_medico_general(sueldo,edad,nombre,anti,calif,Id,ex,pac,controlador,yei,j):
    j.destroy()
    controlador-=1
    yei+=1
    objeto=nombre
    objeto=Medico_General(sueldo,edad,nombre,anti,calif,Id,ex,pac)
    medicos_generales.append(objeto)
    llenado_m_generales(controlador,yei,medicos_generales)

def creador_obj_cirujano(sueldo,edad,nombre,antiguedad,calif,ID,disponible,operaciones,enfermeras,control,yei,j):
    j.destroy()
    control-=1
    yei+=1
    objet=nombre
    objet=Medico_Cirujano(sueldo,edad,nombre,antiguedad,calif,ID,disponible,operaciones,enfermeras)
    medicos_cirujanos.append(objet)
    llenado_cirujanos(control,yei,medicos_cirujanos)
   
def creador_obj_laboratorista(sueldo,edad,nombre,antiguedad,calif,ID,disponible,vacunas,contro,yei,j):
    j.destroy()
    contro-=1
    yei+=1
    obje=nombre
    obje=Medico_Laboratorista(sueldo,edad,nombre,antiguedad, calif,ID,disponible,vacunas)
    medicos_laboratoristas.append(obje)
#if a new objet is required, this method is called to pop up thethe filling in format
    llenado_laboratorista(contro,yei,medicos_laboratoristas)

#The functions that have_ "medical specialty" ask for the parameters required by the instantiation of objects, they block the accept button and control how many times the data of the doctors will be requested
def llenado_m_generales(usar,yei,lista_m):
    #Ask data from the medic
    # An if is used to control how many times this operation will be carried out. If using == 0, a new entry label will appear and a button will ask how many doctors of the next class are going to be, and then the function in charge of filling the data of that doctor will be invoked.
       if(usar!=0):
           Ldoc=tk.Label(mFrame,text="Ingrese el nombre del doctor no. "+str(yei)).grid(row=4,column=0)
           Edoc=tk.Entry(mFrame)
           Edoc.grid(row=4,column=1)
           #Button that validates the name invoking the function validate_name etc
           bto_1=tk.Button(mFrame,text="Validar",command=lambda:validar_nombre_m_general(float(Esue.get()),int(Eed.get()),str(Edoc.get()),int(Eop.get()),int(Eexito.get()),str(EI.get()),int(Eex.get()),int(Eenfer.get()),usar,yei,lista_m)).grid(row=4,column=3)
           Lsue=tk.Label(mFrame,text="Ingrese el sueldo del médico general no."+str(yei)).grid(row=5,column=0)
           Esue=tk.Entry(mFrame)
           Esue.grid(row=5,column=1)
           Led=tk.Label(mFrame,text="Escriba la edad del médico general").grid(row=6,column=0)
           Eed=tk.Entry(mFrame)
           Eed.grid(row=6,column=1)
           LI=tk.Label(mFrame,text="Ingrese el ID del médico general no. "+str(yei)).grid(row=7,column=0)
           EI=tk.Entry(mFrame)
           EI.grid(row=7,column=1)
           Lex=tk.Label(mFrame,text="¿Es exclusivo (1) o trabaja cono otros hospitales (0) el médico general? no. "+str(yei)).grid(row=8,column=0)
           Eex=tk.Entry(mFrame)
           Eex.grid(row=8,column=1)
           Lop=tk.Label(mFrame,text="¿Cuanto tiempo lleva trabajando el medico general? no. "+str(yei)).grid(row=9,column=0)
           Eop=tk.Entry(mFrame)
           Eop.grid(row=9,column=1)
           Lexito=tk.Label(mFrame,text="En una escala de 0 a 10 que calificación tiene el médico? no. "+str(yei)).grid(row=10,column=0)
           Eexito=tk.Entry(mFrame)
           Eexito.grid(row=10,column=1)
           Lenfer=tk.Label(mFrame,text="¿Cuantos pacientes ha tratado el médico? no. "+str(yei)).grid(row=11,column=0)
           Eenfer=tk.Entry(mFrame)
           Eenfer.grid(row=11,column=1)
       else:
          Label_c=tk.Label(mFrame,text="Ingrese el número de cirujanos").grid(row=13,column=0)
          Eciru=tk.Entry(mFrame,textvariable=numC)
          Eciru.grid(row=13,column=1)
          numC.set(Eciru.get())
          segundoboton=tk.Button(mFrame,text="Aceptar",command=lambda:llenado_cirujanos(int(Eciru.get()),1,medicos_cirujanos)).grid(row=14,column=0)

#The validate_ "x-specialty" functions are responsible for validating the rest of the data, it also destroys the second validate button and if the data is correct, it will enable the accept button that invokes another function
def validar_m_general(s,e,n,t,c,i,ex,p,usar,yei,bto):
    bto.destroy()
    if((s>=10000 and s<=80000) and (e>=20 and e<=70) and (ex==1 or ex==0) and (c>=1 and c<=10) and (p>=1 and p<=20) and(t>=1 and t<=(e-18))):
        botonAce2=tk.Button(mFrame,text="Aceptar",command=lambda :creador_obj_medico_general(s,e,n,t,c,i,bool(ex),p,usar,yei,botonAce2))
        botonAce2.grid(row=12,column=0)
    else:
        if(s<10000 or s>80000):
            messagebox("Sueldo")
        if(e<20 or e>70):
            messagebox("Edad")
        if (ex!=1 and ex!=0):
            messagebox("Disponibilidad")
        if (c<1 or c>10):
            messagebox("Calificación")
        if (p<1 or p>20):
            messagebox("Pacientes")
        else:      
            messagebox("Antiguedad")
#All the validate_name_ "x-specialty" functions are in charge of verifying if the name has already been registered previously or not by displaying a messagebox in which it says this name has already been registered or if it has been validated
#Also a second validate button will be enabled when the first validation turns out correct
def validar_nombre_m_general (sueldo,edad,nombre,anti,calif,ID,ex,p,usar,yei,lista_medica):
    fake=0
    if yei!=1:
        for z in range (len(lista_medica)):
            if nombre==lista_medica[z].nombre:
                tk.messagebox.showwarning("Dato Incorrecto","Ese doctor ya ha sido registrado.")
                fake=1
        if fake==0:
            bto=tk.Button(mFrame,text="Validar",command=lambda:validar_m_general(sueldo,edad,nombre,anti,calif,ID,ex,p,usar,yei,bto))
            bto.grid(row=12,column=1)
            tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
    else:
        tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
        bto=tk.Button(mFrame,text="Validar",command=lambda:validar_m_general(sueldo,edad,nombre,anti,calif,ID,ex,p,usar,yei,bto))
        bto.grid(row=12,column=1)

def elegir_accion_m_general (op2,lista):
    fake=0
    for i in range(len(lista)):
                if op2.lower()==lista[i].nombre.lower():
                    tk.messagebox.showinfo("Dato correcto","El nombre si está en la lista")
                    save=i
                    fake=1                                    
    if(fake==1):
     mFramegene=tk.Frame(raiz)
     mFramegene.pack(side="top",anchor="w")
     mFramegene.config(width=300,height=300,bg="blue")
     Lag=tk.Label(mFramegene,text="¿Qué desea hacer con el médico?"+lista[save].nombre).grid(row=0,column=0)
     r1g=tk.Radiobutton(mFramegene,text="1. Borrar del sistema",value=1,variable=botong,command=lambda:accion_m_general(save)).grid(row=1,column=0)
     r2g=tk.Radiobutton(mFramegene,text="2. Verificar disponibilidad",value=2,variable=botong,command=lambda:accion_m_general(save)).grid(row=2,column=0)
     r3g=tk.Radiobutton(mFramegene,text="3. Seleccionar grado de estudios",value=3,variable=botong,command=lambda:accion_m_general(save)).grid(row=3,column=0)
     r4g=tk.Radiobutton(mFramegene,text="4 Asignar/Terminar trabajo",value=4,variable=botong,command=lambda:accion_m_general(save)).grid(row=4,column=0)
     r5g=tk.Radiobutton(mFramegene,text="5. Salir",value=5,variable=botong,command=mFramegene.destroy).grid(row=5,column=0)

    if fake==0:
                tk.messagebox.showwarning("Dato incorrecto","No se encuentra el nombre seleccionado")
                return ng.set("")

def accion_m_general(save):
    u=botong.get()
    n=tk.Frame(raiz)
    n.pack(side="top")
    n.config(bg="green")
    if(u==1):
       medicos_generales[save].pagar(n)
       lae=tk.Label(n,text="Se ha eliminado a "+medicos_generales[save].nombre+" del sistema.").grid(row=2,column=0)
       medicos_generales.remove(medicos_generales[save])
    elif(u==2):
        medicos_generales[save].available(n)
    elif(u==3):
        medicos_generales[save].estudiar(n)
    elif(u==4):
        medicos_generales[save].estado(n)
    elif(u==5):
        n.destroy
    elif(u==6):
        n.destroy

def llenado_cirujanos(ata,yei,lista_m):
    #General medic data entry
     if(ata!=0):
       Ldock=tk.Label(mFrame,text="Ingrese el nombre del cirujano no. "+str(yei)).grid(row=15,column=0)
       Edock=tk.Entry(mFrame)
       Edock.grid(row=15,column=1)
       bto_2=tk.Button(mFrame,text="Validar",command=lambda:validar_nombre_cirujano(float(Esuek.get()),int(Eedk.get()),str(Edock.get()),int(Eopk.get()),int(Eexitok.get()),str(EIk.get()),int(t1.get()),int(Eexk.get()),int(Eenferk.get()),ata,yei,lista_m)).grid(row=15,column=3)
       Lsuek=tk.Label(mFrame,text="Ingrese el sueldo del cirujano no."+str(yei)).grid(row=16,column=0)
       Esuek=tk.Entry(mFrame)
       Esuek.grid(row=16,column=1)
       Ledk=tk.Label(mFrame,text="Escriba la edad del cirujano"+str(yei)).grid(row=17,column=0)
       Eedk=tk.Entry(mFrame)
       Eedk.grid(row=17,column=1)
       LIk=tk.Label(mFrame,text="Ingrese el ID del cirujano no. "+str(yei)).grid(row=18,column=0)
       EIk=tk.Entry(mFrame)
       EIk.grid(row=18,column=1)
       Lexk=tk.Label(mFrame,text="¿Cuanta operaciones ha realizado el cirujano? no. "+str(yei)).grid(row=19,column=0)
       Eexk=tk.Entry(mFrame)
       Eexk.grid(row=19,column=1)
       Lopk=tk.Label(mFrame,text="¿Cuanto tiempo lleva trabajando el cirujano ? no. "+str(yei)).grid(row=20,column=0)
       Eopk=tk.Entry(mFrame)
       Eopk.grid(row=20,column=1)
       Lexitok=tk.Label(mFrame,text="En una escala de 0 a 10 cual calificación tiene el cirujano ? no. "+str(yei)).grid(row=21,column=0)
       Eexitok=tk.Entry(mFrame)
       Eexitok.grid(row=21,column=1)
       Lenferk=tk.Label(mFrame,text="¿Cuantas enfermeras tiene a cargo el cirujano ? no. "+str(yei)).grid(row=22,column=0)
       Eenferk=tk.Entry(mFrame)
       Eenferk.grid(row=22,column=1)
       t=tk.Label(mFrame,text="¿Esta disponible (1) o está ocupado(0) no. "+str(yei)).grid(row=23,column=0)
       t1=tk.Entry(mFrame)
       t1.grid(row=23,column=1)
     else:
       Label_la=tk.Label(mFrame,text="Ingrese el número de laboratorista").grid(row=24,column=0)
       Ela=tk.Entry(mFrame,textvariable=numL)
       Ela.grid(row=24,column=1)
       numL.set(Ela.get())
       segundoboton=tk.Button(mFrame,text="Aceptar",command=lambda:llenado_laboratorista(int(Ela.get()),1,medicos_laboratoristas)).grid(row=25,column=0)

def validar_cirujanos(s,e,n,t,c,i,ex,op,enf,usar,yei,bto):
    bto.destroy()
    if((s>=10000 and s<=80000) and (e>=20 and e<=70) and (ex==1 or ex==0) and (c>=1 and c<=10) and (op>=1 and op<=30) and(t>=1 and t<=(e-18))and (enf>=1 and enf<=4)):
        botonAce2=tk.Button(mFrame,text="Aceptar",command=lambda :creador_obj_cirujano(s,e,n,t,c,i,bool(ex),op,enf,usar,yei,botonAce2))
        botonAce2.grid(row=24,column=0)
    else:
        if(s<10000 or s>80000):
            messagebox("Sueldo")
        if(e<20 or e>70):
            messagebox("Edad")
        if (ex!=1 and ex!=0):
            messagebox("Disponibilidad")
        if (c<1 or c>10):
            messagebox("Calificación")
        if (op<0 or op>30):
            messagebox("Operaciones")
        if (enf<1 or enf>4):
            messagebox("Enfermeras")
        else:      
            messagebox("Antiguedad")      

def validar_nombre_cirujano (sueldo,edad,nombre,anti,calif,ID,ex,op,enf,usar,yei,lista_medica):
    fake=0
    if yei!=1:
        for z in range (len(lista_medica)):
            if nombre==lista_medica[z].nombre:
                tk.messagebox.showwarning("Dato Incorrecto","Ese doctor ya ha sido registrado.")
                fake=1
        if fake==0:
            bto=tk.Button(mFrame,text="Validar",command=lambda:validar_cirujanos(sueldo,edad,nombre,anti,calif,ID,ex,op,enf,usar,yei,bto))
            bto.grid(row=24,column=1)
            tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
    else:
        tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
        bto=tk.Button(mFrame,text="Validar",command=lambda:validar_cirujanos(sueldo,edad,nombre,anti,calif,ID,ex,op,enf,usar,yei,bto))
        bto.grid(row=24,column=1)

def elegir_accion_cirujano(op2,lista):
    fake=0
    for i in range(len(lista)):
                if op2.lower()==lista[i].nombre.lower():
                    tk.messagebox.showinfo("Dato correcto","El nombre si está en la lista")
                    fake=1
                    p=lista[i].nombre
                    save=i
    if(fake==1):
     mFrameciru=tk.Frame(raiz)
     mFrameciru.pack(side="top",anchor="w")
     mFrameciru.config(width=300,height=300,bg="blue")
     Lag=tk.Label(mFrameciru,text="¿Qué desea hacer con el cirujano"+p).grid(row=0,column=0)
     r1g=tk.Radiobutton(mFrameciru,text="1. Borrar del sistema",value=1,variable=botong,command=lambda:accion_cirujano(save)).grid(row=1,column=0)
     r2g=tk.Radiobutton(mFrameciru,text="2. Verificar disponibilidad",value=2,variable=botong,command=lambda:accion_cirujano(save)).grid(row=2,column=0)
     r3g=tk.Radiobutton(mFrameciru,text="3. Actualizar no. de enfermeras a cargo",value=3,variable=botong,command=lambda:accion_cirujano(save)).grid(row=3,column=0)
     r4g=tk.Radiobutton(mFrameciru,text="4. Asignar/Terminar trabajo",value=4,variable=botong,command=lambda:accion_cirujano(save)).grid(row=4,column=0)
     r5g=tk.Radiobutton(mFrameciru,text="5. Salir",value=6,variable=botong,command=mFrameciru.destroy).grid(row=5,column=0)
                   
                       
    return save
    if fake==0:
                tk.messagebox.showwarning("Dato incorrecto","No se encuentra el nombre seleccionado")
                return ng.set("")
def accion_cirujano(save):
    u=botong.get()
    n=tk.Frame(raiz)
    n.pack(side="top")
    n.config(bg="green")
    if(u==1):
       medicos_cirujanos[save].pagar(n)
       lae=tk.Label(n,text="Se ha eliminado a "+medicos_cirujanos[save].nombre+" del sistema.").grid(row=2,column=0)
       medicos_cirujanos.remove(medicos_cirujanos[save])
    elif(u==2):
        medicos_cirujanos[save].available(n)
    elif(u==3):
        medicos_cirujanos[save].registro(n)
    elif(u==4):
        medicos_cirujanos[save].estado(n)
       
       
def llenado_laboratorista(ato,yei,lista_m):
   #comes from llenado_ c here the laboratory data is filled
     if(ato!=0):
       Ldockt=tk.Label(mFrame,text="Ingrese el nombre del laboratorista no. "+str(yei)).grid(row=6,column=4)
       Edockt=tk.Entry(mFrame)
       Edockt.grid(row=4+2,column=3+2)
       bto_3=tk.Button(mFrame,text="Validar",command=lambda:validar_nombre_laboratorista(float(Esuekt.get()),int(Eedkt.get()),str(Edockt.get()),int(Eopkt.get()),int(Eexitokt.get()),str(EIkt.get()),int(v1.get()),int(Eexkt.get()),ato,yei,lista_m)).grid(row=4+2,column=4+2)
       Lsuekt=tk.Label(mFrame,text="Ingrese el sueldo del laboratorista no."+str(yei)).grid(row=5+2,column=2+2)
       Esuekt=tk.Entry(mFrame)
       Esuekt.grid(row=5+2,column=3+2)
       Ledkt=tk.Label(mFrame,text="Escriba la edad del laboratorista"+str(yei)).grid(row=6+2,column=2+2)
       Eedkt=tk.Entry(mFrame)
       Eedkt.grid(row=6+2,column=3+2)
       LIkt=tk.Label(mFrame,text="Ingrese el ID del laboratorista no. "+str(yei)).grid(row=7+2,column=2+2)
       EIkt=tk.Entry(mFrame)
       EIkt.grid(row=7+2,column=3+2)
       Lexkt=tk.Label(mFrame,text="¿Cuanta vacunas ha realizado el laboratorista? no. "+str(yei)).grid(row=8+2,column=2+2)
       Eexkt=tk.Entry(mFrame)
       Eexkt.grid(row=8+2,column=3+2)
       Lopkt=tk.Label(mFrame,text="¿Cuanto tiempo lleva trabajando el laboratorista ? no. "+str(yei)).grid(row=9+2,column=2+2)
       Eopkt=tk.Entry(mFrame)
       Eopkt.grid(row=9+2,column=3+2)
       Lexitokt=tk.Label(mFrame,text="En una escala de 0 a 10 cual calificación tiene el laboratorista ? no. "+str(yei)).grid(row=10+2,column=2+2)
       Eexitokt=tk.Entry(mFrame)
       Eexitokt.grid(row=10+2,column=3+2)
       v=tk.Label(mFrame,text="¿Esta disponible el doctor 1 o 0? no. "+str(yei)).grid(row=11+2,column=2+2)
       v1=tk.Entry(mFrame)
       v1.grid(row=11+2,column=3+2)
     else:
         #this is a tester if you want to print the objects to know if everything is working correctly
          print("Blabla ")
         
         
def validar_laboratorista(s,e,n,t,c,i,ex,vac,usar,yei,bto):
    bto.destroy()
    if((s>=10000 and s<=80000) and (e>=20 and e<=70) and (ex==1 or ex==0) and (c>=1 and c<=10) and (vac>=1 and vac<=10) and(t>=1 and t<=(e-18))):
        botonAce3=tk.Button(mFrame,text="Aceptar",command=lambda :creador_obj_laboratorista(s,e,n,t,c,i,bool(ex),vac,usar,yei,botonAce3))
        botonAce3.grid(row=12+2,column=2+2)
    else:
        if(s<10000 or s>80000):
            messagebox("Sueldo")
        if(e<20 or e>70):
            messagebox("Edad")
        if (ex!=1 and ex!=0):
            messagebox("Disponibilidad")
        if (c<1 or c>10):
            messagebox("Calificación")
        if (vac<1 or  vac>10):
            messagebox("Vacunas")
        else:      
            messagebox("Antiguedad")

         
def validar_nombre_laboratorista (sueldo,edad,nombre,anti,calif,ID,ex,vac,usar,yei,lista_medica):
    fake=0
    if yei!=1:
        for z in range (len(lista_medica)):
            if nombre==lista_medica[z].nombre:
                tk.messagebox.showwarning("Dato Incorrecto","Ese doctor ya ha sido registrado.")
                fake=1
        if fake==0:
            bto=tk.Button(mFrame,text="Validar",command=lambda:validar_laboratorista(sueldo,edad,nombre,anti,calif,ID,ex,vac,usar,yei,bto))
            bto.grid(row=12+2,column=3+2)
            tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
    else:
        tk.messagebox.showinfo("Dato Correcto","Se ha validado el nombre escrito.")
        bto=tk.Button(mFrame,text="Validar",command=lambda:validar_laboratorista(sueldo,edad,nombre,anti,calif,ID,ex,vac,usar,yei,bto))
        bto.grid(row=12+2,column=3+2)
##In all the functions choose_action_ "x-specialty" after having selected a name, a menu will be displayed that will allow you to make changes to the data already saved if the name is in the list, if not, the program will send a message to warn that such name is not on the list
def elegir_accion_laboratorista (op2,lista):
    fake=0
    for i in range(len(lista)):
                if op2.lower()==lista[i].nombre.lower():
                    tk.messagebox.showinfo("Dato correcto","El nombre si está en la lista")                  
                    fake=1
                    p=lista[i].nombre
                    save=i
     #Here a frame will be created and destroyed as many times as needed
     
# Here are the radiobuttons that send a value to an established function to execute the change that the user wants to makeon the object previously selected
    if(fake==1):
     mFramegene=tk.Frame(raiz)
     mFramegene.pack(side="top",anchor="w")
     mFramegene.config(width=250,height=250,bg="blue")
     Lag=tk.Label(mFramegene,text="¿Qué desea hacer con el laboratorista?"+p).grid(row=0,column=0)
     r1g=tk.Radiobutton(mFramegene,text="1. Borrar del sistema",value=1,variable=botong,command=lambda:accion_laboratorista(save)).grid(row=1,column=0)
     r2g=tk.Radiobutton(mFramegene,text="2. Verificar disponibilidad",value=2,variable=botong,command=lambda:accion_laboratorista(save)).grid(row=2,column=0)
     r3g=tk.Radiobutton(mFramegene,text="3. Agendar una prueba",value=3,variable=botong,command=lambda:accion_laboratorista(save)).grid(row=3,column=0)
     r4g=tk.Radiobutton(mFramegene,text="4 Asignar/Terminar trabajo",value=4,variable=botong,command=lambda:accion_laboratorista(save)).grid(row=4,column=0)
     r5g=tk.Radiobutton(mFramegene,text="5. Salir",value=6,variable=botong,command=mFramegene.destroy).grid(row=5,column=0)

    elif fake==0:
                tk.messagebox.showwarning("Dato incorrecto","No se encuentra el nombre seleccionado")
                return ng.set("")
#
#All functions accion_ "x-specialty" get a value sent by the radiobutton of the function that is just above, depending on the selected value it will call a method of the class, in addition another frame will be created that will be constructed and destroyed as many times are necessary
def accion_laboratorista(save):
    u=botong.get()
    n=tk.Frame(raiz)
    n.pack(side="top")
    n.config(bg="green")
    if(u==1):
       medicos_laboratoristas[save].pagar(n)
       lae=tk.Label(n,text="Se ha eliminado a "+medicos_laboratoristas[save].nombre+" del sistema.").grid(row=2,column=0)
       medicos_laboratoristas.remove(medicos_laboratoristas[save])
    elif(u==2):
        medicos_laboratoristas[save].available(n)
    elif(u==3):
        if medicos_laboratoristas[save].disponible==True:
                    medicos_laboratoristas[save].realizar_pruebas(n)
        else:
         tk.messagebox.showinfo("Atención","El médico ya se encontraba realizando pruebas")
    elif(u==4):
         medicos_laboratoristas[save].estado(n)
    elif(u==5):
        n.destroy
def messagebox (value):
    tk.messagebox.showwarning("Dato Incorrecto",value+" fuera de Rango")
 
    #invoked within the method Content_tab_modify () once the button was pressed previously, a number will arrive here
    #depending on the value it will execute different actions
def botone():
    s=boton.get()
    #After choosing between 1 to 3 a new label will be created with a listbox that will display the data from the subclass requested
    # there is a for that will insert all the data in a listobox so that they are all displayed. In addition, a scrollbar was programmed inside this listbox so that the user can move freely in the printed results
    #after there is an entry and a button where you will select a name and at the same time itn will invoke a function and tell you if the name is in the list or not and if it is in the list it will allow you to modify data about that person
    #Option 4 displays a menu to print various comparative tables to obtain clearer information on the data found in this database, this was made possible by the other library we are using, Matploitlib
    if(s==1):
     lala=tk.Label(mFramemodi,text="\tNombre\tEdad\tSueldo\tAntiguedad\tCalificación\tID General\tDisponibilidad\t Pacientes tratados\t Estudios ",bg="blue").grid(row=6,column=0)
     lo=tk.Listbox(mFramemodi,width=124)
     scroll=tk.Scrollbar(mFramemodi,command=lo.yview)
     lo.config(yscrollcommand=scroll.set)
     scroll.grid(row=7,column=1,sticky="ns")
     for i in range(len(medicos_generales)):
       lo.insert(str(i),"          "+ medicos_generales[i].nombre+"\t            "+str(medicos_generales[i].edad)+"\t         "+str(medicos_generales[i].sueldo)+"                  "+str(medicos_generales[i].antiguedad)+"                                "+str(medicos_generales[i].calif)+"                 "+ medicos_generales[i].ID+"              "+str(medicos_generales[i].disponible)+"                "+str(medicos_generales[i].pacientes)+"                "+medicos_generales[i].titulo)
     lo.grid(row=7,column=0)
     Ln=tk.Label(mFramemodi,text="Ingrese el nombre").grid(row=8,column=0)
     En=tk.Entry(mFramemodi,textvariable=ng)
     En.grid(row=8,column=1)
     ba=tk.Button(mFramemodi,text="Aceptar",command=lambda:elegir_accion_m_general(str(En.get()),medicos_generales)).grid(row=9,column=0)
    elif(s==2):
     lala=tk.Label(mFramemodi,text="Nombre\tEdad\tSueldo\tAntiguedad\tCalificación\tID General\tOperaciones realizadas\tEnfermeras acargo\tDisponibilidad",bg="pink").grid(row=6,column=0)
     lo=tk.Listbox(mFramemodi,width=124)
     scroll=tk.Scrollbar(mFramemodi,command=lo.yview)
     lo.config(yscrollcommand=scroll.set)
     scroll.grid(row=7,column=1,sticky="ns")
     for i in range(len(medicos_cirujanos)):
       lo.insert(str(i),"             "+ medicos_cirujanos[i].nombre+"                "+str(medicos_cirujanos[i].edad)+"                         "+str(medicos_cirujanos[i].sueldo)+"                     "+str(medicos_cirujanos[i].antiguedad)+"                                  "+str(medicos_cirujanos[i].calif)+"                            "+ str(medicos_cirujanos[i].ID)+"                     "+str(medicos_cirujanos[i].operaciones)+"         "+str(medicos_cirujanos[i].enfermeras)+"             "+str(medicos_cirujanos[i].disponible))
     lo.grid(row=7,column=0)
     Ln=tk.Label(mFramemodi,text="Ingrese el nombre").grid(row=8,column=0)
     En=tk.Entry(mFramemodi,textvariable=ng)
     En.grid(row=8,column=1)
     ba=tk.Button(mFramemodi,text="Aceptar",command=lambda:elegir_accion_cirujano(str(En.get()),medicos_cirujanos)).grid(row=9,column=0)
    elif(s==3):
     lala=tk.Label(mFramemodi,text="Nombre\tEdad\tSueldo\tAntiguedad\tCalificación\tID General\t\tVacunas realizadas\tDisponibilidad",bg="yellow").grid(row=6,column=0)
     lo=tk.Listbox(mFramemodi,width=124)
     scroll=tk.Scrollbar(mFramemodi,command=lo.yview)
     lo.config(yscrollcommand=scroll.set)
     scroll.grid(row=7,column=1,sticky="ns")
     for i in range(len(medicos_laboratoristas)):
       lo.insert(str(i),"              "+ medicos_laboratoristas[i].nombre+"                     "+str(medicos_laboratoristas[i].edad)+"            "+str(medicos_laboratoristas[i].sueldo)+"                 "+str(medicos_laboratoristas[i].antiguedad)+"                         "+str(medicos_laboratoristas[i].calif)+"                      "+ str(medicos_laboratoristas[i].ID)+"                       "+str(medicos_laboratoristas[i].vacunas)+"                               "+ str(medicos_laboratoristas[i].disponible))
     lo.grid(row=7,column=0)
     Ln=tk.Label(mFramemodi,text="Ingrese el nombre").grid(row=8,column=0)
     En=tk.Entry(mFramemodi,textvariable=ng)
     En.grid(row=8,column=1)
     ba=tk.Button(mFramemodi,text="Aceptar",command=lambda:elegir_accion_laboratorista(str(En.get()),medicos_laboratoristas)).grid(row=9,column=0)
    elif(s==4):
         MF=tk.Frame(raiz)
         MF.pack(side="left",anchor="n")
         MF.config(bg="black")
         Lag4=tk.Label(MF,text="Menu comparación").grid(row=0,column=0)
         Lag5=tk.Label(MF,text="1. Comparación de sueldos").grid(row=1,column=0)
         Lag6=tk.Label(MF,text="2. Comparación de calificaciones").grid(row=2,column=0)
         Lag7=tk.Label(MF,text="3. Comparación de antiguedades").grid(row=3,column=0)
         Lag8=tk.Label(MF,text="4. Comparación de edades").grid(row=4,column=0)
         Lag9=tk.Label(MF,text="5. Regresar al menú principal").grid(row=5,column=0)
         Lag10=tk.Label(MF,text="Escriba la opción").grid(row=6,column=0)
         el=tk.Entry(MF)
         el.grid(row=6,column=1)
         bu=tk.Button(MF,text="Aceptar",command=lambda: findr(int(el.get()),MF)).grid(row=6,column=2)
    elif(s==5):
        mFramemodi.destroy()
        tk.messagebox.showinfo("Hasta luego","Gracias por su preferencia")
#Method that recieves and validates the entry if option 4 is selected
#Once the validation has been passed, the frame will be removed and menu will be displayed in which the user will select the desired option
def findr (value, MF):
    if value>=1 and value<=5:
        if value==5:
            MF.destroy()
        else:
            Lag11=tk.Label(MF,text="1. Comparación individual").grid(row=7,column=0)
            Lag12=tk.Label(MF,text="2. Comparación general").grid(row=8,column=0)
            Lag13=tk.Label(MF,text="Seleccione la opción deseada: ").grid(row=9,column=0)
            et=tk.Entry(MF)
            et.grid(row=9,column=1)
            bu=tk.Button(MF,text="Aceptar",command=lambda:findr_2(value,int(et.get()),MF))
            bu.grid(row=9,column=2)
    else:
        tk.messagebox.showwarning("Dato Incorrecto","El escrito valor no es válido")
# Function that displays another menu that validates the previously entered option and invokes by means of a button another function that will give way to graph printing
def findr_2 (value_1,value_2,MF):
    if value_2==1:
        Lag11=tk.Label(MF,text="1. Médico General ").grid(row=10,column=0)
        Lag12=tk.Label(MF,text="2.Cirujano ").grid(row=11,column=0)
        Lag13=tk.Label(MF,text="3.Laboratorista ").grid(row=12,column=0)
        ey=tk.Entry(MF)
        ey.grid(row=12,column=1)
        by=tk.Button(MF,text="Aceptar",command=lambda:findr_3(value_1,int(ey.get()))).grid(row=12,column=2)
#If general comparison is selected, advanced chain is called to graph the data asigned by the first entry.    
    elif value_2==2:
        advanced_chain(medicos_generales,medicos_cirujanos,medicos_laboratoristas,value_1)
    else:
        tk.messagebox.showwarning("Dato Incorrecto","El escrito valor no es válido")
#Function that calls chain function and asigns the graphic to be made based on the value given in the last entry (regarding the type of medic) and the value given by the first entry(the data to be graphed).       
def findr_3(value_1,value_3):
    if value_3==1:
        chain(medicos_generales,value_1,"generales","b","+")
    elif value_3==2:
        chain(medicos_cirujanos,value_1,"cirujanos","r","//")
    elif value_3==3:
        chain(medicos_laboratoristas,value_1,"laboratoristas","y","x")
    else:
        tk.messagebox.showwarning("Dato Incorrecto","El escrito valor no es válido")
#Funtion that receives one list containing the data to be graped and another one with the names that match the data. The rest of the values asign the name, color and texture of the graph.
def bar_graphics (list_x,list_y,value,name,col,sign):
    fig,ax=plt.subplots()
    ax.bar(list_x,list_y,hatch=sign,alpha=0.5,color=col)
    ax.set_ylabel(value)
    ax.set_xlabel("Nombres")
    ax.set_title(value+" de los médicos "+name)
    plt.show()
#Function that receives a list containig the objects of a certain class and creates a list based on the option that is selected to be graphed and another containing the names that match the data. It also receives the name,color and texture of the graph and then procedes to send this values to bar graphics.
def chain (list_main,z,name,col,sign):
    list_x=[]
    list_y=[]
    if z==1:
        for i in range(len(list_main)):
            list_y.append(list_main[i].sueldo)
            value="Sueldos"
    elif z==2:
        for i in range(len(list_main)):
            list_y.append(list_main[i].calif)
            value="Calificaciones"
    elif z==3:
        for i in range(len(list_main)):
            list_y.append(list_main[i].antiguedad)
            value="Antigüedad (Años)"
    else:
        for i in range(len(list_main)):
            list_y.append(list_main[i].edad)
            value="Edad (Años)"
           
    for i in range(len(list_main)):
        list_x.append(list_main[i].nombre)
    bar_graphics(list_x,list_y,value,name,col,sign)
#Function that empties the data of the list containing lists to create three different graph plots. It also receives the title of the graph. 
def bar_graphics2(list_main,value):
    fig,ax=plt.subplots()
    ax.bar(list_main[0],list_main[1],label="generales",hatch="+",alpha=0.5,color="b")
    ax.bar(list_main[2],list_main[3],label="cirujanos",hatch="//",alpha=0.5,color="r")
    ax.bar(list_main[4],list_main[5],label="laboratoristas",hatch="x",alpha=0.5,color="y")
    ax.legend(loc="upper right")
    ax.set_ylabel(value)
    ax.set_xlabel("Nombres")
    ax.set_title(value+" General")
    plt.show()
#Function that creates three lists based on the option selected. It also creates three lists with the names that correspond the data. At the end it creates a list with the lists and send this list accompanied by the variable value that dictates the name of the graph to bar_graphics2.
def advanced_chain(lista_1,lista_2,lista_3,z):
    list_x1=[]
    list_x2=[]
    list_x3=[]
    list_y1=[]
    list_y2=[]
    list_y3=[]
    if z==1:
        for i in range(len(lista_1)):
            list_y1.append(lista_1[i].sueldo)
        for i in range(len(lista_2)):
            list_y2.append(lista_2[i].sueldo)
        for i in range(len(lista_3)):
            list_y3.append(lista_3[i].sueldo)
        value="Sueldos"
    elif z==2:
        for i in range(len(lista_1)):
            list_y1.append(lista_1[i].calif)
        for i in range(len(lista_2)):
            list_y2.append(lista_2[i].calif)
        for i in range(len(lista_3)):
            list_y3.append(lista_3[i].calif)
        value="Calif"
    elif z==3:
        for i in range(len(lista_1)):
            list_y1.append(lista_1[i].antiguedad)
        for i in range(len(lista_2)):
            list_y2.append(lista_2[i].antiguedad)
        for i in range(len(lista_3)):
            list_y3.append(lista_3[i].antiguedad)
        value="Antigüedad"
    else:
        for i in range(len(lista_1)):
            list_y1.append(lista_1[i].edad)
        for i in range(len(lista_2)):
            list_y2.append(lista_2[i].edad)
        for i in range(len(lista_3)):
            list_y3.append(lista_3[i].edad)
        value="Antigüedad"
    for i in range(len(lista_1)):
        list_x1.append(lista_1[i].nombre)
    for i in range(len(lista_2)):
        list_x2.append(lista_2[i].nombre.lower())
    for i in range(len(lista_3)):
        list_x3.append(lista_3[i].nombre.upper())
    lista_main=[list_x1,list_y1,list_x2,list_y2,list_x3,list_y3]
    bar_graphics2(lista_main,value)
       
#for a graphic interface to work propertly ran by Tkinter, raiz.mainloop() codeline is always needed at the end of the code
raiz.mainloop()


