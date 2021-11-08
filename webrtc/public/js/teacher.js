var content = "{'engage':1, 'bored':2}";
function sendStatus() {

    console.log("send try");
    // var output = {sender:"sender", receiver:"receiver"
    //     ,command:"chat", type:"text", data:"msg"};
    socket.emit("message", content);

    // socket.on('chat', message=>{
    //     console.log('from server~', message)
    // })
}

function getStatus() {

    console.log("get try");
    // // var output = {sender:"sender", receiver:"receiver"
    // //     ,command:"chat", type:"text", data:"msg"};
    // socket.emit("message", content);
    var i=0;
    socket.on('chat', message=>{
        console.log('from server~', message, i);
        i++;
    })
}

