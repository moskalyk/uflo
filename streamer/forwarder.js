const app = require('express')();
const app1 = require('express')();

const http = require('http').createServer(app);
const http1 = require('http').createServer(app1);

const io = require('socket.io')(http);
const io1 = require('socket.io')(http1);

const PORT = 3002;
const PORT1 = 3003;

// TODO: refactor with nodejs streams
io.on('connection', function(socket){
    io1.on('connection', function(socket2){
        socket.on('chat_message', function(data){ 
            const MAX_DATA = 5000
            // Perform any other data manipulation in javascript
            if(data.data < MAX_DATA){
                console.log(data)
                socket2.emit('io_message', {data: data.data});
            }
        }); // listen to the event
        console.log('another user connected');
    })
});

http.listen(PORT, function(){
  console.log(`listening on *:${PORT}`);
});


http1.listen(PORT1, function(){
  console.log(`listening on *:${PORT1}`);
});


