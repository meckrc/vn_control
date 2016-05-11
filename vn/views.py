# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

import os

def Hello(request):
    return HttpResponse("Hello, world.")

def mftp_log(request):
    
    cmd='mftp info > /opt/envs/control/vn_control/static/mftp.tmp'
    os.system(cmd)
#    Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE)

    return HttpResponse("Done")
    