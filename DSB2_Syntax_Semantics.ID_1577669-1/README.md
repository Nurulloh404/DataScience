# Intro to Python: Syntax and Semantics

Summary: Today we will help you acquire basic knowledge of the syntax and semantics of Python.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions of the day](#specific-instructions-of-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 00. Data types](#exercise-00-data-types)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 01. Working with files](#exercise-01-working-with-files)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 02. Search by key](#exercise-02-search-by-key)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 03. Search by value and by key](#exercise-03-search-by-value-and-by-key)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 04. Dictionaries](#exercise-04-dictionaries)
9. [Chapter IX](#chapter-ix) \
    9.1. [Exercise 05. Search by value or by key](#exercise-05-search-by-value-or-by-key)
10. [Chapter X](#chapter-x) \
    10.1. [Exercise 06. Sorting a dictionary](#exercise-06-sorting-a-dictionary)
11. [Chapter XI](#chapter-xi) \
    11.1. [Exercise 07. Sets](#exercise-07-sets)
12. [Chapter XII](#chapter-xii) \
    12.1. [Exercise 08. Working with strings as lists](#exercise-08-working-with-strings-as-lists)
13. [Chapter XIII](#chapter-xiii) \
    13.1. [Exercise 09. Caesar cipher](#exercise-09-caesar-cipher)
    
   
## Chapter I

### Foreword

Python is the most popular programming language for data science. What makes it so well-suited for this type of task? Python is an interpreted language. This allows you to easily interact with different pieces of code and quickly obtain results. This is exactly what we need when analyzing data from different angles or trying different hyperparameters for a machine learning model. Additionally, Python has many libraries suitable for scientific tasks, including data science. Add to that its simple syntax, and you have the most popular programming language for data science tasks.

For fun, take a look at these 19 beautiful guiding principles that influenced the design of Python:

* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren’t special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one — and preferably only one — obvious way to do it.
* Although that way may not be obvious at first unless you’re Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it’s a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea — let’s do more of those!

If you forget any of them, just write "import this" in Python, and they will quickly appear.

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

* No code should be in the global scope. Use functions!
* Each file must end with a function call in a condition similar to the following: `if __name__ == '__main__': your_function(whatever parameter is required)`.
* You may place error handling in this same condition.
* No imports are allowed except those mentioned in the "Authorized Functions" section of the title block of each exercise.
* You can use any built-in function unless it is prohibited in an exercise.
* The exceptions raised by the open() function are not to be handled.
* The interpreter to be used is Python 3.

## Chapter IV

### Exercise 00. Data types

- Turn-in directory: `ex00/`.
- Files to turn in: `data_types.py`.
- Allowed functions: any import is restricted.

Like any other language, Python has several built-in data types. In this exercise, you will become familiar with the most popular and useful ones.

1. Create a script called `data_types.py` and define a `data_types()` function. In this function, declare 8 variables with different types and print their types to the standard output.
2. You must reproduce the following output exactly:
    
        > python3 data_types.py
        [int, str, float, bool, list, dict, tuple, set]

3. Do not write the data types explicitly in your print. Remember to call your function at the end of your script, as explained in today's instructions:
    
        if __name__ == '__main__':
            data_types()
    
4. Put your file in the `ex00` folder in the `src` directory of your repository.

## Chapter V

### Exercise 01. Working with files

- Turn-in directory: `ex01/`.
- Files to turn in: `read_and_write.py`.
- Allowed functions: any import is restricted.

For this exercise, feel free to define as many functions as you need and name them whatever you like. In the attached file `ds.csv`, which you may recognize from the previous day, there are several columns separated by commas containing different data about vacancies.

1. Design a Python script called `read_and_write.py` that opens the file [ds.csv](https://drive.google.com/file/d/1tDEDTytYaUrfJsXD5z5QvJSb5VNlL-eZ/view), reads the data it contains, replaces all the comma delimiters with "\t", and saves the data to a new file `ds.tsv`. Be careful, your data may contain commas. If you replace them, you will corrupt the data.
2. Put your script in the `ex01` folder in the `src` directory of your repository.

## Chapter VI

### Exercise 02. Search by key

- Turn-in directory: `ex02/`.
- Files to turn in: `stock_prices.py`.
- Allowed functions: `import sys`.

1. You have the following dictionaries to copy to one of your functions:

        COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

        STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

2. Write a program that takes the name of a company (e.g., Apple) as an argument and displays its stock price (e.g., 287.73) on the standard output. If the program is given a company name that is not in the dictionary, it should display "Unknown company." If no arguments are provided, or if too many arguments are provided, your program should do nothing and quit.

        $> python3 stock_prices.py tesla
        724.88
        $> python3 stock_prices.py Facebook
        Unknown company
        $> python3 stock_prices.py Tesla Apple

## Chapter VII

### Exercise 03. Search by value and by key

- Turn-in directory: `ex03/`.
- Files to turn in: `ticker_symbols.py`.
- Allowed functions: `import sys`.

1. You will use the same two dictionaries as in the previous exercise. Copy them again using one of the functions in your script.
2. Create a program that takes a ticker symbol (e.g., AAPL) and displays the company name and stock price, using a space as the delimiter. The program's behavior should be identical to that of the previous exercise.

      $> python3 ticker_symbols.py tsla
      Tesla 724.88
      $> python3 ticker_symbols.py FB
      Unknown ticker
      $> python3 ticker_symbols.py TSLA AAPL

## Chapter VIII

### Exercise 04. Dictionaries

- Turn-in directory: `ex04/`.
- Files to turn in: `to_dictionary.py`.
- Allowed functions: any import is restricted.

1. Create a script named `to_dictionary.py` in one of the functions and for this function copy the following list of tuples as is:

        list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]

2. Your script should transform this variable into a dictionary, with the number as the key and the country as the value. As you can see, the same key may have several values. The script must display the dictionary's contents on standard output according to this precise formatting:

        '132' : 'France'
        '132' : 'Germany'
        '178' : 'Spain'
        ...

3. Think about why the order is not necessarily identical to that of the example.

## Chapter IX

### Exercise 05. Search by value or by key

- Turn-in directory: `ex05/`.
- Files to turn in: `all_stocks.py`.
- Allowed functions: `import sys`.

1. You still have those two dictionaries from `ex02`. And you should still copy them into one of your functions in the script.
2. Write a program that exhibits the following behavior:
    - The program should take a string containing many expressions separated by commas as an argument.
    - For each expression in the string, the program should detect whether it is a company name, a ticker symbol, or neither.
    - The program should not be case-sensitive, but it should be able to work with whitespaces.
    - If there are no arguments or too many arguments, the program should display nothing.
    - When there are two commas in a row in the string, the program should not display anything.
    - The program must display the results separated by line breaks and use the following formatting:

          $ python3 all_stocks.py 'TSLA , aPPle, Facebook'
          TSLA is a ticker symbol for Tesla
          Apple stock price is 287.73
          Facebook is an unknown company or an unknown ticker symbol
          $ python3 all_stocks.py 'TSLA,, apple'
          $ python3 all_stocks.py 'TSLA, , apple'
          $ python3 all_stocks.py TSLA AAPL

## Chapter X

### Exercise 06. Sorting a dictionary

- Turn-in directory: `ex06/`.
- Files to turn in: `dict_sorter.py`.
- Allowed functions: any import is restricted.

1. For this exercise, take the list of tuples from `ex04` containing countries and numbers, and create a dictionary where the countries are the keys and the numbers are the values. Copy it into one of your functions in the script.
2. Write a program that displays the country names first in descending order by number and then in alphabetical order by name if the numbers are equal. Display one per line without the numbers:

       The USA
       Spain
       Italy
       France
       Germany
       ...

## Chapter XI

### Exercise 07. Sets

- Turn-in directory: `ex07/`.
- Files to turn in: `marketing.py`.
- Allowed functions: `import sys`.

For this exercise, imagine that you work in a marketing department. You will work with two different lists of email accounts. The first list contains the email accounts of your clients. The second list contains the email accounts of participants in your most recent event, some of whom were your clients. The third list contains the email accounts of clients who viewed your most recent promotional email.

In business terms, you need to:
1. Create a list of clients who have not seen your promotional email yet. This list will be sent to the call center to contact these individuals.
2. Create a list of participants who are not your clients. Send them an introductory email about your products.
3. Create a list of clients who did not participate in the event. Send them a link to the event video and slides.

Technical details:
- Create different functions that convert your lists to sets. Use the set operators necessary to perform the aforementioned business tasks and return the required lists of email accounts.
- Arrange your code in a script. The script takes the name of the task to be performed as an argument: `call_center`, `potential_clients`, or `loyalty_program`. If the wrong name is given, raise an exception.
- For this exercise, use the following three lists:

      clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
      'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
      'elon@paypal.com', 'jessica@gmail.com']
      participants = ['walter@heisenberg.com', 'vasily@mail.ru',
      'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
      'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
      recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

## Chapter XII

### Exercise 08. Working with strings as lists

- Turn-in directory: `ex08/`.
- Files to turn in: `names_extractor.py`, `letter_starter.py`.
- Allowed functions: `import sys`.

Imagine working in a corporation where all email accounts follow the same template: name.surname@corp.com.

1. Create a script that uses the path to a file containing these email addresses as an argument. All emails in the file are delimited by '\n'. The script should return a table with the following fields: Name, Surname, and Email, all of which are delimited by "\t". The name and surname values should start with a capital letter. The table should be stored in the file `employees.tsv`.

Example:
![1](misc/images/1.png)

2. Create another script that takes an email address, searches for the corresponding name in the file created by the first script, and returns the first paragraph of a letter:
    _Dear Ivan, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires._
3. Using the structure `'la-la {0}'.format(text)` is prohibited. Please use f-strings instead. They are faster and more readable.

## Chapter XIII

### Exercise 09. Caesar cipher

- Turn-in directory: `ex09/`.
- Files to turn in: `caesar.py`.
- Allowed functions: `import sys`.

There is a method called the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) that helps to encode text by shifting the alphabetical order. For example, the encoded version of "hello" might be "tqxxa" if we use a shift of 12.

1. Write a program that will encode or decode any string using a given shift according to the argument provided:

       $ python3 caesar.py encode 'ssh -i private.key user@school21.ru' 12
       eet -u bduhmfq.wqk geqd@eotaax21.dg
       $ python3 caesar.py decode 'eet -u bduhmfq.wqk geqd@eotaax21.dg' 12
       ssh -i private.key user@school21.ru

2. If the scripts are given a string containing Cyrillic symbols, for example, the scripts should raise the exception: "The script does not support your language yet." If an incorrect number of arguments is given, raise an exception.
