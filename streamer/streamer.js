
const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const PORT = 3002;

io.on('connection', function(socket){
	console.log('a user connected');

    process.stdin.on('data', function(chunk) {
        const line = chunk.toString();
        const parse = line.split('FEED:');
        if(parse.length > 1 ){
        	const data = parse[1];
        	const rawInt = data.split('.0')[0];
        	console.log('-------------------')
            console.log({data: rawInt})
        	socket.emit('io_message', {data: rawInt});
        }
    });
});

http.listen(PORT, function(){
  console.log(`listening on *:${PORT}`);
});


