import serial, struct, time, collections

class TimeoutError(Exception):
    pass


class Coherent(object):

    def __init__(self, port, baud=19200):
        """
        port: serial COM port (0==COM1, 1==COM2, ...)
        """
        self.port = port
        self.baud = baud
        self.sp = serial.Serial(int(self.port), baudrate=self.baud, bytesize=serial.EIGHTBITS)
        time.sleep(0.3)  ## Give devices a moment to chill after opening the serial line.
        self.write("PROMPT=0\r\n")
        self.readPacket()
        self.write("ECHO=0\r\n")
        self.readPacket()
        self.write("HEARTBEAT=0\r\n")
        self.readPacket()

    def getPower(self):
        v = self['UF']
        try:
            return float(v)
        except:
            print v, type(v)
            raise
    
    def getWavelength(self):
        return float(self['VW'])
    
    def setWavelength(self, wl, block=False):
        """Set wavelength to wl in nanometers. 
        If block=True, do not return until the tuning is complete."""
        self['WAVELENGTH'] = int(wl)
        if block:
            while True:
                if not self.isTuning():
                    break
                time.sleep(0.1)
                    
    def getWavelengthRange(self):
        return float(self['TMIN']), float(self['TMAX'])
        
    def isTuning(self):
        """Returns True if the laser is currently tuning its weavelength"""
        return self['TS'] != '0'
        
    def getShutter(self):
        """Return True if the shutter is open."""
        return bool(int(self['SHUTTER']))
    
    def setShutter(self, val):
        """Open (True) or close (False) the shutter"""
        self['SHUTTER'] = (1 if val else 0)
        
    def setAlignment(self, align):
        """Set (1) or unset (0) alignment mode
        Note: disabling alignment mode can take several seconds.
        """
        self['ALIGN'] = align
        
    def getAlignment(self):
        return self['ALIGN']
        
    def __getitem__(self, arg):  ## request a single value from the laser
        #print "write", arg
        self.write("?%s\r\n" % arg)
        ret = self.readPacket()
        #print "   return:", ret
        return ret
        
    def __setitem__(self, arg, val):  ## set a single value on the laser
        #print "write", arg, val
        self.write("%s=%s\r\n" % (arg,str(val)))
        ret = self.readPacket()
        #print "   return:", ret
        return ret

    def clearBuffer(self):
        d = self.read()
        time.sleep(0.1)
        d += self.read()
        if len(d) > 0:
            print "Sutter MP285: Warning: tossed data ", repr(d)
        return d
    
    def read(self):
        ## read all bytes waiting in buffer; non-blocking.
        n = self.sp.inWaiting()
        if n > 0:
            return self.sp.read(n)
        return ''
    
    def write(self, data):
        self.read()  ## always empty buffer before sending command
        self.sp.write(data)
        
    def close(self):
        self.sp.close()

    #def raiseError(self, errVals):
        ### errVals should be list of error codes
        #errors = []
        #for err in errVals:
            #hit = False
            #for k in ErrorVals:
                #if ord(err) & k:
                    #hit = True
                    #errors.append((k,)+ErrorVals[k])
            #if not hit:
                #errors.append((ord(err), "Unknown error code", ""))
        #raise MP285Error(errors)
                    
    def readPacket(self, expect=0, timeout=10, block=True):
        ## Read until a CRLF is encountered (or timeout).
        ## If expect is >0, then try to get a packet of that length, ignoring CRLF within that data
        ## if block is False, then return immediately if no data is available.
        start = time.time()
        res = ''
        errors = []
        packets = []
        while True:
            s = self.read()
            #print "read:", repr(s)
            if not block and len(s) == 0:
                return
            
            if expect > 0:  ## move bytes into result without checking for \r
                nb = expect-len(res)
                res += s[:nb]
                s = s[nb:]
            
            try:
                while len(s) > 0:  ## pull packets out of s one at a time
                    res += s[:s.index('\r\n')]
                    s = s[s.index('\r\n')+2:]
                    packets.append(res)
                    res = ''
            except ValueError:   ## partial packet; append and wait for more data
                res += s  
                
            if len(res) == 0:
                if len(packets) == 1:
                    if 'Error' in packets[0]:
                        raise Exception(packets[0])
                    return packets[0]   ## success
                if len(packets) > 1:
                    raise Exception("Too many packets read.", packets)
            
            time.sleep(0.01)
            if time.time() - start > timeout:
                raise TimeoutError("Timeout while waiting for response. (Data so far: %s, %s)" % (repr(res), repr(s)))



if __name__ == '__main__':
    c = Coherent(port=4, baud=19200)
    print "Power:", c.getPower()
    print "Wavelength:", c.getWavelength()
