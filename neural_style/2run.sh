#!/bin/bash

python neural_style.py --content kd/slt.jpg --styles kd/ducks.jpg --output quacks.jpg --iterations 500 --checkpoint-output checkpoint/qu%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/sharpened.jpg --styles kd/suit.jpg --output ssuit.jpg --iterations 500 --checkpoint-output checkpoint/ssuit%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/dragon.jpg --styles kd/tk2.jpg --output tkdragon.jpg --iterations 500 --checkpoint-output checkpoint/tkd%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/sharpened.jpg --styles kd/warhol.jpg --output wb8.jpg --iterations 500 --checkpoint-output checkpoint/wb%s.jpg --checkpoint-iterations 50

