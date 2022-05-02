import gym

env = gym.make('FrozenLake-v1', is_slippery = False)

episode_number  = 5
timestep_number = 100

for episode in range(episode_number):
    observation = env.reset()

    for timestep in range(timestep_number):

        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done:
            env.render()
            print('Episode : {:02d} | Timestep : {:02d} | Rewards : {:02.0f}'.format(episode + 1, timestep + 1, reward))
            break

env.close()