# RAH protocol wrapper in python

## Installation

```sh
git clone https://github.com/vicharak-in/pyrah
sudo python3 setup.py install
```

## Usage

```python
import pyrah

pyrah.rah_write(b"Hello World!")
data = pyrah.rah_read()
print(data)
```
