import datetime as date_time
import log_class.model.logger as logger

log_file = 'file.log'

class LoggerFile(logger.Logger):
    def get_info(self, message, object):
        self.__printFile('INFO', message, object)

    def get_warning(self, message, object):
        self.__printFile('WARNING', message, object)

    def get_error(self, message, object):
        self.__printFile('ERROR', message, object)
    
    def get_debug(self, message, object):
        self.__printFile('DEBUG', message, object)
    
    def __printFile(self, level, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(date_time.datetime.now())} [{level}] {message, str(object)}\n'
            file.writelines(data)