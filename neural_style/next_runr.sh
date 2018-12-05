#!/bin/bash

python neural_style.py --content kd/suit.jpg --styles kd/gothic.jpg --output gothicdeez8.jpg --iterations 1000 --checkpoint-output checkpoint/gothic8test%s.jpg --checkpoint-iterations 50
python neural_style.py --content kd/sharpened.jpg --styles kd/banana.jpg --output bananabear.jpg --iterations 500 --checkpoint-output checkpoint/naners%s.jpg --checkpoint-iterations 50
