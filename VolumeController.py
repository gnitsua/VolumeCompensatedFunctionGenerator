import numpy as np
from simple_pid import PID

from MicrophoneManager import MicrophoneManager


class VolumeController():
    def __init__(self, desired_rms):
        self.microphone = MicrophoneManager(32000)
        self.desired_rms = desired_rms
        # self.pid = PID(0.05, 0, 0.1, setpoint=1)
        self.pid = PID(0.3, 0, 0, setpoint=1)
        self.pid.output_limits = (0, 10)

    def __iter__(self):
        return self

    def __next__(self):
        raw_data = next(self.microphone)

        try:
            rms = np.mean(np.abs(raw_data))
        except ValueError:
            rms = 0

        scale_value = self.pid(rms / self.desired_rms)
        print(rms,rms / self.desired_rms)
        return scale_value
