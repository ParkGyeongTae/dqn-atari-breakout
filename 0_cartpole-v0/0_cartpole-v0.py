# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

import gym

env = gym.make('CartPole-v0')

# 새로운 에피소드 호출
env.reset()

for _ in range(1000):

    # 행동 이전 관찰값
    env.render()

    # 행동 이후 관찰값
    env.step(env.action_space.sample())

env.close()