# PIPE GRAPH

> Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new “features”. -- Doug McIlroy (The UNIX Philosophy)

Ever written a script to fetch some data, and then wanted to create an animated plot for it? Or written a long running simulation whose results you want to view in real time? Ever been in that situation where the graphing code itself becomes bigger than the original thing your script did? I have been there again and again, so I decided to create these simple utilities to save time and be re-used whenever I (or _you_) need them.

Introducing Pipe-Graph and Pipe-Hist: **Use the power of the UNIX pipe!** Pipe incoming data into these small python scripts and get an animated realtime plot of the data!

Contributions are Welcome! Just send create an issue or send a PR!

**If you think this project is useful, please give it a star, so that other people can also see it!**

## Installation:

Simply download the script, make sure it has executable permissions and it is in your `$PATH`. Also ensure you have a working matplotlib.

```sh
$ git clone https://github.com/kartikay26/pipe-graph/
$ sudo pip3 install matplotlib
$ sudo cp pipe-graph/graph.py /usr/bin
$ sudo cp pipe-graph/hist.py /usr/bin
$ rm -rf pipe-graph
```

## Usage / Examples:

### Graphs:

Just output the data from any command in CSV format and pipe it into `graph.py`!

The top line should have the title of each series and the rest of the input will be the data.

Remember to flush stdout from the input program or you will not see any data!

```sh
$ graph.py -h
usage: graph.py [-h] [--timedelay TIMEDELAY]

Generate animated graph of incoming csv data

optional arguments:
  -h, --help            show this help message and exit
  --timedelay TIMEDELAY, -t TIMEDELAY
```


Example:

```sh
$ python bitcoin_prices.py
BTC/USD, ETH/USD, XRP/USD
6864.05, 159.34, 0.18271
10235.23, 158.92, 0.17893
450.23, 1783.12, 0.1233
...
^C

$ python bitcoin_prices.py | graph.py
```

or,

```sh
$ python pipe-graph/examples/sir_model.py | graph.py
```

Output:

![SIR model](https://i.imgur.com/aKOnhSc.png)

To simulataneously save results to a file while graphing it too, use the `tee` command:

```sh
$ python examples/coin_flips.py | tee simulation_results.txt | ./graph.py 
$ cat simulation_results.txt
heads
484
478
477
504...
```

### Histograms:

Use `hist.py`. The first line is taken as title (string) and the rest of the lines are taken as data (float).

```sh
$ hist.py -h
usage: hist.py [-h] [--timedelay TIMEDELAY] [--bins BINS] [--low LOW]
               [--high HIGH]

Generate histogram of incoming numbers.

optional arguments:
  -h, --help            show this help message and exit
  --timedelay TIMEDELAY, -t TIMEDELAY
  --bins BINS, -b BINS
  --low LOW, -lo LOW
  --high HIGH, -hi HIGH

First line of input contains title, and subsequent lines have data points.
Remember to flush stdout from the input program or you will not see any data!
```

Example program to generate data by flipping coins:

```python
"""
coin_flips.py -- keep doing N=1000 coin flips and print result
"""

import random
import sys

N = 1000

print("heads")

while True:
    heads = 0
    for i in range(N):
        coin_flip = random.choice([0,1])
        heads += coin_flip
    print(heads)
    sys.stdout.flush()
```

```sh
$ python pipe-graph/examples/coin-flip.py | hist.py -b 50 -lo 450 -hi 550
```

Output:

![coin flips](https://i.imgur.com/GhqY7v2.png)

The output is a binomial distribution `Bin(N=500,p=0.5)` as expected.
