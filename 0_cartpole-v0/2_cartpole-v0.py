# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

import gym

env = gym.make('CartPole-v0')
observation = env.reset()

# 게임 환경에서 선택할 수 있는 행동
action = env.action_space.sample()

print(action)

# 결과
# 0 or 1
# 0 또는 1을 출력