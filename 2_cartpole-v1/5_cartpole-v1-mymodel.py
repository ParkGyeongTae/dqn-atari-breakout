import gym 
import random 
import math 
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('CartPole-v1')

model = torch.load('model.pt')
# print(model)
# exit()

max_time_step   = 500
episode_numbers = 50
random_action   = random.randrange(0, 2)

# self.model(states)
# model.load_state_dict(torch.load('model.pt'))
# print(model.load_state_dict(torch.load('model.pt')))

for episode in range(episode_numbers):

  observation = env.reset()
  rewards = 0

  for time_step in range(max_time_step):

    # env.render()

    q_value = model(torch.FloatTensor([observation]))

    # print(torch.argmax(q_value).item())
    # exit()

    # print(q_value)

    observation, reward, done, info = env.step(torch.argmax(q_value).item())

    rewards += reward

    if done:
      print("episode :", episode + 1, ", rewards :", rewards)
      break

env.close()