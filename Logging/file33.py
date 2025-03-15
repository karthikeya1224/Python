import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.debug('this is a debug  message')
logging.info('this is an informational message')
logging.warning("this is warning")
logging.error('this is an error message,server not responding')
logging.critical("this is very important server is down")