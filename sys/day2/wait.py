#!/usr/bin/python

import os

pid = os.fork()
if pid < 0:
     
