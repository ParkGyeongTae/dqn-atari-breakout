import gym

import numpy as np
import random
import matplotlib.pyplot as plt

# 모두 같은 값이면 random하게 가고, 큰값이면 큰값으로 이동하는 함수
def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return random.choice(indices)

env = gym.make('FrozenLake-v1', is_slippery = False)

# 16, 4
Q_Table = np.zeros([env.observation_space.n, env.action_space.n])

episode_number = 2000

rList = []

for episode in range(episode_number):

    # 환경 초기화
    state = env.reset()
    rAll = 0
    done = False
    
    while not done:

        # 처음에 다 0이면 랜덤하게 가고, 큰값이 있으면 큰값으로 이동
        action = rargmax(Q_Table[state, :])

        # 실행
        new_state, reward, done, info = env.step(action)

        # Q 업데이트
        Q_Table[state, action] = reward + np.max(Q_Table[new_state, :])
        rAll += reward
        state = new_state

    rList.append(rAll)

print('성공률 :', str(sum(rList) / episode_number))
print('Q-테이블')
print('LEFT DOWN RIGHT UP')
print(Q_Table)

plt.bar(range(len(rList)), rList, color = 'red')
plt.show()