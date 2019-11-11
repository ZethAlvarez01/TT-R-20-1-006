function buscar(elemento) {
    var cte = elemento.getAttribute('id');
    //console.log(cte);
    var arreglo = cte.split("-");

    $.ajax({
        url: "/buscar_palabra/" + arreglo[0] + "/"
    }).done(function(res) {
        var significado = res.palabra;
        //console.log(significado);
    });

}