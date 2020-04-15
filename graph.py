#!python3

import time
import threading
import matplotlib.pyplot as plt
from argparse import ArgumentParser

lgd = []
data = []

parser = ArgumentParser(
    prog="graph.py",
    description="Generate animated graph of incoming csv data"
)
parser.add_argument("--timedelay", "-t", default=0.1, type=float)

args = parser.parse_args()


def main():
    thread1 = threading.Thread(target=input_thread, name="Input thread")
    thread2 = threading.Thread(
        target=plot_thread, name="Plot thread", daemon=True)
    thread1.start()
    thread2.start()


def input_thread():
    global lgd
    lgd = [x for x in input().strip(",").split(',')]
    for _ in range(len(lgd)):
        data.append([])
    while True:
        line = [float(x) for x in input().strip(",").split(',')]
        for i in range(len(line)):
            data[i].append(line[i])


def plot_thread():
    plt.ion()
    plt.style.use("seaborn")
    fig = plt.figure()
    plt.legend()
    while True:
        for i in range(len(lgd)):
            plt.plot(data[i], linewidth=1, label=lgd[i])
        plt.legend()
        plt.draw()
        time.sleep(args.timedelay)
        fig.canvas.flush_events()
        plt.clf()


if __name__ == "__main__":
    main()
