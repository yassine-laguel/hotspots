from __future__ import print_function
import os
from concurrent import futures


def run(cmd):
    print(cmd)
    os.system(cmd)


data = '/home/pcurran/github_packages/hotspots/examples/2_docking/virtual_screening/akt1'
script = "virtual_screening.py"
weights = [0, 10, 100]

cmds = ["""python {} {} {}""".format(script, data, weight) for weight in weights]

with futures.ProcessPoolExecutor(max_workers=3) as executor:
    executor.map(run, cmds)