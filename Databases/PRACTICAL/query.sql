use TrainSchedule

/*
    Create a database to manage train schedules. The database will store data about the routes of all the trains. 
    The entities of interest to the problem domain are: Trains, Train Types, Stations, and Routes. 
    Each train has a name and belongs to a type. A train type has a name and a description.  Each station has a name. 
    Station names are unique. Each route has a name, an associated train, and a list of stations with arrival and 
    departure times in each station. Route names are unique. The arrival and departure times are represented as hour:minute pairs, 
    e.g., train arrives at 5 pm and leaves at 5:10 pm.
*/

IF OBJECT_ID('RoutesStations', 'U') IS NOT NULL
    DROP TABLE RoutesStations

IF OBJECT_ID('Stations', 'U') IS NOT NULL
    DROP TABLE Stations

IF OBJECT_ID('Routes', 'U') IS NOT NULL
    DROP TABLE Routes

IF OBJECT_ID('Trains', 'U') IS NOT NULL
    DROP TABLE Trains

IF OBJECT_ID('TrainTypes', 'U') IS NOT NULL
    DROP TABLE TrainTypes


CREATE TABLE TrainTypes(
    train_type_id INT PRIMARY KEY IDENTITY(1, 1),
    train_type_name VARCHAR(100),
    type_description VARCHAR(200)
)

CREATE TABLE Trains(
    train_id INT PRIMARY KEY IDENTITY(1, 1),
    train_name VARCHAR(100),
    train_type_id INT REFERENCES TrainTypes(train_type_id)
)

CREATE TABLE Stations(
    station_id INT  PRIMARY KEY IDENTITY(1, 1),
    station_name VARCHAR(100) UNIQUE
)

CREATE TABLE Routes(
    route_id INT PRIMARY KEY IDENTITY(1, 1),
    route_name VARCHAR(100) UNIQUE,
    train_id INT REFERENCES Trains(train_id)
)

CREATE TABLE RoutesStations(
    route_id INT REFERENCES Routes(route_id),
    station_id INT REFERENCES Stations(station_id),
    arrival TIME,
    departure TIME,
    PRIMARY KEY(route_id, station_id)
)


-- Insert values into the tables

INSERT INTO TrainTypes
    (train_type_name, type_description)
VALUES
    ('type1', 'description type1'),
    ('type2', 'description type2')

INSERT INTO Trains
    (train_name, train_type_id)
VALUES
    ('train1', 1),
    ('train2', 2),
    ('train3', 1)

INSERT INTO Stations
    (station_name)
VALUES
    ('station1'),
    ('station2'),
    ('station3')

INSERT INTO Routes
    (route_name, train_id)
VALUES
    ('route1', 1),
    ('route2', 2),
    ('route3', 3)

INSERT INTO RoutesStations
    (route_id, station_id, arrival, departure)
VALUES
    (1, 1, '9:00am', '9:10am'),
    (1, 3, '10:00am', '10:10am'),
    (1, 2, '11:00am', '11:10am'),
    (2, 1, '5:00pm', '5:10pm'),
    (2, 3, '6:00pm', '6:10pm'),
    (3, 2, '10:00pm', '10:10pm')


SELECT *
FROM Stations

SELECT *
FROM TrainTypes

SELECT *
FROM Trains

SELECT *
FROM Routes

SELECT *
FROM RoutesStations


-- 1. Write an SQL script that creates the corresponding relational data model.

-- 2. Implement a stored procedure that receives a route, a station, arrival and departure times, and adds the station to the route. 
-- If the station is already on the route, the departure and arrival times are updated.
GO
CREATE PROC uspAddOrUpdateRoutesStations(@RouteName VARCHAR(100), @StationName VARCHAR(100), @arrival TIME, @departure TIME) AS
BEGIN
    DECLARE @idRoute INT = (SELECT route_id FROM Routes WHERE route_name = @RouteName)
    DECLARE @idStation INT = (SELECT station_id FROM Stations WHERE station_name = @StationName)

    -- check if the idRoute and idStation are not null
    IF @idRoute IS NOT NULL AND @idStation IS NOT NULL
        -- the station is already on the route, so the arrival and departure times are updated
        IF EXISTS (SELECT * FROM RoutesStations WHERE route_id = @idRoute AND station_id = @idStation)
            UPDATE RoutesStations
            SET arrival = @arrival, departure = @departure
            WHERE route_id = @idRoute AND station_id = @idStation
        -- the station is not on the route, so we add it
        ELSE
            INSERT INTO RoutesStations
                (route_id, station_id, arrival, departure)
            VALUES
                (@idRoute, @idStation, @arrival, @departure)
END
GO

EXEC uspAddOrUpdateRoutesStations @RouteName = 'route1', @StationName = 'station1', @arrival = '11:15am', @departure = "11:00am"
EXEC uspAddOrUpdateRoutesStations @RouteName = 'route2', @StationName = 'station2', @arrival = '11:00am', @departure = "11:15am"

-- DELETE FROM RoutesStations

SELECT *
FROM RoutesStations


-- 3. Create a view that shows the names of the routes that pass through all the stations.
GO
CREATE VIEW viewRouteNamesWithAllStations AS
    SELECT R.route_name
    FROM Routes R
    WHERE route_id IN (
        SELECT route_id 
        FROM RoutesStations
        GROUP BY route_id
        having COUNT(*) = (SELECT COUNT(*) FROM Stations)
        )
GO

SELECT *
FROM RoutesStations

SELECT *
FROM Stations

SELECT *
FROM viewRouteNamesWithAllStations


-- 4. Implement a function that lists the names of the stations with more than R routes, where R is a function parameter.
GO
CREATE FUNCTION ufListStationNamesWithRoutes (@numberRoutes INT)
RETURNS TABLE AS RETURN
    SELECT S.station_name
    FROM Stations S INNER JOIN RoutesStations RS ON RS.station_id = S.station_id
    GROUP BY S.station_id, S.station_name
    HAVING COUNT(*) > @numberRoutes
GO

SELECT *
FROM RoutesStations

SELECT *
FROM ufListStationNamesWithRoutes(2)
