import gym
import random

env = gym.make('CartPole-v1')

max_time_step   = 100
episode_numbers = 10
random_action   = random.randrange(0, 2)

for episode in range(episode_numbers):

  observation = env.reset()
  rewards = 0

  for time_step in range(max_time_step):

    # env.render()
    observation, reward, done, info = env.step(random_action)

    rewards += reward

    if done:
      print("episode :", episode + 1, ", rewards :", rewards)
      break

env.close()