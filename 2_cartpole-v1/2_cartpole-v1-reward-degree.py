import gym
import random

env = gym.make('CartPole-v1')

max_time_step   = 100
episode_numbers = 5

for episode in range(episode_numbers):

  observation = env.reset()
  rewards = 0

  for time_step in range(max_time_step):

    env.render()

    if observation[2] > 0:
      action = 1
    elif observation[2] < 0:
      action = 0
    else:
      action = random.randrange(0, 2)

    observation, reward, done, info = env.step(action)

    rewards += reward

    if done:
      print("episode :", episode + 1, ", rewards :", rewards)
      break

env.close()