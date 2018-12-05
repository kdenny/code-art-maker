import requests

d = {
    'source': '/Users/kevindenny/Documents/neural-style/kd/phl2.jpg',
    'style': '/Users/kevindenny/Documents/neural-style/kd/silkprint.jpg',
}

u = 'http://localhost:8000/projects/'

r = requests.post(u, d)
print(r.text)