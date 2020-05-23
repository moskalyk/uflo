// const key = process.argv[2]
// console.log(`Connecting with key: ${key}`)

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

const IS_HOST = process.argv.length > 2 ? false : true


const PORT =  IS_HOST ? 3001 : 3002 

const ram = require('random-access-memory')
const replicate = require('@hyperswarm/replicator')
const hypercore = require('hypercore')

const key = !IS_HOST && Buffer.from(process.argv[2], 'hex')
const feed = key ? hypercore(ram, key, {valueEncoding: 'json'}) : hypercore(ram, {valueEncoding: 'json'})

feed.on('ready', () => {
	console.log(`Using Room: ${feed.key.toString('hex')}`)
	replicate(feed, { live: true })
})

io.on('connection', (socket) => {
	console.log('a user connected');

	socket.on('update', (hz) => {
		console.log(hz);
		feed.append({hz: hz})
	});

	feed.createReadStream({
		live: true
	}).on('data', (data) => {
		console.log(data)

		if(!IS_HOST) socket.emit('hz_message', data);
	})

});

http.listen(PORT, () => console.log(`listening on *:${PORT}`));


