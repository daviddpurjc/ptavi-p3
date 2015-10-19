#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        parser = make_parser()
        ccHandler = SmallSMILHandler()
        parser.setContentHandler(ccHandler)
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    for linea in ccHandler.get_tags():       
        dicc = linea[1]
        for elem in dicc:
            if elem == 'src':
                if dicc[elem].startswith('http://'):
                    ddp2 = urllib.request.urlopen(dicc[elem])
                    print(ddp2.read())
                    ddp2.close()
                    indice = str.rfind(dicc[elem], '/')
                    dicc[elem] = dicc[elem][indice+1:]
        print()

    for linea in ccHandler.get_tags():       
        print (linea[0], end="\t")
        dicc = linea[1]
        for elem in dicc:
            if dicc[elem] != "":
                print (elem, dicc[elem], sep='="', end='"\t')
        print()

    misdatos = ccHandler.get_tags()
    json.dump(misdatos, open("karaoke.json",'w'), sort_keys=True, indent=4, separators=(',', ': '))
