#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time
from bottle import route, run


@route('/')
def index():
    return('Strawberry-aroma')
    

@route('/aroma')
def aroma():
    subprocess.call('python irrp.py -p -g21 -f codes aroma:on'.split())
    time.sleep(5)
    subprocess.call('python irrp.py -p -g21 -f codes aroma:off'.split())
    return('aroma')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

