# VolumeCompensatedFunctionGenerator


This repository contains code for controlling the Agilent 33210A function generator. It can be used to generate arbitrary Sine wave forms that vary in both frequency and magnitude. 

## Installation
You will need to install both the Keysight Control Expert software and the IOControl software. After doing this you should be able to connect and control the function generator over USB using the included software. Once this is working, the code in this repo should be able to connect automatically

Note: You cannot connect both the IOControl software and this software at the same time.

## Usage

After using Excel to generate the input file (an example can be seen in sweep.csv). Simply run the program, which will sweep over the file once and send commands to the funciton generator.


## Other features
In this repo there is also code that uses a PID control loop and a microphone to control the output level of the scope. In testing, this system did not work well as there is significant delay between the microphone and the scope changing amplitudes. That said, it may serve as a starting point for someone who finds it useful.