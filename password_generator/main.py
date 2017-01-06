import os
import logging

from password_generator import utils
from password_generator import generator

LOG_PATH = "logs"

def main():
    utils.configure_rolling_logger(os.path.join(LOG_PATH, "application.log"))

    generator.Generator(8).generate()

if __name__ == "__main__":
    main()

