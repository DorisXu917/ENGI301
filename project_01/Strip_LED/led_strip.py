"""
--------------------------------------------------------------------------
LED Strip 
--------------------------------------------------------------------------
License:   
Copyright 2023 Doris Xu

Based on Code from:  https://github.com/rpliu3/ENGI301/tree/master/Project_01/code
Copyright 2019 Rebecca Liu

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
Software API:

  * opc.client ensures that server is running so that LED string can be displayed
  
--------------------------------------------------------------------------
Background Information: 
 
   * Base code for LED functions came from the following repositories:
        https://markayoder.github.io/PRUCookbook/01case/case.html#_neopixels_5050_rgb_leds_with_integrated_drivers_ledscape
        https://markayoder.github.io/PRUCookbook/06io/io.html#io_uio
        https://github.com/Yona-Appletree/LEDscape.git
        https://github.com/zestyping/openpixelcontrol

"""


import time
import opc

class led_strip():
    """ led_strip class"""
    ADDRESS = None
    client = None
    STR_LEN = None
    leds = None
    
    
    def __init__(self, address = 'localhost:7890', length = 56):
        # Initialize the led light strip 
        self.ADDRESS = address
        self.client  = opc.Client(address)
        self.STR_LEN = length
        self.leds    = [(0, 0, 0)] * self.STR_LEN
        
        # put pixel
        if self.client.can_connect():
            print ('connected to %s' % address)
        else:
            print ('WARNING: could not connect to %s' % address)
    # End def
    
    
    
    def black_out_all_leds(self):
        # This function turns off all the lights in the led trip 
        print("Black Out LEDs")
        
        for i in range(self.STR_LEN):
            self.leds[i] =  (0, 0, 0) # turns off al the RBG colors 
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        '''
        The author of this class realized that the OPC driver is one command behind
        As a consequence of that, the last line of the program will not execute 
        To address this issue and make sure all the commands are executed, the last command of 
        each function is repeated twice 
        '''
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
    # End def
    
    def device_start_up_routine(self):
        '''
        This start-up routine turns all the lights in the strip on one by one
           and sets the color to white
        This routine checks for the connectivity of the light strip
        '''
        # start with all the LEDs off
        self.black_out_all_leds()

        # run the start up routine
        # sets every light to be a soft white 
        for i in range(self.STR_LEN):
            self.leds[i] = (50, 50, 50) 
            # put pixel
            if not self.client.put_pixels(self.leds, channel=0):
                print ('not connected')
            
            if not self.client.put_pixels(self.leds, channel=0):
                print ('not connected')
            
            time.sleep(0.05)
        
        self.black_out_all_leds()

    # End def
    
    
    def game_finish_up_routine(self):
        '''
        At the end of the demonstration, set the lights on the 4 sides of the sandbox to be a soft purple color 
        '''
        self.black_out_all_leds()

        # run the start up routine
        for i in range(self.STR_LEN):
            self.leds[i] = (30, 0, 50) # sets every light to be a soft white 
                
            if not self.client.put_pixels(self.leds, channel=0):
                print ('not connected')
            
            if not self.client.put_pixels(self.leds, channel=0):
                print ('not connected')
                
            time.sleep(0.05)
        
        self.black_out_all_leds()
        
    # End def
    
    
    def green_light(self, light_ID):
        # Set any specified led to green
        
        print("Green Light = {0}".format(light_ID))
        self.leds[light_ID] = (0, 50, 0)
        
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
    #End def 
    
    def red_light(self, light_ID):
        # Set any specified led to red
        
        print("Red Light = {0}".format(light_ID))
        self.leds[light_ID] = (50, 0, 0)
        
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
    #End def
    
    # set the logic table lights when x = 0 and y = 0
    # 1st row of the logic table
    def row_1_lights(self):
        # set x to red 
        self.leds[44] = (50, 0, 0) 
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        # set y to red 
        self.leds[45] = (50, 0, 0) 
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        #set z to red    
        self.leds[46] = (50, 0, 0) 
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def
    
    # set the logic table lights when x = 1 and y = 0
    # 2nd row of the logic table
    def row_2_lights(self):
        # set x to green
        self.leds[47] = (0, 50, 0)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        # set y to red    
        self.leds[48] = (50, 0, 0) # set x to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        # set z to red     
        self.leds[49] = (50, 0, 0) # set z to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def
            
    # set the logic table lights when x = 0 and y = 1
    # 3rd row of the logic table
    def row_3_lights(self):
        # set x to red
        self.leds[50] = (50, 0, 0)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        # set y to green
        self.leds[51] = (0, 50, 0) # set x to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        # set z to red     
        self.leds[52] = (50, 0, 0) # set z to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def     
    
    # set the logic table lights when x = 1 and y = 1
    # 4th row of the logic table
    def row_4_lights(self):
        # set x to red
        self.leds[53] = (0, 50, 0)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        # set y to green
        self.leds[54] = (0, 50, 0) # set x to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        
        # set z to red     
        self.leds[55] = (0, 50, 0) # set z to red
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
            
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def     
            
        
    
    