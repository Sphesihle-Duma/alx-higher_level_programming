#!/bin/bash
# A script that shows all allowed options
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2
