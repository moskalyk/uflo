

from agent import Agent

import numpy as np
import random
import time

action_set = [
	"INCREASE_PARAM",
	"DECREASE_PARAM",
	"SAME_PARAM",
]

DATA_LOCATION = "/home/vgrok/Projects/neuro-club/neuro-analysis/raw_data/"

sound_params = {
	0 : {
		"type": "dust",
		"dev": 0.1,
		"param": "parts",
		"default": 3,
		"other": {}
	},
	1 : {
		"type": "noise",
		"dev": 0.1,
		"param": "osc",
		"default": 0.2,
		"other": {},
	},
	2 : {
		"type":"pulse",
		"dev": 0.1,
		"param": "freq",
		"default": 240,
		"other": {}
	},
	3 : {
		"type": "sine",
		"dev": 0.1,
		"param": "freq",
		"default": 240,
		"other": {}
	},
	4 : {
		"type": "bin",
		"dev": 0.1,
		"param": "diff",
		"default": 7.43,
		"other": {}
	}
}

# ~delta = 1; // 0.5 - 2. deep sleep, unsconsciousness
# ~theta = 5.5; // 4 - 7. Meditative, drowsy, sleeping. Memory, spatial learning
# ~mu = 9; // 9 - 11. associated with voluntary movement
# ~alpha = 10; // 7.5 - 12.5. Relaxed states of mind
# ~beta1 = 14; // 12.5 - 16. Normal waking consciousness
# ~beta2 = 18; // 16.5 - 20.
# ~beta3 = 24; // 20.5 - 28
# ~gamma = 35; // 32 - 100. Visual awareness, transcendental mental states

# // extra bonus vibrations:
# ~schumann1 = 7.83;
# ~schumann2 = 14.3;
# ~schumann3 = 20.8;
# ~schumann4 = 27.3;
# ~schumann5 = 33.8;

freqs = [
	1,
	5.5,
	7.83,
	9,
	14.3,
	10,
	14,
	18
]

from supercollider import Server, Synth, Buffer, AudioBus, ADD_TO_TAIL, Group
import time
import random
from matplotlib import pyplot as plt
import socketio

n_episodes = 4
episode_length = 2 


# TODO: include in a MeatSpace variable and instantiate in MindSpace
fnirs_buffer = [0,0,0,0,0]
fnirs_total = []
observeration_window = 20

sio = socketio.Client()
sio.connect('http://localhost:3002')

server = Server()

def send_ping():
    global start_timer
    start_timer = time.time()
    sio.emit('ping_from_client')


@sio.event
def connect():
    print('connected to server')
    send_ping()

@sio.event
def chat_message(sid):
    # print("message ", sid)
    # print(sid['data'])
    fnirs_buffer.append(sid['data'])
    # print("message ", data)

@sio.event
def pong_from_server(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    sio.sleep(1)
    send_ping()

# NeuronSpace() // Options parameters

class BandSpace(object):

	def __init__(self, actions, experiment_name='ex'):
		# self.agent = Agent(lr = 0.01, input_dims=[5], gamma= 0.99, n_actions=actions, l1_size = 128, l2_size = 128) 
		self.band_history_scores = []
		score = 0
		self.mind_env = MindSpace()
		self.bands = []
		self.experiment_name = experiment_name


	def compose(self):
		while 1:
			time.sleep(2)
			print("composing...")
		# get all params and add sounds in sequence based on normalized weights


	def clear_band_space(self):
		self.mind_env.clear_band_connections()

		# print 
		print('Scores')
		print(self.band_history_scores)
		print(fnirs_buffer)

		if(len(fnirs_buffer) > 5 ):
		# Save
			np.savetxt(DATA_LOCATION + self.experiment_name + '.csv', np.array(fnirs_buffer).astype(np.float), delimiter=',')

		# np.savetxt('test.out', x, delimiter=',')

		# plot
		plt.plot(np.hstack(self.band_history_scores))
		plt.savefig('plot_rewards.png')
		plt.figure()
		plt.plot(np.array(fnirs_buffer[5:], dtype=float))
		plt.savefig('plot_fnirs.png')

	def new_band(self, band_idx):
		print('New Band with index ' + str(band_idx))
		self.mind_env.learn_new_sound(band_idx)

		agent = Agent(lr = 0.1, input_dims=[20], gamma= 0.99, n_actions=3, l1_size = 128, l2_size = 128) 

		score_history = []
		score = 0

		for i in range(n_episodes):
			print('episode: ', i, "score %.f" % score)
			done = False
			score = 0

			# get observation
			observeration = self.mind_env.reset() 

			while not done:

				action = agent.choose_action(observeration)
				observeration_, reward, done = self.mind_env.step(action)

				agent.store_rewards(reward)
				observeration = observeration_
				score += reward

			score_history.append(score)
			agent.learn()
			print('learning...')

			print("self.env.is_steady")
			print(self.mind_env.is_steady)

			if self.mind_env.is_steady:
				break


		print('Proceeding to next band')
		print(score_history)
		self.band_history_scores.append(score_history)
		self.mind_env.reset_steady_state()
		print(self.mind_env.is_steady)

		return 


class MindSpace(object):

	def __init__(self, episode_length = episode_length, observation_time_delay = 2, steady_count_max = 4):

		self.sound_space = SoundSpace()
		self.possibleActions = action_set
		self.history = [0]
		self.episode_count = 0
		self.episode_length = episode_length
		self.observation_time_delay = observation_time_delay
		self.is_steady = False
		self.steady_count = 0
		self.steady_count_max = steady_count_max
		# self.sound_space.add_ban


	def learn_new_sound(self, sound_idx):
		self.sound_space.add_sound(sound_idx)

	def clear_band_connections(self):
		self.sound_space.clear_all_synths()

	def step(self, action_idx):

		# print("Performing Action")
		# print(action_set[action])
		# Perform some action

		self.sound_space.perform_action(action_set[action_idx])
		# self.sound_space.perform_action(action_set[action_idx], "freq")
		if action_set[action_idx] == "SAME_PARAM":
			self.steady_count += 1
			print("Steady Count: ", self.steady_count)
			print(self.is_steady)
			print(self.steady_count)
			print(self.steady_count_max)

		if self.steady_count == self.steady_count_max:
			self.is_steady = True
			print('is Steady')

		# sio.wait()
		# print(sio.wait())
		time.sleep(self.observation_time_delay)

		obs = self.get_observation()
		reward = self.calculate_reward(obs)

		# increment episode
		self.episode_count += 1
		# print('episode count')
		# print(self.episode_count)
		print('Reward')
		print(reward)

		done = False

		if self.episode_count > self.episode_length or self.is_steady:
			done = True


		return obs, reward, done

	def reset_steady_state(self):
		self.is_steady = False
		self.steady_count = 0
	
	def reset(self):
		self.episode_count = 0

		return self.get_observation()

	def get_observation(self, window = observeration_window):


		# TODO: convolve inputs
		# obs = [random.random() for i in range(window)]
		obs = fnirs_buffer[-window:]
		parsed_obs = []

		for i in range(window):
			# print(obs)
			parsed_obs.append(obs)

		return np.array(obs).astype(np.float)

	def calculate_reward(self, seq):

		# compute reward, can apply various heuristics here
		x = np.mean(seq)
		y = np.mean(self.history[-1])
		self.history.append(seq)
		
		if x <= y:
			# return 1 
			print('------------------')
			print(x)
			print(y)
			print(x - y)
			print("reward: ", (5.0 * (y - x)))
			return (5.0 * (y - x)) # play with reward heuristics
		else:
			return -10

		# return 100


class SoundSpace(object):
	def __init__(self):
		self.freq = 440
		self.parts = 10

		self.group = Group(server)
		# self.synth = Synth(server, "sine", { "freq" : self.freq, "gain" : -12.0 }, target=self.group)
		self.mul = 0.1
		self.bus = AudioBus(server, 2)
		self.synth_index = -1

		self.synth = None
		self.synths = []

	def add_sound(self, index = -1):
		print('ADDING_SOUND')

		self.synth_index = index
		synth = None

		params = sound_params[index]

		if index is 0:

			print('playing sound index ' + str(index))
			print(params['type'])
			synth = Synth(server, params['type'], { "out": self.bus }, target=self.group)
			synth.set("parts", 5)
			reverb = Synth(server, 'reverb', { "in": self.bus, "out": 0 }, target=self.group, action=ADD_TO_TAIL)
		elif index is 4: # TODO: only for custom sounds

			print('playing custom sound')

			opts = {}
			
			opts[params['param']] = params['default']
			# if == 
			opts['gain'] = 0.5

			synth = Synth(server, params['type'], opts, target=self.group)

		else:
			print('playing sound index ' + str(index))

			opts = {}
			opts["osc"] = 0.2
			
			opts[params['param']] = params['default']

			# customized for the sine sound
			if index is 3:
				opts['gain'] = 0.2
			else:
				opts['gain'] = 0.5


			synth = Synth(server, params['type'], opts, target=self.group)

			
		self.synths.append(synth)
		self.synth = synth

	def clear_all_synths(self):
		print("Freeing group")
		self.group.free()

	def perform_action(self, action):
		print("performing action")
		print(self.synth_index)

		sound = sound_params[self.synth_index]
		dev = sound['dev']
		param = sound['param']
		default = sound['default']

		if action == "INCREASE_PARAM":

			# get old param
			old_param = self.synth.get(param)

			# update param
			new_param = old_param * (1 + dev)

			print("checking_max")

			if not new_param > default * 1.5:
				# if new_param > default

				print('Setting ' + param + " to " + str(new_param) + " from " + str(old_param))
				# set param
				self.synth.set(param, new_param)


			# # parts_new = self.parts * random.uniform(0.1, 5)
			# parts_new = self.parts * self.parts*(1 + self.mul)

			# # self.freq = self.freq*(1 + self.mul)
			# # self.synth.set(param, parts_new)
			# old_osc = self.synth.get("osc")
			# print("old_osc")
			# old_osc = old_osc if old_osc is not None else 0

			# print(old_osc)
			# print(self.synth.get("osc"))
			# print(random.uniform(1 - dev, 1 + dev))

			# new_osc = old_osc * random.uniform(1 - dev, 1 + dev)
			
			# print(new_osc)

			# self.synth.set("osc", new_osc)
			# self.synth.set("gain", new_osc)

			print("( + ) INCREASE_PARAM")
			# self.group.free()

		elif action == "DECREASE_PARAM":

			# get old param
			old_param = self.synth.get(param)

			# update param
			new_param = old_param * (1 - dev)

			print("checking_min")
			if not new_param < default * 1.5:

				print(new_param > default * 1.5)

				print('Setting ' + param + " to " + str(new_param) + " from " + str(old_param))

			# set param
				self.synth.set(param, new_param)

			# parts_new = self.parts * self.parts*(1 - self.mul)

			# # self.freq = self.parts * self.parts*(1 - self.mul)
			# # self.synth.set(param, self.freq)
			# old_osc = self.synth.get("osc")
			# print("old_osc")
			# old_osc = old_osc if old_osc is not None else 0
			# print(old_osc)
			# print(self.synth.get("osc"))
			# print(random.uniform(1 - dev, 1 + dev))

			# new_osc = old_osc * random.uniform(1 - dev, 1 + dev)
			# print(new_osc)
			# self.synth.set("osc", new_osc)
			# self.synth.set("gain", new_osc)

			print("( - ) DECREASE_PARAM")
			# self.group.free()

		elif action == "SAME_PARAM":
			# self.freq = self.freq*(1 - self.mul)
			# self.synth.set(param, self.freq)

			print("( = ) SAME_PARAM")
			# self.group.free()

		# if action == "INCREASE_PARAM":
		# 	# parts_new = self.parts * random.uniform(0.1, 5)
		# 	parts_new = self.parts * self.parts*(1 + self.mul)

		# 	# self.freq = self.freq*(1 + self.mul)
		# 	# self.synth.set(param, parts_new)
		# 	old_osc = self.synth.get("osc")
		# 	print("old_osc")
		# 	old_osc = old_osc if old_osc is not None else 0

		# 	print(old_osc)
		# 	print(self.synth.get("osc"))
		# 	print(random.uniform(1 - dev, 1 + dev))

		# 	new_osc = old_osc * random.uniform(1 - dev, 1 + dev)
			
		# 	print(new_osc)

		# 	self.synth.set("osc", new_osc)
		# 	self.synth.set("gain", new_osc)

		# 	print("( + ) INCREASE_PARAM")
		# 	# self.group.free()

		# elif action == "DECREASE_PARAM":

		# 	parts_new = self.parts * self.parts*(1 - self.mul)

		# 	# self.freq = self.parts * self.parts*(1 - self.mul)
		# 	# self.synth.set(param, self.freq)
		# 	old_osc = self.synth.get("osc")
		# 	print("old_osc")
		# 	old_osc = old_osc if old_osc is not None else 0
		# 	print(old_osc)
		# 	print(self.synth.get("osc"))
		# 	print(random.uniform(1 - dev, 1 + dev))

		# 	new_osc = old_osc * random.uniform(1 - dev, 1 + dev)
		# 	print(new_osc)
		# 	self.synth.set("osc", new_osc)
		# 	self.synth.set("gain", new_osc)

		# 	print("( - ) DECREASE_PARAM")
		# 	# self.group.free()

		# elif action == "SAME_PARAM":
		# 	# self.freq = self.freq*(1 - self.mul)
		# 	# self.synth.set(param, self.freq)

		# 	print("( = ) SAME_PARAM")
		# 	# self.group.free()


		# elif action == "DECREASE_VOLUME":
		# 	print("DECREASE_VOLUME")
			
		# elif action == "INCREASE_VOLUME":
		# 	print("INCREASE_VOLUME")
