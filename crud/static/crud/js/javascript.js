
//RELOJ 
const $tiempo = document.querySelector('.tiempo'),
$fecha = document.querySelector('.fecha');

function digitalClock(){
    let f = new Date(),
    dia = f.getDate(),
    mes = f.getMonth() + 1,
    anio = f.getFullYear(),
    diaSemana = f.getDay();

    dia = ('0' + dia).slice(-2);
    mes = ('0' + mes).slice(-2)

    let timeString = f.toLocaleTimeString();
    document.getElementById('tiempo').innerHTML = timeString;

    let semana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'];
    let showSemana = (semana[diaSemana]);
    document.getElementById('fecha').innerHTML = `${showSemana} ${dia}-${mes}-${anio}` 
}
setInterval(() => {
    digitalClock()
}, 1000);

//DARK MODE
var content = document.getElementsByTagName('body')[0];
var darkMode = document.getElementById('dark-change');
darkMode.addEventListener('click', function(){
    darkMode.classList.toggle('active');
    content.classList.toggle('night');
})

//Geolocalizacion
function findMe(){
    var output = document.getElementById('map');
    if(navigator.geolocation){
        output.innerHTML = "<p>Tu navegador soporta geolocalizacion</p>";
    }else{
        output.innerHTML = "<p>Tu navegador NO soporta geolocalizacion</p>";
    }
    function localizacion(posicion){
        var latitude = posicion.coords.latitude;
        var longitude = posicion.coords.longitude;

        output.innerHTML = "<p>Latitud:"+latitude+"<br>Longitud:"+longitude+"</p>";
    }
     
    function error(){
        output.innerHTML = "<p>No se pudo obtener tu ubicacion</p>";
    }
    navigator.geolocation.getCurrentPosition(localizacion,error);
}


//API clima
let lon;
let lat;
let temperature = document.querySelector(".temp")
let summary = document.querySelector(".summary")
let loc = document.querySelector(".location")
let icon = document.querySelector(".icon")
const kelvin = 273.15

window.addEventListener("load",() => {
    
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition((position) =>{
            
            console.log(position);
            lon = position.coords.longitude;
            lat = position.coords.latitude;
        
        //ID API
        const api_id = "86814f2f1068ed6dea4d7773705b5702";

        const url_base = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api_id}`;

        fetch(url_base)
        .then((response) =>{

            console.log("RESPUESTA JSON");
            
            return response.json();
        })

        .then((data) => {
            console.log("ESTA ES LA DATA")
            console.log(data);

            temperature.textContent = 
             Math.floor(data.main.temp - kelvin) + "°C";
            summary.textContent = data.weather[0].description;
            loc.textContent = data.name + "," + data.sys.country;
        });

    });
        
    }
});




