import nidaqmx


class Spectrometer():
    
    '''spectrometer class the only object is the position but the communication
    with the DAQ is handled in this class and not the UI'''
    
    
    #init function
    def __init__(self):
        #file where we will store the last position
        
        try:
            f = open('last_position.txt', 'r')
            last_position = float(f.readline())
            
        except:
            print("there was an error trying to load the data from last_position.txt")
        
        #print success if the except doesn't trigger
        else:
            print('successfully loaded last position\n')
        
        #close the file always
        finally:
            f.close()
        
        #set the position
        self.position = last_position
    
    #getter method google @property for reasoning
    @property
    def position(self):
        return self._position
    
    #setter method related to @property
    @position.setter
    def position(self,wavelength):
        #check these conditons before accepting a value
        if isinstance(wavelength, float) and wavelength > 0:
            self._position = wavelength
            

        else:
            print('not valid entry')
        return
    
    #print function for the spectrometer function
    def __str__(self):
        #for now will only print the position
        return float(self.position)
    

    def recalibrate(self,wavelength):
        self.position = wavelength

    def move(self,wavelength):
        pass

    
    def scan(self,start,end,step):
        pass
    
    def abort():
        pass
    
    def stop():
        pass

    def save(self):
        try:
            #open the file where we save the information
            f = open('last_position.txt', 'w')
            #write the last position
            f.write(str(self.position))
        
        #if there is an error with the write print it
        except:
            print('there was an error writing to last_positoin.txt')
        #if we succeed print success message    
        else:
            print('position saved')
        #no matter what happens close the file    
        finally:
            f.close()
