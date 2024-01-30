#CREATE DATABASE employee_db;


-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode ->>
SET sql_safe_updates = 0;

USE employee_db;

DESCRIBE e_db;

SELECT * FROM e_db;

# --------------------------------------------------------------------- Cleaning the emp_id column ---------------------------------------
# This SQL code modifies the "e_db" table, changing the name of column ï»¿id to emp_id. 
ALTER TABLE e_db
CHANGE COLUMN ï»¿id emp_id VARCHAR(20) NULL;


# --------------------------------------------------------------------- Cleaning the "Birthdate Column".----------------------------------

SELECT birthdate FROM e_db;

# This SQL code updates the "birthdate" column in the "e_db" table, transforming date formats containing either "/" or "-" to the standardized format '%Y-%m-%d', while setting other cases to NULL.
UPDATE e_db
SET birthdate = CASE
	WHEN birthdate LIKE '%/%' THEN date_format(str_to_date(birthdate, '%m/%d/%Y'), '%Y-%m-%d')
    WHEN birthdate LIKE '%-%' THEN date_format(str_to_date(birthdate, '%m-%d-%Y'), '%Y-%m-%d')
    ELSE NULL
END;

# change the data type of the birthday column.
ALTER TABLE e_db
MODIFY COLUMN birthdate DATE;


#  -------------------------------------------------------------------------------- cleaning hire_date column ---------------------------------
select  hire_date from e_db;

# This SQL code updates the "hire_date" column in the "e_db" table, transforming date formats containing either "/" or "-" to the standardized format '%Y-%m-%d', while setting other cases to NULL.
UPDATE e_db
SET hire_date = CASE
	WHEN hire_date LIKE '%/%' THEN date_format(str_to_date(hire_date, '%m/%d/%Y'), '%Y-%m-%d')
    WHEN hire_date LIKE '%-%' THEN date_format(str_to_date(hire_date, '%m-%d-%Y'), '%Y-%m-%d')
    ELSE NULL
END;

# change the data type of the " hire_date column ".
ALTER TABLE e_db
MODIFY COLUMN hire_date DATE;


# ---------------------------------------------------------------------------------------------- Cleaning the "termdate" column.---------------------------
select termdate from e_db;

# This SQL code updates the "termdate" column in the "e_db" table, converting the date and time string to the '%Y-%m-%d' format, specifically handling the UTC format. It applies the update only to non-null and non-empty "termdate" values.

UPDATE e_db
SET termdate = IF(termdate IS NOT NULL AND termdate != '', date(str_to_date(termdate, '%Y-%m-%d %H:%i:%s UTC')), '0000-00-00')
WHERE true;

SELECT termdate from e_db;

SET sql_mode = 'ALLOW_INVALID_DATES';

ALTER TABLE e_db
MODIFY COLUMN termdate DATE;

# ---------------------------------------------------------------------------------------------------------- creating a new column "AGE" ----------------------
ALTER TABLE e_db ADD COLUMN age INT;

# This SQL code updates the "age" column in the "e_db" table, calculating the age based on the "birthdate" column and the current date.
UPDATE e_db
SET age = timestampdiff(YEAR, birthdate, CURDATE());

################################################################################################################################################################

