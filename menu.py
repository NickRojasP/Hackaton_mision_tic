# Estructura de dato diccionario
def semana(i) :  
        conmutador = {
                0 : 'Cambiar contraseña' ,
                1 : 'Ingresar coordenadas actuales' ,
                2 : 'Ubicar zona wifi más cercana' ,
                3 : 'Guardar archivo con ubicación cercana' ,
                4 : 'Actualizar registros de zonas wifi desde archivo,' ,
                5 : 'Elegir opción de menú favorita' ,
                6 : 'Cerrar sesión'
                }
        return conmutador.get (i,"día de la semana no válido")
dia = semana(int(input("Digita el # dia de la semana: ")))
print(dia)