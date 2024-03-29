"""
--------------------------------------------------------------------------
Arcade Button Driver
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

Button Driver

  This driver is built for buttons that have a pull up resistor between the
button and the processor pin (i.e. the input is "High"/"1" when the button is
not pressed) and will be connected to ground when the button is pressed (i.e. 
the input is "Low" / "0" when the button is pressed)

Software API:

  Button(pin)
    - Provide pin that the button monitors
    
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    wait_for_press(function=None)
      - Wait for the button to be pressed 
      - Optionally takes in an argument "function" which is the function 
        to be executed when waiting for the button to be pressed
      - Function consumes time
      - Returns a tuple:  
        (<time button was pressed>, <data returned by the "function" argument>)

"""

import os
import random
import time
import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Button():
    """ Button Class """
    pin             = None
    unpressed_value = None
    pressed_value   = None
    sleep_time      = None
    
    def __init__(self, pin=None):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        
        # By default the unpressed_value is "1" and the pressed
        # value is "0".  This is done to make it easier to change
        # in the future
        self.unpressed_value = 1
        self.pressed_value   = 0
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = 0.1

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        GPIO.setup(self.pin, GPIO.IN)

    # End def


    def is_pressed(self):
        """ Is the Button pressed?
        
           Returns:  True  - Button is pressed
                     False - Button is not pressed
        """
        if GPIO.input(self.pin) == self.pressed_value:
            return True
        else:
            return False
            
    # End def


    def wait_for_press(self, function=None):
        """ Wait for the button to be pressed.  This function will 
           wait for the button to be pressed and released so there
           are no race conditions.
        
           Arguments:
               function - Optional argument that is the functon to 
                          executed while waiting for the button to 
                          be pressed
        
           Returns:
               tuple - [0] Time button was pressed
                     - [1] Data returned by the "function" argument
        """
        function_return_value = None
        button_press_time     = None
        
        # Execute function if it is not None
        #   - This covers the case that the button is pressed prior 
        #     to entering this function
        if function is not None:
            function_return_value = function()
        
        # Wait for button press
        #   If the function is not None, execute the function
        #   Sleep for a short amount of time to reduce the CPU load
        
        
        while(GPIO.input(self.pin) == self.unpressed_value):
        
            if function is not None:
                function_return_value = function()
                
            time.sleep(self.sleep_time)
        
        # Record time
        button_press_time = time.time()
        
        # Wait for button release
        #   Sleep for a short amount of time to reduce the CPU load
        #

        while(GPIO.input(self.pin) == self.pressed_value):
            time.sleep(self.sleep_time)
        
        # Compute the button_press_time
        button_press_time = time.time() - button_press_time

        # Return a tuple:  (button press time, function return value)        
        return (button_press_time, function_return_value)
        
    # End def

# End class

