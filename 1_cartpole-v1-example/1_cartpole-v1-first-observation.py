import gym

env = gym.make('CartPole-v1')

first_observation = env.reset()

print('first_observation : ', first_observation)

'''

import gym

env = gym.make('CartPole-v1')

# 첫 관찰값
first_observation = env.reset()

print(first_observation)

# 결과
#  [카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율]
# [0.00803868 -0.01096694 -0.02077952 -0.00761259]

'''