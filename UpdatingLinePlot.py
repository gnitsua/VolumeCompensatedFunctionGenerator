import matplotlib.pyplot as plt
import numpy as np
import math

class UpdatingLinePlot():
    def __init__(self, xmin = 0, xmax = 100, ymin = 0, ymax = 100, color="r",data_iterator=None):
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('close_event', self.handle_close)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim([xmin, xmax])
        self.ax.set_xlim([ymin, ymax])
        self.line1 = None
        self.data = data_iterator
        self.running = False

    def plot(self):
        if(self.data != None):
            self.running = True
            for chunk in self.data:
                if (self.running == True):
                    if(self.line1 == None):# first iteration
                        self.line1, = self.ax.plot(chunk, 'ro')
                    else:
                        self.line1.set_ydata(chunk)
                        plt.pause(0.00000001)
        else:
            pass #default to 0
        plt.show()

    def handle_close(self,evt):
        self.running = False