# Pandas: working with Dataframes

Summary: Today we will help you acquire skills with Pandas.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions for the day](#specific-instructions-for-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Exercise 00. Load and save](#exercise-00-load-and-save)
5. [Chapter V](#chapter-v) \
    5.1. [Exercise 01. Basic operations](#exercise-01-basic-operations)
6. [Chapter VI](#chapter-vi) \
    6.1. [Exercise 02. Preprocessing](#exercise-02-preprocessing)
7. [Chapter VII](#chapter-vii) \
    7.1. [Exercise 03. Selects and aggregations](#exercise-03-selects-and-aggregations)
8. [Chapter VIII](#chapter-viii) \
    8.1. [Exercise 04. Enrichment and transformations](#exercise-04-enrichment-and-transformations)
9. [Chapter IX](#chapter-ix) \
    9.1. [Exercise 05. Pandas optimizations](#exercise-05-pandas-optimizations)
    
   
## Chapter I

### Foreword

Fun facts about pandas:

* Pandas are big eaters. Every day, they spend up to 12 hours filling their tummies, consuming up to 12 kilograms of bamboo.
* Unlike most other bears, pandas do not hibernate. When winter approaches, they head to lower elevations in their mountain homes, where it is warmer, and continue to eat bamboo.
* Sadly, these beautiful bears are endangered, and it’s estimated that only around 1,000 remain in the wild.
* On average, pandas defecate 40 times a day.
* According to legend, the panda was once an all-white bear. When a little girl tried to save a panda cub from a leopard, the leopard killed the girl instead. The pandas came to her funeral wearing armbands of black ashes. As they wiped their eyes, hugged each other, and covered their ears, the ashes smudged into their fur.
* A panda’s entire mating process takes about two or three days. After mating, the females chase the males out of their territory and raise their cubs alone.
* A giant panda usually gives birth to a single cub. Sometimes twins are born, but when this happens, the mother typically ignores the weaker cub. She does not have enough energy to care for two cubs.
* A giant panda’s face is cute, but not chubby. Its shape is the result of massive cheek muscles.
* Keeping even a single panda in a zoo is expensive. It costs five times more to keep a panda than the next most expensive animal, an elephant.
* If you think any of this is relevant to library pandas, it isn't. The name is derived from the term "panel data", which is an econometrics term for data sets that include observations over multiple time periods for the same individuals.

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
* For each major subtask in the exercise list (black bullets), your `ipynb` file should contain an `h2` heading to help your peers easily navigate your code.
* No imports are allowed except those mentioned in the "Authorized Functions" section of the title block of each exercise.
* You can use any built-in function unless it is prohibited in the exercise.
* Save and load all required data in the subfolder `data/`.

## Chapter IV

### Exercise 00. Load and save

- Turn-in directory: `ex00/`.
- Files to turn in: `load_and_save.ipynb`.
- Allowed functions: `import pandas as pd`.

Congratulations! You've completed five days and one rush. You dedicated them to building good fundamental skills in working with Python. You now know all the basic data types and useful built-in functions. You also know how to work with a virtual environment, use OOP and logging, parse data from websites, and send messages in a Rocket.Chat channel. The following week will focus more on data science. It will be a week full of Pandas exercises. Pandas is one of the most popular and useful libraries in the field. You will love it, too!

For this exercise, load the [log file](https://drive.google.com/file/d/1kgByP3EZHL8xAm-oGaBpf0-fPdVIYRaY/view) (put it in the directory `data` in the `src` directory of the day) into a dataframe, change the delimiter, and save it to a different file.

The task is:

1. `read_csv`:
   - Filter the rows with index 2 and 3 using the `skiprows` argument. We know that these observations were fake.
   - Filter the last two rows from the footer using the `skipfooter` argument. We know that these observations were fake, too.
   - Assign the following names to the columns: `datetime`, `user`.
   - Use datetime as the index column.
2. Rename `datetime` to `date_time`.
3. `to_csv`:
   - Use `’;’` as the delimiter.
   - Save it to a file named `feed-views-semicolon.log`.

The result of `read_csv` should be as follows:

```
In [3]: df.head()
Out[3]:
user
date_time
2020-04-17 12:01:08.463179 artem
2020-04-17 12:01:23.743946 artem
2020-04-17 12:35:52.735016 artem
2020-04-17 12:36:21.401412 oksana
2020-04-17 12:36:22.023355 oksana

In [4]: df.tail()
Out[4]:
user
date_time
2020-05-21 16:36:40.915488 ekaterina
2020-05-21 17:49:36.429237 maxim
2020-05-21 18:45:20.441142 valentina
2020-05-21 23:03:06.457819 maxim
2020-05-21 23:23:49.995349 pavel
```

Think about how many lines of code you would have needed to write if you had had
to do it without Pandas.

## Chapter V

### Exercise 01. Basic operations

- Turn-in directory: `ex01/`.
- Files to turn in: `basic_operations.ipynb`.
- Allowed functions: `import pandas as pd`.

We are confident that you understand this is not everything Pandas can do for you. Let's explore more.

In this exercise, you will work with a log of users who visited a page, including their timestamps.


1. Create a dataframe called `views` with two columns: `datetime` and `user` by reading `feed-views.log`.
   - Convert the `datetime` to the `datetime64[ns]` `Dtype`.
   - Extract the year, month, day, hour, minute, and second from the values of the `datetime` column to new columns.
2. Create the new column `daytime`.
   - Assign a particular time of day value if an hour is within a particular interval. For example, assign "afternoon" if the hour is greater than 11 and less than or equal to 17.
   - 0–3:59 = night, 4–6:59 = early morning, 7–10:59 = morning, 11–16:59 = afternoon, 17–19:59 = early evening, 20–23:59 = evening.
   - Use the method `cut` to solve this subtask.
   - Assign the column `user` as the index.
3. Calculate the number of elements in your dataframe.
   - Use the method `count()`.
   - Calculate the number of elements in each time-of-day category using the `value_counts()` method.
4. Sort the values in your dataframe by hour, minute, and second in ascending order simultaneously, not one by one.
5. Calculate the minimum and maximum for the hours and the mode for the daytime categories.
   - Calculate the maximum hour for the rows where the time of day is night.
   - Calculate the minimum hour for rows where the time of day is morning.
   - In addition, find out who visited the page during those hours and provide one example.
   - Calculate the mode for the hour and daytime.
6. Show the three earliest and latest hours of the day and their corresponding usernames using `nsmallest()` and `nlargest()`.
7. Use the `describe()` method to get the basic statistics for the columns.
   - To find the most popular visiting interval, calculate the interquartile range for the hour by extracting values from the result of the `describe()` method and storing them in the variable `iqr`.

## Chapter VI

### Exercise 02. Preprocessing

- Turn-in directory: `ex02/`.
- Files to turn in: `preprocessing.ipynb`.
- Allowed functions: `import pandas as pd`.

You will train machine learning models one day (no later than this week), but most of them require clean, enriched data without duplicates or missing values. Pandas is a great tool for this. Not only does it provide the means to perform descriptive analysis and better understand your data, but it also allows you to preprocess it. That's what you're going to do in this exercise.

1. [Download](https://drive.google.com/open?id=1kFMUiXtrlw5B6WTjJ-mUm4-STV28Zsvn) and read the CSV file, making `ID` the index column.
2. Count the number of observations using the method `count()`.
3. Drop the duplicates, taking into account only the following columns: `CarNumber`, `Make_n_Model`, and `Fines`.
   - Between two equal observations, choose the last one.
   - Check the number of observations again.
4. Work with missing values.
   - Check how many values are missing from each column.
   - Drop all columns with over 500 missing values using the argument `thresh`. Check how many missing values are in each column.
   - Replace all the missing values in the `Refund` column with the previous value in that column for that cell. Use the argument method and check how many values are missing from each column.
   - Replace all the missing values in the `Fines` column with the mean value of this column (excluding NA/NULL values when computing the mean). Check how many values are missing from each column.
5. Split and parse the make and model.
   - Use the apply method for both splitting and extracting values to the new columns, `Make` and `Model`.
   - Drop the column `Make_n_Model`.
   - Save the dataframe in the `auto.json` JSON file in the format below:
    ```
    [{"CarNumber":"Y163O8161RUS","Refund":2.0,"Fines":3200.0,"Make":"Ford",
    "Model":"Focus"},
    {"CarNumber":"E432XX77RUS","Refund":1.0,"Fines":6500.0,"Make":"Toyota",
    "Model":"Camry"}]
    ```

## Chapter VII

### Exercise 03. Selects and aggregations

- Turn-in directory: `ex03/`.
- Files to turn in: `selects_n_aggs.ipynb`.
- Allowed functions: `import pandas as pd`.

Okay, great! Now that we have cleaned our data, all the duplicates have been removed, the missing values have been deleted, and the columns have been reorganized for easier analysis. Now, we can proceed. We have many questions that need answering.

1. Load the JSON file that you created in the previous exercise into a dataframe.
   - Set the `CarNumber` column as the index.
2. Make the following selections:
   - Display the rows where the fines are greater than 2,100.
   - Display the rows where the fines are greater than 2,100 and the refund equals 2.
   - Display the rows where the models are from the list: `[’Focus’, ’Corolla’]`.
   - Display the rows where the car number is from the list: `[’Y7689C197RUS’, ’92928M178RUS’, ’7788KT197RUS’, ’H115YO163RUS’, ’X758HY197RUS’]`.
3. Make the aggregations with the `make` and `model`.
   - Display the median fines grouped by `make`.
   - Display the median fines grouped by `make` and `model`.
   - Display the number of fines grouped by `make` and `model` to understand if we can trust the median values.
   - Display the minimum and maximum fines grouped by `make` and `model` to better understand the variance.
   - Display the standard deviation of fines grouped by `make` and `model` to better understand the variance.
4. Make aggregations with car numbers.
   - Display the car numbers, grouped by the number of fines in descending order. We want to find those who most often violated the law.
   - Select from the initial dataframe all the rows corresponding to the top-1 car number. We want to zoom in a little bit.
   - Display the car numbers grouped by sum of fines in descending order. We want to find those who paid the most.
   - Select all the rows corresponding to the top-1 car number from the initial dataframe. We want to zoom in a little bit.
   - Display a table that answers the question, "Are there any car numbers connected to different models?"

## Chapter VIII

### Exercise 04. Enrichment and transformations

- Turn-in directory: `ex04/`.
- Files to turn in: `enrichment.ipynb`.
- Allowed functions: `import pandas as pd`, `import numpy as np`, `import requests`.

Cool! The more data you have, though, the better the analysis you can conduct. Let's enrich our initial dataset.

1. Read the JSON file that you saved in ex02.
   - One of the columns is a float, so let's define its format in Pandas using `pd.options.display.float_format`: floats should be displayed with two decimals.
   - There are missing values from the Model; do not do anything with them.
2. Enrich the dataframe using a sample from that dataframe.
   - Create a sample with 200 new observations using `random_state = 21`.
     - The sample should not contain new combinations of the `car number`, `make`, and `model`, so the entire dataset will be consistent in this regard.
     - There are no restrictions on the `refund` and `fines` columns. You can randomly select a value from these columns and apply it to any car number.
   - Concatenate the sample with the initial dataframe to create a new dataframe, `concat_rows`.
3. Enrich the `concat_rows` dataframe with a new column containing generated data.
   - Create a series named "Year" with random integers from 1980 to 2019.
   - Use `np.random.seed(21)` before generating the years.
   - Concatenate the series with the data frame and name it `fines`.
4. Enrich the dataframe with data from another dataframe.
   - Create a new dataframe with car numbers and their owners.
      - Get the most popular surnames in the US (you can find the file [surname.json](datasets/surname.json) in the folder datasets).
      - Create a new series with the surnames. They should not contain special characters, such as commas or brackets. The count should equal the number of unique car numbers in the sample (use `random_state = 21`).
      - Create the dataframe `owners` with two columns: `CarNumber` and `SURNAME`.
   - Append five more observations to the `fines` dataframe. Come up with your own ideas for `CarNumber`, etc.
   - Delete the last 20 observations from the `owners` dataframe and add three new observations that are not the same as those added to the `fines` dataframe.
   - Join the two dataframes.
     - The new dataframe should contain **only** the car numbers that exist in **both** dataframes.
     - The new dataframe should contain **all** the car numbers from **both** dataframes.
     - The new dataframe should contain **only** the car numbers from the `fines` dataframe.
     - The new dataframe should contain **only** the car numbers from the `owners` dataframe.
5. Create a pivot table from the `fines` dataframe. It should look like this (the values are the sums of the fines), but with all the years. The values may be different for you.

    ![pivot-table](misc/images/pivot-table.png)

6. Save both the `fines` and `owners` dataframes to CSV files without an index.

## Chapter IX

### Exercise 05. Pandas optimizations

- Turn-in directory: `ex05/`.
- Files to turn in: `optimizations.ipynb`.
- Allowed functions: `import pandas as pd`, `import gc`.

We are returning to the topic of code efficiency. By now, you should know the basics of Pandas. Now, it's time to learn some advanced features that most Pandas users don't know about or use.

1. Read the `fines.csv` file that you saved in the previous exercise.
2. Iterations: in all the following subtasks, you need to calculate `fines/refund*year` for each row. Create a new column with the calculated data. Measure the time using the magic command `%%timeit` in the cell.
   - Write a function that loops through the dataframe using `for i in range(0, len(df))`, `iloc`, and `append()` to a list. Assign the result of the function to a new column in the dataframe.
   - Do it using `iterrows()`.
   - Do it using `apply()` and a lambda function.
   - Do it using `Series` objects from the dataframe.
   - Do it as in the previous subtask, but use the method `.values`.
3. Indexing: measure the time using the magic command `%%timeit` in the cell.
   - Get a row for a specific `CarNumber`, for example, "O136HO197RUS."
   - Set the index in your dataframe with `CarNumber`.
   - Again, get a row for the same `CarNumber`.
4. Downcasting:
   - Run `df.info(memory_usage='deep')`, and pay attention to the Dtype and memory usage.
   - Make a `copy()` of your initial dataframe into another dataframe, `optimized_df`.
   - Downcast from `float64` to `float32` for all columns.
   - Downcast from `int64` to the smallest numerical Dtype possible.
   - Run `info(memory_usage='deep')` for your new dataframe. Pay attention to the Dtype and memory usage.
5. Categories:
   - Change the `object` type columns to `category`.
   - This time, check the memory usage. It will probably decrease by 2–3 times compared to the initial dataframe.
6. Memory clean:
   - Using the library `gc` and the command `%reset_selective`, clean the memory of your initial dataframe only.