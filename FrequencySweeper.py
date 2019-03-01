import csv
import time

from Agilent33220A import Agilent33220A


class FrequencySweeper():
    """
    This class is designed to read a csv and perform a linearly interpolated sweep between the values.
    Input file should be of the form, where time is the time in millisecond

    Time1,Frequency1,Voltage1
    Time2,Frequency2,Voltage2
    .
    .
    .
    TimeN,FrequencyN,Voltage3



    """

    def __init__(self, filename, scope=None):
        try:
            self.file = csv.reader(open(filename, "r"), delimiter=',')
            if (scope == None):  # no scope object provide, so let's create one
                self.scope = Agilent33220A()
        except FileNotFoundError:
            print("file not found")
        except Exception as e:
            raise e  # not sure what is going to be thrown yet

    def start(self):
        start = time.time()  # convert to string so the time and the csv data are the same type
        self.scope.write("OUTP ON")
        self.scope.write("FUNC SIN")
        for point in self.file:
            assert (len(point) == 3)
            try:
                current_time = int(point[0])/1000
                frequency = int(point[1])
                amplitude = float(point[2])
                while (time.time() - start) < current_time:
                    time.sleep(0.001)
                self.scope.write("FREQ %i"%(frequency))
                self.scope.write("VOLT %i"%(amplitude))
            except ValueError:
                raise AssertionError("file is invalid")

        self.scope.write("OUTP OFF")
