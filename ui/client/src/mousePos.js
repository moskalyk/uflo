/* 
 event: NUIT DE L'INFO 2018
 location: TOULOUSE
 team : AVE AS TEAM
 author : Guillaume Bonnet (GitHub: @stabla)
*/
const wrapperEl = document.getElementById('canva-container'),
    scrollerEl = document.getElementById('scroller');

var X, // Red, it's x axis
    Y, // Green, it's y axis
    depth; // Blue, it's scroll

var colorInputValue = document.getElementsByClassName('color')[0];
var colorHexaInputValue = document.getElementsByClassName('color-hexa')[0];

window.mobileAndTabletcheck = function() {
  var check = false;
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
  return check;
};

function doChange() {
    /* clear Canvas */
    guillocheJS.fn.clearIt();
    guillocheJS.initialStateMemory = JSON.parse(JSON.stringify(guillocheJS.figure));
    /* ReDraw Guilloché */
    guillocheJS.fn.drawIt();
}

var options = {
    majorR: guillocheJS.figure.majorR,
    minorR: guillocheJS.figure.minorR,
    steps: guillocheJS.figure.steps,
    Multiplier: guillocheJS.figure.Multiplier,
    angle: guillocheJS.figure.angle,
    radius: guillocheJS.figure.radius,
    amplitude: guillocheJS.figure.amplitude
};

const changeX = function(x) {
    guillocheJS.figure.majorR = x/5;
    doChange();
}

const changeY = function(y) {
    guillocheJS.figure.minorR = (y/1000);
    doChange();
}

const changeZ = function(z) {
    guillocheJS.figure.amplitude = z
    doChange()
}


wrapperEl.onmousemove = function (e) {
    X = e.pageX - wrapperEl.offsetLeft;
    Y = e.pageY - wrapperEl.offsetTop;

    // Ratio is the size (= the width/height taken) of each colors on the wrapper. Because R or G or B (Red, Green, Blue) have 0 to 255 values possibles, the ratio of width, and height, have to be divided by 255. 
    var widthRatio = wrapperEl.offsetWidth / 255;
    var heightRatio = wrapperEl.offsetHeight / 255;

    // Round value, because we want not X.XXXX but only X. X is between {0;255} and is a natural number. 
    xValue = Math.round(X / widthRatio);
    yValue = Math.round(Y / heightRatio);


};


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


var translatedData = 0
var MAX = 0;
var MIN = 0;
var trip = 0;

async function play() {

  // Sleep in loop
  var i = 0
  var dir = true
  var mul = 2

  while(1){
      await sleep(5);
      var mover = 1

      if(dir) i=i+mover
      else if (!dir) i=i-mover

      // console.log(i)
      // console.log(i)
      // buffer.push(translatedData)

      // changeX(translatedData)
      // changeX(translatedData)
      changeX(i)
      changeY(i)
      // console.log(`i: ${i}`)
      // // console.log(`data: ${translatedData}`)
      // console.log(`min: ${MIN}`)
      //console.log(`min: ${translatedData*(mul - 1)}`)
      // console.log(`max: ${MAX}`)
      // console.log(`max: ${translatedData*mul}`)

      if(i > MAX) dir = false
      // if(i > translatedData*mul) dir = false
      else if (i <= MIN) dir = true
      // else if (i <= translatedData*(mul - 1)) dir = true
  }
      


}

setTimeout(() => {
  // TUNE MEs
  var mul = 20
  // console.log('HERE')
  // console.log(Math.max.apply(null, buffer))
  // console.log(Math.min.apply(null, buffer))
  MAX = Math.max.apply(null, buffer) *mul
  MIN = Math.min.apply(null, buffer)*mul
}, 2000)

const buffer = []
const window_size = 10
const reducer = (accumulator, currentValue) => accumulator + currentValue;

function translate(data){
  // console.log("pushing")
  // console.log(data)
  buffer.push(Number(data))

  if(buffer.length > window_size) {
    buffer.shift()
    // console.log(buffer)
  }

  // console.log(`buffer length${buffer.length}`)

  return buffer.reduce(reducer)
}


play()
socket()

async function socket() {

  var socket = io('http://localhost:3002');
  socket.on('connect', function(){
    console.log('connected!')
  });
  socket.on('data', (data) => {
    console.log("NEW")
    // console.log(data.data)
    translatedData = translate((data.data) / 20)
    console.log(translatedData)

    // changeX(translatedData)
    // changeY(translatedData)
  });

  socket.on('disconnect', function(){});

  socket.on('connect', async () => {
    console.log(socket.disconnected)

  });
}

    // let socket = new WebSocket("ws://localhost:3002/");

    // socket.onopen = function(e) {
    //   console.log("[open] Connection established");
    //   console.log("Sending to server");
    //   // socket.send("My name is John");
    // };

    // socket.onmessage = function(event) {
    //   console.log(`[message] Data received from server: ${event.data}`);
    // };

    // socket.onclose = function(event) {
    //   if (event.wasClean) {
    //     console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    //   } else {
    //     // e.g. server process killed or network down
    //     // event.code is usually 1006 in this case
    //     console.log('[close] Connection died');
    //   }
    // };

    // socket.onerror = function(error) {
    //   console.log(`[error] ${error.message}`);
    // };

wrapperEl.addEventListener("scroll", function () {
    var depth = wrapperEl.scrollY || wrapperEl.scollTop || wrapperEl.scrollTop;

    var depthRatio = (scrollerEl.offsetHeight - wrapperEl.offsetHeight) / 255;
    depthValue = Math.round(depth / depthRatio);

    changeZ(depthValue);
});





window.onload = function () {
    console.log('initialized');
};
