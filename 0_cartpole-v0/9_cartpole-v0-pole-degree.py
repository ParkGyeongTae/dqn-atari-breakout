import gym

env = gym.make('CartPole-v0')
observation = env.reset()

for i in range(100):

    env.render()

    if observation[2] > 0:
        action = 1
    else:
        action = 0

    observation, reward, done, info = env.step(action)
    print(observation, done)

    if done:
        print(i+1)
        break

env.close()

'''

import gym

env = gym.make('CartPole-v0')

# 에피소드 실행
observation = env.reset()

# 100 timestep
for i in range(100):

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