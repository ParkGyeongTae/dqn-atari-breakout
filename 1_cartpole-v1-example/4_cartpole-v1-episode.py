import gym
# import random

env = gym.make('CartPole-v1')

episode_number  = 3
timestep_number = 100

for episode in range(episode_number):

  observation = env.reset()

  for timestep in range(timestep_number):

      env.render()

      print(observation)

      action = env.action_space.sample()
      # action = random.randrange(0, 2)
      observation, reward, done, info = env.step(action)

      if done:

          print('Max Timestep :', timestep + 1)
          break

env.close()



'''

import gym

env = gym.make('CartPole-v1')

# 5번의 에피소드를 진행
for episode in range(5):

  observation = env.reset()

  # 각 에피소드마다 100번의 timestep을 진행
  for t in range(100):

      env.render()

      print(observation)

      action = env.action_space.sample()
      observation, reward, done, info = env.step(action)

      # 실패하면 종료
      if done:

          print('Max Timestep :', t + 1)
          break

env.close()

# 결과
# [ 0.02180032 -0.04335631  0.03196771  0.03386761]
# [ 0.02093319 -0.23892175  0.03264506  0.3364628 ]
# [ 0.01615476 -0.04427921  0.03937431  0.0542505 ]
# [ 0.01526917 -0.23994297  0.04045932  0.3590917 ]
# [ 0.01047031 -0.04541883  0.04764116  0.07943609]
# [ 0.00956194 -0.24119021  0.04922988  0.38676116]
# [ 0.00473813 -0.43697518  0.0569651   0.6945506 ]
# [-0.00400137 -0.6328391   0.07085612  1.0046085 ]
# [-0.01665815 -0.8288322   0.09094828  1.3186748 ]
# [-0.0332348  -1.0249789   0.11732178  1.6383808 ]
# [-0.05373437 -0.8314116   0.1500894   1.3844393 ]
# [-0.07036261 -1.0280526   0.17777818  1.7200456 ]
# Max Timestep :  12

'''