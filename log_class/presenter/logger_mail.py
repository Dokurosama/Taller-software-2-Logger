import log_class.model.logger as logger
import log_class.model.logger_sender_mail as logger_mail

receiver_email_address = 'andres.canas@uptc.edu.co'

class LoggerMail(logger.Logger):

    def get_info(self, message, object):
        self.__printMail(receiver_email_address, 'INFO', message, object)

    def get_warning(self, message, object):
        self.__printMail(receiver_email_address,'WARNING', message, object)

    def get_error(self, message, object):
        self.__printMail(receiver_email_address, 'ERROR', message, object)
    
    def get_debug(self, message, object):
        self.__printMail(receiver_email_address, 'DEBUG', message, object)

    def __printMail(self,receiver_email_address, level, message, object):
        mail_log = logger_mail.LogMail(receiver_email_address, level, message, object)
        mail_log.send_email()