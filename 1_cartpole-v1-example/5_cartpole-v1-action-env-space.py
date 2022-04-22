import gym

env = gym.make('CartPole-v1')

print('action_space           : ', env.action_space)
print('observation_space      : ', env.observation_space)

print('observation_space.high : ', env.observation_space.high)
print('observation_space.low  : ', env.observation_space.low)

'''

import gym

env = gym.make('CartPole-v1')

# 행동 공간
print('action_space           : ', env.action_space)
# 환경 공간
print('observation_space      : ', env.observation_space)

# 환경의 최대값
print('observation_space.high : ', env.observation_space.high)
# 환경의 최소값
print('observation_space.low  : ', env.observation_space.low)

# 결과
# action_space           :  Discrete(2)
# observation_space      :  Box([-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38], [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38], (4,), float32)
# observation_space.high :  [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
# observation_space.low  :  [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]

# Discrete = 고정된 범위의 음이 아닌 숫자를 허용하는 공간
# Box = n-차원의 박스, 유효 관찰값은 4개 숫자의 배열

'''