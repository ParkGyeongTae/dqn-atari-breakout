import gym

# 기본 내장 (CartPole)
env = gym.make('CartPole-v0')

# 새로운 에피소드 호출
env.reset()

for _ in range(1000):

    # 행동 이전 관찰값
    env.render()

    # 행동 이후 관찰값
    env.step(env.action_space.sample())

env.close()