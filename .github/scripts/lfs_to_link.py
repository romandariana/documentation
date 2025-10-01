#!/usr/bin/env python3
import re
from os import path, getcwd
from glob import glob
from sys import argv

reg_fig = re.compile(r'(.*?\s|^)\.\.\s+(figure|image)::\s+(.+?)\s*$')
reg_dow0 = re.compile(r'(.*?\s|^):download:`([^<]+)<([^>]+)>`')
reg_dow1 = re.compile(r'(.*?\s|^):download:`([^`]+)`')

def get_lfs_types(root):
    types_lfs = []
    git_attr = path.join(root, ".gitattributes")
    with open(git_attr, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and 'filter=lfs' in line:
                match = re.match(r"\*\.([a-zA-Z0-9]+)", line)
                if match:
                    types_lfs.append('.'+match.group(1))
    return types_lfs

def process_fig(path_, root, m, len_, new_, ln, types_lfs):
    indent, kind, img = m.groups()
    if img.startswith('/'):
        img = path.join(root, img[1:])

    path__ = img.strip()
    if path__.startswith(('http://', 'https://', '//')):
        return False, ln
    is_lfs = False
    for ext in types_lfs:
        if path__.endswith(ext):
            is_lfs = True
    if not is_lfs:
        return False, ln

    path__ = path.abspath(path.join(path_, '..', path__))[len_:]
    path__ = path.join(new_, path__)

    if path__ != img:
        return True, f"{indent}.. {kind}:: {path__}\n"
    return False, ln

def process_dow(path_, root, m, len_, new_, ln, titled, types_lfs):
    if titled:
        lw, title, dow = m.groups()
    else:
        lw, dow = m.groups()

    if dow.startswith('/'):
        dow = path.join(root, dow[1:])

    path__ = dow.strip()
    if path__.startswith(('http://', 'https://', '//')):
        return False, ln
    is_lfs = False
    for ext in types_lfs:
        if path__.endswith(ext):
            is_lfs = True
    if not is_lfs:
        return False, ln

    path__ = path.abspath(path.join(path_, '..', path__))[len_:]
    path__ = path.join(new_, path__)

    if titled:
        ln = re.sub(reg_dow0, r"\1:download:`\2<{new_}>`".format(new_=path__), ln)
    else:
        ln = re.sub(reg_dow1, r"\1:download:`{new_}`".format(new_=path__), ln)
    if path__ != dow:
        return True, ln
    return False, ln

def process_file(path_, root, len_, new_, types_lfs):
    with open(path_, "r") as f:
        lines = f.readlines()
    changed = False
    out_lines = []
    for ln in lines:
        m = reg_fig.match(ln)
        if m:
            changed, ln_ = process_fig(path_, root, m, len_, new_, ln, types_lfs)
            out_lines.append(ln_)
            continue

        m = reg_dow0.match(ln)
        if m:
            changed, ln_ = process_dow(path_, root, m, len_, new_, ln, True, types_lfs)
            out_lines.append(ln_)
            continue

        m = reg_dow1.match(ln)
        if m:
            changed, ln_ = process_dow(path_, root, m, len_, new_, ln, False, types_lfs)
            out_lines.append(ln_)
            continue

        out_lines.append(ln)

    if not changed:
        return

    with open(path_, "w") as f:
        f.write(''.join(out_lines))

def main():
    root = getcwd()
    types_lfs = get_lfs_types(root)
    len_ = len(root)+1
    targets = glob(path.join(root, '**/*.rst'), recursive=True)

    for f in sorted(set(targets)):
        process_file(f, root, len_, argv[1], types_lfs)

if __name__ == "__main__":
    main()

