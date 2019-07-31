import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="the file to output")

args = parser.parse_args()

if __name__ == "__main__":
    try:
        with open(args.file) as f:
            print(f.read())
    except FileNotFoundError:
        print("file not found", file=sys.stderr)
