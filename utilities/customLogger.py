import logging #predefined package which is available in python
import os

class LogGen:
    @staticmethod
    def loggen():
        log_path = ".\\Logs\\automation.log"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            filename=log_path,
            format='%(asctime)s | %(levelname)s | %(name)s | [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

