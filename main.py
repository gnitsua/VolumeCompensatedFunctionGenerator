from FrequencySweeper import FrequencySweeper
from KeysightAmplitudeController import KeysightAmplitudeController

if __name__ == "__main__":
    # function_generator = KeysightAmplitudeController(1641, 0.1, 1)
    # function_generator = KeysightAmplitudeController(1600, 0.3, 1)
    # function_generator.autolevel(True)
    sweeper = FrequencySweeper("sweep.csv")
    sweeper.start()
    # volume_controller = VolumeController(700)
    # plot = UpdatingLinePlot(-4000,4000,0,4000,"r",volume_controller)
    # plot = UpdatingLinePlot(0,1,-1,1,"r",function_generator)
    # plot.plot()
