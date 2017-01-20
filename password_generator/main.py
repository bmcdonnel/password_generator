import argparse
import os
import logging

from password_generator import utils
from password_generator import generator

LOG_PATH = "logs"

def main():
    utils.configure_rolling_logger(os.path.join(LOG_PATH, "application.log"))

    args = parse_arguments()

    print generator.Generator.generate(args.pattern)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern', required=True)

    return parser.parse_args()

if __name__ == "__main__":
    main()

