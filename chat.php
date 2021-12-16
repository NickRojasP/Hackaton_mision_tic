<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="css/estilos.css">
    <title>Supermercado Dack</title>
</head>
<body>
    <ul>
        <li class="logo" style="float:left"><a href="index.html"><img img src="imgs/canasta.png" width="70" height="70" alt="canasta">   
        <li class="logo" style="float:right"><a href="index.html"><img img src="imgs/carrocompras.png" width="70" height="70" alt="carrito">          
        </a></li>
        <li align='center'><h1>Supermercado Dack</h1></li>
        
    </ul>
    <header>
        <nav class="navegacion">
            <ul class="menu">
                <li><a href="index.html">Inicio</a>
                <li><a href="#">Categorías</a>
                <ul class="submenu">
                    <li><a href="#">Alimentos</a></li>
                    <li><a href="#">Licores</a></li>
                    <li><a href="#">Farmacia</a></li>
                    <li><a href="#">Bebidas</a></li>
                    <li><a href="#">Papelería</a></li>
                    <li><a href="#">Express</a></li>
                    <li><a href="#">Aseo</a></li>
                    <li><a href="#">Hogar</a></li>
                    <li><a href="#">Otros</a></li>
                </ul></li>
                <li><a href="#"><img img src="imgs/lupita.png" width="15" height="15" alt="alimentos">Búsqueda del producto</a></li>
                <li><a href="#"><img img src="imgs/ubicacion.png" width="15" height="15" alt="alimentos">Ingresa tu ubicación</a></li>
                <li><a href="asistencia.html"><img img src="imgs/soporte-en-linea.png" width="15" height="15" alt="alimentos">Atención al usuario</a></li>
                <li><a href="chat.html"><img img src="imgs/chat.png" width="15" height="15" alt="alimentos">Chat en linea</a></li>
            </ul>
    </header></nav>
    <div id="conte">
        <div id="caja-chat">
            <div id="chat">
                <div id="datos-chat">
                  <span>Asesor</span>
                  <span>Hola,¿Como estas?</span>
                  <span>10:04 a.m.</span>  
                </div>
            </div>
        </div>
        <form method="post" action="index.php">
            <input type="text" name="nombre" placeholder="Ingresa tu nombre">
            <textarea name="mensaje" placeholder="Ingresa tu mensaje"></textarea>
            <input type="submit" name="enviar" value="Enviar"
        </form>
    </div>