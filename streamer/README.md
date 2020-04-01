# neurostreamer 

### streamer.js: Parse date from std.in

Can be used to pipe date from a seperate process.

e.g. logs from android studio

```

$ adb logcat | node streamer.js

```

### forwarder.js: Forward data from socket.io (browser) connection to python socket.io

The use of [blueberry SDK](https://github.com/blueberryxtech/blueberry-js-sdk) uses the BLE experimental chrome feature for external devices. In order to use such feature, one must [set the correct flags first](https://developers.google.com/web/updates/2015/07/interact-with-ble-devices-on-the-web).

Then run,

```

$ node forwarder.js

```


