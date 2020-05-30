import time 
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
import tarfile
  
  
class OnMyWatch: 
    # Set the directory on watch 
    watchDirectory = "/migration"
  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
  
class Handler(FileSystemEventHandler): 
  
    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None 
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now
	    tf = tarfile.open("checkpoint1.tgz")
	    tf.extractall()
	    os.system("python hostb2.py")
	    exit()
              
  
if __name__ == '__main__': 
    watch = OnMyWatch() 
watch.run() 
