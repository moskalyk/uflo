const hypercore = require('hypercore')
const ram = require('random-access-memory')
const replicate = require('@hyperswarm/replicator')

const IS_HOST = process.argv.length > 2 ? false : true
const key = !IS_HOST && Buffer.from(process.argv[2], 'hex')
const feed = key ? hypercore(ram, key, {valueEncoding: 'json'}) : hypercore(ram, {valueEncoding: 'json'})

feed.on('ready', () => {
	console.log(`Using Room: ${feed.key.toString('hex')}`)
	replicate(feed, { live: true })

	feed.createReadStream({ live: true }).on('data', (data) => {
		console.log(data)
		if(!IS_HOST) console.log('hz_message: ', data);
	})
})

IS_HOST && setInterval(() => feed.append({hz: Math.floor(Math.random() * 5)}), 10000)



