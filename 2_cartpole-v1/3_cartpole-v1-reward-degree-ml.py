from keras.models                import Sequential
from keras.layers                import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

import gym
import random

# max_time_step   = 100
# episode_numbers = 5

# for episode in range(episode_numbers):

#   observation = env.reset()
#   rewards = 0

#   for time_step in range(max_time_step):

#     env.render()

#     if observation[2] > 0:
#       action = 1
#     elif observation[2] < 0:
#       action = 0
#     else:
#       action = random.randrange(0, 2)

#     observation, reward, done, info = env.step(action)

#     rewards += reward

#     if done:
#       print("episode :", episode + 1, ", rewards :", rewards)
#       break

# env.close()


def data_preparation(episode_numbers, choise_numbers, f, render = False):
  game_data = []

  for episode in range(episode_numbers):

    score = 0
    game_steps = []
    observation = env.reset()

    for step in range(max_time_step):
      if render:
        env.render()

      action = f(observation)
      game_steps.append((observation, action))
      observation, reward, done, info = env.step(action)
      score += reward

      if done:
        print("episode :", episode + 1, ", score :", score)
        break

    game_data.append((score, game_steps))
  
  game_data.sort(key = lambda s:-s[0])
  
  training_set = []

  for i in range(choise_numbers):
    for step in game_data[i][1]:
      if step[1] == 0:
        training_set.append((step[0], [1, 0]))
      else:
        training_set.append((step[0], [0, 1]))

  if render:
    for i in game_data:
      print("Score: {0}".format(i[0]))
  
  return training_set

# 모델 구축
def build_model():

  model = Sequential()
  model.add(Dense(128, input_dim = 4, activation = 'relu'))
  model.add(Dense(52, activation = 'relu'))
  model.add(Dense(2, activation = 'softmax'))
  model.compile(loss='mse', optimizer = Adam())

  return model

# 모델 학습
def train_model(model, training_set):

  X = np.array([i[0] for i in training_set]).reshape(-1, 4)
  y = np.array([i[1] for i in training_set]).reshape(-1, 2)
  model.fit(X, y, epochs = epochs_numbers)

def predictor(s):
  return np.random.choice([0, 1], p = model.predict(s.reshape(-1, 4))[0])

# 메인
env = gym.make('CartPole-v1')

episode_numbers = 1000
choise_numbers  = 50
max_time_step   = 200
epochs_numbers  = 100

model = build_model()
training_data = data_preparation(episode_numbers, choise_numbers, lambda random_action: random.randrange(0, 2))
train_model(model, training_data)

data_preparation(10, 1, predictor, True)