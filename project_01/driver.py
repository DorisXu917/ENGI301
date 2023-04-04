"""
--------------------------------------------------------------------------
Arcade Style Logic Sandbox Demo Driver 
--------------------------------------------------------------------------
License:   
Copyright 2023 Doris Xu

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Sandbox Driver
  This driver integrates 
  
  This driver contains functions for three arcade buttons that have a pull up resistor between the
button and the processor pin (i.e. the input is "High"/"1" when the button is
not pressed) and will be connected to ground when the button is pressed (i.e. 
the input is "Low" / "0" when the button is pressed)

Software API:

  Button(pin)
    - Provide pin that the button monitors

  LED_Strip(id)
    - Provide id of the LED that is being addressed 
    
The demo will first run a start-up routine to check the connecticity of the led strip
Then it will dim all the lights 
The user will press the red arcade button to start the demo
    - By starting the demo, the user is setting the x and y inputs to 0
The user can then interact with the demo by pressing different buttons
    - The blue button corresponds to the input x 
    - The green button corresponds to the input y 
Corresponding lights (green signifies 1 and red signifies 0) will light up in the logic table 
    as the buttons are pressed 
To finish the demo, the user will press the red button again, and the demo will run through a
game finish up routine -- all the lights will turn on one at a time, to a soft purple color
"""

import led_strip as led
import arcade_button as button
import time
import time
import sys 
import os

#--------------------------------------------------------------------------------
# Initialization
#--------------------------------------------------------------------------------
    # set up buttons
green_button = button.Button("P2_2")
blue_button = button.Button("P2_4")
red_button = button.Button("P2_6")
    
    # set up the led strip 
strip = led.led_strip()

    # set up the logic table led IDs
logic_table_row1_ids = [44, 45, 46]
logic_table_row2_ids = [47, 48, 49]
logic_table_row3_ids = [50, 51, 52]
logic_table_row4_ids = [53, 54, 55]

#--------------------------------------------------------------------------------
# Initialize the board
#--------------------------------------------------------------------------------
    # light up the entire led strip in order to check all the lights 
strip.device_start_up_routine()
strip.black_out_all_leds()
'''
The author of this class realized that the OPC driver is one command behind
As a consequence of that, the last line of the program will not execute 
To address this issue and make sure all the commands are executed, the last command of 
each function is repeated twice 
'''
strip.black_out_all_leds()

#--------------------------------------------------------------------------------
# The game routine
#--------------------------------------------------------------------------------
    
    # ask the player to start the game 
print("Is the red button pressed?")
print("    {0}".format(red_button.is_pressed()))

print("Press and hold the red button.")

while not red_button.is_pressed():
    time.sleep(0.1)

# set the initial logic table state -- x = 0, y = 0, z = 0
# set the 1st row led lights 
strip.red_light(44)
strip.red_light(45)
strip.red_light(46)
# if the opc driveris one command behind, make sure all the lights still turn on 
strip.red_light(46)


'''
Demonstrate the AND gate -- x = 1, y = 0, z = 0
'''

print("Press and Hold the Blue Button")

while not blue_button.is_pressed():
    time.sleep(0.1)
    
# reset all led lights 
strip.black_out_all_leds()
# set the 2nd row led lights 
strip.green_light(47)
strip.red_light(48)
strip.red_light(49)
# if the opc driveris one command behind, make sure all the lights still turn on 
strip.red_light(49)


'''
Demonstrate the AND gate -- x = 0, y = 1, z = 0
'''

print("Press and Hold the Green Button")

while not green_button.is_pressed():
    time.sleep(0.1)

# reset all led lights 
strip.black_out_all_leds()
# set the 3rd row led lights 
strip.red_light(50)
strip.green_light(51)
strip.red_light(52)
# if the opc driveris one command behind, make sure all the lights still turn on 
strip.red_light(52)


'''
Demonstrate the AND gate -- x = 1, y = 1, z = 1
'''
print("Press and Hold BOTH Blue and Green Buttons")

while not (green_button.is_pressed() and  blue_button.is_pressed()):
    time.sleep(0.1)

# reset all led lights 
strip.black_out_all_leds()
# set the 4th row led lights 
strip.green_light(53)
strip.green_light(54)
strip.green_light(55)
strip.green_light(55) # to make sure the last light lights up

print("Press and Hold Red Button to Finish")
while not red_button.is_pressed():
    time.sleep(0.1)
strip.game_finish_up_routine()

print("Demo Completed!")
time.sleep(1)
os.system("mplayer file_example_MP3_700KB.mp3")
print("Congratulations!")

# reset the led strip at the end of the demonstration 
strip.black_out_all_leds()
strip.black_out_all_leds()
