import gym
import random

env = gym.make('CartPole-v1')

max_time_step = 100

observation = env.reset()

for i in range(max_time_step):

  env.render()

  observation, reward, done, info = env.step(random.randrange(0, 2))

  if done:
    break

env.close()