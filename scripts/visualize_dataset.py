import argparse
import d4rl
import gym
import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_name', type=str, default='maze2d-umaze-v0')
    args = parser.parse_args()

    env = gym.make(args.env_name)
    
    dataset = env.get_dataset()
    if 'infos/qpos' not in dataset:
        # raise ValueError('Only MuJoCo-based environments can be visualized')
        qpos = dataset['observations'][:, :30]
        qvel = np.zeros_like(qpos)[:, :29]
    else:
        qpos = dataset['infos/qpos']
        qvel = dataset['infos/qvel']
    rewards = dataset['rewards']
    actions = dataset['actions']
    print(dataset['terminals'].shape[0] / dataset['terminals'].sum(), dataset['terminals'].sum())

    env.reset()
    env.set_state(qpos[0], qvel[0])
    for t in range(qpos.shape[0]):
        env.set_state(qpos[t], qvel[t])
        env.render()
