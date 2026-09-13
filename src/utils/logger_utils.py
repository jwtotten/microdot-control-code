import logging

class MicrodotLogger:
    def __init__(self, name: str):
        self.logger = self._setup_logger(name)

    def _setup_logger(self, name: str):
        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='/tmp/myapp.log',
                            filemode='w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger().addHandler(console)
        return logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')