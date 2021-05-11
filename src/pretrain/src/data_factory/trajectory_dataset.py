from torch.utils.data import Dataset

from ..utils import Trajectory

class TrajectoryDataset(Dataset):
    def __init__(self, trajectory:Trajectory):
        self.trajectory = trajectory

    def __len__(self):
        pass

    def __getitem__(self, key):
        pass
    