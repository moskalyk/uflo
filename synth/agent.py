import torch as T
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim

import numpy as np
import random
import time

class PolicyNetwork(nn.Module):
	def __init__(self, lr, input_dims, fc1_dims, fc2_dims, n_actions):
		super(PolicyNetwork, self).__init__()

		self.input_dims = input_dims
		self.lr = lr
		self.fc1_dims = fc1_dims
		self.fc2_dims = fc2_dims
		self.n_actions = n_actions
		self.fc1 = nn.Linear(*self.input_dims, self.fc1_dims)
		self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
		self.fc3 = nn.Linear(self.fc2_dims, self.n_actions)
		self.optimizer = optim.Adam(self.parameters(), lr=lr)
		self.device = T.device('cuda' if T.cuda.is_available() else 'cpu')
		print('Using device:', self.device)
		self.to(self.device)

	def forward(self, obs):
		state = T.Tensor(obs).to(self.device)
		x = F.relu(self.fc1(state))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)

		return x

class Agent(object):
	def __init__(self, lr, input_dims, gamma=0.99, n_actions=3, l1_size=256, l2_size=256):
		self.gamma = gamma

		self.reward_memory = []
		self.action_memory = []

		self.policy = PolicyNetwork(lr, input_dims, l1_size, l2_size, n_actions)

	def choose_action(self, obs):
		# print("obs")
		# print(obs)
		probabilites = F.softmax(self.policy.forward(obs))
		print('action_probs')
		print(probabilites)
		action_probs = T.distributions.Categorical(probabilites)
		print(action_probs.probs)
		action = action_probs.sample()

		# Added randomness
		r = random.random()
		print(r)

		item = action.item()

		if r > 0.5:
			print('SWITCH_IT_UP')
			r1 = random.random()
			if r1 > 0.66:
				action = T.tensor(0)
			elif r1 > 0.33 and r1 <= 0.66:
				action = T.tensor(1)
			else:
				action = T.tensor(2)


		print('ACTION')

		print(action)
		print(action.item())

		log_probs = action_probs.log_prob(action)
		self.action_memory.append(log_probs)

		return action.item()

	def store_rewards(self, reward):
		self.reward_memory.append(reward)

	def learn(self):
		self.policy.optimizer.zero_grad()
		G = np.zeros_like(self.reward_memory, dtype=np.float64)

		for t in range(len(self.reward_memory)):
			G_sum = 0
			discount = 1
			for k in range(t, len(self.reward_memory)):
				G_sum += self.reward_memory[k] * discount
				discount *= self.gamma
			G[t] = G_sum
		mean = np.mean(G)
		std = np.std(G) if np.std(G) > 0 else 1
		G = (G - mean) / std
		# print("G")
		# print (G)

		G = T.Tensor(G).to(self.policy.device)

		loss = 0

		for g, logprob in zip(G, self.action_memory):
			loss += -g * logprob

		loss.backward()
		self.policy.optimizer.step()

		self.action_memory = []
		self.reward_memory = []