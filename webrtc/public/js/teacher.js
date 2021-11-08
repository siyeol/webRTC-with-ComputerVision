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

//학생들의 ip를 받아온 flask에 요청을 보내서 취합된 ip를 보여줌

let IPlist;
function getIpList() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', "http://127.0.0.1:5000/sendIPlist", true);
    xhr.onload = function () {
        if (this.status === 200) {
            IPlist = this.response;
            console.log("received all student IP");
        }
        else {
            console.error(xhr);
        }
    };
    xhr.send(null);
}


function getENGfromStudent(ipAddress) {
    // getIpClient();
    let xhr = new XMLHttpRequest();
    xhr.open('GET', ipAddress, true);
    xhr.onload = function () {
        if (this.status === 200) {
            let objects = JSON.parse(this.response);
            console.log(objects);

        }
        else {
            console.error(xhr);
        }
    };
    xhr.send(null);
}

//update engagement every 1sec
async function getAllENGfromStudent() {
    for(var i=0;i<IPlist.length;i++){
        setInterval(getENGfromStudent(IPlist[i]), 1000);
    }
}


function getTeacher() {
    getIpList();
    getAllENGfromStudent();
}