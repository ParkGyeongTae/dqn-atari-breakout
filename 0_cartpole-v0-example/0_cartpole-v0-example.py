import gym

env = gym.make('CartPole-v0')

env.reset()

for i in range(500):

    env.render()
    env.step(env.action_space.sample())

env.close()

'''

import gym
env = gym.make('CartPole-v0')

# 새로운 에피소드를 시작
env.reset()

# 500 이라는 시간 동안 (약 10초 정도)
for i in range(500):

    # 행동 이전 관찰값
    env.render()

    # 행동 이후 관찰값
    env.step(env.action_space.sample())

# 환경 종료
env.close()

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

'''