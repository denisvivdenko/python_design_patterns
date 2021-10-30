# Singleton

The singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.

The main criticism of the singleton pattern is that it is just a pretty way to get a global
state, which is one of the things you want to avoid when writing programs. One of the
reasons why you want to avoid global state is that code in one part of your project may
alter the global state and cause unexpected results in a completely unrelated piece of
code.


That said, when you have parts of a project that do not affect the execution of your
code, like logging, it is acceptable to use global state. Other places where global state
may be used are in caching, load balancing, and route mapping. In all these cases,
information flows in one direction, and the singleton instance itself is immutable (it does
not change). No part of the program attempts to make a change in the singleton, and
as such there is no danger of one part of a project interfering with another part of the
project because of the shared state.

# Additional Information

- Attributes of a class are function objects that define corresponding methods of its instances. 

- The __getattr__ method intercepts attribute references and the __setattr__ intercepts all attribute assignments.

```
  def __getattr__(self, name):
    return getattr(self.instance, name)

  def __setattr__(self, name):
    return setattr(self.instance, name)
```

- Whenever a class is instantiated __new__ and __init__ methods are called. __new__ method will be called when an object is created and __init__ method will be called to initialize the object. In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls. cls represents the class that is needed to be instantiated, and the compiler automatically provides this parameter at the time of instantiation.

```
 def __new__(cls):
    if not SingletonObject.instance:
      SingletonObject.instance = SingletonObject.__SingletonObject()
```