import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_in", type=str, help="the file name to read in")
parser.add_argument("file_out", type=str, help="the file name to print out")
parser.add_argument("letter", type=str, help="the letter to remove")

args = parser.parse_args()

if __name__ == "__main__":
    try:
        with open(args.file_in, "r") as f_in:
            contents_in = f_in.read()
            with open(args.file_out, "w") as f_out:
                contents_out = contents_in.replace(args.letter, '')
                print(contents_out, file=f_out)
        
    except FileNotFoundError:
        print("file not found", file=sys.stderr)
