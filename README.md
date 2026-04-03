# Python-Parallel-Text-Handling-Processor

## Overview

This project highlights the performance difference between **Sequential Execution** and **Parallel Processing using Multiprocessing** for analyzing customer reviews.

The system processes multiple text files, evaluates sentiment using a simple rule-based method, measures execution time, and saves the output into a SQLite database.

---

## Key Features

* Simple rule-based sentiment evaluation (+1 for positive, -1 for negative)
* Categorization of reviews (Positive / Negative / Neutral)
* Sequential processing (step-by-step execution)
* Parallel processing using multiple CPU cores
* Comparison of execution time for both approaches
* Storage of processed data in SQLite database
* Display of Process IDs to show parallel task execution

---

## Working Process

1. The program reads multiple files containing customer feedback.
2. Each review is analyzed using a rule-based scoring system:

   * Positive words increase the score (+1)
   * Negative words decrease the score (-1)
3. Based on the final score, the review is classified as:

   * Score greater than 0 → Positive
   * Score less than 0 → Negative
   * Score equal to 0 → Neutral
4. The system then compares performance by calculating:

   * Time taken for sequential execution
   * Time taken for multiprocessing execution
5. All processed results are stored in a SQLite database (`reviews.db`).

---

## Technologies Implemented

* Python Programming Language
* Multiprocessing Library
* SQLite Database (sqlite3)
* Time Module (for performance tracking)
* OS Module (for process handling)


