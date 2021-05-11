"""
    Motion Pipeline
    Copyright (C) 2021
    Vladimir Litvinenko
"""
import numpy as np
from scipy.interpolate import interp1d

from .trajectory import Trajectory


class Interpolator:
    """Interpolator for motions
    """
    def __init__(self, kind:str="linear"):
        assert kind in ("linear", "quadratic", "cubic"), \
               'kind parameter should be "linear", "quadratic" or "cubic"'
        self.kind = kind

    def interpolate(self, trajectory:Trajectory) -> Trajectory:
        interpolated_trajectory = Trajectory()
        interpolated_trajectory.add_servos(trajectory.servos())
        for servo in trajectory.servos():
            interpolated_trajectory[servo] = interp1d(trajectory[servo]["t"], trajectory[servo]["angle"], kind=self.kind)
        return np