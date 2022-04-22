import gym

env = gym.make('CartPole-v1')

observation = env.reset()
action = env.action_space.sample()
step = env.step(action)

print('observation : ', observation)
print('action      : ', action)
print('step        : ', step)

'''

import gym

env = gym.make('CartPole-v1')

# 에피소드 시작
observation = env.reset()

# 임의의 행동 실행
action = env.action_space.sample()

# step : action을 실행했을 때의 결과 (observation, reward, done, info)
step = env.step(action)

print('first_observation : ', first_observation)
print('action            : ', action)
print('step              : ', step)

# 결과
# first_observation :  [0.03486872  0.04418433 -0.00933439  0.02904002]
# action            :  0
# step              :  (array([ 0.0357524 , -0.15080252, -0.00875359,  0.3187633 ], dtype=float32), 1.0, False, {})

'''