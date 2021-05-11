"""[summary]
"""
import torch

from ..utils import Interpolator, JSONParser, Trajectory

class DataFactory():
    def __init__(self, directory="datasets"):
        self.json_parser = JSONParser()
        self.interpolator = Interpolator()

    def make_dataset(self, final_size, interpolation:str="linear", split=(80, 10, 10), num_workers=4,
                                device="cpu"):
        pass
