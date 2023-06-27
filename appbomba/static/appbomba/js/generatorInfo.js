$("#btnInfo").click(function (event) {
    event.preventDefault();
    var pokemon = $("#txtInd").val().toLowerCase();
    
    $.ajax({
        url: "https://pokeapi.co/api/v2/pokemon/" + pokemon,
        error: function () {
        $("#informacion").html("<span>Pokemon no encontrado. Vuelve a buscar.</span>");
        },
        dataType: "json",
        success: function (data) {
        console.log(data);
        var $n_pokemon = data.name.toUpperCase();
        var $i_pokemon = data.sprites.front_default;
        var $t_pokemon = data.types.map(function(type) { return type.type.name.toUpperCase() }).join(", ");
        var $h_pokemon = data.abilities.map(function(ability) { return ability.ability.name.toUpperCase() }).join(", ");

        // agregamos la info y la imprimimos
        $("#informacion").empty();
        $("#informacion")
        .append(`
            <img src="${$i_pokemon}" alt="${$n_pokemon}">
            <div>
                <br><span>Nombre: ${$n_pokemon}</span>
                <br><span>Tipo: ${$t_pokemon}</span>
                <br><span>Habilidades: ${$h_pokemon}</span>
            </div>`);
        },
        type: "GET",
    });
});