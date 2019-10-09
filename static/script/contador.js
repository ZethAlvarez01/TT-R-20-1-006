function contadorCaracter(obj) {
    document.getElementById("n-caracteres").innerHTML = 'Número de caracteres: ' + obj.value.length;
}

function detecta(e){
    if(e.keyCode == 32){
        alert("Espacio detectado");
    }
}