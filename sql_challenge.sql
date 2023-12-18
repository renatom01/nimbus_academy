-- Setting the database
USE DATABASE nimbus_test;
-- Selecting email_address column
SELECT email
FROM public.data_table AS data_t
JOIN public.email_table AS email_t ON data_t.join_id = email_t.join_id
-- Join using the join_id column
WHERE
  -- column_1 needs to be divisible by 2 without creating a decimal number
  data_t.column_1 % 2 = 0
  -- column_2 needs to be smaller than column_1
  AND data_t.column_2 < data_t.column_1
  -- Column_3 needs to end with a 1
  AND data_t.column_3 % 10 = 1;