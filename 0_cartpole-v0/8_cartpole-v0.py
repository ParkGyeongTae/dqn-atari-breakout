import gym
# from gym.wrappers import Monitor

env = gym.make('CartPole-v0')
env.reset()

for i in range(10):
    env.render()

    # 왼쪽으로만 밀기 action = 0
    observation, reward, done, info = env.step(0)

    # 오른쪽으로만 밀기 action = 1
    # observation, reward, done, info = env.step(1)
    
    print(observation, done)
    if done:
        break

env.close()