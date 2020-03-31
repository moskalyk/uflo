// const hypercore = require('hypercore')
// const feed = hypercore('./data', {valueEncoding: 'json'})

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const PORT = 3002;

// app.get('/batch', (req,res) => {
// 	feed.getBatch(0, 10, {valueEncoding: 'json'}, (e, values) => {
// 		if(e) res.send(e).status(500);
// 		res.send({values: values}).status(200);
// 	});
// });

io.on('connection', function(socket){
	console.log('a user connected');
	// feed.getBatch(0, 10, { valueEncoding: 'json' }, (e, values) => {
	// 	if(e) res.send(e).status(500);
    // socket.emit('data', {data: 100});
	// });

    // process.stdin.setEncoding('utf8');

    process.stdin.on('data', function(chunk) {
        const line = chunk.toString();
        const parse = line.split('FEED:');
        // console.log('data')

        // console.log(chunk)
        if(parse.length > 1 ){
        	const data = parse[1];
        	const rawInt = data.split('.0')[0];
        	console.log('-------------------')
        	// console.log(rawInt)
        	// feed.append({data: rawInt})
            console.log({data: rawInt})
            // console.log('Emitting')
        	socket.emit('chat_message', {data: rawInt});
            // socket.emit('data', {data: rawInt});
        }
    });


});

http.listen(PORT, function(){
  console.log(`listening on *:${PORT}`);
});


