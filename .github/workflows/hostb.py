import time 
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
  
  
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
  
        elif event.event_type == 'created': 
            # Event is created, you can process it now 
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now
	    os.system("docker run -d --name looper busybox:latest /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'")
              
  
if __name__ == '__main__': 
    watch = OnMyWatch() 
    watch.run() 
