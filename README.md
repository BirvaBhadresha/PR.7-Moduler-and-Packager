# Multi-Utility Toolkit

# Video
https://drive.google.com/file/d/1a7I-NbcOx_tmk0IPl3k8FUq1fhvd-LvJ/view?usp=drive_link

## Project Overview

The **Multi-Utility Toolkit** is a beginner-friendly Python project that
combines built-in Python modules and custom modules into one menu-driven
application.

The project demonstrates the use of Python modules, packages, functions,
file handling, date and time operations, mathematical calculations,
random data generation, UUID generation, and dynamic module exploration
using `dir()`.

## Objectives

-   Use Python built-in modules such as `datetime`, `time`, `math`,
    `random`, and `uuid`.
-   Create and use custom Python modules.
-   Organize custom modules inside a package.
-   Use the `__init__.py` file for package structure.
-   Use functions to keep the program modular and easy to understand.
-   Use the `__name__ == "__main__"` concept.
-   Explore module attributes dynamically using `dir()`.
-   Create a simple menu-driven user interface.
-   Perform basic file operations.

## Project Structure

``` text
Moduler & Packager/
│
├── main.py
│
└── package/
    ├── __init__.py
    ├── calculation.py
    └── fileoperation.py
```

### File Description

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `main.py`                           Contains the main menu and connects
                                      all operations

  `package/__init__.py`               Initializes the custom package

  `package/calculation.py`            Contains mathematical calculation
                                      functions

  `package/fileoperation.py`          Contains file creation, writing,
                                      reading, and appending functions
  -----------------------------------------------------------------------

## Modules Used

### 1. datetime

Used for: - Displaying the current date and time - Calculating the
difference between dates - Formatting dates

### 2. time

Used for: - Stopwatch functionality - Countdown timer

### 3. math

Used inside `calculation.py` for: - Factorial - Trigonometric
calculations - Circle area - Mathematical constants such as pi

### 4. random

Used for: - Random number generation - Random list generation - Random
password generation - Random OTP generation

### 5. uuid

Used for: - Generating unique identifiers using UUID4

## Mathematical Operations

The `calculation.py` custom module contains the following functions:

### Factorial

Calculates the factorial of a number using Python's `math.factorial()`.

Example:

``` text
Enter a number: 5
Factorial: 120
```

### Compound Interest

Calculates compound interest using:

``` text
Amount = Principal × (1 + Rate / 100) ^ Time
Compound Interest = Amount - Principal
```

Example:

``` text
Enter principal amount: 10000
Enter rate of interest (in %): 2
Enter time (in years): 5

Compound Interest: 1040.81
```

### Trigonometric Calculations

Calculates: - Sine - Cosine - Tangent

The entered angle is converted from degrees to radians before
calculation.

### Areas of Geometric Shapes

The project can calculate areas such as: - Circle - Rectangle

## Random Data Generation

The random operations include:

1.  Generate Random Number
2.  Generate Random List
3.  Create Random Password
4.  Generate Random OTP

Example:

``` text
Enter password length: 8
Generated Password: Kd8@qZp1
```

The generated password will be different each time.

## UUID Generation

The UUID operation generates a unique identifier using:

``` python
uuid.uuid4()
```

Example:

``` text
Generated UUID: f47ac10b-58cc-4372-a567-0e02b2c3d479
```

The actual UUID will be different each time.

## File Operations

The custom `fileoperation.py` module is used for basic file handling.

Available operations:

1.  Create a new file
2.  Write to a file
3.  Read from a file
4.  Append to a file

Example:

``` text
Enter file name: example.txt
File created successfully!
```

## Dynamic Module Exploration

The project uses Python's `dir()` function to display available
attributes of a module.

Example:

``` text
Enter module name to explore: math
Available Attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan', ...]
```

This demonstrates how Python modules can be explored dynamically.

## Package Usage

The project uses a custom package named `package`.

The mathematical module is imported in `main.py` using:

``` python
from package import calculation
```

Functions are then called using:

``` python
calculation.factorial(number)
calculation.compound_interest(principal, rate, years)
calculation.trigonometric(angle)
```

This demonstrates the use of custom modules and packages in Python.

## Main Menu

The application provides the following options:

``` text
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes (dir())
7. Exit
```

The user can select an option and perform the required operation.

## How to Run the Project

### Step 1: Open the project folder

Open the `Moduler & Packager` folder in VS Code.

### Step 2: Check the project structure

Make sure the files are arranged as follows:

``` text
Moduler & Packager/
├── main.py
└── package/
    ├── __init__.py
    ├── calculation.py
    └── fileoperation.py
```

### Step 3: Open the terminal

In VS Code, open:

``` text
Terminal → New Terminal
```

### Step 4: Run the program

Use:

``` bash
python main.py
```

### Step 5: Use the menu

Enter the number of the operation you want to perform.

## Technologies Used

-   Python 3
-   VS Code
-   Python Standard Library
-   Custom Python Modules
-   Python Package

## Key Python Concepts Demonstrated

-   Functions
-   Modules
-   Packages
-   `__init__.py`
-   `if __name__ == "__main__"`
-   `datetime`
-   `time`
-   `math`
-   `random`
-   `uuid`
-   File handling
-   `dir()`
-   Menu-driven programming
-   Importing custom modules

## Advantages

-   Simple and easy-to-use menu-driven interface
-   Demonstrates Python modular programming
-   Separates mathematical and file operations into custom modules
-   Uses standard Python libraries
-   Easy to extend with new utilities
-   Suitable for beginners learning Python modules and packages

## Conclusion

The Multi-Utility Toolkit demonstrates how Python can be organized into
reusable modules and packages. It combines standard modules with custom
modules to perform practical operations such as mathematical
calculations, date and time processing, random data generation, UUID
creation, and file handling.

The project provides a simple example of modular programming and
demonstrates how separating functionality into different files makes a
Python program easier to understand, maintain, and extend.
