# Quick-Calc (Software Engineering & Testing Assignment)

Quick-Calc is a simple calculator application built for an Advanced Software Engineering practical assignment.  
It supports addition, subtraction, multiplication, division (with safe handling of division by zero), and a clear (C) operation that resets the calculator state.

This project focuses on clean, testable code and a multi-layered testing strategy (unit + integration tests) managed with Git and GitHub.

---

## Features
- Addition, subtraction, multiplication, division
- Division-by-zero handled gracefully in the input layer
- Clear (C) resets input and result to zero
- Unit tests for core logic + integration tests for the input layer

---

## Setup Instructions

### Requirements
- Python 3.11+ (tested with Python 3.12)
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yurekliozn-ui/swe-testing-assignment.git
   cd swe-testing-assignment
Testing Framework Research (Pytest vs Unittest)

Python provides the built-in unittest framework and the widely used third-party framework pytest.
unittest is part of the standard library and follows an object-oriented style (test classes, setup/teardown methods, and many assertions). This can be a benefit for large enterprise-style codebases, but it often leads to more boilerplate and less readable tests for small projects.

pytest emphasizes simplicity and developer experience. Tests are usually written as plain functions with normal assert statements, and pytest provides powerful features such as fixtures, parameterization, and rich failure output. These features make it easy to write tests that are clean, concise, and scalable without forcing a specific class-based structure.

For Quick-Calc, pytest was selected because it allows writing expressive tests with minimal boilerplate, which supports rapid development and clear demonstration of the testing pyramid (many unit tests + a few integration tests). The readability and strong assertion introspection also make it easier to understand failures and maintain the test suite.
