#!/usr/bin/env python3

import argparse
import logging
import os
import signal
import subprocess
import sys

import gpiozero


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')


def signal_handler(sig, frame):
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Run commands based on GPIO actions.")
    parser.add_argument("--dry-run", action="store_true", default=False, help="dry run only")
    parser.add_argument("--on", type=int, default=[], action="append", help="GPIO pin on which to perform an action")
    parser.add_argument("--command", type=str, default=[], action="append", help="command to run")
    options = parser.parse_args()

    def action(command):
        def inner():
            logging.info("Running '%s'...", command)
            if not options.dry_run:
                subprocess.run(command, shell=True)
                logging.info("Done.")
        return inner

    buttons = []
    for index, pin in enumerate(options.on):
        command = options.command[index]
        button = gpiozero.Button(pin)
        button.when_pressed = action(command)
        buttons.append(button)
        logging.info("%s: %s", pin, command)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
        

if __name__ == "__main__":
    main()
