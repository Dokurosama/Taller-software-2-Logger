import log_class.presenter.logger_factory_impl as logger_factory_impl


def get_function_logger(type_logger):
    logger = logger_factory_impl.LoggerFactoryImpl().get_logger(type=type_logger)
    logger.get_info('Mensage generico', 200)
    logger.get_warning('Mensage generico', 404)
    logger.get_error('Mensage generico', 401)
    logger.get_debug('Mensage generico', 500)

def main() -> None:
    type_logger = str(input("""
        [c]Para salida por consola
        [f]Para salida hacia el archivo
        [e]Para salida por email
        >>>: """))
    get_function_logger(type_logger)

if __name__ == '__main__':
    main()