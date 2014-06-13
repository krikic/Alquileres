#-------------------------------------------------------------------------------

class Clientes():
    def __init__ (self):
        self.__NIF=""
        self.__nombre = ""
        self.__apellidos=""
        self.__alquileres = []     # LISTA DE alquileres

    def getNIF(self):
        return self.__NIF

    def setNIF(self,NIF):
        self.__NIF = NIF


    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        if len(nombre) > 20:
            print ("ERROR")
            return
        self.__nombre = nombre

    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self,apellidos):
        if len(apellidos) > 20:
            print ("ERROR")
            return
        self.__apellidos = apellidos


    def addAlquiler (self,alq):
        self.__alquileres.append(alq)

    def getAlquileres(self):
        return self.__alquileres


    def Imprimir (self):
        print ("NIF cliente ",self.getNIF())
        print ("Nombre",self.getNombre())
        print ("Apellidos",self.getApellidos())






class Coches():
    def __init__ (self):
        self.__matricula=""
        self.__marca=""
        self.__modelo=""
        self.__precio=0
        self.__disponible=None
        self.__alquileres=[]

    def getmatricula(self):
        return self.__matricula

    def setmatricula(self,matricula):
        self.__matricula = matricula

    def getmarca(self):
        return self.__marca

    def setmarca(self,marca):
        self.__marca = marca


    def getmodelo(self):
        return self.__modelo

    def setmodelo(self,modelo):
        self.__modelo = modelo

    def getprecio(self):
        return self.__precio

    def setprecio(self,precio):
        self.__precio = precio

    def getdisponible(self):
        return self.__disponible

    def setdisponible(self,disponible):
        self.__disponible = disponible


    def addAlquiler (self,alq):
        self.__alquileres.append(alq)

    def getAlquileres(self):
        return self.__alquileres

    def Imprimir (self):
        print ("Matricula ",self.getmatricula())
        print ("Marca",self.getmarca())
        print ("Modelo",self.getmodelo())
        print ("Precio",str(self.getprecio()))
        print ("Disponible",self.getdisponible())



class Alquiler():

    def __init__(self,clientes,coches):
        self.__clientes = clientes
        self.__coches=coches
        self.__fechaalquiler=""
        self.__retornada=False
        self.__fechaRetorno=""
        self.__importe=0
        self.__completada=False

    def getCliente(self):
        return self.__clientes

    def getCoches(self):
        return self.__coches

    def getFechaAlquiler(self):
        return self.__fechaalquiler

    def retornar (self,fecha):
        self.__retornada=True
        self.__fechaRetorno = fecha

    def getRetornada(self):
        return self.__retornada

    def getFechaRetorno (self):
        return self.__fechaRetorno

    def setfechaRetorno(self,fechaRetorno):
        self.__fechaRetorno = fechaRetorno


    def getFechaAlquiler(self):
        return self.__fechaalquiler

    def setfechaAlquiler(self,fechaalquiler):
        self.__fechaalquiler = fechaalquiler

    def getimporte(self):
        return self.__importe

    def setimporte(self,importe):
        self.__importe = importe

    def getcompletada(self):
        return self.__completada

    def setcompletada(self,completada):
        self.__completada = completada






class GestionAlquiler():
    def __init__(self):
        self.__clientes = []
        self.__coches= []
        self.__alquileres=[]


    def cargarFichero (self):
        self.__clientes = []
        self.__coches= []
        self.__alquileres=[]


        try:
            F = open ("alquileres.txt","r")
            for x in F:
                datos = x.replace("\n","").split("\t")
                tipo = datos[0]
                if tipo == "CL":
                    J = Clientes()
                    J.setNIF(datos[1])
                    J.setNombre(datos[2])
                    J.setApellidos(datos[3])
                    self.__socios.append(J)
                if tipo == "CO":
                    J=Coches()
                    J.setmatricula(datos[1])
                    J.setmarca(datos[2])
                    J.setmodelo(datos[3])
                    J.setprecio(datos[4])
                    J.setdisponible(datos[5])
                    self.__coches.append(J)

                if tipo == "AL":
                    clientes = [xx for xx in self.__clientes if xx.getNIF() == datos[1]]
                    coches = [xx for xx in self.__coches if xx.getmatricula() == datos[2]]
                    J=Alquiler(clientes[0],coches[0])
                    clientes[0].addAlquiler(J)
                    coches[0].addAlquiler(J)
                    J.setfechaAlquiler(datos[3])
                    J.setfechaRetorno(datos[4])
                    J.setimporte(datos[5])
                    J.setcompletada(datos[6])
                    self.__alquileres.append(J)

            F.close()
        except:
            print ("No encuentro el fichero")

    def guardarFichero(self):
        F = open("alquileres.txt","w")
        for x in self.__clientes:
            F.write("CL" + "\t" + x.getNIF() + "\t"+x.getNombre()+"\t"+x.getApellidos() +"\n")

        for x in self.__coches:
            F.write ("CO" + "\t" + x.getmatricula() + "\t" + x.getmarca()+ "\t" +x.getmodelo()+"\t"+str(x.getprecio())  +"\t"+x.getdisponible()+ "\n")

        for x in self.__alquileres:
            strRetornada = "N"
            if x.getRetornada(): strRetornada = "S"
            F.write ("AL" + "\t" + x.getCliente().getNIF() + "\t" +x.getCoches().getmatricula() + "\t" + x.getFechaAlquiler()+ "\t" + strRetornada + "\t" + x.getFechaRetorno() + "\n")
            F.close()

    def AgregarCliente (self,cliente):
        jBuscar = [j for j in self.__clientes if j.getNIF() == cliente.getNIF()]
        if len(jBuscar) == 0:
            self.__clientes.append(cliente)
            return True
        else:
            return False

    def getCliente (self):
        return self.__clientes


    def AgregarCoche (self,coche):
        jBuscar = [j for j in self.__coches if j.getmatricula() == coche.getmatricula()]
        if len(jBuscar) == 0:
            self.__coches.append(coche)
            return True
        else:
            return False

    def getCoches (self):
        return self.__coches

    def alquilar (self,NIF,matricula,fechaalquiler,fecharetorno,importe,completada):
        cliente = [x for x in self.__clientes if x.getNIF() == NIF]
        if len(cliente) == 0:
            return False
        coche = [x for x in self.__coches if x.getmatricula() == matricula]

        if len(coche) == 0:
            return False
        alquiler = Alquiler(cliente[0],coche[0],fechaalquiler,fecharetorno,importe,completada)
        coche[0].addAlquiler(alquiler)
        cliente[0].addAlquiler(alquiler)
        self.__alquileres.append(alquiler)
        return True


class GestionCoches():
    def __init__(self):
        self.__gestionCoches = GestionAlquiler()
        self.__gestionCoches.cargarFichero()

    def guardarFichero (self):
        self.__gestionCoches.guardarFichero()

    def AgregarCoche(self):
        m = Coches()
        s = input ("Matricula: ")
        m.setmatricula(s)
        s = input ("Marca: ")
        m.setmarca(s)
        s = input ("Modelo: ")
        m.setmodelo(s)
        s = int(input ("Precio: "))
        m.setprecio(s)
        m.setdisponible("S")

        result=self.__gestionCoches.AgregarCoche(m)
        if not result:
            print ("No se ha podido agregar el coche")

    def AgregarCliente(self):
        m = Clientes()
        s = input ("NIF: ")
        m.setNIF(s)
        s = input ("Nombre: ")
        m.setNombre(s)
        s = input ("Apellidos: ")
        m.setApellidos(s)

        result=self.__gestionCoches.AgregarCliente(m)
        if not result:
            print ("No se ha podido agregar el coche")


    def VisualizarCochesDisponibles (self):

        print ("Lista de coches")
        print ("================")
        for x in self.__gestionCoches.getCoches():
            if(x.getdisponible()=="S"):
             print (x.getmatricula(),x.getmarca(),x.getmodelo(),str(x.getprecio()),x.getdisponible())

    def VisualizarCochesAlquilados (self):
            print ("Lista de coches alquilados")
            print ("================")
            for x in self.__gestionCoches.getCoches():
              if(x.getdisponible()=="N"):
                 print (x.getmatricula(),x.getmarca(),x.getmodelo(),str(x.getprecio()),x.getdisponible())




    def Alquilar (self):
        NIF = input("NIF del cliente: ")
        matricula = input("Matricula del coche: ")
        fecha = input("Fecha alquiler: ")
        fecharetorno = input("Fecha retorno: ")
        importe=int(input("importe:"))
        completada=input("completada:")
        for x in self.__gestionCoches.getCoches():
           if (self.getdisponible()=="S"):
            asi=self.setdisponible ("N")
            self.__gestionCoches.getCoches().append(asi)
            result = self.__gestionCoches.alquilar(NIF,matricula,fecharetorno,importe,completada)

            if not result:
                print ("No se ha podido alquilar la pelicula")



def Menu():
    print ("Menu:")
    print ("1 - Alquilar un coche disponible")
    print ("2 - Listar los coches disponibles")
    print ("3 - Listar los coches alquilados")
    print ("4 - añadir un nuevo coche")
    print ("5 - añadir un nuevo cliente")
    print ("6 - Ingresos totales entre dos fechas")
    print ("0 - Salir")
    op = -1
    while op < 0 or op > 6:
        op = int(input("Introducir opcion: "))
    return op



def main():
    gestion = GestionCoches()
    opcion = -1
    while opcion != 0:
        opcion = Menu()
        if opcion == 1:
            gestion.Alquilar()
        elif opcion == 2:
            gestion.VisualizarCochesDisponibles()
        elif opcion == 3:
            gestion.VisualizarCochesAlquilados()
        elif opcion == 4:
            gestion.AgregarCoche()
        elif opcion == 5:
            gestion.AgregarCliente()
        elif opcion ==6:
            gestion.IngresosTotales()
    gestion.guardarFichero()


if __name__ == '__main__':
    main()









