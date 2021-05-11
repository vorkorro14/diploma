from warnings import warn

class Trajectory:
    def __init__(self):
        self._servos = []

    def servos(self):
        return self._servos

    def add_servos(self, new_servos:list):
        assert all([isinstance(servo, str) for servo in new_servos]), \
            'Servo name must be str'
        for servo in new_servos:
            if not servo in self._servos:
                self._servos.append(servo)
            else:
                warn(f'Servo {servo} is already in trajectory')
            
    def servo_trajectories(self):
        pass

    def poses(self):
        pass