# MovieLens Analytics

Summary: This rush will help you to strengthen the skills acquired in the previous days.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions for the day](#specific-instructions-for-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Mandatory part](#mandatory-part)
5. [Chapter V](#chapter-v) \
    5.1. [Bonus part](#bonus part)
6. [Chapter VI](#chapter-vi) \
    6.1. [Turn-in and peer-evaluation](#turn-in-and-peer-evaluation)

## Chapter I

### Foreword

Why do we enjoy movies? What makes them so attractive?
Although movies are a relatively modern phenomenon, they have an ancient mechanism at their core: the story.

People have loved stories since ancient times. Think of them as universal containers that effectively transfer useful information from a source to a person. By sparking our emotions and imagination, stories establish a good connection and package information in a way that can be easily consumed
by a human being. Stories were crucial for survival for our ancestors. They contain personal experiences that can be applied to your life. For example, you may discover that some areas around your village are dangerous. Or, you may find some great places to gather mushrooms.

Our attention to stories has survived for centuries. When a speaker begins a presentation with a story, it captures our attention. We love books. We love music and songs. We love movies.

So, how can you use stories in data science? Good reports have elements of storytelling. Try telling a story through your analysis.

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

* No code should be in the global scope. Use functions!
* Any exception that goes uncaught will invalidate your work, even if the error was one you were asked to test.
* The interpreter to use is Python 3.
* Any built-in function is allowed.
* You can import the following libraries: os, sys, urllib, requests, beautifulsoup, json, pytest, collections, functools, datetime, re.
* Use Jupyter Notebook to create the report.

## Chapter IV

### Mandatory part

During this time, you will work on your own analytical report. You will analyze data from the MovieLens database. By the end, you will have two files: `movielens_analysis.py` and `movielens_report.ipynb`. In the first file, you will create your own module with classes and methods. The second file contains the report itself, created using only your module.

#### Module

Remember, the goal of the rush is to strengthen your skills.

Try to apply as much as you can from what you learned in previous days.

1. Use a smaller version of the MovieLens dataset, [download](https://drive.google.com/file/d/1CwC887F6FMneXea2yCpDrlrf47Em664u/view?usp=sharing) it, please. Use the first 1,000 values from the dataset.
2. Read the `README.txt` file carefully. Focus on the file structures.
3. In your module, you will need to create four classes corresponding to four files from the data, as well as one class for testing.
4. The classes and methods below are obligatory, but you can add anything that suits your needs.

_The classes Ratings, Tags, Movies, and Links can be found in the code samples._

Class Tests:

Create tests using PyTest for each method of the above classes.

They should check:

- if the methods return the correct data types,
- if the list elements have the correct data types,
- if the returned data is sorted correctly.

Run the tests before moving on to the next stage.

#### Report

Prepare your report using only the classes and methods from `movielens_analysis.py`.

Do it in **Jupyter Notebook**. It is an excellent tool, especially for data scientists. It allows you to work with the code interactively by launching and relaunching different cells with different values. You don't have to rerun your entire code from the beginning. You can also put text in the cells, which is a great feature for making reports. Install it in your environment.

In this section, we will give you more freedom. We are not going to define the structure of your report. The goal of the report is to tell an interesting story about the MovieLens dataset. Find the right structure and sequence.

The only constraints are:
1. You must use every method in movielens_analysis.py, except for the class Tests.
2. Every cell in your notebook must contain the magic command `%timeit`.
3. All other imports and built-in functions are prohibited. If you need them, put them in your module in advance.

## Chapter V

### Bonus part

1. Add more methods to the classes that you may find useful and interesting for your report. Don't forget to test them, either.
2. Improve the tests. Also, check the correctness of your calculations. Manually precalculate some results and metrics, and check if the methods return the correct information when given specific inputs.
3. Develop your report so that it tells a story in an interactive, question-and-answer style. Make it intriguing, emotional, interesting, and easy to read.

## Chapter VI

### Submission and peer-evaluation

Submit your work using your Git repository as usual. Only work in your repository will be graded during review.

You will be evaluated on your review (no functions that do all the heavy lifting for you) as well as your ability to present, explain, and justify your choices during the correction.
