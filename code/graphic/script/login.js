function greet() {
    console.log('hola')
    var name = document.getElementById('name').value;
    eel.get_playlists_frontend()(function(result) {
        console.log(result);
    });
}