# Intro to Python: Efficient code practices

Summary: Today we will help you write code that works faster.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions for the day](#specific-instructions-for-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 00. List comprehensions](#exercise-00-list-comprehensions)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 01. Map](#exercise-01-map)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 02. Filter](#exercise-02-filter)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 03. Reduce](#exercise-03-reduce)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 04. Counter](#exercise-04-counter)
9. [Chapter IX](#chapter-ix) \
    9.1. [Exercise 05. Generator](#exercise-05-generator)
    
   
## Chapter I

### Foreword

- There are two English words that are often confused: "efficiency" and "effectiveness".
- To highlight the difference, here's a short joke: \
    My motto is "Efficiency. Efficiency. Efficiency". Oops! I guess I only need to say it once.
- Or, as Peter Drucker once said: "Efficiency is doing things right; effectiveness is doing the right things".
- Your code should be both effective and efficient. And vice versa.
- One of the best games for learning efficiency is Factorio. Google it.

Download it. Try to get back to Module 4. Not everyone will be able to.

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

### Specific instructions for the day

* No code in the global scope. Use functions!
* Each file must end with a function call in a condition similar to:
    ```python
    if __name__ == '__main__':
        # your tests and your error handling
    ```
  
* Any exception that goes uncaught will invalidate the work, even if it is an error that you were asked to test.
* No imports are allowed except those mentioned in the "Authorized Functions" section of each exercise's title block.
* You can use any built-in function unless it is prohibited in the exercise.

## Chapter IV

### Exercise 00. List comprehensions

- Turn-in directory: `ex00/`.
- Files to turn in: `benchmark.py`.
- Allowed functions: `import timeit`.

Imagine your task is to find all the Gmail addresses in a list of email addresses. The usual approach is to create a loop and iterate through the initial list, appending the required values to a new list.

However, this method can be inefficient when dealing with large amounts of data. A more efficient, Pythonic way to complete the task is to use list comprehensions.

For this exercise, you need to:
1. Write two functions:
  - In the first, implement the usual approach with a loop and append.
  - In the second, use a list comprehension instead.
2. Use `timeit` to measure the time required to run those functions 90,000,000 times and compare them.
3. Put this into a script that prints: "It is better to use a list comprehension" if the time required for the list comprehension is less than or equal to the time required for the loop and: "It is better to use a loop" if not.
4. Also, add the time values at the end, after the printout described above. Order them from shortest to longest.

Please use the following list of email addresses:
```
emails = [’john@gmail.com’, ’james@gmail.com’, ’alice@yahoo.com’, 
’anna@live.com’, ’philipp@gmail.com’]
```

5. Duplicate each value five times. The list will then contain 25 elements, but only five unique ones.

Here is an example of the script being launched:

```
$ ./benchmark.py
it is better to use a list comprehension
55.71611063099999 vs 58.849982983
```

## Chapter V

### Exercise 01. Map

- Turn-in directory: `ex01/`.
- Files to turn in: `benchmark.py`.
- Allowed functions: `import timeit`.

Okay, you probably noticed the difference: list comprehensions are slightly more efficient and readable than loops. However, that is not the only option.

There's also `map()`!

Map comes from functional programming. With map, you don't have to iterate through a list.

Instead, you can apply a function to an iterable. That's what you're going to do in this exercise!

Modify the script from the previous exercise:

1. Write a function that that does the same thing: creates a list of Gmail addresses from the initial list of 25 emails but using a map. Try `map()` and `list(map())`. Note the difference in speed.
2. You still need to compare which function is faster. Now, you have three options: loop, list comprehension, and map. Add one more phrase to your code: "It is better to use a map". Finally, display all three time values in ascending order by length.

The example:
```
$ ./benchmark.py
it is better to use a map
29.32016281 vs 54.620376492999995 vs 55.99120069
```

Check the results of all the functions. Are they all identical? They do not have to be.

## Chapter VI

### Exercise 02. Filter

- Turn-in directory: `ex02/`.
- Files to turn in: `benchmark.py`.
- Allowed functions: `import timeit`, `import sys`.

Did you notice that what you did in the previous exercises was filtering? Why not use the corresponding `filter()` function instead of list comprehensions and maps? It works almost the same way as `map()`. You'll love it!

Add a new function to your benchmark that uses `filter()`. This time, let's refactor the code. Create a script that takes the name of the function (loop, list comprehension, map, or filter) and the number of calls to be performed for the benchmark. In return, the script should provide the time it takes to make that number of calls to the function.

The examples:
```
$ ./benchmark.py loop 10000000
6.230267604
$ ./benchmark.py list_comprehension 10000000
6.214286791
$ ./benchmark.py map 10000000
3.063598874
$ ./benchmark.py
```

## Chapter VII

### Exercise 03. Reduce

- Turn-in directory: `ex03/`.
- Files to turn in: `benchmark.py`.
- Allowed functions: `import timeit`, `import sys`, `from functools import reduce`.

In addition to `map()` and `filter()`, there is another function that may be useful to you in the future: `reduce()`. You can use it instead of loops, and it is usually more efficient for calculating sums. In this exercise, you need to calculate the sum of the squares up to the given argument. For example, if 5 is given, the sum is `1 + 4 + 9 + 16 + 25 = 55`.

1. In your script, create two functions:
    - In the first, implement the usual approach with a loop and `sum = sum + i*i`.
    - In the second, use `reduce()`.

2. Let's create a script that takes the name of the function (loop or reduce) as an argument, as well as the number of calls to be performed for the benchmark and the number for the sum of the calculation of squares. In return, it should provide the time it takes to make that number of calls to the function.

The example:
```
$ ./benchmark.py loop 10000000 5
6.230267604
$ ./benchmark.py reduce 10000000 5
3.063598874
```

## Chapter VIII

### Exercise 04. Counter

- Turn-in directory: `ex04/`.
- Files to turn in: `benchmark.py`.
- Allowed functions: `import timeit`, `import random`, `from collections import Counter`.

"Know the built-in functions" is one of the most important commandments for a Python coder. Here we will use the collections module that comes with Python. It contains several container data types, one of which is **Counter**. Counter is very handy when you need to count unique values in a list, for example. It is also faster than any function you could write yourself. But don't take our word for it; check it out for yourself!

1. Generate a list with one million random values from 0 to 100 (remember list comprehensions?).
2. Write a function that creates a dictionary from the list where the keys are the numbers from 0 to 100 and the values are their counts.
3. Write a function that returns the top ten most common numbers, where the keys are the numbers and the values are the counts. The input is the list.
4. Solve steps 2 and 3 using Counter.
5. Make a comparison: your script should display the time spent on steps 2 and 3 with and without Counter.

Example:
```
$ ./benchmark.py
my function: 0.4501532
Counter: 0.0432341
my top: 0.1032348
Counter's top: 0.017573
```

## Chapter IX

### Exercise 05. Generator

- Turn-in directory: `ex05/`.
- Files to turn in: `ordinary.py`, `generator.py`.
- Allowed functions: `import sys`, `import resource`; for Windows: `import sys`, `import os`, `import psutil`.

Code efficiency is not only about time, but also about RAM usage. This is especially important when working with big data. Could smaller-scale data also cause you trouble? You're already used to conducting experiments. Let's do another one.

1. Download the [MovieLens dataset](https://files.grouplens.org/datasets/movielens/ml-25m.zip).
2. Unzip it. You will need the `ratings.csv` file (678.3 MB isn't that big, right?).
3. Create the first script `ordinary.py`. It should have only one function: reading all the lines in the file into a list and returning it. In the main program, write a loop that iterates through the list and calls pass. Give the path to the file as an argument to the script.
4. Create the second script `generator.py`. This script does the same thing, but your function must use a generator. The keyword `yield` is used to read one line at a time and return it to the caller. In the main program, write a loop that iterates through the generator and calls pass. Give the path to the file as an argument to the script.
5. Both scripts should display Peak memory usage in GB and user mode time plus System mode time in seconds. If you have a Windows OS, use the corresponding functions to get the same metrics.

Example:
```
$ ./ordinary.py ratings.csv
Peak Memory Usage = 2.114 GB
User Mode Time + System Mode Time = 5.77s
$ ./generator.py ratings.csv
Peak Memory Usage = 0.005 GB
User Mode Time + System Mode Time = 9.04s
```
