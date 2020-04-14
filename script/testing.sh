#!/bin/bash
source ~/.bashrc
pip3 show coverage
python3 -m coverage run -m --source=. pytest ./test/testing.py ./Service_1/app.py 
python3 -m coverage report ./test/testing.py ./Service_1/app.py 
# python3 -m coverage run -m pytest /var/lib/jenkins/workspace/sfia1/test/testing.py
# python3 -m coverage report