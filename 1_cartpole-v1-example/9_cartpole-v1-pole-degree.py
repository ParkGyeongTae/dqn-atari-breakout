import gym
import random

env = gym.make('CartPole-v1')

max_time_step = 100

observation = env.reset()

for time_step in range(max_time_step):

    env.render()

    if observation[2] > 0:
        action = 1
    elif observation[2] < 0:
        action = 0
    else:
        action = random.randrange(0, 2)

    observation, reward, done, info = env.step(action)
    print(observation, done)

    if done:
        print("Max Time Step :", time_step + 1)
        break

env.close()

'''

import gym

env = gym.make('CartPole-v1')

# 에피소드 실행
observation = env.reset()

# 100 timestep
for i in range(100):

    # GUI로 현재 진행상황을 출력
    env.render()
    
    # 막대가 오른쪽으로 기울었으면
    # 카트를 오른쪽으로 밀기
    if observation[2] > 0:
        action = 1

    # 막대가 왼쪽으로 기울었으면
    # 카트를 왼쪽으로 밀기
    else:
        action = 0

    observation, reward, done, info = env.step(action)
    print(observation, done)

    if done:
        print(i + 1)
        break

env.close()

'''