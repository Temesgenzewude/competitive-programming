# Write your MySQL query statement below

# SELECT Email FROM
# (SELECT Email, COUNT(Email) as c 
#  FROM Person 
#  GROUP BY Email) 
#  AS temp
 
#  WHERE c> 1
 
 SELECT Email 
 FROM Person
 GROUP BY Email
 HAVING COUNT(Email) > 1
 
 
 
