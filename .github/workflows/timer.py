class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        print ("0:00:00.000")
    
    def stop(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print message + str(self.stop - self.start)
    def elapsed(self, message="Order for handover received "):
        """Time elapsed since start was called"""
        print message + str(datetime.datetime.now() - self.start)[:-3]
