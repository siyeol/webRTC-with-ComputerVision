var teacherIP = window.location.href;
teacherIP =teacherIP.split(".")[0];
teacherIP =teacherIP.replace(teacherIP.split("-")[0],"");
teacherIP =teacherIP.replaceAll("-", ".").substring(1);
alert(teacherIP);

var myIP;
$(document).ready(function(){
    $.getJSON('https://api.ipify.org?format=jsonp&callback=?', function(data) {
        console.log(JSON.stringify(data, null, 2));
        // console.log(data.ip);
        myIP=data.ip;
    });
    postMyIP(myIP);
});

//send
function postMyIP(ip) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', window.location.href+"/recvIP", true);
    xhr.onload = function () {
        if (this.status === 200) {
            // let objects = JSON.parse(this.response);
            console.log("sent IP");
        }
        else {
            console.error(xhr);
        }
    };
    xhr.send(ip);
}