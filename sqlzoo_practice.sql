
--- *************   (https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial)    **********----------------------
--1.
--List each country name where the population is larger than that of 'Russia'.

--world(name, continent, area, population, gdp)

SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')


--2.
--Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

--Per Capita GDP  (gdp/population)

SELECT
	name
FROM 
	World
Where 
	gdp/population >(SELECT 
						gdp/population 
					FROM 
						world 
					WHERE 
						name ='United Kingdom') 
AND continent = 'Europe'


--3.

--List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
SELECT 
	name,
	continent
FROM 
	world
WHERE
    continent in (Select continent from world Where name ='Argentina') or
    continent = (Select continent from world Where name ='Australia')
Order BY
    name

SELECT 
  name,
  continent
FROM 
  world
WHERE
  continent in (
				(Select continent from world Where name ='Argentina'),
				(Select continent from world Where name ='Australia')
				)
Order BY
  name


--4.
--Which country has a population that is more than United Kingom but less than Germany? Show the name and the population.
SELECT name,population
 FROM world
WHERE 
   population BETWEEN (select population from world where name = 'United Kingdom')
AND
   (Select population from world Where name ='Germany')
and name NOT IN ('United Kingdom','Germany')


--5.Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.
--Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

select 
   name,  
   CONCAT(CAST(ROuND(100*population/(SELECT population from world where name = 'Germany'),0) as int),'%') AS 
      percentage
FROM 
  world 
WHERE 
  continent = 'Europe'


--  6.
--Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)
SELECT
	name
FROM
	world
WHERE
	GDP >= ALL(SELECT 
				continent
               FROM 
				world
               WHERE GDP>0
			   AND contient ='Europe')


--7.Find the largest country (by area) in each continent, show the continent, the name and the area:
SELECT 
	continent, 
	name, 
	area 
FROM 
	world x   
WHERE area >= 
ALL(SELECT 
		area 
	FROM 
		world y 
   	WHERE 
		y.continent = x.continent )


--8.
--List each continent and the name of the country that comes first alphabetically.
SELECT 
	continent, 
	name 
FROM 
	world x   
WHERE 
	name <= ALL(SELECT 
					name 
				FROM 
					world y
				WHERE y.continent = x.continent)


--  9.
-- Find the continents where all countries have a population <= 25000000. 
-- Then find the names of the countries associated with these continents. 
-- Show name, continent and population.


SELECT 
   name,
   continent,
   population 
FROM 
	world x  -- using x as an alias
WHERE
 25000000 >= ALL  (SELECT 
						population  
					FROM 
						world y --using y as an alias
WHERE y.continent = x.continent and population > 0 )


--10.
--Some countries have populations 
--more than three times that of all of their neighbours (in the same continent).
--Give the countries and continents.

--Still open

SELECT 
	name, 
	continent
FROM 
	world x  
WHERE 
	population > ALL(SELECT population*3
                     FROM world y  
                     WHERE y.continent =  x.continent 
                     AND y.name != x.name)
--SELECT  CustomerID,
--        ContactName,                                                                              --the string to extract from = ContactName
--        RIGHT(ContactName,len(ContactName)-CHARINDEX(' ', ContactName)) AS [ContactLastName]      --RIGHT(the string to extract from, len(TTL # of Chars) - the number of characters to extract)
--FROM Customers                                                                                    --the number of characters in the contact name = LEN(ContactName)
--                   