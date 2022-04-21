import gym

env = gym.make('CartPole-v0')
observation = env.reset()
print(observation)

observation, reward, done, info = env.step(0)
print(observation)

env.close()


'''

import gym

env = gym.make('CartPole-v0')

# 에피소드 실행
observation = env.reset()

# 처음 관찰값
print(observation)

# 0이라는 행동을 실행
observation, reward, done, info = env.step(0)

# 행동 이후 관찰값
print(observation)

env.close()

# 결과
# [0.00967408  0.04968553 -0.01428431 -0.00555329]
# [0.01066779 -0.14522868 -0.01439537  0.28258875]

'''