CREATE TABLE student(
    student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
); -- Creating table

INSERT INTO student VALUES(1,'Jack', 'Biology'); -- Inserting row in position 1
INSERT INTO student VALUES(2,'Kate', 'Sociology'); -- Inserting row in position 2
INSERT INTO student(student_id,name) VALUES(3,'Camila')
INSERT INTO student VALUES(4,'Gordo', 'Math');

SELECT * FROM student;

DESCRIBE student;

--Adding constrains to the tables
DROP TABLE student;

--Example 3: With autoincrement and default values
CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'Undecided',
    PRIMARY KEY(student_id)
); -- Creating table, --Column name can not be empty

INSERT INTO student(name,major) VALUES('Jack', 'Biology'); -- Inserting row in position 1
INSERT INTO student(name,major) VALUES('Kate', 'Sociology');
INSERT INTO student(name,major) VALUES('Camila','Math');
INSERT INTO student(name) VALUES('Gordo');

SELECT * FROM student;

--Example 2: Using not noll and default values by columns

CREATE TABLE student(
    student_id INT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'Undecided',
    PRIMARY KEY(student_id)
); -- Creating table, --Column name can not be empty

INSERT INTO student VALUES(1,'Jack', 'Biology'); -- Inserting row in position 1
INSERT INTO student VALUES(2,'Kate', 'Sociology'); -- Inserting row in position 2
INSERT INTO student VALUES(3,'Camila','Math');
INSERT INTO student(student_id,name) VALUES(4,'Gordo');

SELECT * FROM student;

--Example 1: Not null and unique

CREATE TABLE student(
    student_id INT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE,
    PRIMARY KEY(student_id)
); -- Creating table, --Column name can not be empty

INSERT INTO student VALUES(1,'Jack', 'Biology'); -- Inserting row in position 1
INSERT INTO student VALUES(2,'Kate', 'Sociology'); -- Inserting row in position 2
INSERT INTO student VALUES(3,NULL,'Math'); -- Chillo porque se puso imposicion que no hubieran NULL
INSERT INTO student VALUES(3,'Kate', 'Biology'); -- Inserting row in position 2

--Updating and Delenting rows using where, set, update, delete

--Printing values
SELECT * FROM student;


--Getting table ready for exercises
DROP TABLE student;

CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'Undecided',
    PRIMARY KEY(student_id)
); -- Creating table, --Column name can not be empty

INSERT INTO student(name,major) VALUES('Jack', 'Biology'); -- Inserting row in position 1
INSERT INTO student(name,major) VALUES('Kate', 'Sociology');
INSERT INTO student(name,major) VALUES('Camila','Math');
INSERT INTO student(name) VALUES('Gordo');
