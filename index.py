import bottle
from bottle import route, run, template
import os
import image
import threading

PHOTO_DIR = "photos"
processing_lock = threading.Lock()
is_processing = False  # flag to track background task

def process_async():
    global is_processing

    def target():
        global is_processing
        with processing_lock:
            is_processing = True
        try:
            image.process(PHOTO_DIR)
        finally:
            with processing_lock:
                is_processing = False

    with processing_lock:
        if is_processing:
            return  # Already running → skip

    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

@route('/')
def index():
    title = "Image Processor App"
    process_async()
    msg = "Image processing started in the background (if not already running)."
    return template('index.tpl', data=msg, title=title)

@route('/status')
def status():
    title = "Processing Status"
    with processing_lock:
        status = "Running..." if is_processing else "Idle"
    return template('index.tpl', data=f"Processing status: {status}", title=title)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=False, reloader=True)

serverApp = bottle.default_app()
