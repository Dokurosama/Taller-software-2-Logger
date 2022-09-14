from log_class.model.logger import Logger
from log_class.model.logger_factory import LoggerFactory
from log_class.presenter.logger_console import LoggerConsole
from log_class.presenter.logger_file import LoggerFile
from log_class.presenter.logger_mail import LoggerMail

class LoggerFactoryImpl(LoggerFactory):

    def get_logger(self, type) -> Logger:
        dictionary = {
            'c': LoggerConsole(),
            'f': LoggerFile(),
            'e': LoggerMail()
        }
        return dictionary[type]

