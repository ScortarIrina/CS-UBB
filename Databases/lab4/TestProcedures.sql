USE DanceStudio


-- Procedures to simplify the process for adding specific tests, 
-- tables, views and for creating the connections between them

GO
CREATE OR ALTER PROCEDURE addToTables (@tableName VARCHAR(50)) AS
BEGIN

	-- the table was already added
    IF @tableName IN (SELECT [Name] FROM [Tables]) BEGIN			
        PRINT 'Table already present in tables'
        RETURN
    END

	-- there is no such table in the database
    IF @tableName NOT IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES) BEGIN
        PRINT 'Table not present in the database'
        RETURN
    END

	-- add the table in the tables
    INSERT INTO Tables (Name)
    VALUES
        (@tableName)

END



GO 
CREATE OR ALTER PROCEDURE addToViews (@viewName VARCHAR(50)) AS
BEGIN

	-- the view was already added
    IF @viewName IN (SELECT Name from Views) BEGIN
        PRINT 'View already present in views'
        RETURN
    END

	-- there is no such view in the database
    IF @viewName NOT IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS) BEGIN
        PRINT 'View not present in database'
        RETURN
    END

	-- add view to the table
    INSERT INTO Views (Name)
    VALUES
        (@viewName)

END



GO
CREATE OR ALTER PROCEDURE addToTests (@testName VARCHAR(50)) AS
BEGIN

	-- the test was already added
    IF @testName IN (SELECT Name from Tests) BEGIN
        PRINT 'Test already present in Tests'
        RETURN
    END

	-- add the test to the table
    INSERT INTO Tests (Name)
    VALUES
        (@testName)

END



GO
CREATE OR ALTER PROCEDURE connectTableToTest (@tableName VARCHAR(50), @testName VARCHAR(50), @rows INT, @pos INT) AS
BEGIN

	-- there is no such table in Tables
	IF @tableName NOT IN (SELECT Name FROM Tables) BEGIN
        PRINT 'Table not present in Tables'
        RETURN
    END

	-- there is no such test in Tests 
	IF @testName NOT IN (SELECT Name FROM Tests) BEGIN
        PRINT 'Test not present in Test'
        RETURN
    END

	-- duplicate position
	IF EXISTS( 
		SELECT * 
		FROM TestTables T1 JOIN Tests T2 ON T1.TestID = T2.TestID
		WHERE T2.[Name] = @testName AND Position = @pos
	) BEGIN
        PRINT 'Position provided conflicts with previous positions'
        RETURN
    END

	-- insert data into TestTables
	INSERT INTO TestTables 
		(TestID, TableID, NoOfRows, Position) 
	VALUES (
		(SELECT Tests.TestID FROM Tests WHERE Name = @testName),
		(SELECT Tables.TableID FROM Tables WHERE Name = @tableName),
		@rows,
		@pos
	)

END



GO
CREATE OR ALTER PROCEDURE connectViewToTest (@viewName VARCHAR(50), @testName VARCHAR(50)) AS
BEGIN

	-- there is no such view in Views
	IF @viewName NOT IN (SELECT Name FROM Views) BEGIN
        PRINT 'View not present in Views'
        RETURN
    END

	-- there is no such test in Tests
	IF @testName NOT IN (Select Name FROM Tests) BEGIN
        PRINT 'Test not present in Tests'
        RETURN
    END

	-- insert data into TestViews
	INSERT INTO TestViews 
		(TestID, ViewID)
	VALUES(
		(SELECT Tests.TestID FROM Tests WHERE Name = @testName),
		(SELECT Views.ViewID FROM Views WHERE Name = @viewName)
	)

END



-- Delete data from a table
GO
CREATE OR ALTER PROCEDURE deleteDataFromTable (@tableID INT) AS
BEGIN

	-- there is no such table in tables
	IF @tableID NOT IN (SELECT [TableID] FROM [Tables]) BEGIN
		PRINT 'Table not present in Tables.'
		RETURN
	END

	DECLARE @tableName NVARCHAR(50) = (SELECT [Name] FROM [Tables] WHERE TableID = @tableID)
	PRINT 'Delete data from table ' + @tableName
	DECLARE @query NVARCHAR(100) = N'DELETE FROM ' + @tableName
	PRINT @query
	EXEC sp_executesql @query

END



-- Delete data from all the tables involved in a test
GO
CREATE OR ALTER PROCEDURE deleteDataFromAllTables (@testID INT) AS
BEGIN

	-- no such test in Tests table
	IF @testID NOT IN (SELECT [TestID] FROM [Tests]) BEGIN
		PRINT 'Test not present in Tests.'
		RETURN
	END

	PRINT 'Delete data from all tables for the test ' + CONVERT(VARCHAR, @testID)
	DECLARE @tableID INT
	DECLARE @pos INT
	
    -- cursor to iterate through the tables in the descending order of their position
	DECLARE allTableCursorDesc CURSOR LOCAL FOR
		SELECT T1.TableID, T1.Position 
		FROM TestTables T1 
		INNER JOIN Tests T2 ON T2.TestID = T1.TestID
		WHERE T2.TestID = @testID
		ORDER BY T1.Position DESC

	OPEN allTableCursorDesc
	FETCH allTableCursorDesc INTO @tableID, @pos
	WHILE @@FETCH_STATUS = 0 BEGIN
		EXEC deleteDataFromTable @tableID
		FETCH NEXT FROM allTableCursorDesc INTO @tableID, @pos
	END

	CLOSE allTableCursorDesc
	DEALLOCATE allTableCursorDesc

END



-- Insert data into a specific table
GO
CREATE OR ALTER PROCEDURE insertDataIntoTable (@testRunID INT, @testID INT, @tableID INT) AS
BEGIN

	IF @testID NOT IN (SELECT [TestID] FROM [Tests]) BEGIN
		PRINT 'Test not present in Tests.'
		RETURN
	END

	IF @testRunID NOT IN (SELECT [TestRunID] FROM [TestRuns]) BEGIN
		PRINT 'Test run not present in TestRuns.'
		RETURN
	END

	IF @tableID NOT IN (SELECT [TableID] FROM [Tables]) BEGIN
		PRINT 'Table not present in Tables.'
		RETURN
	END

	DECLARE @startTime DATETIME = SYSDATETIME()
	DECLARE @tableName VARCHAR(50) = (
		SELECT [Name] 
		FROM [Tables] 
		WHERE TableID = @tableID
	)
	PRINT 'Insert data into table ' + @tableName
	DECLARE @numberOfRows INT = (
		SELECT [NoOfRows] 
		FROM [TestTables]
		WHERE TestID = @testID AND TableID = @tableID
	)

	-- generate random data in the table
	EXEC generateRandomDataForTable @tableName, @numberOfRows
	DECLARE @endTime DATETIME = SYSDATETIME()
	INSERT INTO TestRunTables(TestRunID, TableID, StartAt, EndAt)
	VALUES (@testRunID, @tableID, @startTime, @endTime)

END



-- Insert data into all the tables involved in a test
GO
CREATE OR ALTER PROCEDURE insertDataIntoAllTables (@testRunID INT, @testID INT) AS
BEGIN

	
	IF @testID NOT IN (SELECT [TestID] FROM [Tests]) BEGIN
		PRINT 'Test not present in Tests.'
		RETURN
	END

	IF @testRunID NOT IN (SELECT [TestRunID] FROM [TestRuns]) BEGIN
		PRINT 'Test run not present in TestRuns.'
		RETURN
	END

	PRINT 'Insert data in all the tables for the test ' + CONVERT(VARCHAR, @testID)
	DECLARE @tableID INT
	DECLARE @pos INT

	--cursor to iterate through the tables in ascending order of their position
	DECLARE allTableCursorAsc CURSOR LOCAL FOR
		SELECT T1.TableID, T1.Position
		FROM TestTables T1
		INNER JOIN Tests T2 ON T2.TestID = T1.TestID
		WHERE T1.TestID = @testID
		ORDER BY T1.Position ASC

	OPEN allTableCursorAsc
	FETCH allTableCursorAsc INTO @tableID, @pos
	WHILE @@FETCH_STATUS = 0 BEGIN
		EXEC insertDataIntoTable @testRunID, @testID, @tableID
		FETCH NEXT FROM allTableCursorAsc INTO @tableID, @pos
	END

	CLOSE allTableCursorAsc
	DEALLOCATE allTableCursorAsc

END



-- Select data from a view
GO
CREATE OR ALTER PROCEDURE selectDataFromView (@viewID INT, @testRunID INT) AS
BEGIN

	IF @viewID NOT IN (SELECT [ViewID] FROM [Views]) BEGIN
		PRINT 'View not present in Views.'
		RETURN
	END

	IF @testRunID NOT IN (SELECT [TestRunID] FROM [TestRuns]) BEGIN
		PRINT 'Test run not present in TestRuns.'
		RETURN
	END

	DECLARE @startTime DATETIME = SYSDATETIME()
	DECLARE @viewName VARCHAR(100) = (
		SELECT [Name]
		FROM [Views]
		WHERE ViewID = @viewID
	)
	PRINT 'Selecting data from the view ' + @viewName
	DECLARE @query NVARCHAR(150) = N'SELECT * FROM ' + @viewName
	EXEC sp_executesql @query

	DECLARE @endTime DATETIME = SYSDATETIME()
	INSERT INTO TestRunViews(TestRunID, ViewID, StartAt, EndAt)
	VALUES (@testRunID, @viewID, @startTime, @endTime)

END



-- Select data from all the views
GO
CREATE OR ALTER PROCEDURE selectAllViews (@testRunID INT, @testID INT) AS
BEGIN

	IF @testID NOT IN (SELECT [TestID] FROM [Tests]) BEGIN
		PRINT 'Test not present in Tests.'
		RETURN
	END

	IF @testRunID NOT IN (SELECT [TestRunID] FROM [TestRuns]) BEGIN
		PRINT 'Test run not present in TestRuns.'
		RETURN
	END

	PRINT 'Selecting data from all the views from the test ' + CONVERT(VARCHAR, @testID)
	DECLARE @viewID INT

	--cursor to iterate through the views
	DECLARE selectAllViewsCursor CURSOR LOCAL FOR
		SELECT T1.ViewID FROM TestViews T1
		INNER JOIN Tests T2 ON T2.TestID = T1.TestID
		WHERE T1.TestID = @testID

	OPEN selectAllViewsCursor
	FETCH selectAllViewsCursor INTO @viewID
	WHILE @@FETCH_STATUS = 0 BEGIN
		EXEC selectDataFromView @viewID, @testRunID
		FETCH NEXT FROM selectAllViewsCursor INTO @viewID
	END

	CLOSE selectAllViewsCursor
	DEALLOCATE selectAllViewsCursor

END



-- Run a test
GO
CREATE OR ALTER PROCEDURE runTest (@testID INT, @description VARCHAR(MAX)) AS
BEGIN

	IF @testID NOT IN (SELECT TestID FROM Tests) BEGIN
		PRINT 'Test not present in Tests.'
		RETURN
	END

	EXEC deleteDataFromAllTables @testID
	PRINT 'Running test with the id ' + CONVERT(VARCHAR, @testID)
	
	INSERT INTO TestRuns([Description]) 
	VALUES (@description)
	DECLARE @testRunID INT = (
		SELECT MAX(TestRunID)
		FROM TestRuns
	)
	DECLARE @startTime DATETIME = SYSDATETIME()
	EXEC insertDataIntoAllTables @testRunID, @testID
	EXEC selectAllViews @testRunID, @testID
	DECLARE @endTime DATETIME = SYSDATETIME()

	UPDATE [TestRuns] SET StartAt = @startTime, EndAt = @endTime
	DECLARE @timeDifference INT = DATEDIFF(SECOND, @startTime, @endTime)
	PRINT 'The test with id ' + CONVERT(VARCHAR, @testID) + ' took ' + CONVERT(VARCHAR, @timeDifference) + ' seconds.'

END



-- Run all the tests
GO
CREATE OR ALTER PROCEDURE runAllTests AS
BEGIN

	DECLARE @testName VARCHAR(50)
	DECLARE @testID INT
	DECLARE @description VARCHAR(2000)

	--cursor to iterate through the tests
	DECLARE allTestsCursor CURSOR LOCAL FOR
		SELECT *
		FROM Tests

	OPEN allTestsCursor
	FETCH allTestsCursor INTO @testID, @testName
	WHILE @@FETCH_STATUS = 0 BEGIN
		PRINT 'Running ' + @testName
		SET @description = 'Test results for test with the ID ' + CAST(@testID AS VARCHAR(2))
		EXEC runTest @testID, @description
		FETCH NEXT FROM allTestsCursor INTO @testID, @testName
	END

	CLOSE allTestsCursor
	DEALLOCATE allTestsCursor

END



------------------------------------------ VIEWS ------------------------------------------

-- a view with a SELECT statement operating on one table
GO
CREATE OR ALTER VIEW dancersWithEvenID AS
	SELECT D.dancer_id, D.first_name, D.last_name
	FROM Dancer D
	WHERE D.dancer_id % 2 = 0


--  a view with a SELECT statement operating on at least 2 tables
GO
CREATE OR ALTER VIEW instructorsAndWorkshops AS
	SELECT I.first_name, I.last_name, W.instructor_id, W.workshop_id
	FROM Instructor I INNER JOIN Workshop W on W.instructor_id = I.[instructor_id]


-- a view with a SELECT statement that has a GROUP BY clause and operates on at least 2 tables
GO
CREATE OR ALTER VIEW groupCostumesByDancer AS
	SELECT D.dancer_id, D.first_name, COUNT(*) AS costumes
	FROM Dancer D 
	INNER JOIN Costume C ON D.dancer_id = C.dancer_id
	GROUP BY D.dancer_id, D.first_name

GO



------------------------------------ CREATE THE TESTS ------------------------------------

-- first test
-- a table with a single-column primary key and no foreign keys;
-- a table with a single-column primary key and at least one foreign key;
-- a table with a multi-column primary key
-- a view with a SELECT statement that has a GROUP BY clause and operates on at least 2 tables

EXEC addToTests 'Test1'

EXEC addToViews 'groupCostumesByDancer'
EXEC connectViewToTest 'groupCostumesByDancer', 'Test1'

EXEC addToTables 'Member'
EXEC connectTableToTest 'Member', 'Test1', 100, 1

EXEC addToTables 'Dancer'
EXEC connectTableToTest 'Dancer', 'Test1', 100, 2

EXEC addToTables 'Instructor'
EXEC connectTableToTest 'Instructor', 'Test1', 80, 3

EXEC addToTables 'Shoes'
EXEC connectTableToTest 'Shoes', 'Test1', 70, 4

EXEC addToTables 'Costume'
EXEC connectTableToTest 'Costume', 'Test1', 50, 5


-- second test
-- a table with a single-column primary key 
-- a view with a SELECT statement operating on one table

EXEC addToViews 'dancersWithEvenID'
EXEC addToTests 'Test2'
-- EXEC addToTables 'Dancer'
EXEC connectTableToTest 'Dancer', 'Test2', 100, 1
EXEC connectViewToTest 'dancersWithEvenID', 'Test2'


-- third test
-- a view with a SELECT statement operating on at least two tables
-- a table with no foreign key and a single-column primary key and a table with a foreign key

EXEC addToTests 'Test3'
-- EXEC addToTables 'Instructor'
EXEC connectTableToTest 'Instructor', 'Test3', 100, 1

EXEC addToTables 'Workshop'
EXEC connectTableToTest 'Workshop', 'Test3', 100, 2

EXEC addToViews 'instructorsAndWorkshops'
EXEC connectViewToTest 'instructorsAndWorkshops', 'Test3'


SELECT *
FROM [Views]

SELECT *
FROM [Tables]

SELECT *
FROM [Tests]

SELECT *
FROM [TestTables]

SELECT *
FROM [TestViews]

SELECT *
FROM [TestRuns]

SELECT *
FROM [TestRunTables]

SELECT *
FROM [TestRunViews]


SELECT *
FROM Dancer

SELECT *
FROM Instructor

SELECT *
FROM Shoes

SELECT *
FROM Costume

SELECT *
FROM Member

SELECT *
FROM Workshop

delete from [Views]
delete from [Tables]
delete from [Tests]
delete from [TestTables]
delete from [TestViews]
delete from [TestRuns]
delete from [TestRunTables]
delete from [TestRunViews]


-----------------
EXEC runAllTests
-----------------
