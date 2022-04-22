import gym

env = gym.make('CartPole-v1')

env.reset()
action = env.action_space.sample()

print(action)

'''

import gym

env = gym.make('CartPole-v1')

# 새로운 에피소드 시작
env.reset()

# 게임 환경에서 선택할 수 있는 행동
action = env.action_space.sample()

print(action)

# 실행시 0과 1을 반복 -> 할 수 있는 행동은 0 또는 1이구나..

'''