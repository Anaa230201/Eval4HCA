"""
Evaluacion Unidad 4 resolucioon al problema
"""
#Declarar super clase
class Empresa:
    def __init__(self,Titulo,Trabajador, rango):
        self.__Titulo = Titulo
        self.__Trabajador = Trabajador
        self.__rango = rango


    #Declarar getters y setters
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
    def __del__(self):
        print("El objeto", type(self).__name__,"fue destruido")
#para empleado1
class Empleado(Empresa):
    _Categoria = "Trabajador"
    def __init__(self, Titulo, Rango, Nombre,edad,estatura,sueldo):
        super().__init__(self._Categoria, Titulo,Rango)
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

class Persona(Empleado):
    _Categoria = "Persona"
    def __init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,Vestimenta, Domicilio=None):
        super().__init__(Titulo,Rango,Nombre,edad,estatura,sueldo)
        self.__PuestoS = PuestoS
        self.__Domicilio =Domicilio
        self.__Vestimenta=Vestimenta
    def getInfo(self):
        super().getInfo()
        print("El puesto que solcita es:",self.__PuestoS)
        print("El empleado viste con:",self.__Vestimenta)

        if self.__Domicilio !=None:
            print("Esta persona vive en", self.__Domicilio)

    def setPuest(self, NuevoPues):
        self.__PuestoS = NuevoPues

    def setRango(self, nuevoDomicilio):
        self.__Domicilio = nuevoDomicilio
class Entrevistado(Persona):
    _Categoria = "Contrato"
    def __init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,Vestimenta,Domicilio=True):
        super().__init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,Vestimenta)
        self.__Vestimenta=Vestimenta

    def getInfo(self):
        super().getInfo()

        if self.__Vestimenta ==True:
            print("su vesimenta Es adecuada")
        elif self.__Vestimenta==False:
            print("su vestimenta no es apta para hoy")

#aqui comienza iter para el manejo de converscion
class Entrevistador(Empleado):
    _Categoria = "Entrevista"
    def __init__(self, Titulo, Rango, Nombre,edad,estatura,sueldo,Saludo,indicacion):
        super().__init__(Titulo, Rango, Nombre,edad,estatura,sueldo)
        self.__Saludo = Saludo
        self.__indicacion= indicacion
    def __describir(self):
        print("manejo un sueldoo de", self.__sueldo)
        print("Espere", self.__Saludo)
class Curriculum(Entrevistado):
    _Categoria = "Entrevista"
    def __init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,profesion):
        super().__init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS)
        self.__profesion = profesion
        #hasta aquino
class Datos(Curriculum):
    _Categoria = ""
    def __init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,profesion):
        super().__init__(self, Titulo,Rango,Nombre,edad,estatura,sueldo,PuestoS,profesion)




List=[]
