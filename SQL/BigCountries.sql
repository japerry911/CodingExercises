"""
---Big Countries---
A country is big if it has an area of bigger than 3 million square km or a 
population of more than 25 million.

Write a SQL solution to output big countries' name, population and area.
"""

SELECT World.name, World.population, World.area
FROM World
WHERE World.area > 3000000 OR World.population > 25000000;