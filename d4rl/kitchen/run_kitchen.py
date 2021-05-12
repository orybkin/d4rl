import gym
import d4rl
import cv2
#from envs.d4rl_envs import KitchenEnv
from d4rl.kitchen.kitchen_envs import KitchenMicrowaveV0
import imageio
from matplotlib import pyplot as plt

for ee_control_type in ['6dof', '3dof_gripper_rot', '3dof']:
    env = KitchenMicrowaveV0(control_mode='end_effector', ee_control_type= ee_control_type)

    env.reset()
    done = False
    imgs = []
    for i in range(150):
        a = env.action_space.sample()
        im = env.render(mode="rgb_array")
        o, r, d, i = env.step(a)
        imgs.append(im)
    imageio.mimsave('ctrl_type_'+str(ee_control_type)+'.gif', imgs)
