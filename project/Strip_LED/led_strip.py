
import time
import opc

class led_strip():
    """ led_strip class"""
    ADDRESS = None
    client = None
    STR_LEN = None
    leds = None
    
    def __init__(self, address = 'localhost:7890', length = 30):
        self.ADDRESS = address
        self.client = opc.Client(address)
        self.STR_LEN = length
        self.leds = [(0, 0, 0)] * self.STR_LEN
        
        if self.client.can_connect():
            print ('connected to %s' % address)
        else:
            print ('WARNING: could not connect to %s' % address)
    # End def
    
    def black_out_all_leds(self):
        self.leds = [(0, 0, 0)] * self.STR_LEN
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    # End def
    
    def start_up_routine(self):
        # start with all the LEDs off
        self.black_out_all_leds()

        # run the start up routine
        for i in range(self.STR_LEN):
            self.leds[i] = (50, 50, 50)
                
            if not self.client.put_pixels(self.leds, channel=0):
                print ('not connected')
            
            time.sleep(0.5)
            
        self.black_out_all_leds()
    # End def
            
        
    
    