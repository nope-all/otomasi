#!/bin/bash

if ! python3 --version; then
      sudo apt-get install python3
fi
python3 install-docker-portainer.py;