class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    #   self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes)
      

                
    def ingresarPaciente(self, p):
        self.__lista_pacientes.append(p)
        
        ########NOTA: Se comentaron estas lineas para cambiar la estructura de ingresar paciente
        
        # # 1- solicito los datos por teclado
        # nombre = input("Ingrese el nombre: ")
        # #cedula = int(input("Ingrese la cedula: "))   
        # genero = input("Ingrese el genero: ")
        # servicio = input("Ingrese el servicio: ")
        # # 2- creo el objeto Paciente y le asigno los datos
        # p = Paciente()
        # p.asignarNombre(nombre)
        # p.asignarCedula(cedula)
        # p.asignarGenero(genero)
        # p.asignarServicio(servicio)        
        # # 3- guardo el Paciente en  la lista        
        # self.__lista_pacientes.append(p)
        # # self.__lista_pacientes[p.verCedula()] = p
        # # 4- actualizo la cantidad de pacientes en el sistema
        # self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(self.__numero_pacientes) + " pacientes")

    
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
                
    def VerificarPaciente(self, cedula):
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                return False               
                
def main():
                
    mi_sistema = Sistema()

    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            
            # 1- solicito los datos por teclado
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))  

            if mi_sistema.VerificarPaciente(cedula) == False:
                print("El paciente ya se encuentra registrado.")
                continue 
            else:
                pass
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2- creo el objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)        
            # 3- guardo el Paciente en  la lista        
            mi_sistema.ingresarPaciente(p)
            
            #### self.__lista_pacientes[p.verCedula()] = p
            
            # 4- actualizo la cantidad de pacientes en el sistema
            #self.__numero_pacientes = len(self.__lista_pacientes)
            


        elif opcion == 2:
            mi_sistema.verNumeroPacientes()
            ###### NOTA: Se comenta esta línea para cambiar la estructura de sistema
            #print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
            
        elif opcion == 3:
            mi_sistema.verDatosPaciente()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
        
