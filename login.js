
    var Buscar_producto= document.getElementById("Buscar producto");
    var msg='Bienvenido a la pagina de Supermecado Dark';
    alert(msg);

    $(document).ready(function () {
        //Click al boton para pedir permisos
        $("#perdir_ubic").click(function () {
        //Si el navegador soporta geolocalizacion
        if (!!navigator.geolocation) {
        //Pedimos los datos de geolocalizacion al navegador
        navigator.geolocation.getCurrentPosition(
        //Si el navegador entrega los datos de geolocalizacion los imprimimos
        function (position) {
        window.alert("Ubicacion permitida");
        $("#nlat").text(position.coords.latitude);
        $("#nlon").text(position.coords.longitude);
        },
        //Si no los entrega manda un alerta de error
        function () {
        window.alert("Ubicacion no permitida");
        }
        );
        }
        });
        });

        if(Buscar_producto.value === null){
        alert("Error")
        }