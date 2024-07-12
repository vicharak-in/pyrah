# RAH protocol wrapper in python

## Installation

```sh
git clone https://github.com/vicharak-in/pyrah
sudo python3 setup.py install
```

## Usage

```python
import pyrah

APPID = 3

pyrah.rah_write(APPID, b"Hello World!")
data = pyrah.rah_read(APPID, 10) # Here 10 is length of data count we need
print(data)
```
