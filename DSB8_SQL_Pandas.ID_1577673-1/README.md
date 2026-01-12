# SQL and Pandas

Summary: Today you will acquire skills with SQL.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions for the day](#specific-instructions-for-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 00. Select](#exercise-00-select)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 01. Subquery](#exercise-01-subquery)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 02. Join](#exercise-02-join)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 03. Aggregations](#exercise-03-aggregations)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 04. A/B testing](#exercise-04-a/b-testing)
    
   
## Chapter I

### Foreword

Is it "Sequel" or "Ess Kyew Ell"? How do you correctly pronounce SQL? Some interviewers reject interviewees if they don't pronounce it correctly. Apparently, knowing the correct pronunciation is important.

Originally, SQL was spelled SEQUEL (Structured English Query Language), but it was later discovered that this was the registered trademark of an aircraft company, so the spelling was changed. The authors had to change it. Since then, it has been SQL (Structured Query Language). One of the authors [was asked](http://patorjk.com/blog/2012/01/26/pronouncing-sql-s-q-l-or-sequel/) which pronunciation is correct. He answered:

```
"Since the language was originally named SEQUEL, many people continued to pronounce the name that way after it was shortened to SQL. Both pronunciations are widely used and recognized. As for which is more 'official', I guess the authority would be the ISO standard, which is spelled (and presumably pronounced) 'S-Q-L'.

Thanks for your interest!"

— Don Chamberlin
```

One of the authors said that either method can be used. "S-Q-L" is supposedly the more official method. What do other "authority" figures think?

Apparently, the official pronunciation of "MySQL" is "My Ess Kyew Ell" (not "My Sequel"). However, the official Oracle documentation says that the correct pronunciation is "Sequel".

Before diving into the exercises, you must make an important choice: Will you pronounce it "Sequel" or "S-Q-L"? Would you prefer a more informal or formal approach? Where does your heart lie?

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

* Use the Jupyter notebook to work with your code.
* For each major subtask in the list of exercises, your ipynb file should have an H2 heading to help your peers easily navigate your code.
* No imports are allowed except those mentioned in the "Authorized Functions" section of the title block of each exercise.
* You can use any built-in function as long as it is not prohibited by the exercise.
* Today, you may only use the following Pandas methods: `io.sql.read_sql` and `to_sql`, unless otherwise prescribed in the exercise.
* Save and load all required data in the `data/` subfolder.

## Chapter IV

### Exercise 00. Select

- Turn-in directory: `ex00/`.
- Files to turn in: `ex00_first_select.ipynb`.
- Allowed functions: `import pandas as pd`, `import sqlite3`.

Having only Python in your toolbox can be limiting. Do you remember the first day of Bootcamp, when you used command-line tools because they're more efficient for certain tasks? Today, you will work with SQL. Why might that be useful to you? Sometimes, your data might not be stored in CSV or JSON files, but rather in a database. In that case, you would need to extract the data somehow. SQL can be used with Apache Spark and Hive, which are tools for processing big data. With Hive, it's called HQL.

Download [the SQLite database](https://drive.google.com/open?id=1zQ8AR2Ry3ajzB3UZO1Sfk3xtDJlzQF2M). Throughout the day, you will work with different tables from the database using Pandas. They are all connected and refer to the same project. The dataset is real and comes from an educational company. The company has its own platform where students can check if their solution is correct and receive other feedback. The table checker stores logs of which labs users checked and when.

![lada](misc/images/lada.png)

The company created a new page on the platform called "Newsfeed", where these logs are visible to all students in the program. Logs of page visits are stored in a separate table called "pageviews". The hypothesis was that the page would create peer pressure and prompt students to start working on the labs earlier. This could be beneficial because students could complete more iterations and experiment with different approaches. In this series of exercises, you will determine whether this hypothesis is correct.

![lenta](misc/images/lenta.png)

But first, let's start with something simple. For this exercise, you need to retrieve filtered data from a database table. Why is it important to filter the data in the query but not in Pandas afterward? Because tables can be enormous. If you try to retrieve the entire table, you won't be able to process it. Always keep this in mind.

First, choose only the columns you need.

Second, select the rows you need.

In more detail:

1. Put the database in the data subfolder in the src directory.
2. Create a connection to the database using the sqlite3 library.
3. Get the schema of the `pageviews` table using `pd.io.sql.read_sql()` and the query `"PRAGMA table_info(pageviews);"`.
4. Get only the first ten rows of the `pageviews` table to see what the table looks like.
5. Use one query to get the subtable where:
   - Only "uid" and "datetime" are used.
   - Only user data (`user_*`), not admin data, is used.
   - It is sorted by "uid" in ascending order.
   - The index column is "datetime".
   - "datetime" is converted to a `DatetimeIndex`.
   - The name of the dataframe is `pageviews`.
6. Close the connection to the database.

## Chapter V

### Exercise 01. Subquery

- Turn-in directory: `ex01/`.
- Files to turn in: `ex01_subquery.ipynb`.
- Allowed functions: `import pandas as pd`, `import sqlite3`.

Okay, let's try something more complicated. Have you heard of subqueries? They're like queries inside queries. How could they be useful to you? Typically, you might want to perform aggregations on a select that you had previously made. Note, however, that nested queries run first, followed by the main query.

Here's what you need to do:

1. Create a connection to the database using the `sqlite3` library.
2. Get the schema of the `checker` table.
3. Get only the first ten rows of the table to see what the table looks like.
4. Count how many rows satisfy the following conditions using one query with any number of subqueries.
   - Count the rows from the `pageviews` table, but only those from the `checker` table with:
     - `status = 'ready'`, we do not want to analyze logs that are
    status checking;
     - `numTrials = 1`, we only want to analyze the first commits because they tell us when a student started working on a lab;
     - "labnames" should be from the list: `laba04`, `laba04s`, `laba05`, `laba06`, `laba06s`, and `project1`. Only these were active during the experiment.
   - Store the checkers in the dataframe with the column "cnt".
5. Close the connection.

## Chapter VI

### Exercise 02. Join

- Turn-in directory: `ex02/`.
- Files to turn in: `ex02_joins.ipynb`.
- Allowed functions: `import pandas as pd`, `import sqlite3`.

In this exercise, you will create a so-called datamart. A datamart is a table used for analytics. It is typically formed by combining different tables. For this exercise, we will collect various pieces of user data, such as their first commit date and their first visit to the newsfeed. This will help us analyze the data later.

Read the full task description to see what you need to do:

1. Create a connection to the database using the `sqlite3` library.
2. Create a new table called `datamart` in the database by joining the tables `pageviews` and `checker` using only one query.
   - The table should have the following columns: "uid", "labname", "first_commit_ts", and "first_view_ts".
   - "first_commit_ts" is a new name for the "timestamp" column in the checker table. It shows the first commit from a particular lab and user.
   - "first_view_ts" shows the first time a user visited the pageviews table. It is the timestamp of when a user visited the newsfeed.
   - `status = 'ready'` should still be a filter.
   - `numTrials = 1` should still be a filter.
   - "labnames" should be from the list: `laba04`, `laba04s`, `laba05`, `laba06`, `laba06s`, and `project1`.
   - The table should contain only users (uids with user_*), not admins.
   - "first_commit_ts" and "first_view_ts" should be parsed as `datetime64[ns]`.
3. Using Pandas methods, create two dataframes: `test` and `control`.
   - `test` should contain users with values in "first_view_ts".
   - `control` should contain users with missing values in "first_view_ts".
   - Replace the missing values in the control table with the average "first_view_ts" value of the test users. We will use this value for future analyses.
   - Save both tables in the database. You will use them in the next exercises.
4. Close the connection.

_A small piece of advice: do this step by step, from simple to more complex. This will help you debug your queries._

## Chapter VII

### Exercise 03. Aggregations

- Turn-in directory: `ex03/`.
- Files to turn in: `ex03_aggs.ipynb`.
- Allowed functions: `import pandas as pd`, `import sqlite3`.

Our previous work was merely data preparation. We didn't gain any insights from it. It's time to change that. Do you remember our hypothesis that users would start working on labs earlier if they saw the newsfeed? The key metric for us is the time between when a user starts working on a lab (their first commit) and the lab's deadline.

For this exercise, you need to:

1. Create a connection to the database using the `sqlite3` library.
2. Get the schema of the `test` table.
3. Get only the first ten rows of the `test` table to see what it looks like.
4. Find the minimum value of the delta between the first commit and the deadline of the corresponding lab for all users using only one query.
   - Do this by joining the table with the `deadlines` table.
   - The difference should be displayed in hours.
   - Do not take lab `project1` into account; it has longer deadlines and will be an outlier.
   - The value should be stored in the dataframe `df_min` with the corresponding uid.
5. Do the same thing for the maximum, but use only one query. The dataframe name is `df_max`.
6. Do the same thing, but for the average. Use only one query. This time, your dataframe should not include the uid column. The dataframe name is `df_avg`.
7. We want to test the hypothesis that users who visited the newsfeed just a few times have a lower delta between the first commit and the deadline. To do this, calculate the correlation coefficient between the number of pageviews and the difference.
   - Using only one query, create a table with the following columns: "uid", "avg_diff", and "pageviews".
   - "uid" is the uids that exist in the `test`.
   - "avg_diff" is the average delta between the first commit and the lab deadline per user.
   - "pageviews" is the number of Newsfeed visits per user.
   - Do not take the lab `project1` into account.
   - Store it in the dataframe `views_diff`.
   - Use the Pandas `corr()` method to calculate the correlation coefficient between the number of pageviews and the difference.
8. Close the connection.

## Chapter VIII

### Exercise 04. A/B testing

- Turn-in directory: `ex04/`.
- Files to turn in: `ex04_ab-test.ipynb`.
- Allowed functions: `import pandas as pd`, `import sqlite3`.

So, let's finally find out if the newsfeed affected the students' behavior. Did they start working on the labs earlier? Remember, we have two tables prepared in the database: a test group and a control group. We are going to conduct an A/B test. First, we need to calculate the difference between the first commit and the deadline, both before and after the students visited the page for the first time. We need to do the same for the control group.

In other words, each user in the test group has their own timestamp for their first visit to the newsfeed. We want to calculate the average delta (first commit minus deadline) before and after that timestamp. We will do the same for users in the control group. You might say, "But they did not visit the newsfeed at all". That is correct. Earlier, we decided to use the average timestamp of the first view from the test group for control group users.

If the delta before the first newsfeed visit is significantly different compared to the delta afterward in the test group, but we don't see the same effect in the control group, then creating the page was a great idea. We can roll it out to the whole group.

In more detail:

1. Use the `sqlite3` library to create a connection to the database.
2. Using one query per group, create two dataframes, `test_results` and `control_results`, with the columns "time" and "avg_diff" and two rows.
   - The "time" column should contain the values "after" and "before".
   - The "avg_diff" should contain the average delta for all users for the time period before and after their first visit to the page.
   - Only take into account users with observations before and after.
3. We are still not using the lab `project1`.
4. Close the connection.
5. Have the answer ready: "Did the hypothesis turn out to be true, and does the page affect students' behavior?"