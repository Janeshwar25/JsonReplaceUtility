import logging

from pathlib import Path

from colorama import init
from colorama import Fore

init(autoreset=True)


class Logger:

    def __init__(self, root: Path):

        log_folder = root / "logs"

        log_folder.mkdir(exist_ok=True)

        self.logger = logging.getLogger("JsonReplace")

        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(
            log_folder / "execution.log",
            encoding="utf8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def info(self, msg):

        print(Fore.CYAN + msg)

        self.logger.info(msg)

    def warning(self, msg):

        print(Fore.YELLOW + msg)

        self.logger.warning(msg)

    def error(self, msg):

        print(Fore.RED + msg)

        self.logger.error(msg)

    def success(self, msg):

        print(Fore.GREEN + msg)

        self.logger.info(msg)
