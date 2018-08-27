# Python: Frequently Used Terms

### Class
A "template" or constructor for *objects*, which can combine information and behavior. Used in Object-Oriented Programming. Creating a new *class* creates a new type of *object*, allowing new *instances* of that type to be made. To create a class, use the keyword `class`:

```
>>> class MyClass:      # here we create the class
>>>   x = 5

>>> p1 = MyClass()      # here we create the object (see below)
>>> print(p1.x)
  5
```

### Object
An encapsulation of variables and functions. In Python, everything is an object: strings, lists, functions--even modules. Typically, an object is a member or an "instance" of a class: it takes variables and functions from that class. It Accepts *arguments* (called *parameters*), and possible `return` objects.

```
>>> p1 = MyClass()    # p1 is an object
>>> print(p1.x)
  5
```

### Variable
A reserved memory location to store values. When you create a variable you reserve some space in memory.

### Function
A callable object. A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

### Method
A function that belongs to an *object*. E.g. list objects have methods called `.append`, `.insert`, `.remove`, `.sort`, and so on.

### Expression
Combinations of values and operators that always evaluate down to a single value. E.g. the code snippet `2 * 2`

### Statement
An instruction that does not evaluate down to a value. E.g. the code snippet `while True:`

### Parameter
These are defined by the names that appear in a function definition. E.g. `def calc_sum(a,b):`

### Argument
The values actually passed to a *function* when calling it. E.g. `calc_sum(2,5)`

### Recursive function
Function that, somewhere in its body, calls itself.
