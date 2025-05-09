import bottle
from bottle import route, run, template
import threading
import image

def call_service():
    # Run image processing in the background
    directoryName = 'photos'
    image.process(directoryName)

@route('/')
def index():
    # Avoid blocking response by running in background
    threading.Thread(target=call_service).start()
    return template('index.tpl', data="Processing started!", title="Image Processor App")

if __name__ == '__main__':
    # reloader removed to avoid excess CPU in production
    run(host='0.0.0.0', port=8000, debug=False)

serverApp = bottle.default_app()
