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
        #print(line_raw)
        line_mod = line_raw
        if not '$$' in line_raw:
            if not display:
                latex = re.findall('\\$(.*?)\\$', line_raw)
                for l in latex:
                    print(l)
                    q = urllib.parse.quote(l)
                    md = '![%s](https://latex.codecogs.com/gif.latex?%s)' % (q, q)
                    line_mod = line_mod.replace('$%s$' % l, md)
                
                imgs = re.findall('\[.*?\]\((\\..*?)\)', line_mod)
                for i in imgs:
                    q = urllib.parse.quote(i.replace('\\', '/'))[1:]
                    #print("%s" % q)
                    line_mod = line_mod.replace(i, 'https://raw.githubusercontent.com/tristanbatchler/COMP3702/master%s' % q)
            else:
                q = urllib.parse.quote(line_mod)
                md = '[%s](https://latex.codecogs.com/gif.latex?%s)' % (q, q)
                line_mod = line_mod.replace(line_mod, md)
        else: 
            display = not display
            line_mod = ''

        lines_mod.append(line_mod)
        #print(line_mod)

    with open(args.file_in, 'w') as f:
        for item in lines_mod:
            f.write("%s" % item)