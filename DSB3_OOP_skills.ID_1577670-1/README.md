# Intro to Python: OOP skills

Summary: Today we will help you acquire a basic knowledge of the OOP approach in
Python.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions of the day](#specific-instructions-of-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 00. Simple class](#exercise-00-simple-class)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 01. Method](#exercise-01-method)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 02. Constructor](#exercise-02-constructor)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 03. Nested class](#exercise-03-nested-class)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 04. Inheritance](#exercise-04-inheritance)
9. [Chapter IX](#chapter-ix) \
    9.1. [Exercise 05. Config and the main program](#exercise-05-config-and-the-main-program)
10. [Chapter X](#chapter-x) \
    10.1. [Exercise 06. Logging](#exercise-06-logging)
    
   
## Chapter I

### Foreword

Data scientists often hear the complaint that they write shitcode. By the way, if you're looking for examples of Python shitcode for educational purposes, you can find many [here](https://shitcode.net/latest/language/python). Why? Because the average data scientist uses
inefficient techniques, hard-coded variables, and neglects object-oriented programming.

Don't be like them.

Here are the top few examples from the website mentioned above:
* How to get the absolute value in just 6 lines of python
    ```python
    def absolute\_value(value):
        if str(value)[0]=='-':
            value = -1 * value
            return value
        else:
            return value
    ```
* How to evaluate the factorial of 40000 in approximately 1 second:
    ```python
    for module in next\_possible\_modules:
        import math; math.factorial(40000) # approx. a 1 second operation
        end\_time = start\_time + timedelta(minutes=module.duration)
    ```

* Gotta check that date
    ```python
    if (SelectionAndTimeData[1] < 2000 or \
            SelectionAndTimeData[2] < 1 or SelectionAndTimeData[2] > 12 or \
            SelectionAndTimeData[3] < 1 or SelectionAndTimeData[3] > 31 or \
            SelectionAndTimeData[4] < 0 or SelectionAndTimeData[4] > 24 or \
            SelectionAndTimeData[5] < 0 or SelectionAndTimeData[5] > 60 or \
            SelectionAndTimeData[2] < 0 or SelectionAndTimeData[2] >60):
        print('***********************************************************')
        print(' Entered date is not valid')
        print('***********************************************************')
    ```

## Chapter II

### Instructions

* Use this page as your only reference. Do not pay attention to rumors or speculation about how to prepare your solution.
* Here and throughout, we use Python 3 as the only correct version of Python.
* The python files for python exercises (module01, module02, module03) must have the following block at the end: `if __name__ == ‘__main__’`.
* Pay attention to the permissions of your files and directories.
* To be assessed your solution must be in your GIT repository.
* Your solutions will be evaluated by your peers in the bootcamp.
* You should not leave any other files in your directory other than those explicitly specified in the exercise instructions. It is recommended that you modify your .gitignore to avoid any accidents.
* Your solution must be in your GIT repository for evaluation. Always push only to the develop branch! The master branch will be ignored. Work in the src directory.
* When you need to get precise output in your programs, it is forbidden to display a precalculated output instead of performing the exercise correctly.
* Have a question? Ask your neighbor on the right. If that fails, try your neighbor on the left.
* Your reference materials are your peers, the internet, and Google.
* Read the examples carefully. They may require information that is not specified elsewhere in the subject.
* May the Force be with you!

## Chapter III

### Specific instructions of the day

* No code in the global scope. Use functions!
* Each file must end with a function call in a condition similar to:
    ```python
    if __name__ == '__main__':
        # your tests and your error handling
    ```
    
* Any exception that goes uncaught will invalidate your work, even if it is an error that you were asked to test.
* No imports are allowed except those mentioned in the "Authorized Functions" section of each exercise's title block.
* Any built-in function is allowed.

## Chapter IV

### Exercise 00. Simple class

- Turn-in directory: `ex00/`.
- Files to turn in: `first_class.py`.
- Allowed functions: all imports are restricted.

This will be an easy warm-up exercise to introduce you to object-oriented programming in Python.

1. Create a Python script called `first_class.py` that contains a class called Must_Read. This class reads the `data.csv` file and prints it. You can hardcode the name of the CSV file inside the class. Place the `print()` function inside your class. You will learn about methods and constructors later; for now, forget about them.
2. `data.csv` contains the following data. You can create the file however you want.

    ```
    head,tail
    0,1
    1,0
    0,1
    1,0
    0,1
    0,1
    0,1
    1,0
    1,0
    0,1
    1,0
    ```
  
Example of launching the script:

    ```
    $ python3 first_class.py
    head,tail
    0,1
    1,0
    0,1
    1,0
    0,1
    0,1
    0,1
    1,0
    1,0
    0,1
    1,0
    ```

## Chapter V

### Exercise 01. Method

- Turn-in directory: `ex01/`.
- Files to turn in: `first_method.py`.
- Allowed functions: all imports are is restricted.

In the previous exercise, you created a class. Honestly, nobody creates classes like that in real life. Classes typically group together functions with similar topics and parameters. This is a better way to organize them. In this case, the functions are called methods.

1. For this exercise, move the code from the body of the class to the `file_reader()` method. Methods are like functions in that they can return something. Classes cannot do that. Therefore, replace `print()` with `return()` in the method. Change the name of the class to "Research."
2. The script must still have the exact same behavior. It needs to display the contents of the `data.csv` file. Save the script as `first_method.py`.

## Chapter VI

### Exercise 02. Constructor

- Turn-in directory: `ex02/`.
- Files to turn in: `first_constructor.py`.
- Allowed functions: `import sys`, `import os`.

Hardcoding the file name in the method was not a good idea. Ideally, we would be able to provide the file path as a script parameter. It would also be great if we did not have to include the path in every method we bring in later. Fortunately, there is a solution. Python classes can have a constructor: `__init__()`. This method runs first when an instance of a class is created.

Modify your code as follows:
1. Inside the Research class, create an `__init__()` method that takes the path to the file to be read as an argument.
2. Modify the `file_reader()` method. This method does almost the same thing as in the previous exercise — it just reads the file and returns its data. The difference is that the path to the file should be used from the `__init__()` method.
3. If a file with a different structure is given and your program cannot read it, raise an exception. The correct file contains a header with two strings separated by a comma. One or more lines follow that contain either 0 or 1, but never both, and are delimited by a comma.
4. Modify the main program. The script must still behave exactly the same. The path to the file should be provided as an argument to the script. The script should display the contents of the `data.csv` file. Save the script as `first_constructor.py`.

Example of launching the script:
```
$ python3 first_constructor.py data.csv
head,tail
0,1
1,0
0,1
1,0
0,1
0,1
0,1
1,0
1,0
0,1
1,0
```

## Chapter VII

### Exercise 03. Nested class

- Turn-in directory: `ex03/`.
- Files to turn in: `first_nest.py`.
- Allowed functions: `import sys`, `import os`.

Now, let's delve deeper into OOP in Python. Can one class be contained within another? Sure, why not? We can benefit from this by giving our code a clearer structure and uniting several methods in one nested class.

For this exercise, you need to:
1. Modify the `file_reader()` method by adding an argument called "has_header" with the default value of True. Use it if your file has a header; if not, use False. This method's return value is no longer a string, but rather a list of lists, such as [0, 1] or [1, 0]. Therefore, the has_header argument influences how the file is processed. In both cases, the return value should be the same without a header.
2. Create a nested class called "Calculations" without a constructor. In that class, create two methods: `counts()` and `fractions()`. The `counts()` method takes data from the `file_reader()` method as an argument and returns the count of heads and tails (e.g., 3 and 7). The `fractions()` method takes the counts of heads and tails as arguments and calculates the fractions as percentages (e.g., 30% and 70%). 

The script should display:
- the data from `file_reader()`;
- the counts from the `counts()` method;
- the fractions from `fractions()` method.

Here is an example:
```bash
$ python3 first_nest.py data.csv
[[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]
5 6
0.4545 0.5454

```

## Chapter VIII

### Exercise 04. Inheritance

- Turn-in directory: `ex04/`.
- Files to turn in: `first_child.py`.
- Allowed functions: `import sys`, `from random import randint`.

Do you have one class with many useful methods, but need another class with some or all of those methods? No problem! Just inherit one from the other.

Here's what you need to do in this exercise:
1. In the previous exercise, the argument data was in your method `counts()`. Now, let's move it to the constructor of the Calculations class. This data may be useful for future methods of this class.
2. Create a new class called "Analytics" that inherits from Calculations.
3. In the new class, create two methods:
  - `predict_random()`: takes the number of predictions to return and returns a list of lists of predicted observations of heads and tails. If heads equals 1, then tails equals 0, and vice versa. For example, the output would be: [1, 0], [1, 0], [0, 1].
  - `predict_last()`: returns the last item of data from `file_reader()` (this method has the same functionality as in the previous exercise) as a list. 

The script should display:
- the data from `file_reader()`;
- the counts from `counts()` method;
- the fractions from `fractions()` method;
- the list of lists from `predict_random()` for the three steps;
- the list from `predict_last()`.

## Chapter IX

### Exercise 05. Config and the main program

- Turn-in directory: `ex05/`.
- Files to turn in: `config.py`, `analytics.py`, `make_report.py`.
- Allowed functions: `import os`, `from random import randint`.

Okay. Now, we need to make our code clearer. First, we need to transfer all the script's logic into a different file. Second, we need to move all the parameters into a config file. Then, we will import the configuration and module files into the main program script.

Here are the details:
1. Create a file called `config.py` where you will store external parameters, such as "num_of_steps" for `predict_random()`.
2. Delete the logic after the `if __name__ == '__main__'` block from your script from the previous exercise.
3. Rename that script `analytics.py`.
4. Add to the class Analytics a method that saves any given result to a file with a given extension, such as `save_file(data, file name, 'txt')`.
5. Create a new file called `make_report.py` where the entire program logic will be written. The result saved in the file should look like this. You may need to add additional methods to `analytics.py`.

**Report:**

We made 12 observations by tossing a coin: five were tails and seven were heads. The probabilities are 41.67% and 58.33%, respectively. Our forecast is that the next three observations will be: one tail and two heads.

The text template must be stored in `config.py`.

- For this exercise, `config.py` may contain code in the global scope for variables.
- For this exercise, neither `config.py` nor `analytics.py` must contain the block `if __name__ == '__main__'`.

## Chapter X

### Exercise 06. Logging

- Turn-in directory: `ex06/`.
- Files to turn in: `config.py`, `analytics.py`, `make_report.py`.
- Allowed functions: `import os`, `from random import randint`, `import logging`, `import requests` (or urllib), `import json`.

By now, you have written a module containing several classes with methods, a program that uses the module, and a configuration file. But what if you encounter problems during production that require debugging? How will you do it? That's right! You need to log them. 

1. The first task of the exercise is to have each method in every class log useful debugging information. Store this information in the file `analytics.log`. The format is date, time, and message, all separated by a space:

        2020-05-01 22:16:16,877 Calculating the counts of heads and tails

2. The second task is to write a method in the Research class that sends a message to a Telegram channel using webhooks. The message should contain either: "The report has been successfully created" or: "The report hasn't been created due to an error."

- In this exercise, `config.py` may contain code in the global scope for variables.
- In this exercise, neither `config.py` nor `analytics.py` has to contain the block `if __name__ == '__main__'`.
