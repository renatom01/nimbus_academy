# SQL Query and Python Code README

## SQL Query

### Objective
The SQL query is designed to retrieve email addresses from a database named `nimbus_test`. It involves joining two tables (`data_table` and `email_table`) based on a common column (`join_id`). The query includes filtering conditions on columns `column_1`, `column_2`, and `column_3` of the `data_table` to meet specific criteria.

### Instructions
1. **Setting the Database:**
    - Use the `nimbus_test` database.

    ```sql
    USE DATABASE nimbus_test;
    ```

2. **Selecting Email Addresses:**
    - Select the `email` column from the joined tables (`data_table` and `email_table`) based on the `join_id`.

    ```sql
    SELECT email
    FROM public.data_table AS data_t
    JOIN public.email_table AS email_t ON data_t.join_id = email_t.join_id
    ```

3. **Filtering Conditions:**
    - Filter rows based on the following conditions:
        - `column_1` should be divisible by 2 without creating a decimal number.
        - `column_2` should be smaller than `column_1`.
        - `column_3` should end with a 1.

    ```sql
    WHERE
      data_t.column_1 % 2 = 0
      AND data_t.column_2 < data_t.column_1
      AND data_t.column_3 % 10 = 1;
    ```

### Expected Results
The query has been run on snowflake and returned the email: 1867945546@theinformationlab.nl

### Screenshot
![Screen Shot 2023-12-17 at 18 20 24](https://github.com/renatom01/nimbus_academy/assets/80773401/3a3b659c-ef42-4531-83b6-9ad1b8451ce1)


---

## Python Code

### Objective
The Python code defines a function named `multiply_func` that generates random pairs of integers (`A` and `B`) in the range [1, 9]. It calculates their product `C = A * B` and prints the values of `A` and `C`. The function continues this process until it finds a pair `(A, B)` such that the product `C` equals 4, at which point it prints a success message and exits the loop.

### Instructions
1. **Import Library:**
    - Import the `random` library.

    ```python
    # Importing library
    import random
    ```

2. **Function Description:**
    - The function randomly generates pairs of integers `A` and `B`.
    - Calculates their product `C = A * B`.
    - Prints the values of `A` and `C`.
    - Continues the process until a pair `(A, B)` results in `C = 4`.

    ```python
    def multiply_func():
        # ... (function details as per the code provided)
    ```

3. **Function Calling:**
    - Call the `multiply_func` function.

    ```python
    # Function calling
    multiply_func()
    ```

### Expected Results
The function is expected to print values of `A` and `C` until it finds a pair `(A, B)` that results in `C = 4`.

### Screenshot
![Screen Shot 2023-12-18 at 10 05 58](https://github.com/renatom01/nimbus_academy/assets/80773401/d9dd0daf-871b-4a50-a255-0ef3d00031ea)


---


