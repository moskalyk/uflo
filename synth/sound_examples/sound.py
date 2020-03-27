from supercollider import Server, Synth, Buffer, AudioBus, ADD_TO_TAIL, Group
import time
import random

server = Server()

# for i in range(10):
# 	time.sleep(2)
# 	freq = 440.0 + i*100
# 	print(freq)


# 	synth = Synth(server, "sine", { "freq" : freq, "gain" : -12.0 })
# 	synth.set("freq", freq)

# freq = 440
# # group = Group(server)
# synth = Synth(server, "sine", { "freq" : freq, "gain" : -12.0 })
# synth.set("freq", freq)


# # range_set = .1
freq = 440

try:
    synth = Synth(server, "sine", { "freq" : 440.0, "gain" : -18.0 })
    print("Created synth")
    # print("Frequency: %.1f" % synth.get("freq"))
    while True:
        time.sleep(1)
        synth.set("freq", freq * random.uniform(0.90, 1.1))
except KeyboardInterrupt:
    synth.free()
    print("Freed synth")


# range_set = .1
osc = 1
dev = 0.5

try:
    synth = Synth(server, "noise", { "osc" : 1, "gain": 0.1 })
    print("Created synth")
    # print("Frequency: %.1f" % synth.get("freq"))
    while True:
        time.sleep(2)
        
        new_osc = osc * random.uniform(1 - dev, 1 + dev)
        print(new_osc)
        synth.set("osc", new_osc)
        synth.set("gain", new_osc)

except KeyboardInterrupt:
    synth.free()
    print("Freed synth")


# range_set = .1
osc = 1
dev = 0.5
freq = 440

try:
    synth = Synth(server, "pulse", { "osc" : 0.5, "freq": freq })
    print("Created synth")
    # print("Frequency: %.1f" % synth.get("freq"))
    while True:
        time.sleep(2)
        new_osc = osc * random.uniform(1 - dev, 1 + dev)
        print(new_osc)
        synth.set("osc", new_osc)
        synth.set("freq", freq * random.uniform(1 - dev, 1 + dev))

except KeyboardInterrupt:
    synth.free()
    print("Freed synth")



parts = 10

try:
	bus = AudioBus(server, 2)
	group = Group(server)

	synth4 = Synth(server, 'dust', { "out": bus }, target=group)
	reverb = Synth(server, 'reverb', { "in": bus, "out": 0 }, target=group, action=ADD_TO_TAIL)

	synth1 = Synth(server, "sine", { "freq" : 440.0, "gain" : -18.0 }, target=group)
	synth2 = Synth(server, "pulse", { "osc" : 0.5, "freq": freq }, target=group)
	synth3 = Synth(server, "noise", { "osc" : 1, "gain": 0.1 }, target=group)

	while True:
		parts_new = parts * random.uniform(0.1, 5)
		print(parts_new)
		synth4.set("parts", parts_new)
		time.sleep(3)
except KeyboardInterrupt:
    synth1.free()
    synth2.free()
    synth3.free()
    synth4.free()
    reverb.free()
    print("Freed group")

