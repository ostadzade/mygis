# watch_scss.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management import call_command
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            print("\nSCSS file changed. Recompiling...")
            call_command('compress', '--force')

observer = Observer()
observer.schedule(Handler(), path='static/scss/', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()