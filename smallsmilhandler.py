#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar etiquetas
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.lista= []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """

        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('width',"")
            self.backgroundcolor = attrs.get('background-color',"")
            dicc = {'width': self.width,'height': self.height, 'background-color': self.backgroundcolor}
            self.lista.append([name, dicc])
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            dicc = {'id': self.id,'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right}
            self.lista.append([name, dicc])
        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            dicc = {'src': self.src,'region': self.region, 'begin': self.begin, 'dur': self.dur}
            self.lista.append([name, dicc])
        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            dicc = {'src': self.src,'begin': self.begin, 'dur': self.dur}
            self.lista.append([name, dicc])
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            dicc = {'src': self.src,'region': self.region}
            self.lista.append([name, dicc])

    def get_tags(self):
        return self.lista

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
        sys.exit("Usage: python3 smallsmilhandler.py file.smil.")

    print (ccHandler.get_tags())



