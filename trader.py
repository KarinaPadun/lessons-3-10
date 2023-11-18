from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("RATE", type=str)
args.add_argument("AVAILABLE", type=str)
args.add_argument("BUY XXX", type=str)
args.add_argument("SELL XXX", type=str)
args.add_argument("BUY ALL", type=str)
args.add_argument("SELL ALL", type=str)
args.add_argument("NEXT", type=str)
args.add_argument("RESTART", type=str)


