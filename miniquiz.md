## Mini Quiz

This mini quiz will cover object oriented principles and Python scoping.  You should be able to finish this in 15 minutes (but can in less than 5min) using the required readings as a resources.

1. Python Scope -- What should get printed to the console and why (try to do it without running the code)?

```python
def append_to_list(element, my_list=[]):
    my_list.append(element)
    return my_list
    
first_list = append_to_list(12)
print first_list

second_list = append_to_list(42)
print second_list
```


2. Python Modules
What do you need to do to make a folder a Python package?  Assume this is what I want:

```bash
├── my_project
│   ├── code
│   │   └── functions.py
│   ├── main.py
│   └── readme.md
```

```python
# file main.py

from code import functions

...
```


3. Classes -- What does each of the last two lines return?
```python
def bar(self,y):
    return self.x + y
 
class Foo(object):
    x = 9
    def __init__(self,x):
        self.x = x
    bar = bar

foo = Foo(5)

# What happens here?
print Foo.bar(foo,4) == 9
print Foo.bar(Foo,0) == 9
```
