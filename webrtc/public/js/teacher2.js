var studentIP1 = "http://43ea-61-82-78-227.ngrok.io/teacher";
var studentIP2 = "http://43ea-61-82-78-227.ngrok.io/teacher";
var studentIP3 = "http://43ea-61-82-78-227.ngrok.io/teacher";
var studentIP4 = "http://43ea-61-82-78-227.ngrok.io/teacher";
//
function getIP(json) {
    alert("My public IP address is: " + json.ip);
}

$(document).ready(function(){
    $.getJSON('https://api.ipify.org?format=jsonp&callback=?', function(data) {
        alert(JSON.stringify(data, null, 2));
    });
});
// window.onload = function() {
    
// }

function getFromStudent(ipAddress) {
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

window.onload = function() {
    setInterval(getFromStudent(studentIP1), 1000);
    // setInterval(getFromStudent(studentIP2), 1000);
    // setInterval(getFromStudent(studentIP3), 1000);
    // setInterval(getFromStudent(studentIP4), 1000);
}


async function getIpClient() {
    try {
        //https://cors-anywhere.herokuapp.com/http://api.ipify.org/?format=text
      const response = await axios.get('https://api.ipify.org?format=json');
      console.log(response);
    } catch (error) {
      console.error(error);
    }
}

const findIP = (onNewIP) => { // onNewIp - your listener function for new IPs
    // compatibility for firefox and chrome
    const myPeerConnection = window.RTCPeerConnection ||
                             window.mozRTCPeerConnection ||
                             window.webkitRTCPeerConnection
    const pc = new myPeerConnection({ iceServers: [] })
    const noop = () => {}
    const localIPs = {}
    const ipRegex = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/g
  
    const ipIterate = (ip) => {
      if (!localIPs[ip]) onNewIP(ip)
      localIPs[ip] = true
    }
    pc.createDataChannel('') // create a bogus data channel
    pc.createOffer(sdp => {
      sdp.sdp.split('\n').forEach(line => {
        if (line.indexOf('candidate') < 0) return
        line.match(ipRegex).forEach(ipIterate)
      })
      pc.setLocalDescription(sdp, noop, noop)
    }, noop) // create offer and set local description
    pc.onicecandidate = (ice) => { // listen for candidate events
      if (
        !ice ||
        !ice.candidate ||
        !ice.candidate.candidate ||
        !ice.candidate.candidate.match(ipRegex)
      ) return
      ice.candidate.candidate.match(ipRegex).forEach(ipIterate)
    }
  }
  
  const addIP = (ip) => {
    console.log('got ip: ', ip)
  }
  
  findIP(addIP)

  function getTeacher(){
    $('#teacherOn').css("background-color","red");
  }
