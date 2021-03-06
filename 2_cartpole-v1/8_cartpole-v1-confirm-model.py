import gym
import random
import math
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from collections import deque
import matplotlib.pyplot as plt

# 하이퍼 파라미터 정의
EPISODES = 1

EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200

GAMMA = 0.8

LR = 0.001
BATCH_SIZE = 32

class DQNAgent:

  def __init__(self):

    self.model = nn.Sequential(
      nn.Linear(4, 128),
      nn.ReLU(),
      nn.Linear(128, 2)
    )

    '''
    Sequential(
      (0): Linear(in_features=4, out_features=128, bias=True)
      (1): ReLU()
      (2): Linear(in_features=128, out_features=2, bias=True)
    )
    '''
    
    self.optimizer = optim.Adam(self.model.parameters(), LR)
    
    '''
    Adam (
    Parameter Group 0
        amsgrad: False
        betas: (0.9, 0.999)
        eps: 1e-08
        lr: 0.001
        maximize: False
        weight_decay: 0
    )
    '''

    self.steps_done = 0

    ''' 0 '''

    self.memory = deque(maxlen = 10000)

    ''' deque([], maxlen=10000) '''

  def memorize(self, state, action, reward, next_state):

    self.memory.append(
      (
        state,
        action,
        torch.FloatTensor(np.array(reward, ndmin = 1)),
        torch.FloatTensor(np.array(next_state, ndmin = 2))
      )
    )

  def act(self, state):

    eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1. * self.steps_done / EPS_DECAY)

    ''' timestep을 거듭할수록 0.9 부터 내려감 (같은 숫자로 감소) '''

    self.steps_done += 1

    ''' timestep을 거듭할수록 1부터 올라감 (1씩 증가) '''

    if random.random() > eps_threshold:
      return self.model(state).data.max(1)[1].view(1, 1)
    else:
      return torch.LongTensor([[random.randrange(2)]])

    '''
    만약, 0~1 랜덤한 숫자가 eps_threshold 보다 크면
    모델을 적용하고,
    그게 아니면,
    0과 1 랜덤한 숫자를 적용
    '''

  def learn(self):

    if len(self.memory) < BATCH_SIZE:
      return

    batch = random.sample(self.memory, BATCH_SIZE) 
    states, actions, rewards, next_states = zip(*batch)
    states = torch.cat(states)
    actions = torch.cat(actions)
    rewards = torch.cat(rewards)
    next_states = torch.cat(next_states)
    
    current_q = self.model(states).gather(1, actions)
    max_next_q = self.model(next_states).detach().max(1)[0]
    expected_q = rewards + (GAMMA * max_next_q)

    loss = F.mse_loss(current_q.squeeze(), expected_q)
    self.optimizer.zero_grad()
    loss.backward()
    self.optimizer.step()

env = gym.make('CartPole-v1')

agent = DQNAgent()
score_history = []

for e in range(1, EPISODES + 1):

  state = env.reset()
  steps = 0

  '''
  게임 초기화
  '''

  while True:
    state = torch.FloatTensor(np.array(state, ndmin = 2))
    action = agent.act(state)
    next_state, reward, done, info = env.step(action.item())

    if done:
      reward = -1

    agent.memorize(state, action, reward, next_state)
    agent.learn()
    state = next_state
    steps += 1

    if done:
      print("Eposide:{0} Score: {1}".format(e, steps))
      score_history.append(steps)
      break

    '''
    에피소드가 끝나면,
    에피소드 번호, 에피소드 점수를 출력하고,
    score_history 리스트에 steps를 추가
    '''

# torch.save(agent.model, 'model.pt')
# plt.plot(score_history)
# plt.ylabel('score')
# plt.show()