# MySQL Advanced

## Description
This project contains a series of MySQL scripts demonstrating advanced SQL concepts and techniques. Each script addresses specific tasks, showcasing various MySQL features such as triggers, stored procedures, views, and indexing.

## Project Structure
* `0-uniq_users.sql`: Creates a table with a unique email constraint.
* `1-country_users.sql`: Creates a table with an enumeration of countries.
* `2-fans.sql`: Ranks country origins of bands by the number of fans.
* `3-glam_rock.sql`: Lists Glam rock bands ranked by their longevity.
* `4-store.sql`: Creates a trigger to decrease quantity after adding a new order.
* `5-valid_email.sql`: Creates a trigger that resets valid_email when email is changed.
* `6-bonus.sql`: Creates a stored procedure to add a new correction for a student.
* `7-average_score.sql`: Creates a stored procedure to compute and store the average score for a student.
* `8-index_my_names.sql`: Creates an index on the first letter of name in the names table.
* `9-index_name_score.sql`: Creates an index on the first letter of name and score in the names table.
* `10-div.sql`: Creates a function that safely divides two numbers.
* `11-need_meeting.sql`: Creates a view of students who need a meeting based on their score and last meeting date.
* `100-average_weighted_score.sql`: Creates a stored procedure to compute and store the average weighted score for a student.
* `101-average_weighted_score.sql`: Creates a stored procedure to compute and store the average weighted score for all students.

## Requirements
* All scripts should be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
* All files should end with a new line
* All SQL queries should have a comment just before them describing the task
* All files should start with a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of files will be tested using `wc`

## Usage
To run these scripts, you'll need access to a MySQL server. You can execute each script using the MySQL command-line client:

mysql -u username -p database_name < script_name.sql

Replace `username`, `database_name`, and `script_name.sql` with your MySQL username, the name of the database you're using, and the name of the script you want to run, respectively.

## Author
Mohammed Elgaily
