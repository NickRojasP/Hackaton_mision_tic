import os
import time
import random 



#Las regiones nos permiten colapsar ciertas partes del código

#region VARIABLES GLOBALES
opc1="Cambiar contraseña"
opc2="Ingresar coordenadas actuales"
opc3="Ubicar zona wifi más cercana"
opc4="Guardar archivo con ubicación cercana"
opc5="Actualizar registros de zonas wifi desde archivo"
opc6="Elegir opción de menú favorita"
opc7="Cerrar sesión"
listamenu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
contadorerrores=0
UsuarioGuardado="52213"
ClaveGuardada="31225"
captcha1=213
captcha2=((8-7)/(2-1))
captcha=captcha1+captcha2 
listacoordenadas=[]
listadepuracion=[[10.103,-74.902],
                [10.115,-75.085],
                [10.108,-74.801]]
#endregion

def ImprimirLista(): 
    for x in range(len(listamenu)):
        print(f"{x+1} - {listamenu[x]}")

def ValidacionDatos(dato1,dato2):
    if dato1 == dato2:
        return True 
    else:
        return False 

def ReordenarFav(posicion): 
    mover=listamenu[posicion-1]
    listamenu.remove(mover)
    listamenu.insert(0,mover)

def ErrorConMensaje():
    os.system("cls")
    time.sleep(2)

def CambiarClave(claveactual):
    if ValidacionDatos(input("Ingrese la contraseña actual :"), claveactual):
        nuevaclave=input("Ingrese la nueva contraseña : ")
        if ValidacionDatos(nuevaclave,claveactual):
            ErrorConMensaje()
            return claveactual
        else:
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nuevaclave):
                return nuevaclave
            else:
                ErrorConMensaje()
                return claveactual
    else:
        print("Error")
        exit()
        
def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)
    for x in range (0,3):
        listaduplicada.append([])
        lat=input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            ErrorConMensaje()
            break
        lat=float(lat)
        if lat >= 6.077 and lat <= 6.284:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                ErrorConMensaje()
            lon=float(lon)
            if lon >= -76.049 and lon <= -75.841:
                listaduplicada[x].insert(0,lat)
                listaduplicada[x].insert(1,lon)
            else:
                print("Error coordenada")
                listaduplicada=[]
                return listaduplicada
                exit()
        elif lat==0:
            print("Error coordenada")
            exit()
        else:
            print("Error coordenada")
            listaduplicada=[]
            return listaduplicada
            exit()
    time.sleep(2)    
    return listaduplicada

#Creamos la función ordenar latitudes (primero se ejecuta imprimir coordenadas)
def Ordenarlatitudes(listaoriginal):
    #Creamos una función anónima que nos retorna el valor mínimo; ubicado en la posición 0 de la lista original
    #Es decir pasamos por todas las latitudes y buscamos el menor
    print(f"La coordenada {max(listaoriginal,key=lambda posicion: posicion[0])} es la que esta mas al norte")

#Creamos la función ordenar longitudes (primero se ejecuta imprimir coordenadas)
    #Creamos una función anónima que nos retorna el valor máximo; ubicado en la posición 1 de la lista original
    #Es decir pasamos por todas las longitudes y buscamos el mayor
def OrdenarLongitudes(listaoriginal):
    print(f"La coordenada que está mas al oriente es: {max(listaoriginal, key=lambda posicion: posicion[1])}")
    
#Imprimimos la suma de todos los elementos de cada sublista en la posición 0 (latitudes)
#y dividimos entre 3
def PromedioCoordenadas(listaoriginal):
    print(f"El promedio de las latitudes es:   {(listaoriginal[0][0]+listaoriginal[1][0]+listaoriginal[2][0])/3} ")
    print(f"El promedio de las longitud es:   {(listaoriginal[0][1]+listaoriginal[1][1]+listaoriginal[2][1])/3} ")

#Creamos la función que imprime las coordenadas
def ImprimirCoordenads(listaoriginal):
    listaduplicada=list(listaoriginal)
    print("Las coordenas ingresadas son : ")
    #creamos un for que pasará imprimiendo la sublista X ambas posiciones
    for x in range(0,len(listaduplicada)):
        print(f"coordenada [latitud,longitud] {x+1} :['{listaduplicada[x][0]}','{listaduplicada[x][1]}']")
    #llamamos las funciones de ordenar y promedio y mandamos la lista completa como parámetros
    Ordenarlatitudes(listaduplicada)
    PromedioCoordenadas(listaduplicada)
    #guardamos la coordenada que el usuario moverá en una variable llamada choice
    choice=int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú\n"))
    #revisamos si choice es un valor válido
    if choice !=1 and choice !=2 and choice !=3:
        ErrorConMensaje()
        print("Error actualización")
        time.sleep(2)
        exit()
    elif choice==0:
        print("Error coordenada")
        #En caso de error hacemos un return
    else:
        #Si son datos válidos llamamos actualizar coordenadas
        #Mandamos como parámetros choice y la lista
        ActualizarCoordenadas(choice,listaoriginal)
        

def ActualizarCoordenadas(choice,listaoriginal):
    #Duplicamos la lista para ganar acceso a sus métodos
    listaduplicada=list(listaoriginal)
    choice=choice-1 #Le restamos uno a choice para arreglar el desfaze visual del menú
    #Pedimos por la latitud y longitud usando la misma logica de la función ingresar coordenadas
    lat=input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
            ErrorConMensaje()
            break
    lat=float(lat)
    if lat >= 6.077 and lat <= 6.284:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                ErrorConMensaje()
            lon=float(lon)
            if lon >= -76.049 and lon <= -75.841:
                listaduplicada[choice]=lat
                listaduplicada[choice]=lon
            else:
                print("Error coordenada")
                listaduplicada=[]
                return listaduplicada
                exit()
    else:
            print("Error coordenada")
            listaduplicada=[]
            return listaduplicada
            exit()
        
    
    return listaduplicada #En caso éxito retornamos la nueva lista
    

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
UsuarioIngresado=input("Nombre de usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): 
    if ValidacionDatos(input("Ingrese su contraseña:"), ClaveGuardada): 
        verificacion=int(input(f"Complete la suma para continuar {captcha1} + {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<3:
                os.system("cls")
                ImprimirLista()
                opcionelegida=int(input("Por favor selecciona una opción: ")) 
                if opcionelegida >= 0 and opcionelegida <= 8:
                    opcionelegidalista=listamenu[opcionelegida-1] 
                    if opcionelegidalista==opc1:
                        print(opc1)
                        ClaveGuardada=CambiarClave(ClaveGuardada)
                    elif opcionelegidalista==opc2:
                        print(opc2)
                        if listacoordenadas==[]:
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            #Llamamos la función imprimir coordenadas
                            ImprimirCoordenads(listacoordenadas)
                    elif opcionelegidalista==opc3:
                        print(f"Usted ha elegido la opción 3\n")
                        time.sleep(2)
                    elif opcionelegidalista==opc4:
                        print(f"Usted ha elegido la opción 4\n")
                        time.sleep(2)
                    elif opcionelegidalista==opc5:
                        print(f"Usted ha elegido la opción 5\n")
                        time.sleep(2)
                    elif opcionelegidalista==opc6:
                        nuevofavorito=int(input("Seleccione opción favorita : \n")) 
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5: 
                            print(f"Para confirmar por favor responda:\n")
                            time.sleep(1)
                            adivinanza_1=int(input(f"Todo numero multiplicado por mi da el mismo : \n"))
                            if adivinanza_1!=1:
                                ErrorConMensaje()
                                continue
                            else:
                                adivinanza_2=int(input(f"La raiz cuadrada de nueve es.... : \n"))
                                if adivinanza_2!=3:
                                    ErrorConMensaje()
                                    time.sleep(2)
                                    continue
                                else:
                                    os.system("cls")
                                    time.sleep(2)
                                    ReordenarFav(nuevofavorito)
                        else:
                            ErrorConMensaje()
                            continue 
                    elif opcionelegidalista==opc7:
                        print(f"Hasta pronto \n  ")
                        exit()
                else:
                    contadorerrores+=1 
                    ErrorConMensaje()
                    continue    
        else:
            ErrorConMensaje()
            print("Error actualización")
    else:
        ErrorConMensaje()
        print("Error")
else:
    ErrorConMensaje()
    print("Error")