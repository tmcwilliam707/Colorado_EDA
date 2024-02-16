-- Create a temporary table
CREATE TEMPORARY TABLE tutorial.us_housing_units (
    year int,
    month varchar(255),
    west float,
    south float
);

-- Insert some fake data
INSERT INTO tutorial.us_housing_units (year, month, west, south)
VALUES (2000, 'January', 100.0, 200.0),
       (2001, 'February', 150.0, 250.0),
       (2002, 'March', 200.0, 300.0);

-- Run the original query
SELECT year,
       month,
       west,
       south,
       west + south - 4 * year AS nonsense_column
FROM tutorial.us_housing_units;