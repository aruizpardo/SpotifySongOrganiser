function greet() {
    var name = document.getElementById('name').value;
    eel.greet(name)(function(result) {
        document.getElementById('result').innerText = result;
    });
}