# -*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

hexv = Blueprint('hexv', __name__, url_prefix='/')

@hexv.route('/hexview', methods=['POST'])
def hexp():
    path = "./file/" + request.form['file']

    # 출력 변수 선언
    phex = list()
    pascii = list()
    poffset = list()
    offset = 0

    try:
        hexf = open(path, 'rb')
    except IOError:
        return render_template('filelist.html')
    
    while True:
        buf = hexf.read(16)
        buflen = len(buf)
        if buflen == 0: break
        
        hexs = list()
        for i in range(buflen):
            bufchr = chr(buf[i])
            hexs.append("%02X " % (ord(bufchr)))
        phex.append(hexs)
        
        asc = list()
        for i in range(buflen):
            ascchr = chr(buf[i])
            asc.append(ascchr)
        pascii.append(asc)
        
        poffset.append("%08X" % (offset))
        offset += 16

    print(poffset)
    print(phex)
    print(pascii)
    
    hexf.close()
        
    return render_template('hexview.html', offsets=poffset, hexs=phex, asciis=pascii)