# -*- coding: utf-8 -*-

"""extract_paper_titles.py: extract title from pdf journals/papers and
   rename the pdf file itself
"""

import argparse
import os
from pyPdf import PdfFileWriter, PdfFileReader


def do_cmd_args_line():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('-p', '--path', required=True, help='target path')
    parser.add_argument('-d', '--dest', required=True, help='dest path')
    parser.add_argument('--dryrun', action='store_true', help='dryrun')
    args = parser.parse_args()
    return args


def main():
    args = do_cmd_args_line()

    for f in os.listdir(args.path):
        if f.endswith('.pdf'):
            fname = os.path.join(args.path, f)
            pdfile = PdfFileReader(file(fname, 'rb'))

            title = pdfile.getDocumentInfo().title
            subject = pdfile.getDocumentInfo().subject
            author = pdfile.getDocumentInfo().author

            if author == None:
                author = 'Unknown'
            if title == None:
                title = os.path.splitext(f)[0]

            tgtfname = '[{0}] {1}.pdf'.format(author, title)
            ftgtname = os.path.join(args.dest, tgtfname)

            print 'renaming {0} -> {1}'.format(fname, ftgtname)
            if not args.dryrun:
                try:
                    os.rename(fname, ftgtname)
                except Exception as e:
                    print e


if __name__ == '__main__':
    main()
