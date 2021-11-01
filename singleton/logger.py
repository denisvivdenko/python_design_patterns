class Logger(object):
    class _Logger():
        def __init__(self, log_file: str) -> None:
            self.log_file = log_file

        def _write_to_log(self, log_file: str, log_type: str, message: str) -> None:
            with open(log_file, 'a') as logs:
                full_message = f"[{log_type}]: {message}\n"
                logs.write(full_message)

        def write_info_message(self, message: str) -> None:
            self._write_to_log(log_file=self.log_file, log_type="INFO", message=message)

        def write_debug_message(self, message: str) -> None:
            self._write_to_log(log_file=self.log_file, log_type="DEBUG", message=message)

    instance = None

    def __new__(cls, log_file: str = None):
        if not Logger.instance:
            Logger.instance = Logger._Logger(log_file)

        return Logger.instance

    def __getattr__(self, name):
        return getattr(Logger.instance, name)

    def __setattr__(self, name):
        return setattr(Logger.instance, name)