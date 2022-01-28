print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
curso=52213
codigo=31225
curso=int(input("Nombre de usuario: "))
if(curso==52213):
    codigo=int(input("Contraseña:"))
    if(codigo==31225):
        numero_1=213
        numero_2=(8-7)/(2-1)
        suma=numero_1+numero_2
        captcha=int(input(f"Complete la suma para continuar \n {numero_1} + {numero_2} ="))
        if(suma==captcha ):
            print("Sesión iniciada")
            exit()
        else:
            print("Error") 
            exit()  
    else:
        print("Error")
        exit()
else:
    print("Error")
    exit()

