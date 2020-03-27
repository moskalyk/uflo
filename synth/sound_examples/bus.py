from supercollider import Server, Synth, Buffer, AudioBus, ADD_TO_TAIL

import time
import random

#-------------------------------------------------------------------------------
# Create connection to default server on localhost:57110
#-------------------------------------------------------------------------------
server = Server()

#-------------------------------------------------------------------------------
# Create an audio bus to route audio between two synths.
#-------------------------------------------------------------------------------
bus = AudioBus(server, 2)
synth = Synth(server, 'dust', { "out": bus })
reverb = Synth(server, 'reverb', { "in": bus, "out": 0 }, target=server, action=ADD_TO_TAIL)

parts = 10
try:
    while True:
    	parts_new = parts * random.uniform(0.1, 5)
    	print(parts_new)
    	synth.set("parts", parts_new)
    	time.sleep(3)
except KeyboardInterrupt:
    bus.free()
    synth.free()
    reverb.free()