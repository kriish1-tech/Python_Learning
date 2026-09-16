# Python Roadmap: Scratch to Intermediate

> **Goal:** Go from zero Python knowledge to being able to independently build real programs and continue into a specialization such as AI/ML, automation, backend development, or data science.

---

## How to Use This Roadmap

Use the roadmap as a **learning sequence**, not a checklist to rush through.

For each topic:

1. Understand the concept.
2. Write code yourself.
3. Solve problems without looking at solutions.
4. Build something using the concept.
5. Review mistakes and gaps.
6. Move on when you can use the concept reliably.

### Core Learning Loop

**Concept → Practice → Problem Solving → Project → Review**

Do not wait until you know everything before building. Learn enough to act, then use the project to expose what you still need to learn.

---

# 1. Roadmap Overview

## Beginner

You should become comfortable with:

- Python syntax
- Variables and basic types
- Operators
- Conditions
- Loops
- Core data structures
- Functions
- Basic problem solving
- Basic debugging
- Small programs

## Core Python

You should become comfortable with:

- Modules and imports
- Exceptions
- File handling
- Comprehensions
- The standard library
- OOP
- Working with structured data
- Iteration and generators
- Regular expressions

## Intermediate

You should become comfortable with:

- Virtual environments
- Packages and dependencies
- Project structure
- Type hints
- Testing
- Logging
- Git/GitHub
- APIs
- CLI applications
- Multi-module projects
- Reading documentation
- Building independently

---

# 2. Cross-Cutting Skill: Problem Solving

Programming is not primarily about remembering syntax. It is about turning a problem into a sequence of precise instructions.

## Learn

- How to understand a problem
- Identify inputs
- Identify outputs
- Identify constraints
- Break large problems into smaller problems
- Write pseudocode
- Trace code manually
- Identify edge cases
- Test assumptions
- Debug systematically

## Practice

For unfamiliar problems, ask:

1. What exactly is being asked?
2. What information do I have?
3. What should the output be?
4. Can I solve a smaller version first?
5. What steps would I perform manually?
6. What could go wrong?
7. Can I explain my solution before coding it?

## Milestone

You should be able to take a simple programming problem and describe a reasonable solution **before** writing Python code.

---

# 3. Phase 1 — Introduction & Environment

## 3.1 What Is Programming?

Learn:

- Programs
- Source code
- Programming languages
- Interpreters
- Compilers
- Runtime
- Algorithms
- Bugs
- Syntax vs logic

## 3.2 What Is Python?

Learn:

- Python's purpose
- Python interpreter
- Python scripts
- Interactive REPL
- `.py` files
- Python's high-level nature
- Python's dynamic typing

## 3.3 Development Environment

Learn how to:

- Install Python
- Run Python from the terminal
- Create and execute a Python file
- Use a code editor
- Use the Python REPL
- Read error messages
- Run programs repeatedly

## 3.4 Basic Terminal Skills

Learn:

- Current directory
- Listing files
- Changing directories
- Creating files/folders
- Running commands
- Relative vs absolute paths

## 3.5 Packages and `pip`

Understand:

- Package
- Library
- Module
- Dependency
- `pip`
- Installing a package
- Importing a package

## Milestone Project

**Hello Python**

Create a small program that:

- Asks for the user's name
- Asks for basic information
- Prints a formatted introduction
- Performs a few calculations

---

# 4. Phase 2 — Python Syntax & Mental Models

This phase is important because understanding Python's mental model prevents many beginner mistakes.

## 4.1 Syntax

Learn:

- Indentation
- Statements
- Expressions
- Comments
- Blocks
- Line structure

## 4.2 Variables

Learn:

- Assignment
- Variable names
- Naming conventions
- Reassignment
- Multiple assignment

## 4.3 Objects and Values

Understand:

- Everything in Python is an object
- Objects have types
- Objects have identity
- Names refer to objects
- Values can be mutable or immutable

## 4.4 Equality vs Identity

Understand:

- `==`
- `is`
- Equality
- Identity

## 4.5 Mutability

Understand:

- Mutable objects
- Immutable objects
- Why mutation matters
- Why copying can matter

## 4.6 Dynamic Typing

Understand:

- Types belong to objects
- Variables can refer to different types of objects
- Runtime type checking

Useful tools:

- `type()`
- `isinstance()`
- `id()`

## Milestone

You should be able to explain what happens when:

```python
x = 10
y = x
x = 20
```

and understand why `x` and `y` behave the way they do.

---

# 5. Phase 3 — Core Python

## 5.1 Input and Output

Learn:

- `print()`
- `input()`
- Formatting output
- f-strings

## 5.2 Numbers

Learn:

- `int`
- `float`
- Arithmetic
- Division
- Floor division
- Modulo
- Exponentiation
- Numeric comparisons

Operators:

```text
+  -  *  /  //  %  **
```

## 5.3 Boolean Logic

Learn:

- `True`
- `False`
- Comparisons
- `and`
- `or`
- `not`
- Truthiness

## 5.4 Strings

Learn:

- Creating strings
- Indexing
- Slicing
- String methods
- Searching
- Replacing
- Splitting
- Joining
- Formatting
- Escape sequences

Important concepts:

- Strings are immutable
- Strings are sequences

## 5.5 Type Conversion

Learn:

- `int()`
- `float()`
- `str()`
- `bool()`

Understand when conversion succeeds and when it fails.

---

# 6. Control Flow

## 6.1 Conditional Statements

Learn:

- `if`
- `elif`
- `else`
- Nested conditions
- Conditional expressions

## 6.2 Loops

Learn:

- `for`
- `while`
- Iteration
- Loop conditions
- Nested loops

## 6.3 Loop Control

Learn:

- `break`
- `continue`
- `pass`

## 6.4 `range()`

Understand:

- Start
- Stop
- Step
- Common loop patterns

## Practice

Build programs such as:

- Number guessing game
- Multiplication table generator
- Simple calculator
- Grade calculator
- Number checker
- Menu-driven program

---

# 7. Python Data Structures

## 7.1 Lists

Learn:

- Creating lists
- Indexing
- Slicing
- Updating
- Adding/removing elements
- Iterating
- List methods
- Nested lists

Important methods:

```text
append()
extend()
insert()
remove()
pop()
sort()
reverse()
```

## 7.2 Tuples

Learn:

- Creating tuples
- Indexing
- Unpacking
- Immutability
- When tuples are useful

## 7.3 Sets

Learn:

- Creating sets
- Uniqueness
- Adding/removing elements
- Membership
- Union
- Intersection
- Difference

## 7.4 Dictionaries

Learn:

- Key-value relationships
- Creating dictionaries
- Accessing values
- Adding/updating values
- Removing entries
- Iterating over keys and values
- Nested dictionaries

Important methods:

```text
get()
keys()
values()
items()
update()
pop()
```

## 7.5 Choosing the Right Data Structure

Understand when to use:

| Structure | Typical Use |
|---|---|
| List | Ordered collection |
| Tuple | Fixed/immutable collection |
| Set | Unique values and membership |
| Dictionary | Key-value lookup |

---

# 8. Functions

Functions are one of the most important ideas in Python.

## Learn

- Defining functions
- Calling functions
- Parameters
- Arguments
- Return values
- Local variables
- Global variables
- Scope
- Default arguments
- Keyword arguments
- Positional arguments
- `*args`
- `**kwargs`
- Docstrings

## Function Design

Learn to:

- Give functions one clear responsibility
- Choose meaningful names
- Avoid unnecessary global state
- Keep functions understandable
- Reuse code instead of copying it

## Practice

Turn previous programs into reusable functions.

## Milestone

You should be able to take a 50–100 line beginner program and break it into sensible functions.

---

# 9. Beginner Practice & Projects

Do not move forward based only on recognition. Build.

## Practice Problems

Solve problems involving:

- Variables
- Arithmetic
- Strings
- Conditions
- Loops
- Lists
- Dictionaries
- Functions

## Beginner Projects

Build several of these yourself:

1. Calculator
2. Number guessing game
3. Quiz application
4. Expense tracker
5. To-do list
6. Password generator
7. Contact book
8. Simple text-based game
9. Unit converter
10. Student grade manager

## Beginner Exit Criteria

You are ready to move on when you can:

- Write a Python program without copying a tutorial
- Use conditions and loops comfortably
- Use lists and dictionaries appropriately
- Write reusable functions
- Read basic error messages
- Debug simple programs
- Build a small project independently

---

# 10. Phase 4 — Intermediate Python

# 10.1 Comprehensions

Learn:

- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Conditional comprehensions
- Nested comprehensions

Do not use comprehensions merely to make code shorter. Prefer readability.

---

# 10.2 Useful Built-in Functions

Become comfortable with:

```text
len()
sum()
min()
max()
sorted()
reversed()
enumerate()
zip()
any()
all()
map()
filter()
```

Also understand:

- `range()`
- `abs()`
- `round()`
- `type()`
- `isinstance()`

---

# 10.3 Modules and Imports

Learn:

- What a module is
- Importing modules
- `import`
- `from ... import ...`
- Aliases
- Creating your own modules
- Module namespaces
- `__name__`
- `if __name__ == "__main__":`

---

# 10.4 Packages

Understand:

- Package structure
- `__init__.py`
- Import organization
- Third-party packages
- Standard-library packages

---

# 10.5 Python Standard Library

Become familiar with useful modules such as:

- `math`
- `random`
- `statistics`
- `datetime`
- `pathlib`
- `os`
- `sys`
- `json`
- `csv`
- `collections`
- `itertools`
- `functools`
- `re`

The goal is not to memorize the entire standard library.

The goal is to know **what exists and how to find the documentation**.

---

# 11. Errors, Exceptions & Debugging

## 11.1 Errors

Understand:

- Syntax errors
- Runtime errors
- Logical errors

## 11.2 Exceptions

Learn:

- `try`
- `except`
- `else`
- `finally`
- `raise`

Common exceptions:

- `ValueError`
- `TypeError`
- `NameError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`
- `ZeroDivisionError`

## 11.3 Debugging

Learn to:

- Read tracebacks
- Identify where an error occurred
- Reproduce bugs
- Reduce a problem
- Inspect variables
- Add temporary debugging output
- Use a debugger when appropriate

## Debugging Rule

Do not immediately ask someone—or an AI—to fix your error.

First:

1. Read the traceback.
2. Identify the failing line.
3. Understand what Python expected.
4. Inspect your assumptions.
5. Attempt a fix.
6. Then seek help if necessary.

---

# 12. File Handling

Learn:

- Opening files
- Reading files
- Writing files
- Appending
- File modes
- Encoding
- Closing files
- `with`
- `pathlib`

Example concepts:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

Understand:

- Text files
- Binary files
- Paths
- Directories

---

# 13. Structured Data

## JSON

Learn:

- JSON structure
- Serialization
- Deserialization
- `json.load()`
- `json.dump()`
- `json.loads()`
- `json.dumps()`

## CSV

Learn:

- Reading CSV
- Writing CSV
- Rows and columns
- `csv` module

## Practice Project

Build a program that stores and loads application data using JSON.

---

# 14. Object-Oriented Programming

OOP should be learned as a way to model and organize programs—not as a collection of syntax rules.

## 14.1 Classes and Objects

Learn:

- Classes
- Objects
- Attributes
- Methods
- `self`

## 14.2 Constructors

Learn:

- `__init__`
- Instance initialization

## 14.3 Instance vs Class Attributes

Understand:

- Instance attributes
- Class attributes
- Shared vs individual state

## 14.4 Encapsulation

Understand:

- Public attributes
- Naming conventions
- Properties
- Controlled access

## 14.5 Inheritance

Learn:

- Parent classes
- Child classes
- Method overriding
- `super()`

## 14.6 Polymorphism

Understand:

- Common interfaces
- Different implementations
- Duck typing

## 14.7 Special Methods

Become familiar with:

```text
__init__
__str__
__repr__
__len__
__eq__
__lt__
```

Do not memorize every special method.

## 14.8 Composition

Understand:

> "Has-a" relationships can often be better than inheritance.

## 14.9 OOP Design

Learn to ask:

- What objects exist?
- What data belongs to each object?
- What behavior belongs to each object?
- Which relationships exist?
- Is a class actually necessary?

## OOP Project

Build a small library management system, banking simulation, inventory system, or game using multiple classes.

---

# 15. Deeper Python

## 15.1 Iterables

Understand:

- Iterable
- Iterator
- `iter()`
- `next()`

## 15.2 Generators

Learn:

- Generator functions
- `yield`
- Lazy evaluation
- Generator expressions

Understand why generators can be useful for large or streaming data.

## 15.3 Decorators

Learn:

- Functions as objects
- Higher-order functions
- Closures
- Decorator syntax
- Writing simple decorators

## 15.4 Regular Expressions

Learn:

- Pattern matching
- Character classes
- Quantifiers
- Groups
- Searching
- Substitution

Use the `re` module.

## 15.5 Functional Concepts

Understand:

- First-class functions
- Higher-order functions
- `map()`
- `filter()`
- `lambda`
- `functools`

Prioritize readable Python over clever Python.

---

# 16. Professional Python Foundations

# 16.1 Virtual Environments

Understand:

- Why environments exist
- Project isolation
- Creating an environment
- Activating/deactivating it
- Installing dependencies

Learn the standard `venv` workflow.

---

# 16.2 Dependency Management

Understand:

- Dependencies
- Package versions
- Requirements
- Reproducibility

Learn how to record and recreate a project's dependencies.

---

# 16.3 Project Structure

Learn how to organize:

- Source code
- Modules
- Packages
- Tests
- Documentation
- Configuration
- Data
- Dependencies

Aim for projects that another programmer can understand.

---

# 16.4 Environment Variables & Configuration

Understand:

- Configuration vs code
- Environment variables
- Secrets
- Why credentials should not be hard-coded

---

# 16.5 Type Hints

Learn:

- Basic annotations
- Function annotations
- Collections
- Optional values
- Type aliases
- Static type checking concepts

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints should improve clarity, not become a distraction.

---

# 16.6 Code Formatting & Linting

Understand:

- Consistent formatting
- Style checking
- Linting
- Code quality tools

Learn how to use common Python tooling rather than manually enforcing every style rule.

---

# 16.7 Documentation

Learn:

- Comments vs documentation
- Docstrings
- README files
- Usage instructions
- API documentation basics

A project should explain:

- What it does
- How to install it
- How to run it
- How to use it

---

# 17. Testing

Testing is part of professional programming.

## Learn

- Why testing matters
- Test cases
- Assertions
- Unit tests
- Test functions
- Test organization
- Edge cases
- Regression testing

Start with Python's built-in testing capabilities and later explore commonly used testing frameworks.

## Practice

Write tests for:

- Calculator functions
- Data validation
- File-processing functions
- Business logic

---

# 18. Logging

Understand:

- Why `print()` is not enough for larger programs
- Logging levels
- Log messages
- Debugging through logs
- Basic configuration

Become familiar with:

- `logging`

---

# 19. Git & GitHub

Version control is a core development skill.

## Git Fundamentals

Learn:

- Repository
- Working directory
- Staging area
- Commit
- Branch
- Merge
- Remote repository

Basic commands:

```text
git init
git status
git add
git commit
git log
git branch
git switch
git merge
git pull
git push
```

## GitHub

Learn:

- Repositories
- README
- Commits
- Branches
- Pull requests
- Issues
- `.gitignore`

## Milestone

Put your Python projects into Git repositories and maintain them with meaningful commits.

---

# 20. Real-World Python Development

At this stage, stop thinking primarily in terms of isolated Python features.

Start thinking in terms of **applications**.

## Learn to Combine

- Functions
- Modules
- Classes
- Files
- JSON/CSV
- Exceptions
- Testing
- Logging
- Dependencies
- Git

## Build

### CLI Applications

Build programs that:

- Accept command-line arguments
- Validate input
- Perform operations
- Save data
- Handle errors

### API-Based Programs

Learn:

- HTTP basics
- Requests
- URLs
- Methods
- Status codes
- JSON responses
- Authentication concepts
- API documentation

Use a suitable HTTP client library.

### Data Processing

Build programs that:

- Read data
- Clean data
- Transform data
- Analyze data
- Save results

---

# 21. Python Project Ladder

Projects should increase in complexity.

## Level 1 — Beginner

Build:

- Calculator
- Number guessing game
- Quiz
- Unit converter
- Simple to-do list

## Level 2 — Core Python

Build:

- Expense tracker
- Contact manager
- File organizer
- Text analyzer
- Password generator
- Student management system

## Level 3 — Multi-Feature Applications

Build:

- CLI task manager
- Inventory management system
- Library management system
- Personal finance tracker
- Habit tracker

## Level 4 — Real-World Integration

Build:

- API client
- Weather/data application
- CSV/JSON data-processing tool
- Automated file-processing system
- CLI application using external APIs

## Level 5 — Capstone

Build one substantial project that combines most of your learned skills.

Your capstone should include:

- Multiple modules
- Functions
- Appropriate classes where useful
- Persistent data
- Error handling
- Tests
- Logging
- Documentation
- Git
- Dependency management

---

# 22. Mastery System

Do not ask:

> "Have I finished this topic?"

Ask:

> "Can I use this topic?"

## Topic Mastery

For a topic, aim to be able to:

- Explain it in your own words
- Write a simple example from memory
- Recognize when it is useful
- Solve unfamiliar problems using it
- Debug basic mistakes
- Combine it with previous concepts

## Problem-Solving Mastery

You should gradually become able to:

- Understand unfamiliar problems
- Break them down
- Develop an approach
- Implement the approach
- Test it
- Debug it
- Improve it

## Project Mastery

You should be able to:

- Start without a tutorial
- Decide what components are needed
- Search documentation when necessary
- Debug independently
- Finish the project
- Explain your design decisions

---

# 23. "Am I Ready to Move On?" Checklist

Move on when:

- You understand the core idea.
- You can write basic examples without copying.
- You can solve several unfamiliar exercises.
- You can use the concept inside a project.
- You can explain common mistakes.
- You know where to look when you forget something.

You **do not** need perfect mastery before moving forward.

Some concepts become clearer after you use them repeatedly.

---

# 24. Intermediate Python Exit Criteria

You can consider yourself **intermediate in Python** when you can independently:

- Write multi-function programs
- Organize code into modules
- Use core data structures appropriately
- Work with files and structured data
- Handle exceptions
- Use OOP when appropriate
- Understand iterables and generators
- Use decorators at a basic level
- Work with regular expressions
- Create virtual environments
- Manage dependencies
- Use type hints
- Write tests
- Add logging
- Use Git
- Read documentation
- Work with APIs
- Debug unfamiliar problems
- Build a substantial project without following a tutorial step-by-step

The goal is **independence**, not memorization.

---

# 25. What to Learn After Intermediate Python

Once the Python foundation is strong, choose a direction.

## AI / Machine Learning

Learn:

- NumPy
- Pandas
- Matplotlib
- Data preprocessing
- Machine learning fundamentals
- Scikit-learn
- Deep learning
- PyTorch or another deep-learning framework

## Backend Development

Learn:

- HTTP
- REST APIs
- Databases
- SQL
- Web frameworks
- Authentication
- Deployment

Possible frameworks include:

- FastAPI
- Django
- Flask

## Automation

Learn:

- File automation
- APIs
- Web automation
- Task scheduling
- Data processing
- System interaction

## Data Science

Learn:

- NumPy
- Pandas
- Visualization
- Statistics
- Data cleaning
- Exploratory data analysis
- Machine learning

## Software Engineering

Learn:

- Data structures and algorithms
- System design fundamentals
- Design patterns
- Architecture
- Testing
- CI/CD
- Databases
- Networking
- Operating systems

---

# 26. Final Roadmap Checklist

## Foundations

- [ ] What programming is
- [ ] What Python is
- [ ] Python interpreter
- [ ] REPL
- [ ] `.py` files
- [ ] Terminal basics
- [ ] `pip`
- [ ] Packages and modules

## Core Python

- [ ] Variables
- [ ] Types
- [ ] Numbers
- [ ] Strings
- [ ] Booleans
- [ ] Operators
- [ ] Conditions
- [ ] Loops
- [ ] Lists
- [ ] Tuples
- [ ] Sets
- [ ] Dictionaries
- [ ] Functions
- [ ] Scope
- [ ] Problem solving

## Intermediate Python

- [ ] Comprehensions
- [ ] Built-ins
- [ ] Modules
- [ ] Packages
- [ ] Standard library
- [ ] Exceptions
- [ ] Debugging
- [ ] File handling
- [ ] `pathlib`
- [ ] JSON
- [ ] CSV
- [ ] OOP
- [ ] Iterators
- [ ] Generators
- [ ] Decorators
- [ ] Regular expressions

## Professional Foundations

- [ ] Virtual environments
- [ ] Dependencies
- [ ] Project structure
- [ ] Configuration
- [ ] Environment variables
- [ ] Type hints
- [ ] Formatting
- [ ] Linting
- [ ] Documentation
- [ ] Testing
- [ ] Logging
- [ ] Git
- [ ] GitHub
- [ ] APIs

## Building

- [ ] Beginner projects
- [ ] Core Python projects
- [ ] Multi-module project
- [ ] API project
- [ ] Data-processing project
- [ ] Capstone project

## Final Skill

- [ ] Can learn from documentation
- [ ] Can debug independently
- [ ] Can solve unfamiliar problems
- [ ] Can build without tutorials
- [ ] Can explain your code
- [ ] Can choose appropriate Python tools
- [ ] Can continue learning independently

---

# Final Principle

**Do not optimize the roadmap endlessly.**

A roadmap is useful only when it gets you to write code.

Use this sequence:

> **Learn → Practice → Struggle → Build → Debug → Reflect → Continue**

You do not need to know all of Python before building real things.

**Learn enough to act, then act enough to learn.**

[[Master Learning System]]
