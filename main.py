import argparse
from controllers.Controller import Controller


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-viewmode", choices=["demo"])
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    if args.viewmode == "demo":
        myApp = Controller(args.viewmode)
    else:
        myApp = Controller()

    myApp.main()