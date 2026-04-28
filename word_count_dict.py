'''
Questions ENROUTE Data Engineer - First Technical Round


1. ETL VS ELT

TARGET - DWH (SNOWFLAKE)

ETL -> T -> ?????? - Python

ELT -> T -> ?????? - SQL

2. WHERE VS HAVING

SELECTSUM(salary ), DEPARTMENT_ID
FROM DEPARTEMNT
WHERE SUM(salary) > 1000000
GROUP BY DEPARTMENT_ID
HAVING DEPARMENT_ID > 20;

3. COMMON TABLE EXPRESSION (CTE)

with cte_myselection as (
select * from department
)
select * from cte_myselection;

select * from cte_myselection;

CREATE VIEW view_myselection as (
select * from department
);
select * from view_myselection;

4. CTE VS VIEW

DWH
5. FACT VS DIMENSION VS DATA MART

6. STAR SCHEMA VS SNOWFLAKE SCHEMA
FACT -> DIM -> DIM

FACT -> DIM

7. AWS GLUE VS AWS EMR

8. DATALAKE PARTITION?

Partition by country
s3://raw/country=Mexico/*.json
s3://raw/country=Peru/*.json

Partition by date
s3://raw/timestamp="2026-01-30"/*.json

9. RDD VS DATAFRAME

transformation vs action
rdd.map().filter().flatMap().collect()

'''





# CODDING PART

# Create a function that receives a word and returns a dictionary with the count of each letter in the word.
# Examples:
# "apple" -> {'a': 1, 'p':2, 'l':1, 'e':1}
# "pineapple" -> {'p':3, 'i':1, 'n':1, 'e':2, 'a':1, 'l':1}

def word_count(word):
    #CODE HERE
    counts = {}
    for w in word:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts



print(word_count('apple'))
print(word_count('pineapple'))
print(word_count('banana'))
print(word_count('mississippi'))
