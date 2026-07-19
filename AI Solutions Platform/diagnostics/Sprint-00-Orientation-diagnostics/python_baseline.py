# # /*
# # Yes, Python has **classes**, but it does **not** have `struct`s in the same sense as C, C++, or Swift.

# # Here's how to think about it coming from Swift.

# # | Swift      | Python Equivalent    | Notes                                 |
# # | ---------- | -------------------- | ------------------------------------- |
# # | `class`    | `class`              | ✅ Exists                              |
# # | `struct`   | No direct equivalent | ❌ Doesn't exist as a language feature |
# # | `enum`     | `Enum`               | ✅ Exists via module                   |
# # | `protocol` | `Protocol` (typing)  | ✅ Exists for type hints               |

# # ## Python Classes

# # A Python class looks very familiar:

# # ```python
# # class User:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def greet(self):
# #         print(f"Hi, I'm {self.name}")
# # ```

# # Usage:

# # ```python
# # u = User("Swapnil", 25)

# # print(u.name)   # Swapnil
# # u.greet()
# # ```

# # Very similar to Swift:

# # ```swift
# # class User {
# #     let name: String
# #     let age: Int

# #     init(name: String, age: Int) {
# #         self.name = name
# #         self.age = age
# #     }

# #     func greet() {
# #         print("Hi, I'm \(name)")
# #     }
# # }
# # ```

# # ---

# # # What about structs?

# # Python doesn't have a `struct` keyword.

# # Instead, there are several ways to represent lightweight data.

# # ### Option 1: `dataclass` (closest to Swift struct)

# # ```python
# # from dataclasses import dataclass

# # @dataclass
# # class User:
# #     name: str
# #     age: int
# # ```

# # Usage:

# # ```python
# # u = User("Swapnil", 25)

# # print(u.name)
# # print(u.age)
# # ```

# # Swift equivalent:

# # ```swift
# # struct User {
# #     let name: String
# #     let age: Int
# # }
# # ```

# # `@dataclass` automatically generates:

# # * constructor
# # * `__repr__`
# # * equality (`==`)
# # * and more

# # For many "data-only" objects, this is the closest Python analogue to a Swift `struct`.

# # ---

# # ### Option 2: Frozen dataclass (immutable)

# # Swift structs are often used immutably. You can get similar behavior:

# # ```python
# # from dataclasses import dataclass

# # @dataclass(frozen=True)
# # class User:
# #     name: str
# #     age: int
# # ```

# # Now:

# # ```python
# # u.age = 30
# # ```

# # raises an error.

# # ---

# # ## But aren't Python classes reference types?

# # Yes.

# # Every normal Python class instance is a **reference type**.

# # ```python
# # class User:
# #     def __init__(self, name):
# #         self.name = name

# # a = User("Swapnil")
# # b = a

# # b.name = "John"

# # print(a.name)
# # ```

# # Output:

# # ```
# # John
# # ```

# # Exactly like a Swift `class`.

# # ---

# # ## Swift struct copies vs Python objects

# # Swift:

# # ```swift
# # struct User {
# #     var name: String
# # }

# # var a = User(name: "Swapnil")
# # var b = a

# # b.name = "John"

# # print(a.name)
# # ```

# # Output:

# # ```
# # Swapnil
# # ```

# # because structs are value types.

# # Python doesn't do this automatically. Assignment copies the reference:

# # ```python
# # from dataclasses import dataclass

# # @dataclass
# # class User:
# #     name: str

# # a = User("Swapnil")
# # b = a

# # b.name = "John"

# # print(a.name)
# # ```

# # Output:

# # ```
# # John
# # ```

# # If you want an independent copy, use the `copy` module:

# # ```python
# # import copy

# # b = copy.copy(a)       # shallow copy
# # # or
# # b = copy.deepcopy(a)   # deep copy
# # ```

# # ---

# # ## Does Python have something called `struct`?

# # Yes, but it's unrelated to object modeling. The standard library includes a module named `struct` for working with binary data:

# # ```python
# # import struct

# # packed = struct.pack("i", 42)
# # number = struct.unpack("i", packed)
# # ```

# # This is used for reading and writing binary formats, network packets, and similar low-level tasks—not as an alternative to classes.

# # ---

# # ## Summary for a Swift Developer

# # | Swift               | Python                                                                           |
# # | ------------------- | -------------------------------------------------------------------------------- |
# # | `class`             | `class`                                                                          |
# # | `struct`            | `@dataclass` (closest concept)                                                   |
# # | Value semantics     | Not automatic; use copying if needed                                             |
# # | Reference semantics | Default for all class instances and dataclass instances                          |
# # | Immutable struct    | `@dataclass(frozen=True)` (prevents mutation, but does not make it a value type) |

# # Since you're learning Python for AI systems, you'll see `@dataclass` frequently in frameworks because it's a concise way to define configuration objects, messages, request/response models, and other data containers while keeping the code clean.


# # This is one of the most important concepts in Python, especially when you're building AI agents, working with JSON, state management, or message passing.

# # Since you come from Swift, I'll compare everything with Swift reference semantics.

# # ---

# # # Imagine a House

# # Suppose you have a house.

# # Inside the house:

# # * Sofa
# # * TV
# # * Kitchen
# # * Bedroom

# # Now imagine you want another copy of this house.

# # There are **two ways**.

# # ## 1. Shallow Copy

# # A shallow copy builds **a new house**, but **puts the same furniture inside**.

# # ```
# # Original House                 Shallow Copy

# # +-----------+                 +-----------+
# # | Sofa -----|---------------->| Same Sofa |
# # | TV -------|---------------->| Same TV   |
# # | Kitchen --|---------------->| Same Kit. |
# # +-----------+                 +-----------+
# # ```

# # The houses are different.

# # The furniture is shared.

# # ---

# # ## 2. Deep Copy

# # Deep copy builds

# # * new house
# # * new sofa
# # * new TV
# # * new kitchen
# # * everything new.

# # ```
# # Original House               Deep Copy

# # House A                      House B

# #  Sofa A      -------->       Sofa B

# #  TV A        -------->       TV B

# #  Kitchen A   -------->       Kitchen B
# # ```

# # Nothing is shared.

# # ---

# # # Let's see in Python

# # Suppose we have

# # ```python
# # person = {
# #     "name": "Swapnil",
# #     "skills": ["Swift", "Python"]
# # }
# # ```

# # Notice

# # ```
# # Dictionary
# #     |
# #     +-- name
# #     |
# #     +-- skills ---> List
# # ```

# # The list is another object.

# # ---

# # # Shallow Copy

# # ```python
# # import copy

# # person2 = copy.copy(person)
# # ```

# # Memory becomes

# # ```
# # person
# #    |
# #    +---- name

# #    +---- skills --------+
# #                          |
# #                          V
# #                   ["Swift","Python"]

# # person2
# #    |
# #    +---- name

# #    +---- skills --------+
# # ```

# # The dictionary itself is copied.

# # The list is NOT.

# # Both dictionaries point to the same list.

# # ---

# # Now modify the list.

# # ```python
# # person2["skills"].append("AI")
# # ```

# # Now

# # ```
# # person["skills"]
# # ```

# # becomes

# # ```
# # ["Swift","Python","AI"]
# # ```

# # Even though you modified `person2`.

# # Why?

# # Because the list was shared.

# # ---

# # Changing a top-level value doesn't affect the original:

# # ```python
# # person2["name"] = "John"
# # ```

# # Now

# # ```
# # person["name"]
# # ```

# # is still

# # ```
# # Swapnil
# # ```

# # because strings are immutable, and the `"name"` entry in the copied dictionary now points to a different string.

# # ---

# # # Deep Copy

# # Now

# # ```python
# # import copy

# # person2 = copy.deepcopy(person)
# # ```

# # Memory

# # ```
# # person

# # Dictionary
# #      |
# #      +---- List A

# # person2

# # Dictionary
# #      |
# #      +---- List B
# # ```

# # Everything is copied.

# # Now

# # ```python
# # person2["skills"].append("AI")
# # ```

# # Only

# # ```
# # person2
# # ```

# # changes.

# # Original remains

# # ```
# # ["Swift","Python"]
# # ```

# # ---

# # # Visualizing Memory

# # Original

# # ```
# # person

# # Dictionary
# #  |
# #  +-- "Swapnil"

# #  +---> List

# #        Swift

# #        Python
# # ```

# # ---

# # After shallow copy

# # ```
# # person ----------------------+

# #                              |

# # Dictionary A                 |

# #  |                           |

# #  +-----------> List <---------+

# #               Swift

# #               Python

# # Dictionary B
# # ```

# # Two dictionaries.

# # One list.

# # ---

# # After deep copy

# # ```
# # Dictionary A

# #    |

# #    +----> List A

# # Dictionary B

# #    |

# #    +----> List B
# # ```

# # Completely separate.

# # ---

# # # Nested Objects

# # Suppose

# # ```python
# # company = {
# #     "employees": [
# #         {
# #             "name": "Swapnil",
# #             "skills": ["Swift", "Python"]
# #         }
# #     ]
# # }
# # ```

# # There are several layers of objects:

# # ```
# # Dictionary

# # ↓

# # List

# # ↓

# # Dictionary

# # ↓

# # List
# # ```

# # A shallow copy duplicates **only the outermost dictionary**. Every nested object (the list of employees, each employee dictionary, the skills list) is still shared.

# # A deep copy recursively duplicates **every nested object**, so none of them are shared.

# # ---

# # # Why AI Engineers Care

# # Imagine an agent state:

# # ```python
# # state = {
# #     "conversation": [...],
# #     "memory": {...},
# #     "tools": [...]
# # }
# # ```

# # Worker A receives

# # ```python
# # state_copy = copy.copy(state)
# # ```

# # It thinks it's working on its own copy.

# # Then it does

# # ```python
# # state_copy["conversation"].append(new_message)
# # ```

# # Suddenly

# # Worker B also sees that message because the `"conversation"` list was shared.

# # This kind of bug is common when working with nested mutable data.

# # Using

# # ```python
# # copy.deepcopy(state)
# # ```

# # gives each worker its own independent conversation history.

# # ---

# # # Swift Comparison

# # Swift structs use **value semantics**, so assignment creates an independent value:

# # ```swift
# # struct User {
# #     var skills = ["Swift"]
# # }

# # var a = User()
# # var b = a

# # b.skills.append("Python")
# # ```

# # `a.skills` remains:

# # ```
# # ["Swift"]
# # ```

# # because `struct` is a value type. (Swift also uses an optimization called *copy-on-write*, so the actual memory copy may be deferred until one copy is mutated.)

# # Swift classes use **reference semantics**:

# # ```swift
# # class User {
# #     var skills = ["Swift"]
# # }

# # let a = User()
# # let b = a

# # b.skills.append("Python")
# # ```

# # Now both `a.skills` and `b.skills` are:

# # ```
# # ["Swift", "Python"]
# # ```

# # because `a` and `b` reference the same object.

# # ---

# # # Quick Summary

# # | Operation            | Outer object | Nested mutable objects | Result       |
# # | -------------------- | ------------ | ---------------------- | ------------ |
# # | Assignment (`b = a`) | Shared       | Shared                 | Same object  |
# # | `copy.copy(a)`       | New          | Shared                 | Shallow copy |
# # | `copy.deepcopy(a)`   | New          | New                    | Deep copy    |

# # **Rule of thumb:** if your object contains nested mutable objects (lists, dictionaries, sets, or custom objects) and you need a truly independent copy, use `copy.deepcopy()`. If only the outer container needs to be separate while sharing the contents is acceptable, a shallow copy is enough.

# # */

# # from dataclasses import dataclass
# # import asyncio
# # from typing import Protocol

# # @dataclass(frozen = True)
# # class WorkItem:
# #     item_id : str
# #     delay_seconds: float

# # item = WorkItem("a", 0.5)
# # #  item.item_id = "c" --> Throws error

# # class Writable(Protocol):
# #     def write(self, data: dict) -> None:
# #         """This method should write dictionary data."""

# # class Readable(Protocol):
# #     def read(self) -> dict:
# #         """This method should return a dictionary data."""

# # def do_write(writer: Writable, data:dict) -> None:
# #     writer.write(data)

# # def do_read(reader:Readable) -> dict:
# #     return reader.read()

# # @dataclass
# # class Author:
# #     name : str
# #     def write(self, data: dict) -> None:
# #         print(f"{self.name} is writing {data}")    

# # def main():
# #     data = {'name':'Swapnil Dhiman', 'age':30}
# #     author = Author('Swapnil Dhiman from class')
# #     do_write(author,data)

# # class Dog :
# #     def __init__(self, name):
# #         self.name = name

# # from abc import ABC, abstractmethod

# # class Payment(ABC):
# #     @abstractmethod
# #     def pay(self):
# #         pass

# # # class UPI(Payment):
# # #     pass

# # # myUPI = UPI() #Python Checks at Instantiation, Not Definition - Will fail if not defined pay

# # class UPI(Payment):
# #     def pay(self):
# #         print("UPI payment is getting done")

# # upi = UPI()
# # upi.pay()

# # print("Swapnil Dhiman")

# from abc import ABC, abstractmethod
# from typing import Protocol
# from dataclasses import dataclass


# @dataclass
# class WorkItem:
#     item_id : int

# class BaseProcessor(ABC):
#     @abstractmethod
#     def process(self,item):
#         pass

# class APIProcessor(BaseProcessor):
#     def process(self,item):
#         return f"API processed {item.item_id}"

# class FakeProcessor:
#     def process(self,item):
#         return f"API processed {item.item_id}"

# class Processor(Protocol):
#     def process(self,item):
#         ...

# def run(processor:Processor, item):
#     print(processor.process(item))

# item = WorkItem(8)

# api_processor = APIProcessor()
# fake_processor = FakeProcessor()

# run(api_processor, item)
# run(fake_processor, item)


# '''
# Perfect. I actually know **why** you're overwhelmed.

# You're trying to learn **five different concepts at once**, but they depend on one another.

# Imagine someone teaching an iOS developer:

# > "Let's learn Combine. Today we'll cover Publisher, Subscriber, AnyPublisher, Protocol, Generic Constraints, @escaping closures, Result type, Schedulers and AsyncSequence."

# You'd probably say:

# > "Wait... I don't even know what Publisher is."

# That's exactly what's happening here.

# ---

# # Here's how we're going to learn it

# We'll build everything in this order:

# ```
# 1. Classes
#       ↓
# 2. Objects
#       ↓
# 3. self
#       ↓
# 4. Inheritance
#       ↓
# 5. Abstract Classes (ABC)
#       ↓
# 6. Abstract Methods
#       ↓
# 7. Protocol
#       ↓
# 8. Duck Typing
#       ↓
# 9. Iterator
#       ↓
# 10. Connect everything together
# ```

# By the end, the code you pasted will feel almost obvious.

# ---

# # PART 1 — Classes

# You already know Swift.

# Swift

# ```swift
# class Dog {

#     var name: String

#     init(name: String) {
#         self.name = name
#     }

#     func bark() {
#         print("\(name) Woof!")
#     }
# }
# ```

# Python

# ```python
# class Dog:

#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} Woof!")
# ```

# Looks similar.

# ---

# Create object

# ```python
# dog = Dog("Bruno")
# dog.bark()
# ```

# Output

# ```
# Bruno Woof!
# ```

# Nothing scary yet.

# ---

# # PART 2 — What is self?

# This is the FIRST thing that confuses every Swift developer.

# You see this:

# ```python
# def bark(self):
# ```

# and wonder

# > Why am I passing myself??

# Actually...

# You're NOT.

# Python does it automatically.

# Suppose

# ```python
# dog.bark()
# ```

# Python secretly converts this into

# ```python
# Dog.bark(dog)
# ```

# Read that again.

# When you write

# ```python
# dog.bark()
# ```

# Python internally does

# ```python
# Dog.bark(dog)
# ```

# Therefore

# ```
# self == dog
# ```

# Literally.

# ---

# Let's prove it.

# ```python
# class Dog:

#     def bark(self):
#         print(self)
# ```

# ```
# dog = Dog()

# dog.bark()
# ```

# Output

# ```
# <Dog object at 0x103ab....>
# ```

# That is literally the object.

# So

# ```
# self

# ↓

# current object
# ```

# Exactly the same as Swift

# ```swift
# self.name
# ```

# Python just makes it explicit.

# ---

# # Why do we write self.name?

# Suppose

# ```python
# class Dog:

#     def __init__(self, name):

#         self.name = name
# ```

# There are TWO names.

# ```
# parameter

# ↓

# name
# ```

# and

# ```
# object property

# ↓

# self.name
# ```

# Exactly like Swift

# ```swift
# self.name = name
# ```

# Nothing different.

# ---

# # PART 3 — Inheritance

# Suppose we have

# ```
# Animal
# ```

# Dogs are animals.

# Cats are animals.

# Instead of rewriting everything...

# We inherit.

# Swift

# ```swift
# class Animal {

#     func eat() {
#         print("Eating")
#     }
# }

# class Dog: Animal {

#     func bark() {
#         print("Woof")
#     }
# }
# ```

# Python

# ```python
# class Animal:

#     def eat(self):
#         print("Eating")
# ```

# Child

# ```python
# class Dog(Animal):

#     def bark(self):
#         print("Woof")
# ```

# Notice

# ```
# Dog(Animal)
# ```

# means

# ```
# Dog inherits Animal
# ```

# Usage

# ```python
# dog = Dog()

# dog.eat()
# dog.bark()
# ```

# Output

# ```
# Eating

# Woof
# ```

# Dog got eat()

# for free.

# ---

# # PART 4 — Why Abstract Classes exist

# Suppose you're building Walmart.

# You have

# ```
# Payment
# ```

# Can someone pay with

# ```
# Payment()
# ```

# No.

# Payment is just an IDEA.

# Real payments are

# ```
# UPI

# Credit Card

# PayPal
# ```

# So

# ```
# Payment
# ```

# should NEVER be created.

# It only describes what payments should do.

# That's an Abstract Class.

# ---

# Python

# ```python
# from abc import ABC
# ```

# ABC means

# ```
# Abstract Base Class
# ```

# Think

# ```
# Blueprint
# ```

# not

# ```
# Actual building
# ```

# ---

# # PART 5 — Abstract Method

# Suppose every payment MUST have

# ```
# pay()
# ```

# But Payment itself doesn't know HOW.

# UPI pays differently.

# Card pays differently.

# So

# ```python
# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass
# ```

# Notice

# ```
# pass
# ```

# Means

# ```
# Nothing here.

# Children must implement.
# ```

# ---

# Child

# ```python
# class UPI(Payment):

#     def pay(self):
#         print("Paid using UPI")
# ```

# Another

# ```python
# class CreditCard(Payment):

#     def pay(self):
#         print("Paid using Card")
# ```

# Now

# ```python
# upi = UPI()

# upi.pay()
# ```

# Works.

# But

# ```python
# Payment()
# ```

# Error.

# Because

# ```
# Payment

# ↓

# Incomplete Blueprint
# ```

# ---

# Swift equivalent

# ```swift
# class Payment {

#     func pay() {

#         fatalError("Override me")
#     }
# }
# ```

# Same idea.

# Swift doesn't have abstract classes, so developers simulate them with `fatalError()` or protocols.

# ---

# # PART 6 — Protocol

# This is the MOST IMPORTANT concept.

# Forget Python.

# Let's use Swift.

# You know

# ```swift
# protocol Payment {

#     func pay()
# }
# ```

# Now

# ```swift
# class UPI: Payment {

#     func pay() {

#     }
# }
# ```

# and

# ```swift
# class Card: Payment {

#     func pay() {

#     }
# }
# ```

# Great.

# ---

# Python Protocol is basically the SAME idea.

# ```python
# from typing import Protocol

# class Payment(Protocol):

#     def pay(self):
#         ...
# ```

# Notice

# ```
# ...
# ```

# Three dots.

# Means

# ```
# Implementation intentionally missing.
# ```

# Equivalent to

# ```
# pass
# ```

# here.

# ---

# Now here's the magic.

# Swift

# ```
# Must inherit protocol.
# ```

# Python

# No.

# Look.

# ```python
# class UPI:

#     def pay(self):
#         print("UPI")
# ```

# Never inherited.

# Still works.

# Why?

# Because Python checks

# ```
# Does it have pay() ?

# YES.

# Good enough.
# ```

# That's called

# ```
# Structural Typing
# ```

# ---

# # Duck Typing

# The funniest name.

# Imagine.

# You see an animal.

# ```
# Quack

# Walks like duck

# Looks like duck
# ```

# You don't ask

# ```
# Are you officially registered Duck?
# ```

# You simply say

# ```
# Good enough.

# It's a duck.
# ```

# Python does exactly this.

# Suppose

# ```python
# class Dog:

#     def sound(self):

#         print("Woof")
# ```

# and

# ```python
# class Cat:

#     def sound(self):

#         print("Meow")
# ```

# Now

# ```python
# def make_sound(animal):

#     animal.sound()
# ```

# Notice

# We NEVER checked

# ```
# Dog?

# Cat?

# Animal?
# ```

# We don't care.

# If it has

# ```
# sound()
# ```

# It works.

# ```python
# make_sound(Dog())

# make_sound(Cat())
# ```

# Output

# ```
# Woof

# Meow
# ```

# This philosophy is called **duck typing**:

# > "If it walks like a duck and quacks like a duck, treat it as a duck."

# ---

# # ABC vs Protocol

# This is where most people get confused.

# ## ABC (Nominal Typing)

# Think of it as a club membership.

# ```
# Gym Members

# ↓

# Only registered members enter.
# ```

# ```python
# class UPI(Payment)
# ```

# You must explicitly inherit from `Payment`.

# Without inheritance:

# ```
# Not allowed.
# ```

# ---

# ## Protocol (Structural Typing)

# Think of a driving test.

# The instructor doesn't care where you learned.

# They only check:

# ```
# Can you drive?

# Yes.

# Pass.
# ```

# Python checks:

# ```
# Do you have pay() ?

# Yes.

# Welcome.
# ```

# No inheritance needed.

# ---

# # Iterator

# Now another scary word.

# Suppose

# ```python
# numbers = [10,20,30]
# ```

# When you write

# ```python
# for x in numbers:
#     print(x)
# ```

# Python is secretly doing something like this:

# ```python
# it = iter(numbers)

# while True:
#     x = next(it)
#     print(x)
# ```

# An **iterator** is simply an object that remembers "where am I?" as you move through a collection.

# Think of it like a bookmark in a book.

# ```
# Page 1
#  ^
# Bookmark

# next()

# ↓

# Page 2

# next()

# ↓

# Page 3
# ```

# The bookmark keeps moving.

# That's all an iterator does.

# ---

# # Finally... let's connect EVERYTHING

# Imagine we're building a tiny AI processing system.

# ```python
# from abc import ABC, abstractmethod
# from typing import Protocol

# # ----------------------------
# # A simple piece of work
# # ----------------------------
# class WorkItem:
#     def __init__(self, item_id):
#         self.item_id = item_id


# # ----------------------------
# # ABC
# # Every processor MUST implement process()
# # ----------------------------
# class BaseProcessor(ABC):

#     @abstractmethod
#     def process(self, item):
#         pass


# # ----------------------------
# # Inherits from ABC
# # ----------------------------
# class APIProcessor(BaseProcessor):

#     def process(self, item):
#         return f"API processed {item.item_id}"


# # ----------------------------
# # Doesn't inherit anything
# # But has process()
# # ----------------------------
# class FakeProcessor:

#     def process(self, item):
#         return f"Fake processed {item.item_id}"


# # ----------------------------
# # Protocol
# # Says "anything with process() is OK"
# # ----------------------------
# class Processor(Protocol):

#     def process(self, item):
#         ...


# # ----------------------------
# # This function works with any
# # object that has process()
# # ----------------------------
# def run(processor: Processor, item):
#     print(processor.process(item))


# item = WorkItem(101)

# real = APIProcessor()
# fake = FakeProcessor()

# run(real, item)
# run(fake, item)
# ```

# Output:

# ```
# API processed 101
# Fake processed 101
# ```

# Notice what happened:

# * `WorkItem` is a **class** that represents data.
# * `self` refers to the current object inside each method.
# * `APIProcessor` **inherits** from `BaseProcessor`.
# * `BaseProcessor` is an **Abstract Base Class**, so it can't be instantiated and forces subclasses to implement `process()`.
# * `FakeProcessor` doesn't inherit from anything.
# * The `Processor` **Protocol** only describes the required shape ("must have a `process()` method").
# * `run()` accepts **any** object that matches that shape—this is **duck typing** combined with **structural typing**.

# ---

# # One final mapping for a Swift developer

# | Swift                            | Python                                                              |
# | -------------------------------- | ------------------------------------------------------------------- |
# | `class`                          | `class`                                                             |
# | `struct`                         | `@dataclass` (closest equivalent)                                   |
# | `self`                           | `self` (explicit parameter in method definitions)                   |
# | `class Dog: Animal`              | `class Dog(Animal)`                                                 |
# | `protocol`                       | `Protocol`                                                          |
# | `protocol` conformance           | Usually automatic if the required methods exist (structural typing) |
# | `fatalError("Override")` pattern | `ABC` + `@abstractmethod`                                           |
# | `for item in array`              | Uses an iterator under the hood                                     |

# ---

# ## My suggestion for our AI Engineering journey

# Don't try to master all of this in one sitting. You're coming from Swift, where protocols, inheritance, and value/reference semantics already exist, but Python expresses them differently.

# I recommend we spend the next few chapters building a small multi-agent system from scratch. We'll naturally encounter `self`, classes, inheritance, protocols, abstract base classes, iterators, async functions, and type hints in realistic code. By the time we finish that project, these concepts will feel familiar because you'll have *used* them repeatedly rather than just memorized definitions.
# '''

import asyncio

async def task1():
    print("Task 1 starting")
    await asyncio.sleep(2)
    print("Task 1 completed")
    return "result1"


async def task2():
    print("Task 2 starting")
    await asyncio.sleep(1)
    print("Task 2 completed")
    return "result2"

async def main():
    result1, result2 = await asyncio.gather(task1(),task2())
    print(f"Results: {result1}, {result2}")

asyncio.run(main())

'''
Awesome. This actually tells me **where you're stuck**.

You're **not confused by the syntax**.

You're confused by **"Why do these three APIs all exist? They all seem to run multiple tasks."**

That's exactly the right question.

Think of it like this:

> **`create_task()`, `gather()`, and `TaskGroup` are not three different concurrency models.**
>
> They are **three different ways of managing the same tasks.**

This is very similar to iOS.

You can create threads using

* `DispatchQueue.async`
* `OperationQueue`
* Swift `Task`
* `TaskGroup`

All execute work.

The difference is **who manages the lifetime of the work**.

---

# Let's build a real story.

Imagine you're the engineering manager at Walmart.

You have three engineers.

```text
Alice
Bob
Charlie
```

And three tickets.

```text
Ticket A
Ticket B
Ticket C
```

Your goal is to finish all tickets.

There are multiple ways to assign work.

---

# Method 1 — Sequential

You tell Alice

> Finish A.

Only after that...

> Finish B.

Only after that...

> Finish C.

Timeline

```text
A -----

        B -----

                C -----
```

Simple.

Slow.

---

# Method 2 — create_task()

Now imagine you're smarter.

Instead of waiting,

you tell

```text
Alice → Ticket A

Bob → Ticket B

Charlie → Ticket C
```

ALL AT ONCE.

This is

```python
task1 = asyncio.create_task(ticketA())
task2 = asyncio.create_task(ticketB())
task3 = asyncio.create_task(ticketC())
```

Notice something important.

You have NOT waited.

You only hired workers.

They already started.

---

Imagine

```python
task1 = asyncio.create_task(download_pdf())
```

The download immediately starts.

Meanwhile your code continues.

```python
print("Doing other work...")
```

Later

```python
result = await task1
```

means

> Okay.

Now I need the PDF.

If finished already,

great.

Otherwise,

wait.

---

Let's visualize.

```text
create_task()

Time →

Download starts
████████████

Meanwhile

You are coding
■■■■■■■■■■■

Later

await task
```

Notice

Downloading and your code overlapped.

---

So

## create_task() = "Start now, wait later."

That's its superpower.

---

# Example

```python
import asyncio

async def coffee():
    print("Making coffee...")
    await asyncio.sleep(3)
    print("Coffee ready")
    return "☕"

async def main():

    coffee_task = asyncio.create_task(coffee())

    print("Meanwhile eating breakfast")

    await asyncio.sleep(1)

    print("Finished breakfast")

    coffee = await coffee_task

    print(coffee)

asyncio.run(main())
```

Output

```text
Making coffee...

Meanwhile eating breakfast

Finished breakfast

Coffee ready

☕
```

Notice

Coffee started FIRST.

Breakfast happened while coffee was brewing.

Exactly like real life.

---

# Now gather()

Imagine you ordered food.

You ordered

```text
Pizza

Burger

Fries
```

Do you care individually?

No.

You only care

> Bring everything together.

That's gather.

```python
results = await asyncio.gather(

    pizza(),

    burger(),

    fries()

)
```

Internally

```text
Start Pizza

Start Burger

Start Fries
```

Then

```text
WAIT

until ALL finished
```

Returns

```text
[
pizza,

burger,

fries
]
```

Notice

You never handled

Pizza Task

Burger Task

Fries Task

individually.

Gather did.

---

Visual

```text
Gather

      Pizza
        │
        ▼

      Burger
        │
        ▼

      Fries
        │
        ▼

 Wait for ALL

        │

        ▼

Return List
```

---

Think of gather as

```text
Restaurant waiter
```

You don't go

```text
Kitchen

Kitchen

Kitchen
```

Waiter brings everything together.

---

# Then why create_task?

Because sometimes

you DON'T want everything together.

Suppose

Download PDF

Process PDF

Upload PDF

Different timings.

You want

```python
pdf = asyncio.create_task(download())

# Do something else

...

await pdf
```

Much more flexible.

---

# Now TaskGroup

This is where people struggle.

Imagine you're launching a rocket.

Three teams.

```text
Navigation

Fuel

Engine
```

Question.

If

Fuel Team fails...

Should

Engine continue?

NO.

Should

Navigation continue?

NO.

Whole launch must stop.

That's TaskGroup.

---

Let's compare.

---

# gather()

Imagine three students writing an assignment.

```text
Alice

Bob

Charlie
```

Teacher says

> Submit when everyone finishes.

If Bob fails...

Teacher simply tells you

> Bob failed.

Alice and Charlie might already be finished.

No coordinated cleanup.

---

# TaskGroup

Now imagine

a hospital surgery.

Three doctors.

```text
Heart

Lungs

Anesthesia
```

If anesthesia fails...

EVERYBODY STOPS.

Immediately.

Safe shutdown.

That's TaskGroup.

---

Example

```python
async with asyncio.TaskGroup() as group:

    group.create_task(A())

    group.create_task(B())

    group.create_task(C())
```

Suppose

B crashes.

Immediately

```text
Cancel A

Cancel C

Raise Exception
```

Nobody left running.

Very safe.

---

# Visual Timeline

Imagine

```text
Task A

Task B

Task C
```

---

Using gather

```text
Task A ---------- Done

Task B ----X Error

Task C ---------- Done
```

Then

```text
Raise Exception
```

Some work still happened.

---

TaskGroup

```text
Task A ---------- Cancelled

Task B ----X Error

Task C ---- Cancelled
```

Everything cleaned.

Exactly why Swift introduced structured concurrency.

---

# Swift Comparison

Swift

```swift
async let a = fetchUsers()

async let b = fetchOrders()

let users = await a

let orders = await b
```

Closest to

```python
await asyncio.gather(...)
```

---

Swift

```swift
let task = Task {

    await fetch()
}
```

Python

```python
task = asyncio.create_task(fetch())
```

Almost identical.

---

Swift

```swift
await withThrowingTaskGroup(of: User.self) { group in

}
```

Python

```python
async with asyncio.TaskGroup()
```

Almost one-to-one.

---

# The biggest mental model

Imagine you're watching Netflix.

---

### create_task()

You press

```text
Download Episode
```

Download begins.

You continue watching another episode.

Later,

you open Downloads.

---

### gather()

You press

```text
Download Season
```

Netflix downloads all episodes.

When ALL are ready,

it shows

```text
Season Downloaded
```

---

### TaskGroup()

You're downloading a season.

Suddenly

Episode 4

becomes unavailable.

Netflix says

```text
Stop downloading everything.

This download failed.
```

Safer.

---

# Real AI Engineering Example

Suppose you're building a Multi-Agent AI system.

User uploads one PDF.

Now you need

```text
OCR Agent

↓

Embedding Agent

↓

Summarization Agent

↓

Classification Agent
```

### Scenario 1 — `create_task()`

You start OCR immediately:

```python
ocr_task = asyncio.create_task(run_ocr(pdf))
```

While OCR is reading the PDF, you can validate user permissions, log analytics, or prepare output folders. Later, when you actually need the OCR text:

```python
ocr_text = await ocr_task
```

You started the work early and waited only when necessary.

---

### Scenario 2 — `gather()`

Now you already have the extracted text, and you want three independent AI analyses:

* Sentiment
* Summary
* Keywords

These don't depend on each other.

```python
summary, sentiment, keywords = await asyncio.gather(
    summarize(text),
    analyze_sentiment(text),
    extract_keywords(text)
)
```

You simply want **all three results**.

---

### Scenario 3 — `TaskGroup`

Now imagine processing a bank loan application:

```text
Fraud Check
KYC Verification
Credit Score
```

If **KYC fails**, should you continue checking credit score?

No.

The entire workflow should stop immediately.

That's exactly the situation `TaskGroup` is designed for.

---

# The rule I personally use

| If you want to...                                            | Use             |
| ------------------------------------------------------------ | --------------- |
| Start one task now and await it later                        | `create_task()` |
| Run several independent tasks and collect all their results  | `gather()`      |
| Run related subtasks that should succeed or fail as one unit | `TaskGroup()`   |

---

### I think I know what would make this click for you.

In the next lesson, I can **draw memory diagrams and event-loop timelines** (almost like CPU scheduling diagrams in Operating Systems) showing exactly what happens every millisecond for `create_task()`, `gather()`, and `TaskGroup()`.

Instead of just seeing code, you'll literally see:

* which coroutine is running,
* when it hits `await`,
* when the event loop switches,
* what objects exist in memory,
* and why these three APIs behave differently.

For engineers, that visual model is usually the moment async/await finally "clicks."
'''
'''
Excellent. This is exactly the kind of code you'll see in production AI systems (Google ADK, LangGraph, OpenAI Agents SDK, etc.).

The difference between "I can read Python" and "I understand AI backend code" is being able to mentally execute this code.

So let's do exactly that.

---

# First, zoom out.

If I had to explain this whole program in ONE sentence:

> **"We have some work items, we process them concurrently, but we never allow more than 2 to run simultaneously, and each item must finish within 250 ms."**

That's literally what the whole program does.

---

# Step 0 - Imports

```python
import asyncio
from dataclasses import dataclass
from typing import Protocol
```

Nothing scary anymore.

You already know:

* `asyncio` → Async runtime
* `dataclass` → Like a lightweight Swift struct
* `Protocol` → Like a Swift protocol

---

# Step 1 - WorkItem

```python
@dataclass(frozen=True)
class WorkItem:
```

Imagine Swift.

```swift
struct WorkItem {

    let itemId: String
    let delaySeconds: Double
}
```

Python version

```python
@dataclass(frozen=True)
class WorkItem:

    item_id: str
    delay_seconds: float
```

This automatically creates

```python
WorkItem(
    item_id="a",
    delay_seconds=0.05
)
```

No constructor needed.

---

Why `frozen=True`?

Because this is input data.

Once created,

nobody should accidentally modify it.

Imagine

```python
item.item_id = "xyz"
```

❌ Error.

Exactly like

```swift
let item = WorkItem(...)
```

Immutable.

---

Memory

```
WorkItem

+---------------------+

item_id = "a"

delay = 0.05

+---------------------+
```

---

# Step 2 - Protocol

```python
class Processor(Protocol):

    async def process(...)
```

This says

> I don't care WHO you are.

As long as you have

```python
process()
```

you're a Processor.

Exactly like Swift.

```swift
protocol Processor {

    func process(...)
}
```

---

# Step 3 - FakeProcessor

```python
class FakeProcessor:
```

Notice

It NEVER says

```python
class FakeProcessor(Processor)
```

Why?

Protocol.

Python says

```
Does it have

process() ?

↓

Yes.

↓

Good enough.
```

Duck typing.

---

Process function

```python
await asyncio.sleep(item.delay_seconds)
```

Pretend

instead of sleeping,

this is

```
Call OpenAI

↓

Call Gemini

↓

Call Database

↓

Call Redis
```

Sleep is simply simulating network delay.

---

Then

```python
return f"processed:{item.item_id}"
```

returns

```
processed:a
```

Easy.

---

# Step 4

Now comes the interesting part.

```python
async def process_bounded(...)
```

Think

This is your

AI Manager.

Its job is

```
Receive work

↓

Create workers

↓

Limit concurrency

↓

Collect results
```

---

Input

```
items

↓

a

b

c
```

Processor

↓

FakeProcessor

Concurrency

↓

2

---

# Step 5

Semaphore

```python
semaphore = asyncio.Semaphore(2)
```

Imagine

Two chairs.

```
Chair 1

Chair 2
```

Worker must sit on a chair before working.

If chairs full

↓

Wait.

---

# Step 6

Nested function

```python
async def run_one(item):
```

Why nested?

Because

Only

`process_bounded`

needs it.

Nobody else.

Equivalent Swift

```swift
func processBounded() {

    func runOne() {

    }

}
```

Totally legal.

---

run_one

does

```
Take ONE item

↓

Acquire semaphore

↓

Timeout

↓

Process

↓

Release semaphore
```

---

Let's go line by line.

---

## async with semaphore

Imagine

```
Door

↓

Only two people inside
```

Item A

```
Can enter
```

Item B

```
Can enter
```

Item C

```
STOP

Wait outside
```

Exactly Semaphore.

---

When

run_one

finishes

Python automatically

```
Leaves room

↓

Releases chair

↓

Next worker enters
```

You never manually release.

That's why

```python
async with
```

exists.

---

# Timeout

```python
async with asyncio.timeout(0.25)
```

Imagine

Stopwatch.

```
Start

↓

250ms

↓

Still working?

↓

Cancel.
```

Production AI systems ALWAYS have timeouts.

Otherwise

one slow API

blocks forever.

---

# Processor

```python
await processor.process(item)
```

Notice

We don't know

which processor.

Could be

```
Gemini

Claude

OpenAI

Fake

Mock
```

Because

Protocol.

---

# Now the BIG part.

```python
tasks = [

    asyncio.create_task(

        run_one(item)

    )

]
```

Let's slow down.

Items

```
a

b

c
```

Loop

Iteration 1

```
run_one(a)

↓

create_task

↓

Starts immediately
```

Iteration 2

```
run_one(b)

↓

Starts immediately
```

Iteration 3

```
run_one(c)

↓

Starts immediately
```

Notice

Nobody waited.

---

Memory now

```
Task A

Task B

Task C
```

All alive.

---

# But semaphore...

Only two allowed.

So

Timeline

```
Task A enters

Chair1 occupied

↓

Task B enters

Chair2 occupied

↓

Task C

WAITING
```

---

Task A

hits

```python
await sleep(0.05)
```

Now

Task A pauses.

Event loop says

```
Great.

Run somebody else.
```

Task B

starts sleeping.

Task C

still waiting.

---

50ms later

Task A

wakes.

Returns

```
processed:a
```

Leaves semaphore.

Chair free.

Immediately

Task C

enters.

Exactly like

people waiting outside interview room.

---

Visual

```
Semaphore = 2

Time →

A Running

B Running

C Waiting

↓

A Finished

↓

C Starts

↓

B Finished

↓

C Finished
```

---

# gather()

Now

```
Task A

Task B

Task C
```

already exist.

Gather says

> I'll wait until ALL of them finish.

Notice

Gather DID NOT create them.

This is important.

It simply waits.

Equivalent

```
Parent

↓

Children playing

↓

Dinner when everyone home
```

---

Results

```
Task A

↓

processed:a

Task B

↓

processed:b

Task C

↓

processed:c
```

Gather combines

```
[
processed:a,

processed:b,

processed:c
]
```

---

Notice

Result order

```
A

B

C
```

NOT

finish order.

Suppose

B

finished last.

Still

Gather returns

```
[
A,

B,

C
]
```

Because

input order preserved.

Huge interview question.

---

# main()

Creates

```
A

delay

50ms

B

delay

100ms

C

delay

50ms
```

Calls

```python
await process_bounded(...)
```

Now mentally

```
Event Loop

↓

Task A

↓

Task B

↓

Task C

↓

Semaphore blocks C

↓

A finishes

↓

C starts

↓

B finishes

↓

C finishes

↓

Gather collects

↓

Print
```

Output

```
[
'processed:a',

'processed:b',

'processed:c'
]
```

---

# Complete Architecture Diagram

```
                  asyncio.run(main())
                          │
                          ▼
                      Event Loop
                          │
                          ▼
                  process_bounded()
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
   Semaphore(2)                    FakeProcessor
          │                               │
          └───────────────┬───────────────┘
                          ▼
                create_task(run_one)
          ┌──────────┬──────────┬──────────┐
          ▼          ▼          ▼
      Task A      Task B      Task C
          │          │          │
          │          │     Waiting (no permit)
          │          │
          ▼          ▼
 await processor  await processor
   (sleep 50ms)   (sleep 100ms)
          │          │
          ▼          ▼
      returns      returns
          │
          ▼
   Semaphore released
          │
          ▼
      Task C enters
          │
          ▼
      returns
          │
          ▼
   asyncio.gather()
          │
          ▼
['processed:a','processed:b','processed:c']
```

---

# The Production AI Analogy

Replace `FakeProcessor` with a real LLM client:

```python
class GeminiProcessor:
    async def process(self, item):
        return await gemini.generate_content(item.prompt)
```

Now imagine:

* `WorkItem` = one document to summarize.
* `Processor` = "anything that can process a document" (Gemini, OpenAI, Claude, or a fake implementation for tests).
* `create_task()` = start processing all documents immediately.
* `Semaphore(2)` = never send more than two API requests at once (to respect rate limits).
* `timeout(0.25)` = abandon any request that takes too long.
* `gather()` = wait until every document has either been processed or failed, then return the results in the same order as the input.

This pattern is one of the most common building blocks you'll encounter in production AI orchestration systems. Once you're comfortable reading this flow, a lot of frameworks like LangGraph, Google ADK, and OpenAI Agents will start feeling much less magical.
'''
"""Run with: uv run python diagnostics/python_baseline.py"""

import asyncio
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class WorkItem:
    """Immutable input at the domain boundary."""

    item_id: str
    delay_seconds: float


class Processor(Protocol):
    """A structural contract; implementations need not inherit from it."""

    async def process(self, item: WorkItem) -> str:
        ...


class FakeProcessor:
    async def process(self, item: WorkItem) -> str:
        await asyncio.sleep(item.delay_seconds)
        return f"processed:{item.item_id}"


async def process_bounded(
    items: list[WorkItem],
    processor: Processor,
    max_concurrency: int = 2,
) -> list[str]:
    """Process concurrently without allowing unbounded fan-out."""

    semaphore = asyncio.Semaphore(max_concurrency)

    async def run_one(item: WorkItem) -> str:
        async with semaphore:
            # A dependency that exceeds the budget fails this item.
            async with asyncio.timeout(0.25):
                return await processor.process(item)

    # TODO before reading docs:
    # Run all items concurrently while preserving input-order results.
    tasks = [asyncio.create_task(run_one(item)) for item in items]
    return await asyncio.gather(*tasks)


async def main() -> None:
    items = [
        WorkItem("a", 0.05),
        WorkItem("b", 0.10),
        WorkItem("c", 0.05),
    ]
    results = await process_bounded(items, FakeProcessor())
    assert results == ["processed:a", "processed:b", "processed:c"]
    print(results)


if __name__ == "__main__":
    asyncio.run(main())