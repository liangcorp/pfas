#!/bin/bash
source $HOME/projects/djangodev/bin/activate
python -m smtpd -n -c DebuggingServer 192.168.1.6:1025
