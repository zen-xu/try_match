# try_match
Pattern matching

It supports Python 2.7 and 3+

# Installation
Using pip to install
```bash
pip install try-match
```

# Usage
```python
from try_match import Case, match, DefaultCase

### match value
try:
    match(1)
except Case(2):
    raise
except Case(1):
    print(1)
   
# => 1


### match class
try:
    match(1)
except Case(str):
    raise
except Case(int):
    print('int')
    
# => 'int'


### match range
try:
    match(10)
except Case(range(1, 5)):
    raise
except Case(range(9, 20)):
    print(range(9, 20))
    
# => range(9, 20)


### match lambda
try:
    match(2)
except Case(lambda x > 5):
    raise
except Case(lambda x < 5):
     print("x < 5")
     
# => "x < 5"


### default case
try:
    match(1)
except Case(2):
    raise
except Case(3):
    raise
except DefaultCase:
    print("default")
    
# => "default"
```

✨🍰✨ enjoy it
