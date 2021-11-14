import test1 as Entrevista
"¨Programa principal para la entrevista de un nuevo empleado de trabajo"
print("Cargar nuevo archivo")
#llegada de una persona a la empresa para la entrevista de trabajo
print("la empresa SabalodeXalapa suc. Teziutlan")
print("Una persona se acerca a la ventanilla")

Secretaria1=Entrevista.Empresa("Sabalo","Karla","Secretaria","Buen  dia bienvenido")
print(Secretaria1.Presentacion())
Persona1=Entrevista.Persona("Buenas tardes me puede comunicar con el gerente tengo una entrevista de trabajo","Daniel",21,1.80,"saco y camisa","Asesor financiero")
print(Persona1.Pres1())
print("la secretaria llama al gerente e indica el lugar a donde debe diriigirse")
Gerente=Entrevista.EmpleadoT("Buenas tardes ","Carlos","Gerente","una camisa con 3 botones","1.80 metros")
print(Gerente.desc())
print("El gerente comienza a preguntar los datos de la persona")
print(Persona1.getInfo())



