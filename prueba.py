
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
menu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
contador=0
numero_1=123
numero_2=(8-7)/(2-1)
suma=numero_1+numero_2
codigo="31225"
usuario=52213
lista_coordendas=[]
lista_depuracion=[  [10.103,-74.982],
                    [10.115,-75.085],
                    [10.100,-74.801]]
#endregion

def ImprimirLista(): #Nos permite imprimir la lista
    for x in range(len(menu)):
        print(f"{x+1} - {menu[x]}")

def ValidacionDatos(dato1,dato2):#Toma como entrada dos parámetros a comparar, ej: UsuarioGuardado,UsuarioIngresado
    if dato1 == dato2:
        return True #Verdadero si son iguales
    else:
        return False #falso si son diferentes

def ReordenarFav(posicion): #Toma como entrada un parámetro que se usa para crear la variable mover
    mover=menu[posicion-1]
    menu.remove(mover)
    menu.insert(0,mover)

def ErrorConMensaje():#Toma como entrada un mensaje personalizado que se imprimirá en pantalla
    os.system("cls")
    print("Error")
    time.sleep(2)

def cambiar_clave(clave_actual): #cambia la clave actual 
    if (input("Ingrese la contraseña actual :")) == codigo:
        time.sleep(2)
        nueva_clave=input("Ingrese la nueva contraseña : ")
        if ValidacionDatos(nueva_clave,clave_actual):
            print("Error contraseña igual a la anterior")
            return clave_actual
        else:
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nueva_clave):
                return nueva_clave
            else:
                ErrorConMensaje("Las contraseñas no coinciden")
                return clave_actual
    else:
        ErrorConMensaje()
        exit()
    

def ingresar_coordenadas(lista_original):
    lista_duplicada=list(lista_original)
    for x in range (0,3):
        lista_duplicada.append([])
        lat=input("Ingrese la latitud :")
        if lat== "" or lat == " ":
            print("Error")
            time.sleep(2)
            exit()
        elif float(lat) >= 6.077 and float(lat) <= 6.284: 
            lon=input("Ingrese la longitud :")
            if lon== "" or lon == " ":
                print("Error")
                time.sleep(2)
                exit()
            elif float(lon) >= -76.049 and float(lon) <= -75.841:
                lista_duplicada[x].insert(0,lat)
                lista_duplicada[x].insert(1,lon)
                print(lista_duplicada)
            else:
                ErrorConMensaje()
                lista_duplicada=[]
                return lista_duplicada
                exit()
                
        else:  
            ErrorConMensaje()
            lista_duplicada=[]
            return lista_duplicada
            exit()

def ordenar_latitudes(lista_original):
    print(f"La coordenada {max(lista_original,key=lambda posicion: posicion[0])} es la que esta mas al norte")

def promedio_coordenadas(lista_original):
    print(f"El promedio de las latitudes es:   {(lista_original[0][0]+lista_original[1][0]+lista_original[2][0])/3} ")
    print(f"El promedio de las longitud es:   {(lista_original[0][1]+lista_original[1][1]+lista_original[2][1])/3} ")

def imprimir_coordendas(lista_original): #imprime las coordendas que se ingresan 
    print(lista_original)
    lista_duplicada=list(lista_original)
    print(f"Las coordenas ingresadas son :\n")
    for x in range(0,len(lista_duplicada)):
        print(f"coordenada [latitud,longitud] {x+1} :['{lista_duplicada[x][0]}','{lista_duplicada[x][1]}']")
    ordenar_latitudes(lista_duplicada)
    promedio_coordenadas(lista_duplicada)
    escoger_c=int(input(f"Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú\n"))
    if escoger_c!=1 and escoger_c!=2 and escoger_c!=3:
        ErrorConMensaje()
        return
    else:
        actualizar_coordendas(escoger_c,lista_original)
        
        
        

def actualizar_coordendas(escoger_c,lista_original):
    escoger_c=escoger_c-1
    lista_duplicada=list(lista_original)
    for x in range (0,3):
        lista_duplicada.append([])
        lat=input("Ingrese la latitud :")
        if lat== "" or lat == " ":
            print("Error")
            time.sleep(2)
            exit()
        elif float(lat) >= 6.077 and float(lat) <= 6.284: 
            lon=input("Ingrese la longitud :")
            if lon== "" or lon == " ":
                print("Error")
                time.sleep(2)
                exit()
            elif float(lon) >= -76.049 and float(lon) <= -75.841:
                lista_duplicada[escoger_c].insert(0,lat)
                lista_duplicada[escoger_c].insert(1,lon)
                print(f"coordenada [latitud,longitud] {x+1} :['{lista_duplicada[x][0]}','{lista_duplicada[x][1]}']")
                print(f"coordenada [latitud,longitud] {2} :['{lista_duplicada[1][0]}','{lista_duplicada[1][1]}']")
                print(f"coordenada [latitud,longitud] {3} :['{lista_duplicada[2][0]}','{lista_duplicada[2][1]}']")
                promedio_coordenadas(lista_original)
                return
            else:
                ErrorConMensaje()
                lista_duplicada=[]
                return lista_duplicada
                exit()
                
        else:  
            ErrorConMensaje()
            lista_duplicada=[]
            return lista_duplicada
            exit()
    

imprimir_coordendas(lista_depuracion)


print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
curso=int(input("Nombre de usuario: "))
if ValidacionDatos(curso,usuario):
    if ValidacionDatos(input("Ingrese su contraseña: "),codigo):
        captcha=int(input(f"Complete la suma para continuar \n {numero_1} + {numero_2} ="))
        if ValidacionDatos(captcha,suma):
            os.system("cls")
            print("Sesión iniciada")
            time.sleep(2)
        while contador<3:
            menu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
            ImprimirLista() 
            eleccion=int(input(f"Elija una opción : \n"))   
            if eleccion==1:
                codigo=cambiar_clave(codigo)
                continue
            elif eleccion==2:
                if lista_coordendas==[]:
                    lista_coordendas=ingresar_coordenadas(lista_coordendas)
                    print(lista_coordendas)
                    time.sleep(2)
                    os.system("cls")
                    continue
                else:
                    actualizar_coordendas(lista_coordendas) 
                exit()
            elif eleccion==3:
                print(f"Usted ha elegido la opción 3\n")
            elif eleccion==4:
                print(f"Usted ha elegido la opción 4\n")
            elif eleccion==5:
                print(f"Usted ha elegido la opción 5\n")
            elif eleccion==6:
                nuevo_orden=int(input(f"Seleccione opción favorita : \n"))
                if nuevo_orden==1 or nuevo_orden==2 or nuevo_orden==3 or nuevo_orden==4 or nuevo_orden==5:
                    time.sleep(2)
                    print(f"Para confirmar por favor responda:\n")
                    time.sleep(1)
                    adivinanza_1=int(input(f"Todo numero multiplicado por mi da el mismo : \n"))
                    if adivinanza_1!=1:
                        ErrorConMensaje()
                        continue
                    else:
                        print(f"Para confirmar por favor responda:\n")
                    time.sleep(1)
                    adivinanza_2=int(input(f"La raiz cuadrada de nueve es.... : \n"))
                    if adivinanza_2!=3:
                        ErrorConMensaje()
                        time.sleep(2)
                        continue
                    else:
                        os.system("cls")
                        time.sleep(2)
                        ReordenarFav(nuevo_orden)
                else:
                    ErrorConMensaje()
                    exit()
            elif eleccion==7:
                print(f"Hasta pronto \n  ")
                time.sleep(2)
                exit()
            else:
                contador+=1
                ErrorConMensaje()
                os.system("cls")
                continue
            break  
            
        else:
            ErrorConMensaje()
            exit()  
    else:
        ErrorConMensaje()
        exit()
else:
    ErrorConMensaje()
    exit()
