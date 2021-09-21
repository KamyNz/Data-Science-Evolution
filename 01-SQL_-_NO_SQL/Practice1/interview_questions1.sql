--Practical SQL

--from Link: https://learnsql.com/blog/common-sql-job-interview-questions/

--question 1
SELECT school.school_name,student.student_name,school.city,school.school_id
FROM school
JOIN student ON school.school_id=student.school_id
WHERE  student.city <> 'New York' AND school.city=student.city

--question 2
SELECT subject.subject_name, subject.lecturer, subject.max_score as max_condition
FROM subject
JOIN student ON subject.subject_id=student.subject_id
WHERE subject.subject_name <> 'Computer Science'
GROUP BY subject.subject_name
HAVING subject.max_score >= 100 AND subject.max_score <= 200


--question 3

--code1
--the alias might not work because function extract(year,timestamp) should be used
--and in the where clause

--code2
--the equal might not work, it is better to use a view for this

--question 4
SELECT name
FROM worker
WHERE id NOT IN (SELECT manager_id FROM departments)

--What will be the result of the query below?
--R// It should result in Candice Green





--Creating tables for practice:
--DROP TABLE school
CREATE TABLE school(
    school_id   INT AUTO_INCREMENT,
    school_name VARCHAR(20) NOT NULL,
    city        VARCHAR(20) NOT NULL,
    PRIMARY KEY(school_id)
);

INSERT INTO school(school_name,city) VALUES('Stanford','Stanford');
INSERT INTO school(school_name,city) VALUES('University of Cali','San Francisco');
INSERT INTO school(school_name,city) VALUES('Harvard University','New York');
INSERT INTO school(school_name,city) VALUES('MIT','Boston');
INSERT INTO school(school_name,city) VALUES('Yale','New Haven');

--DROP TABLE student
CREATE TABLE student(
    student_id      INT(4),
    student_name    VARCHAR(20) NOT NULL,
    city            VARCHAR(20) NOT NULL,
    school_id       INT
);

INSERT INTO student(student_id,student_name,city,school_id) VALUES('1001','Peter Brebec','New York',1);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1002','John Goorgy','San Francisco',2);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('2003','Peter Brebec','New York',3);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1004','Peter Brebec','New York',5);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1005','Peter Brebec','New York',1);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1006','Peter Brebec','New York',5);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1007','Peter Brebec','New York',2);
INSERT INTO student(student_id,student_name,city,school_id) VALUES('1008','Peter Brebec','New York',2);








--Interview questions, theory

--"What are the basic elements of an SQL query?" , a query requests information from relational database. Allows you to select specific columns from specific tables, filter and sort information if necessary

--SELECT,   to choose columns
--FROM ,    to choose a table
--JOIN ON,  to join a table
--WHERE,    filter records
--GROUP BY, group records
--HAVING,   filter groups
--ORDER BY, to sort output

--What Is the SQL WHERE Clause?
--R//WHERE clause, filter results and add conditions

--What do the LIKE and NOT LIKE operators do?

--Explain the usage of AND, OR, and NOT clauses.

--What is a NULL value?

--What does a JOIN do? What are the different types of JOIN clauses?

--Explain the GROUP BY clause.

--What is the difference between the WHERE and HAVING clauses?

--What does ORDER BY do?

--What does UNION do? What is the difference between UNION and UNION ALL?

--What do the INTERSECT and MINUS clauses do?

--What is the role of the DISTINCT keyword?

--Explain the use of aliases in queries.






-- Doing queries
#1 Create a query that displays EMPFNAME, EMPLNAME, DEPTCODE, DEPTNAME, LOCATION from EMPLOYEE, and DEPARTMENT tables. Make sure the results are in the ascending order based on the EMPFNAME and LOCATION of the department.

#2 Display EMPFNAME and "TOTAL SALARY" for each employee

#3 Display MAX and 2nd MAX SALARY from the EMPLOYEE table.

#4 Display the TOTAL SALARY drawn by an analyst working in dept no 20

#5 Compute average, minimum and maximum salaries of the group of employees having the job of ANALYST.









--CREATING TABLES
CREATE TABLE DEPARTMENT
(
   DEPTCODE   INT(10),
   DeptName   CHAR(30),
   LOCATION   VARCHAR(33)
);

CREATE TABLE EMPLOYEE
(
   EmpCode      INT(4),
   EmpFName     VARCHAR(15),
   EmpLName     VARCHAR(15),
   Job          VARCHAR(45),
   Manager      CHAR(4),
   HireDate     DATE,
   Salary       INT(6),
   Commission   INT(6),
   DEPTCODE     INT(2)
);

--MAKIGN CHANGES
ALTER TABLE DEPARTMENT
ADD PRIMARY KEY (DEPTCODE);

ALTER TABLE DEPARTMENT
CHANGE COLUMN DEPTCODE DEPTCODE INT(10) NOT NULL;

ALTER TABLE DEPARTMENT
CHANGE COLUMN DeptName DeptName CHAR(30) UNIQUE;

ALTER TABLE DEPARTMENT
CHANGE COLUMN LOCATION LOCATION VARCHAR(33) NOT NULL;

ALTER TABLE DEPARTMENT
CHANGE COLUMN DeptName DeptName VARCHAR(15) UNIQUE;

ALTER TABLE EMPLOYEE
ADD PRIMARY KEY (EmpCode);

ALTER TABLE EMPLOYEE
CHANGE COLUMN EmpCode EmpCode INT(4) NOT NULL;

ALTER TABLE EMPLOYEE
ADD FOREIGN KEY (DEPTCODE)
REFERENCES DEPARTMENT(DEPTCODE);

ALTER TABLE EMPLOYEE
CHANGE COLUMN Salary Salary DECIMAL(6,2);

ALTER TABLE EMPLOYEE
ADD COLUMN DOB DATE
AFTER EmpLName;

ALTER TABLE EMPLOYEE
DROP COLUMN DOB;

-- INSERTING VALUES
INSERT INTO DEPARTMENT VALUES (10, 'FINANCE', 'EDINBURGH'),
                              (20,'SOFTWARE','PADDINGTON'),
                              (30, 'SALES', 'MAIDSTONE'),
                              (40,'MARKETING', 'DARLINGTON'),
                              (50,'ADMIN', 'BIRMINGHAM');

INSERT INTO EMPLOYEE
VALUES (9369, 'TONY', 'STARK', 'SOFTWARE ENGINEER', 7902, '1980-12-17', 2800,0,20),
       (9499, 'TIM', 'ADOLF', 'SALESMAN', 7698, '1981-02-20', 1600, 300,30),
       (9566, 'KIM', 'JARVIS', 'MANAGER', 7839, '1981-04-02', 3570,0,20),
       (9654, 'SAM', 'MILES', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
       (9782, 'KEVIN', 'HILL', 'MANAGER', 7839, '1981-06-09', 2940,0,10),
       (9788, 'CONNIE', 'SMITH', 'ANALYST', 7566, '1982-12-09', 3000,0,20),
       (9839, 'ALFRED', 'KINSLEY', 'PRESIDENT', 7566, '1981-11-17', 5000,0, 10),
       (9844, 'PAUL', 'TIMOTHY', 'SALESMAN', 7698, '1981-09-08', 1500,0,30),
       (9876, 'JOHN', 'ASGHAR', 'SOFTWARE ENGINEER', 7788, '1983-01-12',3100,0,20),
       (9900, 'ROSE', 'SUMMERS', 'TECHNICAL LEAD', 7698, '1981-12-03', 2950,0, 20),
       (9902, 'ANDREW', 'FAULKNER', 'ANAYLYST', 7566, '1981-12-03', 3000,0, 10),
       (9934, 'KAREN', 'MATTHEWS', 'SOFTWARE ENGINEER', 7782, '1982-01-23', 3300,0,20),
       (9591, 'WENDY', 'SHAWN', 'SALESMAN', 7698, '1981-02-22', 500,0,30),
       (9698, 'BELLA', 'SWAN', 'MANAGER', 7839, '1981-05-01', 3420, 0,30),
       (9777, 'MADII', 'HIMBURY', 'ANALYST', 7839, '1981-05-01', 2000, 200, NULL),
       (9860, 'ATHENA', 'WILSON', 'ANALYST', 7839, '1992-06-21', 7000, 100, 50),
       (9861, 'JENNIFER', 'HUETTE', 'ANALYST', 7839, '1996-07-01', 5000, 100, 50);
