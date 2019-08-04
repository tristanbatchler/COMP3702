import urllib.parse, re, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_in", type=str, help="the file name to read in")

args = parser.parse_args()

if __name__ == '__main__':
    lines_raw = []
    lines_mod = []

    with open(args.file_in) as f:
        lines_raw = f.readlines()

    display = False
    for line_raw in lines_raw:
        print(line_raw)
        line_mod = line_raw
        if not '$$' in line_raw:
            if not display:
                latex = re.findall('\$.*?\$', line_raw)
                for l in latex:
                    q = urllib.parse.quote(l)
                    html = '<img src="https://latex.codecogs.com/gif.latex\?%s" />' % q
                    line_mod = line_mod.replace(l, html)
            else:
                q = urllib.parse.quote(line_mod)
                html = '<img src="https://latex.codecogs.com/gif.latex\?%s" />' % q
                line_mod = line_mod.replace(line_mod, html)
        else: 
            display = not display
            line_mod = ''

        lines_mod.append(line_mod)
        print(line_mod)

    with open(args.file_in + '.mod.md', 'w') as f:
        for item in lines_mod:
            f.write("%s" % item)