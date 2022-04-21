import gym

env = gym.make('CartPole-v0')

env.reset()

for i in range(10):

    env.render()

    observation, reward, done, info = env.step(0)
    # observation, reward, done, info = env.step(1)

    print(observation, done)

    if done:
        break

env.close()


'''

import gym

env = gym.make('CartPole-v0')

# 에피소드 실행
env.reset()

# 10 timestep을 실행
for i in range(10):

    env.render()
    
    # 카트를 왼쪽으로만 밀었을 때
    observation, reward, done, info = env.step(0)

    # 카트를 오른쪽으로만 밀었을 때
    # observation, reward, done, info = env.step(1)

    print(observation, done)
    
    # 정상 범위를 벗어나면 done = True 다.
    if done:
        break

env.close()

# 결과
# [-0.02204866 -0.19100833 -0.00498798  0.24236873] False
# [-2.5868827e-02 -3.8605869e-01 -1.4060331e-04  5.3347415e-01] False
# [-0.03359    -0.58117867  0.01052888  0.82611275] False
# [-0.04521357 -0.776443    0.02705114  1.1220884 ] False
# [-0.06074243 -0.97190905  0.04949291  1.4231323 ] False
# [-0.08018062 -1.1676068   0.07795555  1.7308645 ] False
# [-0.10353275 -1.3635277   0.11257284  2.046749  ] False
# [-0.1308033  -1.5596104   0.15350783  2.372038  ] False
# [-0.16199552 -1.7557245   0.20094858  2.7077043 ] False
# [-0.19711    -1.9516525   0.25510266  3.0543644 ] True

'''