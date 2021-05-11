import os
import json

from .trajectory import Trajectory

class JSONParser():
    def __init__(self):
        pass

    def get_trajectory(self, json_file:str, directory:str=''):
        with open(os.path.join(directory, json_file), 'r') as file:
            raw_trajectory = json.load(file)
            trajectory = Trajectory()
            trajectory.add_servos(list(raw_trajectory.keys()).remove("remap"))
            for item in raw_trajectory.items():
                if not item[0] == 'remap':
                    pass
