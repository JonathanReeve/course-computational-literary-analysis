# Common error messages (and how to fix them)

## TypeError

You'll usually see this if you try to treat one type as if it's another. If I try to add together an integer (`int`) and a string (`str`), for instance, it'll tell me that it doesn't know how to do this:  

```
>>> 2 + "Hello!"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## IndexError: list index out of range 

This usually means you're trying to get an item from a list, but that item doesn't exist. For example: 

```py
>>> myList = ["Apples", "Bananas", "Oranges"]
>>> print(myList[3]) 

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


## Unexpected results

### If you get a list of letters instead of words

Python will try to run a `for` loop over anything, even if it's not a list. If you run a `for` loop over a string, for instance, it'll iterate over the letters. 

```python
for item in "Hello world!": 
    print(item)
```

#### How to fix it

Tokenize your string, so that you're looping over the words (tokens), and not the string itself. 

###  

