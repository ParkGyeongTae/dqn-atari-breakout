# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

import gym

env = gym.make('CartPole-v0')

# 첫 관찰값
observation = env.reset()

print(observation)

# 결과
# [카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율]
# [-0.0497234  -0.03475072  0.04795611  0.04663042]