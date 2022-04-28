import gym
import random
import torch

env = gym.make('CartPole-v1')

model = torch.load('model.pt')

max_time_step   = 500
episode_numbers = 50
random_action   = random.randrange(0, 2)

for episode in range(episode_numbers):

  observation = env.reset()
  rewards = 0

  for time_step in range(max_time_step):

    # env.render()

    q_value = model(torch.FloatTensor([observation]))

    observation, reward, done, info = env.step(torch.argmax(q_value).item())

    rewards += reward

    if done:
      print("episode :", episode + 1, ", rewards :", rewards)
      break

env.close()