
## Features
1. You can play how fast to find mouse move to where to practice your eyeball.
2. Keep mouse alive and prevent system from sleeping.
3. Avoid triggering Hot Corners on macOS.

## Documentation

- **[Interactive Demo](https://htmlpreview.github.io/?https://github.com/murphytsai/mouse-rover/blob/main/demo.html)** - Try it online! See how Mouse Rover works visually
  - Or download [demo.html](demo.html) and open locally in your browser
- **[Design Specification](DESIGN_SPEC.md)** - Complete design guide for Figma/UI implementation

## Usage
```
$ pip install -r requirements.txt

$ python mouse-rover.py -h
usage: mouse-rover.py [-h] [-a] [-s] [-t TIME]

control for mouse-rover.

optional arguments:
  -h, --help            show this help message and exit
  -a, --always          execute always.
  -s, --small           move in small range.
  -t TIME, --time TIME  trigger interval.

# move randomly every 10 secs.
$ python mouse-rover.py -t10 -a
 ```
