import argparse
import random
import signal
import sys
import time
import logging
from logging.handlers import TimedRotatingFileHandler

from xmlrpc.client import Boolean

import autopy


logger = logging.getLogger("")
logFormatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d [%(threadName)7s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = TimedRotatingFileHandler(
    "mouse-rover.log", when="D", interval=1, backupCount=4
)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger.setLevel(logging.INFO)


SCR_MAX_WIDTH = SCR_MAX_HEIGHT = 0
# BORDER_SIZE to avoid to run into Hot-Corners in Mac.
BORDER_SIZE = 10


def sigint_handler(sig, frame) -> None:
    """
    handle ctrl-c
    """

    logger.info("Bye")
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


def possible_in_hot_corner(x, y) -> Boolean:
    """
    detect if current pos in hot corner.
    """

    if (
        x < BORDER_SIZE
        or x > SCR_MAX_WIDTH - BORDER_SIZE
        or y < BORDER_SIZE
        or y > SCR_MAX_HEIGHT - BORDER_SIZE
    ):
        logger.info("Possible Hot Corner detect x:{} y:{}".format(x, y))
        return True

    return False


def move_to_next_location(small=False) -> tuple():
    """
    move to next location
    """

    curr_loc = get_current_location()
    if small:
        next_x = random.randint(curr_loc[0] - BORDER_SIZE, curr_loc[0] + BORDER_SIZE)
        next_y = random.randint(curr_loc[1] - BORDER_SIZE, curr_loc[1] + BORDER_SIZE)
        if possible_in_hot_corner(next_x, next_y):
            # move to center of screen to avoid trigger action defined in hot-corner.
            next_x, next_y = (SCR_MAX_WIDTH / 2, SCR_MAX_HEIGHT / 2)
    else:
        next_x = random.randint(BORDER_SIZE, SCR_MAX_WIDTH - BORDER_SIZE)
        next_y = random.randint(BORDER_SIZE, SCR_MAX_HEIGHT - BORDER_SIZE)
    next_loc = (next_x, next_y)

    autopy.mouse.move(*next_loc)

    return next_loc


def get_current_location() -> tuple():
    """
    get current location
    """

    loc = autopy.mouse.location()
    loc = tuple(map(lambda x: int(x), loc))
    return loc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="control for mouse-rover.")
    parser.add_argument("-a", "--always", action="store_true", help="execute always.")
    parser.add_argument(
        "-s", "--small", action="store_true", help="move in small range."
    )
    parser.add_argument("-t", "--time", type=int, default=10, help="trigger interval.")
    args = parser.parse_args()
    move_small = args.small
    interval = args.time
    always = args.always

    SCR_MAX_WIDTH = int(autopy.screen.size()[0])
    SCR_MAX_HEIGHT = int(autopy.screen.size()[1])
    logger.info(
        "Screen = {} x {}, small={}, interval={}".format(
            SCR_MAX_WIDTH, SCR_MAX_HEIGHT, move_small, interval
        )
    )

    curr = prev = get_current_location()

    while True:
        prev = curr
        time.sleep(interval)
        curr = get_current_location()
        logger.info("{} {}".format(curr, prev))

        if curr != prev:
            if not always:
                logger.info("Bye")
                break
            logger.info("🐁 move to position:{}".format(curr))
            prev = curr
        else:
            curr = move_to_next_location(small=move_small)
            logger.info("😺 move to position:{}".format(curr))
