# UNIX Command Line Tools

Summary: On the first day, we will help you to acquire the skills of using UNIX
command-line tools for basic data science tasks. You will learn how to use curl, sort, uniq, jq, sed, and cat for data collection and preprocessing.

---

>💡 If this is your very first project, fill out this [form](http://opros.so/kAnXy).

>💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) to leave your feedback on the project. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Exercise 00. First shell script](#exercise-00-first-shell-script)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 01. Transforming JSON to CSV](#exercise-01-transforming-json-to-csv)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 02. Sorting a file](#exercise-02-sorting-a-file)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 03. Replacing strings in a file](#exercise-03-replacing-strings-in-a-file)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 04. Descriptive statistics](#exercise-04-descriptive-statistics)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 05. Partitioning and concatenation](#exercise-05-partitioning-and-concatenation)
    
   
## Chapter I

### Foreword

As a society, we have long known that data helps us make better decisions. In ancient Egypt, for example, the government conducted censuses to determine how much tax revenue they could collect from the population. Earlier still, shepherds counted livestock to determine how many animals they could sell and how many they needed for producing goods.

Since then, we have developed increasingly sophisticated algorithms for data processing. Now, we can replace what we don't know with predictions from machine learning algorithms. This helps us prepare for the future by predicting demand for our goods and making adjustments to our facilities accordingly. We can predict whether a person will repay a loan, allowing us to allocate funds to others and increase our profits.

We have developed not only algorithms, but also technologies and tools that have made data analysis cheaper and more convenient. These technologies have democratized the entire field of data analysis. Today, it is much easier for a company to start using data to its advantage. This explains the hype surrounding big data, artificial intelligence, and similar buzzwords.

Everyone can use data. Everyone can get value from it. It's not just those with a lot of money and resources, as was the case in the past.

As the TV series Mr. Robot notes, "It's an exciting time in the world right now".

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

### Exercise 00. First shell script

- Turn-in directory: `ex00/`.
- Files to turn in: `hh.sh`, `hh.json`.
- Allowed functions: curl, jq.

For this exercise, you will interact with the HeadHunter API to parse information about vacancies. To do so, you must understand how both curl and the [HeadHunter API work](https://dev.hh.ru/).

Write a shell script that:

- gets the name of a vacancy, "data scientist", as an argument (some later exercises will be based on this);
- downloads information about the first 20 vacancies that correspond to the search parameters;
- stores it in a file named `hh.json`.

The result in the file must be formatted so that each field is on a different line. See the example in the [ex00_sample.json](code-samples/ex00_sample.json) file.

Your script must be executable. The interpreter to use is `/bin/sh`.

Place your script and the parsing results in the `ex00` folder in the `src` directory of your repository.

## Chapter IV

### Exercise 01. Transforming JSON to CSV

- Turn-in directory: `ex01/`.
- Files to turn in: `filter.jq`, `json_to_csv.sh`, `hh.csv`.
- Allowed functions: jq.

In the previous exercise, you received a JSON file. Although it is a popular format for APIs, it is inconvenient for actual data analysis. Therefore, you will need to convert it into a CSV file, which is more convenient.

Write a shell script called `json_to_csv.sh` that:
- executes jq with a filter written in a separate file `filter.jq`;
- filters the following 5 columns corresponding to the vacancies: "id," "created_at," "name," "has_test," and "alternate_url";
- save the result to the CSV file `hh.csv`.

See the example below:

![1](misc/images/1.png)

The CSV file must have headers in the first row.

Your script must be executable. The interpreter to use is `/bin/sh`.

Place the filter file that converts JSON to CSV, as well as the result of the conversion, in the `ex01` folder in the `src` directory of your repository.

## Chapter V

### Exercise 02. Sorting a file

- Turn-in directory: `ex02/`.
- Files to turn in: `sorter.sh`, `hh_sorted.csv`.
- Allowed functions: cat, sort, head, tail.

Sometimes, it can be efficient for later stages of data analysis to have your data in a non-random order that is still somehow sorted. In this exercise, you will need to sort a CSV file with multiple columns.

Write a shell script called `sorter.sh` that:
- sorts the `hh.csv` file from the previous exercise according to the "created_at" column, and then by "id" in ascending order;
- saves the result in the CSV file `hh_sorted.csv`.

The CSV file must still have headers in the first row.

Your script must be executable. The interpreter to use is `/bin/sh`.

Place your shell script and your result of the sorting in the `ex02` folder in the `src` directory of your repository.

## Chapter VI

### Exercise 03. Replacing strings in a file

- Turn-in directory: `ex03/`.
- Files to turn in: `cleaner.sh`, `hh_positions.csv`.
- Allowed functions: no restrictions.

Raw data is messy. Before you can start analyzing it, you need to perform a lot of preprocessing. This exercise focuses on that process. If you look at your file from the previous exercise, you will see that every position that contains "Data Scientist" is highlighted (you don't have to check this). This is not surprising, since we used that string as the keyword for the HeadHunter API search. However, it does not provide useful information for us or the algorithms. Honestly, it's just noise that hinders data analysis.

Write a shell script called `cleaner.sh` that:
* takes "Junior," "Middle," or "Senior" from the position name. If the name does not contain any of these words, use "-" (e.g., "Senior Data Scientist" -> "Senior," "Analyst/Data Scientist" -> "-" and "Specialist/Data Scientist (Big Data, Predictive Analytics, Data Mining)" -> "-"). If there are multiple words, keep them all (e.g., "Middle/Senior Data Scientist" -> "Middle/Senior");
* saves the result in the CSV file `hh_positions.csv`.

See the example below:

    "id","created_at","name","has_test","alternate_url"
    "35218725","2020-04-11T18:03:53+0300","Junior",false,"https://hh.ru/vacancy/35218725"
    "36359628","2020-04-11T19:25:48+0300","Senior",false,"https://hh.ru/vacancy/36359628"
    "35895583","2020-04-12T12:06:33+0300","-",false,"https://hh.ru/vacancy/35895583"

The CSV file must have headers in the first row and be sorted as in the previous exercise.

Your script must be executable. Use the interpreter `/bin/sh`.

Place your shell script and the results of your cleaning in the `ex03` folder in the `src` directory of your repository.

## Chapter VII

### Exercise 04. Descriptive statistics

- Turn-in directory: `ex04/`.
- Files to turn in: `counter.sh`, `hh_uniq_positions.csv`.
- Allowed functions: no restrictions.

Before attempting anything more sophisticated, it is best to gain a basic understanding of your data. For this exercise, you need to count the number of unique positions in your file. This will help you understand if your data is skewed in some way. For instance, you might find that there are more seniors than juniors. This information may be useful for further analysis.

Write a shell script called `counter.sh` that:
* counts the unique values in the name column of the file you prepared in the previous exercise;
* sorts the table by that count in descending order;
* stores the result in the CSV file `hh_uniq_positions.csv`.

See the example below:

    "name","count"
    "Junior",10
    "Middle",5
    "Senior",3

The CSV file must have headers in the first row, as shown in the example.

Your script must be executable. Use the interpreter `/bin/sh`.

Place your shell script and the count results in the `ex04` folder in the `src` directory of your repository.

## Chapter VIII

### Exercise 05. Partitioning and concatenation

- Turn-in directory: `ex05/`.
- Files to turn in: `partitioner.sh`, `concatenator.sh`.
- Allowed functions: no restrictions.

When you have a large dataset, it can be useful to divide it into smaller partitions. Each partition contains a specific range of keys. One popular way to partition is by date. Each partition contains data from a specific date. For this exercise, you will need to perform this task.

Write a shell script called `partitioner.sh` that:
- takes as input the result of Exercise 03;
- stores slices of data with different "created_at" dates in separate CSV files named for that date.

See the example of such a file below:

    "id","created_at","name","has_test","alternate_url"
    "35218725","2020-04-11T18:03:53+0300","Junior",false,"https://hh.ru/vacancy/35218725"
    "36359628","2020-04-11T19:25:48+0300","Senior",false,"https://hh.ru/vacancy/36359628"

Write a shell script called `concatenator.sh` that:
- takes the separate files as input from the result of `partitioner.sh`;
- concatenates all the separate files into one CSV file.

The CSV file must have headers in the first row, as in the example. The CSV file resulting from `concatenator.sh` must be equal to the result of Exercise 3.

Your scripts must be executable. The interpreter to use is `/bin/sh`.

Place your shell scripts in the `ex05` folder in the `src` directory of your repository.