
#import logging
#from logging import FileHandler
#file_handler = FileHandler('mylog.log')
#file_handler.setLevel(logging.DEBUG)
#app.logger.addHandler(file_handler)
from pile import app


if __name__ == "__main__":
  #try:
    app.run()
  #except Exception:
  #  app.logger.exception('Failed')
