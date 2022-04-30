# BrainfuckPy
A simple Brainfuck interpreter written in Python.

## Usage
### CLI
The interpreter can either evaluate a file by running:
```
python3 bf-cli.py -f <file>
```
or a string with:
```
python3 bf-cli.py -s <string>
```

### Module
For usage of the interpreter inside another Python script, run:
```python3
from brainfuck import brainfuck

brainfuck(code)
```

## License
Copyright © 2022 [Hüseyin Çelik](https://www.github.com/hueseyincelik).

This project is licensed under [AGPL v3](/LICENSE).
