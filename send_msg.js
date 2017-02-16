var textbox = document.getElementById("text_sent");
var output = document.getElementById("output");
var socket = new WebSocket("ws://" + location.hostname + ":8080");

function send_clicked() {
    socket.send(textbox.value);
}

socket.onmessage = function(event) {
    output.innerHTML = event.data;
};
