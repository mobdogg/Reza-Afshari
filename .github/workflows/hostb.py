import time 
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
import tarfile
import sys
from datetime import datetime 
  
  
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
                time.sleep(7) 
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
	    sys.stdout.write("Migration completed ")
	    print datetime.now().strftime('%H:%M:%S.%f')[:-4]
	    tf = tarfile.open("checkpoint1.tgz")
	    tf.extractall()
	    sys.stdout.write("Checkpoint Extracted ")
	    print datetime.now().strftime('%H:%M:%S.%f')[:-4]
	    os.system("python hostb2.py")
	    exit()
              
  
if __name__ == '__main__': 
    watch = OnMyWatch() 
watch.run() 
