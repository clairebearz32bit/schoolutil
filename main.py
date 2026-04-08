import argparse
from argparse import ArgumentParser

from src.problemcounter import Ranges, parse_ranges

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(title="subcommands")

    count_sp = sub_parsers.add_parser("count", help="count the number of problems in a range")
    arg = {
        "dest": "count_range",
        "help": "list of problems to count"
    }
    count_sp.add_argument(**arg)
    count_sp.add_argument("-e", "--exclude", help="problems to exclude from the range", dest="exclude")

    args = parser.parse_args()
    print(args)

    if args.count_range:
        count_range = parse_ranges(args.count_range)

        exclude = args.exclude

        if exclude:
            exclude = [int(i) for i in exclude.split(" ")]
            count_range = Ranges(ranges=count_range, exclude=exclude)

        else:
            count_range = Ranges(ranges=count_range)

        total = count_range.get_total()
        print(total)
