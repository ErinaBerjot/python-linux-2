import bottle
from bottle import route, run, template
import threading
import image

def call_service():
    # Run image processing on the given directory
    directoryName = 'photos'
    image.process(directoryName)

@route('/')
def index():
    # Start image processing in a background thread to avoid blocking the response
    threading.Thread(target=call_service).start()
    return template('index.tpl', data="Processing started!", title="Image Processor App")

if __name__ == '__main__':
    # Production-safe: debug is off, reloader is not needed
    run(host='0.0.0.0', port=8000, debug=False)

# Export the WSGI application
serverApp = bottle.default_app()
