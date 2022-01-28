#funciones
#funcion limpiar pantalla
import os
import time
#def limpiar_pantalla():
    #os.system("cls")
#fin funcion limpiar pantalla
opc1="Cambiar contraseña"
opc2="Ingresar coordenadas actuales"
opc3="Ubicar zona wifi más cercana"
opc4="Guardar archivo con ubicación cercana"
opc5="Actualizar registros de zonas wifi desde archivo"
opc6="Elegir opción de menú favorita"
opc7="Cerrar sesión"
contador=0

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

curso=int(input("Nombre de usuario: "))
if(curso==52213):
    codigo=int(input("Contraseña:"))
    if(codigo==31225):
        numero_1=213
        numero_2=(8-7)/(2-1)
        suma=numero_1+numero_2
        captcha=int(input(f"Complete la suma para continuar \n {numero_1} + {numero_2} ="))
        if(suma==captcha ):
            os.system("cls")
            print("Sesión iniciada")
            time.sleep(2)
        while contador<3:
            menu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
            for x in range(0,len(menu)):
                print(f"{x+1} - {menu[x]}") 
            eleccion=int(input(f"Elija una opción : \n"))   
            if eleccion==1:
                print(f"Usted ha elegido la opción  1\n")
            elif eleccion==2:
                print(f"Usted ha elegido la opción 2\n")
                exit()
            elif eleccion==3:
                print(f"Usted ha elegido la opción 3\n")
                exit()
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
                        os.system("cls")
                        print("Error")
                        time.sleep(2)
                        continue
                    else:
                        print(f"Para confirmar por favor responda:\n")
                    time.sleep(1)
                    adivinanza_2=int(input(f"La raiz cuadrada de nueve es: : \n"))
                    if adivinanza_2!=3:
                        os.system("cls")
                        print("Error")
                        time.sleep(2)
                        continue
                    else:
                        os.system("cls")
                        time.sleep(2)
                        mover=menu[nuevo_orden-1]
                        menu.remove(mover)
                        menu.insert(0,mover)
                        print("Usted ha elegido la opción 3")
                else:
                    os.system("cls")
                    print("Error")
                    time.sleep(2)
                    exit()
            elif eleccion==7:
                print(f"Hasta pronto \n  ")
                exit()
            else:
                contador+=1
                os.system("cls")
                print("Error")
                time.sleep(2)
                os.system("cls")
                continue
            break  
            
        else:
            print("Error") 
            exit()  
    else:
        print("Error")
        exit()
else:
    print("Error")
    exit()