# Common error messages (and how to fix them)

In general: whatever error you're running into, **you're not the first!** Copy-pasting your error message in Google will often point you to a query on Stack Overflow or Github detailing a similar problem as the one you're having. **Google (or DuckDuckGo!) is your friend**, and a big tip for any programmer is to search for answers to the problems you are having. Solving something on your own can be very rewarding!

## SyntaxError

Syntax errors are the most basic type of error. They arise when Python is unable to understand a line of code. These little errors pop up all the time, due to small errors we make.

```
>>> def just_a_number()
>>>    number = 5

---------------------------------------------------------------------------
Traceback (most recent call last):
File "<stdin>", line 1
  def just_a_number()
                     ^
SyntaxError: invalid syntax
```

### How to fix it.

Note that Python is telling you where the error is. Pay attention to what your error messages say so you can trace your errors quicker.

## TypeError

You'll usually see this if you try to treat one type as if it's another. If I try to add together an integer (`int`) and a string (`str`), for instance, it'll tell me that it doesn't know how to do this:  

```
>>> 2 + "Hello!"

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## IndexError: list index out of range

This usually means you're trying to get an item from a list, but that item doesn't exist. For example:

```
>>> myList = ["Apples", "Bananas", "Oranges"]
>>> print(myList[3])

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

### How to fix it.

This sometimes happens if you just get the index wrong for the thing you're looking for. In that case, simply correct the index. (In the case above, try `myList[2]` instead of `myList[3]`.)

Other times, this happens because you're assuming a list is so long, but it isn't actually. This can happen when you, say, try to truncate a text with something like `myText[:2000]`. If your text isn't at least 2000 words (or letters, if it's a string), this will fail. To fix this, check the length before you index:

```
if len(myText) >= 2000:
    firstChunk = myText[:2000]
```


## KeyError

This happens when you're looking for a particular item in a dictionary, but that item doesn't exist. For example:

```
>>> inventory = {"Apples": 5, "Bananas": 10, "Peaches": 0}
>>> inventory["Kiwis"]

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Kiwis'
```

### How to fix it.

Instead of looking up the item in the dictionary, you can use the dictionary `.get()` method, which will return `None` by default if it can't find an item.

Or you can just test whether an item is in the dictionary, first:

```
>>> inventory = {"Apples": 5, "Bananas": 10, "Peaches": 0}
>>> if "Kiwis" in inventory:
        print(inventory["Kiwis"])
```

## IndentationError

These errors pop up when you're not properly indenting your code. Python cares about this; some other languages (e.g. C) do not.

```
>>> def just_a_number():
>>> number = 5

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
number = 5
     ^
IndentationError: expected an indented block
```

### How to fix it.

Go through your code (the error message will tell you where it's happening!) and check if you have indented your code properly; e.g. when calling a function or in a for-loop.

## NameError

This happens when you're trying to do something with a variable that doesn't exist.  

```
>>> print(a)

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

Be aware that variables exist within a certain *scope*. If you assign a variable in some Jupyter notebook, for instance, you can't call it in anther. This also goes for functions: assigning a variable in a function does not work outside of the scope of that function.

```
>>> def just_a_number():
>>>    number = 5

>>>number += 1

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counter' is not defined
```

### How to fix it.

Backtrack in your code to see if the variable that you think exists, actually does. When it does exist, check the *scope* within which it exists.

## AttributeError

An attribute, in Python, refers to some property that is associated with a particular type of object. You usually call them with the `.` notation. Think about attributes as nouns that belong to an object: the data and abilities that each object type inherently possesses. AttributeErrors are generally raised when Python can't find a specified data or method attribute on an object.

```
>>> myNumber = 8
>>> myNumber.append(4)

---------------------------------------------------------------------------
Traceback (most recent call last)
  File "<stdin>", line 1, in <module>
      1 import nltk
      2
----> 3 tokens = nltk.what("this is a test")

AttributeError: module 'nltk' has no attribute 'what'
```

### How to fix it.

Check all the attributes belonging to the object by calling the built-in function `help()` on an object of that type.

```
>>> help(nltk)
```

##FileNotFoundError

This happens when you're trying to work with something that Python can't locate.

```
>>> text = open("notthere.txt")

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'notthere.txt'
```

These kinds of errors often show up when you are using functions such as `os.listdir`, which offers a list of all filenames in a path. The function will not give you the **entire** path from where your notebook is, just the filenames!

```
>>> import os
>>> path = os.listdir('data') # There is a folder named "data" in the folder I am currently in
>>> path
'Airbnb-reviews.csv',
'austen-emma.txt',
'twitter.txt'

>>> file = open("twitter.txt")

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'twitter.txt'
```

### How to fix it.

Always check if Python is looking into the same directory you think it's looking.

```
>>> file = open("data/twitter.txt")
```

## ImportError

This happens when you're trying to import something from a module that doesn't exist.

```
>>> from nltk import wonderful_tokenizer

---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'wonderful_tokenizer'
```

### How to fix it

`help()` is your friend here: it will yield the package content of the module you're importing. Also, get used to reading a module's documentation.

```
>>> help(nltk)
```

## Unexpected results

### If you get a list of letters instead of words

Python will try to run a `for` loop over anything, even if it's not a list. If you run a `for` loop over a string, for instance, it'll iterate over the letters.

```
for item in "Hello world!":
    print(item)
```

#### How to fix it

Tokenize your string, so that you're looping over the words (tokens), and not the string itself.
