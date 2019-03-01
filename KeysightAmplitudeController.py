import time

import visa

from Agilent33220A import Agilent33220A
from VolumeController import VolumeController


class KeysightAmplitudeController():
    def __init__(self, desired_rms, min_voltage, max_voltage):
        self.min_voltage = min_voltage
        self.max_voltage = max_voltage
        self.voltage_controller = VolumeController(desired_rms)
        self.scope = Agilent33220A()



    def autolevel(self,running):
        while running == True:
            pid_value = next(self.voltage_controller)  # convert from 0-10 to 0-1
            voltage = min(self.max_voltage,pid_value * (self.max_voltage - self.min_voltage) + self.min_voltage)
            print('VOLTage %f' % voltage)
            self.scope.write('VOLT %f' % voltage)
            time.sleep(0.1)


