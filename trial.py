import numpy as np
#from envs.d4rl_envs import KitchenEnv
from d4rl.kitchen.kitchen_envs import KitchenBase
import imageio

env = KitchenBase()
obs = env.reset()
imgs = []
for i in range(150):
    imgs.append(env.render('rgb_array'))
    a = np.random.uniform(-1000,1000, 9)
    _= env.step(a)
imageio.mimsave('out.gif', imgs)


