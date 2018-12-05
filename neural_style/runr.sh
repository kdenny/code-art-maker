#!/bin/bash

python neural_style.py --content kd/sharpened.jpg --styles kd/subway.jpg --output subwaybear.jpg --iterations 500 --checkpoint-output checkpoint/subwayr%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/sharpened.jpg --styles kd/liberty.jpg --output libertybear.jpg --iterations 500 --checkpoint-output checkpoint/libertyr%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/kr.jpg --styles kd/korea_painting.jpg --output kra.jpg --iterations 500 --checkpoint-output checkpoint/krar%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/sharpened.jpg --styles kd/money.jpg --output moneybear_hd.jpg --iterations 1000 --checkpoint-output checkpoint/moneybear_hd%s.jpg --checkpoint-iterations 100 --style-layer-weight-exp 2.0
