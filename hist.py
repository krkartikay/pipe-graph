#!python3

import time
import threading
import matplotlib.pyplot as plt
from argparse import ArgumentParser

title = ""
data = []

parser = ArgumentParser(
    prog="hist.py",
    description="Generate histogram of incoming numbers.",
    epilog="""
    First line of input contains title, and subsequent lines have data points.
    Remember to flush stdout from the input program or you will not see any data!
    """,
)
parser.add_argument("--timedelay", "-t", default=0.1, type=float)
parser.add_argument("--bins", "-b", default=20, type=int)
parser.add_argument("--low", "-lo", type=float)
parser.add_argument("--high", "-hi", type=float)

args = parser.parse_args()


def main():
    thread1 = threading.Thread(target=input_thread, name="Input thread")
    thread2 = threading.Thread(
        target=plot_thread, name="Plot thread", daemon=True)
    thread1.start()
    thread2.start()


def input_thread():
    global title
    title = input().strip(",")
    while True:
        line = input().strip(",")
        data.append(float(line))


def plot_thread():
    plt.ion()
    plt.style.use("seaborn")
    fig = plt.figure()
    while True:
        if args.low is not None and args.high is not None:
            plt.hist(data, bins=args.bins, range=(args.low, args.high))
        else:
            plt.hist(data, bins=args.bins)
        plt.title(title)
        plt.draw()
        time.sleep(args.timedelay)
        fig.canvas.flush_events()
        plt.clf()


if __name__ == "__main__":
    main()
