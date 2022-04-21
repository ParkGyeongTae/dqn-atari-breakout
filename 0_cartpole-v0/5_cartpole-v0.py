# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

import gym

env = gym.make('CartPole-v0')

# action_space = 임의의 행동 공간
print(env.action_space)
# observation_space = 임의의 환경 공간
print(env.observation_space)

# 환경의 최대값
print(env.observation_space.high)
# 환경의 최소값
print(env.observation_space.low)

# 결과
# Discrete(2)
# Box([-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38], [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38], (4,), float32)

# Discrete = 고정된 범위의 음이 아닌 숫자를 허용하는 공간
# Box = n-차원의 박스, 유효 관찰값은 4개 숫자의 배열