-- Advanced Select - Occupations
--https://www.hackerrank.com/challenges/occupations/forum
set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
	) temp
group by RowNumber;

-- otra opcion,MySQL
SELECT 
MIN(CASE WHEN Occupation = 'Doctor' THEN Name ELSE NULL END) AS Doctor,
MIN(CASE WHEN Occupation = 'Professor' THEN Name ELSE NULL END) AS Professor,
MIN(CASE WHEN Occupation = 'Singer' THEN Name ELSE NULL END) AS Singer,
MIN(CASE WHEN Occupation = 'Actor' THEN Name ELSE NULL END) AS Actor
FROM (
  SELECT a.Occupation,
         a.Name,
         (SELECT COUNT(*) 
            FROM Occupations AS b
            WHERE a.Occupation = b.Occupation AND a.Name > b.Name) AS rank
  FROM Occupations AS a
) AS c
GROUP BY c.rank;



-- Advanced Select - PADs
select concat(name,concat('(', concat(substr(occupation,1,1),')'))) from occupations order by name;

select concat('There are a total of',concat(' ',concat(count(occupation),concat(' ',concat(lower(occupation),'s.'))))) as total from occupations
group by occupation order by total;

--Easy, what-type-of-triangle
SELECT CASE
    WHEN A + B  > C and B + C > A AND A + C > B THEN
    CASE
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR B = C OR A = C THEN 'Isosceles'
        ELSE 'Scalene'
    END
    ELSE 'Not A Triangle'
END
FROM TRIANGLES;


-- Revising the Select Query I
SELECT *
FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION >=100000;

-- Revising the Select Query II
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA' AND POPULATION >= 120000;

-- Select All
SELECT *
FROM CITY

-- Select-by-id
SELECT *
FROM CITY
WHERE ID=1661;


-- Japanese-cities-attributes
SELECT *
FROM CITY
WHERE COUNTRYCODE='JPN'

-- Name-of-employees
SELECT NAME
FROM EMPLOYEE
ORDER BY NAME ASC

-- Salary-of-employees
SELECT NAME
FROM EMPLOYEE
WHERE MONTHS < 10 AND SALARY > 2000  
ORDER BY EMPLOYEE_ID ASC
