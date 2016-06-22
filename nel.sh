#!/bin/bash
mkdir people
mkdir others
python facedetect.py --images $1
python detect.py --images $1