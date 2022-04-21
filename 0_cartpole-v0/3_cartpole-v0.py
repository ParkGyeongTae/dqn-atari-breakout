# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

import gym

env = gym.make('CartPole-v0')
observation = env.reset()
action = env.action_space.sample()

# action을 선택했을 때 (observation, reward, done, info)
step = env.step(action)

print('observation : ', observation)
print('action : ', action)
print('step : ', step)

print('1st observation : ', observation)
print('action : ', action)
print('2nd observation : ', step[0])

# 결과
# bservation :  [-0.04539993  0.00742055 -0.04888416 -0.03482315]
# action :  0
# step :  (array([-0.04525152, -0.18696754, -0.04958062,  0.24204445], dtype=float32), 1.0, False, {})

# 1st observation :  [-0.04539993  0.00742055 -0.04888416 -0.03482315]
# action :  0
# 2nd observation :  [-0.04525152 -0.18696754 -0.04958062  0.24204445]
