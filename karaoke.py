#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal():
    """
    Programa principal
    """
    def __init__ (self):
        self.original = ""
        self.resultante = ""
        parser = make_parser()
        ccHandler = SmallSMILHandler()
        parser.setContentHandler(ccHandler)
        parser.parse(open(sys.argv[1]))
        self.etiquetas = ccHandler.get_tags()

    def __str__ (self):
        cadena = ''
        for linea in self.etiquetas:       
            cadena = cadena + linea[0]
            dicc = linea[1]
            for elem in dicc:
                if dicc[elem] != "":
                    cadena = cadena + '\t' + elem + '="' + dicc[elem] + '"\t'

        return (cadena)

    def do_local(self):
        ccHandler = SmallSMILHandler()
        for linea in ccHandler.get_tags():       
            dicc = linea[1]
            for elem in dicc:
                if elem == 'src':
                    if dicc[elem].startswith('http://'):
                        ddp2 = urllib.request.urlopen(dicc[elem])
                        ddp2.read()
                        ddp2.close()
                        indice = str.rfind(dicc[elem], '/')
                        dicc[elem] = dicc[elem][indice+1:]

    def do_json(self, original, resultante):
        if self.resultante == None:
            json.dump(self.etiquetas, open("karaoke.json",'w'), sort_keys=True, indent=4, separators=(',', ': '))
        else:
            json.dump(self.etiquetas, open("locaL.json",'w'), sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":

    try:
        pr = KaraokeLocal()
        parser = make_parser()
        ccHandler = SmallSMILHandler()
        parser.setContentHandler(ccHandler)
        parser.parse(open(sys.argv[1]))
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    print (pr)
    pr.do_json(pr.original,pr.resultante)
    pr.do_local()
    pr.do_json(pr.original,"local.json")
    print (pr)

    

