#!/usr/bin/python3


import os
import sys


class txt_parser():
    def __init__(self):
        self.stdin: str = '' # path to txt file 
        self.stdout: str = '' # optional path to html file, empty for fd1
        self.o: bool = False # -o flag
        return None
    

    def _help(self):
        output: str = ''
        output.join('txt_parser :: txt to html parser\n')
        output.join('path :: path to txt file\n')
        output.join('-o :: path to html file\n')
        output.join('-h :: help menu\n')
        output.join('\n')
        return output


    def run(self, stdin=self.stdin, stdout=self.stdout):
        output: str = ''
        
        # read data from stdin file
        TAB = '    '
        try:
            with open(stdin, 'r') as fi:
                txt = fi.readlines()
                _, title = txt[1].split(TAB)
                title = title.strip()
                _, subtitle = txt[3].split(TAB)
                subtitle = subtitle.strip()
                _, date = txt[5].split(TAB)
                date = date.strip()
            
                indexes = list()
                i = 7
                while txt[i].strip() != 'chapter:':
                    _, index = txt[i].split(TAB)
                    indexes.append(index.strip())
                    i += 1
                chapters = list()
                chapter = ''
                i += 1
                txt_size = len(txt)
                while i < txt_size:
                    if txt[i].strip() == 'chapter:' or i == txt_size-1:
                        chapters.append(chapter.strip())
                        chapter = ''
                    else:
                        chapter += ' ' + txt[i].strip()
                    i += 1
        except Exception as e:
            sys.stderr.write(f'[!] Error reading from stdin file\nException: {e}\n')
            exit(1)
        # html template
        DTAB = '        '
        header = """<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title> hell world </title>
        </head>
        <body style="background-color: #0f0f0f; text-align:center; margin: 0 auto;">"""
        footer = """
        </body>
    </html>
    """
        post = f"""
        <div style="text-align: justify; text-justify: inter-word; margin-left: 1rem;">
            <h3 style="color: #ffffff;"> {title} </h3>
            <h4 style="color: #ffffff;"> {subtitle} </h4>
            <h5 style="color: #ffffff;"> {date} </h5>
        </div>"""
        s = f'\n{DTAB}<div style="text-align: justify; text-justify: inter-word;">\n{2*DTAB}<ol>'
        for index in indexes:
            s += f'\n{3*DTAB}<li style="color: #ffffff;"> {index} </li>'
        s += "\n                </ol>\n        </div></br>"
        post += s
        s = '\n        <div style="text-align: justify; text-justify: inter-word; margin-left: 1rem;">'
        for i in range(len(indexes)):
            s += f'\n{2*DTAB}<h4 style="color: #ffffff;"> {indexes[i]} </h4>'
            s += f'\n{3*DTAB}<p style="color: #ffffff; max-width: 28rem;"> {chapters[i]} </p></br>'
        post += s + f'\n{DTAB}</div>'
        output = f'{header}{post}{footer}'
        
        # output return to fd stdout or file specified
        if self.o:
            print(output)
        else:
            try:
                with open(stdout, 'w') as fo:
                    fo.write(output)
            except Exception as e:
                sys.stderr.write(f'[!] Error writting to stdout file\nException: {e}\n')
                exit(1)
        return 0


    def argparse(self) -> (str, str):
        try:
            self.stdin = sys.argv[1]
        except:
            sys.stderr.write('[!] Error: flag stdin containing type "path to txt file" must be set\n')
            exit(1)
        try:
            if sys.argv[2]:
                if sys.argv[2] == '-o':
                    self.o = True
                    self.stdout = sys.argv[3]
                else:
                    self._help()
        except:
            self.o = False
            self.stdout = ''
        return 0


if __name__ == '__main__':
    txt_parser = txt_parser()
    txt_parser.argparse()
    txt_parser.run()
    exit(0)
