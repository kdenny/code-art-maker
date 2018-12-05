#!/bin/bash

python neural_style.py --content kd/sharpened.jpg --styles kd/waterlillies.jpg --output lillybear.jpg --iterations 500 --checkpoint-output checkpoint/lil%s.jpg --checkpoint-iterations 50

