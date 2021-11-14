"""
Evaluacion Unidad 4 resolucioon al problema
"""
#Declarar super clase
class Empresa:
    def __init__(self,Titulo,Trabajador, rango,SAl):
        self.__Titulo = Titulo
        self.__Trabajador = Trabajador
        self.__rango = rango
        self.__SAl=SAl
    #Declarar getters y setters
    def Presentacion(self):
        print("mi nombre es:",self.__Trabajador)
        print(self.__SAl)
    def getTrabajador(self):
        return self.__Trabajador
    def getRango(self):
        return self.__Rango
    def getTitulo(self):
        return self.__Titulo

    def setTrabajador(self, nuevoTrab):
        self.__Trabajador = nuevoTrab
    def setRango(self,nuevoRango):
        self.__Rango= nuevoRango
 #   def __del__(self):
  #      print("El objeto", type(self).__name__,"fue destruido")
#para empleado1
class Empleado(Empresa):
    _Categoria = "Trabajador"
    def __init__(self,Titulo,Trabajador, rango,SAl,Nombre,edad,estatura,sueldo):
        super().__init__(Titulo,Trabajador, rango,SAl)
        self.__Nombre = Nombre
        self.__edad = edad
        self.__estatura=estatura
        self.__sueldo=sueldo


    def __describir(self):
        print("La empresa:")
        print("\n",super().getTitulo())
        print("Rango:", super().getRango())
        print("Nombre del empleado:", self.__Nombre)
        print("edad del empleado:", self.__edad)
        print("estatura del emplead:",self.__estatura)
        print("el sueldo que recibe es de:",self.__sueldo)
#getters y setters
    def getInfo(self):
        self.__describir()

    def getTitulo(self):
        print(" la empresa:",self.__Titulo)

    def getRango(self):
        return self.__Rango


    def setNombre(self,nuevoNombre):
        self.__Nombre = nuevoNombre
    def setEstatura(self, nuevoEst):
        self.__Nombre = nuevoEst

#subclase para el empleado

class Persona:
    _Categoria = "Persona"
    def __init__(self, Titulo,Nombre,edad,estatura,Vestimenta,PuestoS, Domicilio=None):
        self.__Titulo = Titulo
        self.__Nombre=Nombre
        self.__edad = edad
        self.__estatura = estatura
        self.__PuestoS = PuestoS
        self.__Domicilio =Domicilio
        self.__Vestimenta=Vestimenta
    def getInfo(self):
        print("El puesto que solcita es:",self.__PuestoS)
        print("El empleado viste con:",self.__Vestimenta)
    def Presentacion1(self):
        print("mi nombre es:",self.__Nombre)
        if self.__Domicilio !=None:
            print("Esta persona vive en", self.__Domicilio)

    def setPuest(self, NuevoPues):
        self.__PuestoS = NuevoPues

    def setRango(self, nuevoDomicilio):
        self.__Domicilio = nuevoDomicilio
class Entrevistado(Persona):
    _Categoria = "Contrato"
    def __init__(self, Titulo,Nombre,edad,estatura,Vestimenta,PuestoS, Domicilio=None):
        super().__init__(self, Titulo,Nombre,edad,estatura,Vestimenta,PuestoS)
        self.__Vestimenta=Vestimenta

    def getInfo(self):
        super().getInfo()

        if self.__Vestimenta ==True:
            print("su vesimenta Es adecuada")
        elif self.__Vestimenta==False:
            print("su vestimenta no es apta para hoy")

#aqui comienza iter para el manejo de converscion