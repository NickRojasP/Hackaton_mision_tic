import os
import time
import random
from math import asin,cos,sin,sqrt,radians,degrees

#si el usuario ingresa a la opcion 4 sin datos validos se mostrarará un error.
#mostrar los datos con el siguiente formato
# #informacion = {‘actual’: [‘latitud’, ‘longitud’],‘zonawifi1’: [‘latitud’, ‘longitud’, usuarios],
# ‘recorrido: [‘distancia’, ‘mediotransporte’,‘tiempopromedio’]}
#se creará un archivo con los datos suministrados.
#confirmar su exportación antes de guardar el archivo.

#si el usuario ingresa a la opción 5 se leerá un archivo existente que actualizará
#los datos de la lista de coordenadas predeterminadas.
#mostrar mensaje de confirmacion y presionar 0 para regresar al menú


#region VARIABLES GLOBALES
opc1="Cambiar contraseña"
opc2="Ingresar coordenadas actuales"
opc3="Ubicar zona wifi más cercanas"
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
radio=6372.795477598
listacoordenadas=[]
listadepuracion=[[10.125,-74.948],
                 [10.400,-74.935],
                 [10.127,-74.950]]
listadistancias=[]
restauranteactual=None
distanciaparatiempo=None
listacoordenadaspredet=[[6.124,-75.946,1035],
                        [10.122,-74.908,12],
                        [6.135,-75.976,31],
                        [6.144,-75.836,151]]
#Creamos el diccionario con la informacion que nos pide la rúbrica
informacion = {"actual": ["latitud", "longitud"],
                "zonawifi1": ["latitud", "longitud", "usuarios"],
                "recorrido": ["distancia", "mediotransporte","tiempopromedio"]}
#creamos una bandera que nos permitirá saber si todo está listo para el manejo de ficheros
alistamiento=False
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

def ErrorConMensaje(mensaje):
    os.system("cls")
    print(mensaje)
    time.sleep(2)

def CambiarClave(claveactual):
    if ValidacionDatos(input("Por favor ingrese su contraseña actual: "), claveactual):
        nuevaclave=input("Por favor ingrese su nueva contraseña: ")
        if ValidacionDatos(nuevaclave,claveactual):
            ErrorConMensaje("La nueva contraseña no puede ser igual a la anterior.")
            return claveactual
        else:
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nuevaclave):
                return nuevaclave
                
            else:
                ErrorConMensaje("Las contraseñas no coinciden")
                return claveactual
    else:
        ErrorConMensaje("La contraseña es incorrecta")
        exit()
        
def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)
    for x in range (0,3):
        listaduplicada.append([])
        lat=input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lat=float(lat)
        if lat >= 6.077 and lat <= 6.284:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
            lon=float(lon)
            if lon >= -76.049 and lon <= -75.841:
                listaduplicada[x].insert(0,lat)
                listaduplicada[x].insert(1,lon)
                
                
            else:
                ErrorConMensaje("Error coordenadas")
                listaduplicada=[]
                return listaduplicada
        else:
            ErrorConMensaje("Error coordenadas")
            listaduplicada=[]
            return listaduplicada
    print("Coordenadas Ingresadas correctamente")
    time.sleep(2)    
    return listaduplicada

def Ordenarlatitudes(listaoriginal):
    print(f"La coordenada que está mas al sur es: {min(listaoriginal, key=lambda posicion: posicion[0])}")

def OrdenarLongitudes(listaoriginal):
    print(f"La coordenada que está mas al oriente es: {max(listaoriginal, key=lambda posicion: posicion[1])}")
    
def PromedioCoordenadas(listaoriginal):
    print(f"EL promedio de las latitudes es: {(listaoriginal[0][0]+listaoriginal[1][0]+listaoriginal[2][0])/3}")

def ImprimirCoordenads(listaoriginal):
    
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
    Ordenarlatitudes(listaduplicada)
    OrdenarLongitudes(listaduplicada)
    PromedioCoordenadas(listaduplicada)
    choice=int(input("Por favor ingrese la opción que desea modificar:"))

    if choice !=1 and choice !=2 and choice !=3:
        ErrorConMensaje("Esa opción es inválida")
        return 
    else:
      
        ActualizarCoordenadas(choice,listaoriginal)

def ActualizarCoordenadas(choice,listaoriginal):

    listaduplicada=list(listaoriginal)
    choice=choice-1 
    lat=input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
    lat=float(lat)
    if lat >= 10.103 and lat <= 10.362:
        lon=input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lon=float(lon)
        if lon >= -75.088 and lon <= -74.319:

            listaduplicada[choice][0]=lat
            listaduplicada[choice][1]=lon
            
        else:
            ErrorConMensaje("Longitud fuera del rango")
            listaduplicada=[listaoriginal] 
            return listaduplicada
    else:
        ErrorConMensaje("Latitud fuera del rango")
        listaduplicada=[listaoriginal] 
        return listaduplicada
    
    return listaduplicada
    
def MostrarRestaurantesFav(listaoriginal):
    if listaoriginal==[]:
        ErrorConMensaje("No hay restaurantes favoritos ingresados.")
        exit()
    else:

        ImprimirRestaurantesFav(listaoriginal)
        
def ImprimirRestaurantesFav(listaoriginal):
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
        
    opcion=int(input("Por favor seleccione su restaurante actual: "))
    if opcion == 1 or opcion ==2 or opcion ==3:
        global restauranteactual
        restauranteactual=listacoordenadas[opcion-1]
        informacion["actual"]=restauranteactual #Guardamos la información del restaurante actual en el diccionario
        PrepararDatos(opcion,listaduplicada,listacoordenadaspredet)
    else:
        ErrorConMensaje("Error")

def PrepararDatos(IndRestauranteactual,listaoriginal,coordenadasfijas):
    listaduplicada=list(listaoriginal)
    listaduplicadafijas=list(coordenadasfijas)
    lat1=listaduplicada[IndRestauranteactual-1][0]
    lon1=listaduplicada[IndRestauranteactual-1][1]
    lat1=convertiraRadianes(lat1)
    lon1=convertiraRadianes(lon1)
    
    for x in range(0,len(listaduplicadafijas)):
        for y in range (0,2):
           
            listaduplicadafijas[x][y]=convertiraRadianes(listaduplicadafijas[x][y])
    
    AplicarFormulaDistancia(lat1,lon1,listaduplicadafijas)
    
    pass

def convertiraRadianes(valoraconvertir):
    return radians(valoraconvertir)
    pass

def AplicarFormulaDistancia(lat1, lon1, listaenradianes):

    
    for x in range(0,4):
        lat2=listaenradianes[x][0]
        lon2=listaenradianes[x][1]
        latdelta=lat2-lat1
        londelta=lon2-lon1

        auxiliarcalculo=sin(londelta/2)**2
        auxiliarcalculo=auxiliarcalculo*(cos(lat1)*cos(lat2))
        auxiliarcalculo=(sin(latdelta/2)**2)+auxiliarcalculo
        auxiliarcalculo=sqrt(auxiliarcalculo)
        auxiliarcalculo=asin(auxiliarcalculo)
        auxiliarcalculo=(2*radio)*auxiliarcalculo

        auxiliarcalculo=auxiliarcalculo*1000
        auxiliarcalculo=round(auxiliarcalculo)
       
        listadistancias.append(auxiliarcalculo)

    OrdenarDistancias(listadistancias)

def OrdenarDistancias(distancias):
    distanciasduplicadas=list(distancias)
    min1=distanciasduplicadas.index(min(distanciasduplicadas)) 
    distanciasduplicadas.pop(min1)
   
    min2=distancias.index(min(distanciasduplicadas))
               
    
    ImprimirMensajeCercanias(min1,min2,listacoordenadaspredet,distancias)

def ImprimirMensajeCercanias(min1,min2, basededatos,listadistancias ):
    for x in range (0,4):
        basededatos[x][0]=degrees(basededatos[x][0])
        basededatos[x][1]=degrees(basededatos[x][1])
    

    for x in range (0,len(listacoordenadaspredet)):
        if listacoordenadaspredet[min1][0]==listacoordenadaspredet[x][0] and listacoordenadaspredet[min1][1] == listacoordenadaspredet[x][1]:
            if listacoordenadaspredet[x][2]>listacoordenadaspredet[min1][2]:
                min1=listacoordenadaspredet.index(listacoordenadaspredet[x])
                

    global distanciaparatiempo 
    if basededatos[min1][2] > basededatos[min2][2]:
        
        print(f"1. La zona WIFI más cercana está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} promedio de usuarios.")
        print(f"2. La segunda zona WIFI más cercana está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} promedio de usuarios.")
        opcdestino=int(input("Por favor seleccione la zona WIFI al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1: 
            distanciaparatiempo = listadistancias[min1]
            #guardamos la informacion de la zona wifi elegida como destino en el diccionario
            #teniendo en cuenta la variable min1 y min 2 y referenciando las posiciones
            #de la base de datos
            #debe llamarse antes de cambiar de función
            informacion["zonawifi1"]=[basededatos[min1][0],basededatos[min1][1],basededatos[min1][2]]
            DarIndicaciones(restauranteactual,basededatos[min1])
        elif opcdestino==2:
            distanciaparatiempo = listadistancias[min2]
            informacion["zonawifi1"]=[basededatos[min2][0],basededatos[min2][1],basededatos[min2][2]] 
            DarIndicaciones(restauranteactual,basededatos[min2])
        else:
            ErrorConMensaje("Restaurante destino inválido.")
        
    else:
        print(f"1. La zona WIFI más cercana está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} platos.")
        print(f"2. El segundo restaurante más cercano está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} platos.")
        opcdestino=int(input("Por favor seleccione el restaurante al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1:
            distanciaparatiempo= listadistancias[min2]
            informacion["zonawifi1"]=[basededatos[min2][0],basededatos[min2][1],basededatos[min2][2]]
            DarIndicaciones(restauranteactual,basededatos[min2])
        elif opcdestino==2:
            distanciaparatiempo= listadistancias[min1]
            informacion["zonawifi1"]=[basededatos[min1][0],basededatos[min1][1],basededatos[min1][2]] 
            DarIndicaciones(restauranteactual,basededatos[min1])
        else:
            ErrorConMensaje("Restaurante destino inválido.")

def DarIndicaciones(restactual,restdestino):

    latorigen=restactual[0]
    lonorigen=restactual[1]
    latdestino=restdestino[0]
    londestino=restdestino[1]

    if latorigen>latdestino:
        txt1="el sur"
    elif latorigen<latdestino:
        txt1="el norte"

    else:
        txt1=""
     
 
    if lonorigen>londestino:
        txt2="el occidente"
    elif lonorigen<londestino:
        txt2="el oriente"
    else:
        txt2=""
    

    if txt1=="" and txt2!="": 
        print(f"Debe ir hacia {txt2}")

    elif txt2=="" and txt1!="": 
        print(f"Debe ir hacia {txt1}")

    elif txt1=="" and txt2=="":
        print("Usted ya está en el destino")
        time.sleep(3)
        

    else:
        print(f"Debe dirigirse primero hacia {txt1} y luego hacia {txt2}")
        
        time.sleep(2)
        CalcularTiempoRecorrido()    
   
def CalcularTiempoRecorrido():
    tiempo1="segundos" 
    tiempo2="segundos"
    
    if distanciaparatiempo==0: 
        pass
        
    else:
        auto=distanciaparatiempo/20.83 
        moto=distanciaparatiempo/19.44
        
        if auto > 60: 
            auto=auto/60
            tiempo1="minutos"
        
        
        if moto > 60:
            moto=moto/60
            tiempo2="minutos"
        
        moto=round(moto,2) 
        auto=round(auto,2)
        
       
        print(f"Se tardará aproximadamente {auto} {tiempo1} en auto; y {moto} {tiempo2} en moto")
        
        #creamos algunas variables temporales que permiten guardar
        #la información necesaria para el diccionario
        #distancias, medio de transporte y tiempo.
        tmp1=distanciaparatiempo
        tmp2="En auto tardarías "
        tmp3=f"{auto} {tiempo1}"
        tmp4="moto"
        tmp5=moto
        #guardamos toda la información en el diccionario.
        informacion["recorrido"]=[tmp1,tmp2,tmp3,tmp4,tmp5]
        #declaramos alistamiento como global
        global alistamiento
        #cambiamos el valor a true únicamente en éste punto del código.
        alistamiento=True
        time.sleep(5)

#cremos la función que permite leer un archivo (ya debe estar creado) y se trae como parámetro
def LeerArchivo(archivo):
    #hacemos un try para evitar errores
    try:
        #importante el formato de la linea de texto del archivo es:
        # 30.127,-70.950,7;15.122,-69.908,12;18.305,-72.040,32;8.127,-74.950,50000
        #abrimos el archivo y lo guardamos en una variable
        lineaarchivo=open(archivo).readline()
        #hacemos la separación de los elementos basado en los ;
        lineaarchivo=lineaarchivo.split(";")
        #creamos una lista en blanco
        listatemporalcoord=[]
        #realizamos un for que añada listas vacías a la lista y separamos 
        #la linea, ést vez con las , y guardamos ese dato en una variable
        for x in range(0,4):
            listatemporalcoord.append([])
            tmp=lineaarchivo[x].split(",")
            #creamos otro for y guardamos cada elemento del último split en la lista
            #que creamos
            for y in range(0,3):
                listatemporalcoord[x].append(tmp[y])
        
        #Una vez terminada la distribución de elementos hacemos 2 for anidados
        #que pasen por cada elemento de cada sublista y permitan
        #convertir a float cada elemento, recuerda que al traerse del archivo son tipo string.
        for x in range(len(listatemporalcoord)):
            for y in range(0,len(listatemporalcoord[x])):
                listatemporalcoord[x][y]=float(listatemporalcoord[x][y])
                #Si es la 2da posición convertimos a entero para quitar el decimal.
                if y==2:
                    listatemporalcoord[x][y]=int(listatemporalcoord[x][y])
        #Mostramos un mensaje de confirmación
        print("Coordenadas actualizadas")
        time.sleep(2)
        #mandamos la lista creada hasta el momento al return
        return listatemporalcoord
    #en caso de errores simulamos la creación de la lista mostrando un error
    #y mandando los datos al return
    except IOError:
        ErrorConMensaje("Hasta pronto")
        return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
        
    except FileNotFoundError:
        ErrorConMensaje("Hasta pronto")
        return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
    except ValueError:
        ErrorConMensaje("Dato Inválido")
        return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]
    except:
        ErrorConMensaje("Error.")
        return [[10.127,-74.950,7],[10.122,-74.908,12],[10.305,-75.040,32],[10.127,-74.950,5000]]

#creamos la función que permite crear el archivo.        
def CrearArchivo():
    #revisamos si la variable alistamiento nos permite continuar.
    if alistamiento:
        #de nuevo trabajamos con un try para evitar problemas
        try:
            #creamos un archivo en modo escritura (se crea siempre, se sobre escribe lo anterior)
            #cambiamos la codificacion a utf-8 para latino.
            archivo=open("archivoescritura.txt","w",encoding="utf-8")
            #escribimos el diccionar que creamos durante la ejecución del programa
            archivo.write(str(informacion))
            print("Exportando archivo")
            time.sleep(2)
            exit()
        #mostrmos los errores y realizamos simulación de exportación   
        except IOError:
            print("Error con el fichero")
            time.sleep(1)
            print("Exportando archivo")
            exit()
        except FileNotFoundError:
            print("Error con el fichero")
            time.sleep(1)
            print("Exportando archivo")
            exit()
        except:
            print("Error con el fichero")
            time.sleep(1)
            print("Exportando archivo")
            exit()
    else:
        ErrorConMensaje("Error de alistamiento")
        exit()

 
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
UsuarioIngresado=input("Ingrese su usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): 
    if ValidacionDatos(input("Ingrese su contraseña: "), ClaveGuardada): 
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} + {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls") 
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<5:
                
                listadistancias=[] 
                os.system("cls")
                ImprimirLista()
                opcionelegida=int(input("Por favor selecciona una opción: ")) 
                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegidalista=listamenu[opcionelegida-1] 
                    
                    if opcionelegidalista==opc1:
                        print(opc1)
                        ClaveGuardada=CambiarClave(ClaveGuardada)
                    elif opcionelegidalista==opc2:
                        print(opc2)
                        if listacoordenadas==[]:
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            ImprimirCoordenads(listacoordenadas)
                        
                    elif opcionelegidalista==opc3:

                        MostrarRestaurantesFav(listacoordenadas) 

                    elif opcionelegidalista==opc4:
                        print(opc4)
                        #llamamos la función crear archivo.
                        CrearArchivo()
                    elif opcionelegidalista==opc5:
                        print(opc5)
                        #llamamos la función para leer el archivo con el nombre del fichero como parámetro.
                        #el return se asignará a la lista de coordenadas.
                        listacoordenadaspredet=(LeerArchivo("archivolectura.txt"))
                    elif opcionelegidalista==opc6:
                        print(opc6)
                        nuevofavorito=int(input("Ingrese el número de la opción que desea mover: ")) 
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5: 
                            numerorndm=random.randint(0,10000)
                            if int(input(f"Por favor escriba el siguiente número: {numerorndm}:")) == numerorndm:
                                if int(input("Por favor resuelva la siguiente suma 9 + 9:"))==18:
                                    ReordenarFav(nuevofavorito)
                                
                                else:
                                    ErrorConMensaje("Error comprobación 2") 
                            else:
                                ErrorConMensaje("Error comprobación 1")
                        else:
                            ErrorConMensaje("Opción Inválida")
                            continue 
                    elif opcionelegidalista==opc7:
                        ErrorConMensaje("Hasta pronto")
                        exit()
                else:
                    contadorerrores+=1 
                    ErrorConMensaje("Hasta pronto")
                    continue    
    
        else:
            ErrorConMensaje("Error captcha incorrecto")
    else:
        ErrorConMensaje("Error contraseña incorrecta")
else:
    ErrorConMensaje("Error usuario incorrecto")