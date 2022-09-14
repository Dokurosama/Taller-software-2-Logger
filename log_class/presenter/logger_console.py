from colorama import init, Fore
import datetime as date_time
import log_class.model.logger as lg


init(autoreset=True)

class LoggerConsole(lg.Logger):
    
    def get_info(self, message, object):
        print(f'{Fore.BLUE}{date_time.datetime.now()} [INFO] {message, object}')
    
    def get_warning(self, message, object):
        print(f'{Fore.YELLOW}{date_time.datetime.now()} [WARNING] {message, object}')

    def get_error(self, message, object):
        print(f'{Fore.RED}{date_time.datetime.now()} [ERROR] {message, object}')

    def get_debug(self, message, object):
        print(f'{Fore.MAGENTA}{date_time.datetime.now()} [DEBUG] {message, object}')

