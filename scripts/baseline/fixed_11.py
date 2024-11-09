"""
Baseline solution consisting of cycling through all phases with a fixed duration.
"""

import numpy as np
from tlrl.sim.env import SumoEnv

env = SumoEnv(
    network="sumo/eval/0/intersection.net.xml",
    config="sumo-env.cfg",
    render=True,
    verbose=False,
    rnd_seed=58736,
)
env.reset()

# Constant uniform length cycling
info = env.cycle(11)
disutility_sums.append(info["disutility_sum"])
disutility_avgs.append(info["disutility_avg"])
print("total reward:", sum(env.reward))
print("episode disutility:", info["disutility_sum"])
print("vehicle disutility:", info["disutility_avg"])
