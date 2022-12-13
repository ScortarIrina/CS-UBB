USE DanceStudio


----------------------------------
-- a) modify the type of a column 
----------------------------------
GO
CREATE OR ALTER PROCEDURE setPointsFromPrizeDecimal 
AS
    ALTER TABLE Prize ALTER COLUMN points DECIMAL(4,2)


GO
CREATE OR ALTER PROCEDURE setPointsFromPrizeInt
AS
	ALTER TABLE Prize ALTER COLUMN points INT


----------------------------
-- b) add / remove a column 
----------------------------
GO
CREATE OR ALTER PROCEDURE addInstructorNameToWorkshop 
AS
	ALTER TABLE Workshop ADD instructor_name VARCHAR(30)


GO
CREATE OR ALTER PROCEDURE removeInstructorNameFromWorkshop
AS
	ALTER TABLE Workshop DROP COLUMN instructor_name


--------------------------------------
-- c) add/remove a DEFAULT constraint
--------------------------------------
GO
CREATE OR ALTER PROCEDURE addDefaultToInstructorStyle
AS
	ALTER TABLE Instructor ADD CONSTRAINT default_style DEFAULT('both') FOR style

GO
CREATE OR ALTER PROCEDURE removeDefaultFromInstructorStyle
AS
	ALTER TABLE Instructor DROP CONSTRAINT default_style


---------------------------------
-- d) add / remove a primary key
---------------------------------
GO
CREATE OR ALTER PROCEDURE addSalaryAndNamePKEmployee
AS
	ALTER TABLE Employee
		DROP CONSTRAINT if exists EMPLOYEE_PRIMARY_KEY
	ALTER TABLE Employee
		ADD CONSTRAINT EMPLOYEE_PRIMARY_KEY PRIMARY KEY(first_name, salary)

GO
CREATE OR ALTER PROCEDURE removeSalaryAndNamePKEmployee
AS
	ALTER TABLE Employee
		DROP CONSTRAINT EMPLOYEE_PRIMARY_KEY
	ALTER TABLE Employee
		ADD CONSTRAINT EMPLOYEE_PRIMARY_KEY PRIMARY KEY(employee_id)


-----------------------------------
-- e) add / remove a candidate key
-----------------------------------
GO 
CREATE OR ALTER PROCEDURE newCandidateKeyDancer
AS
	ALTER TABLE Dancer
		ADD CONSTRAINT DANCER_CANDIDATE_KEY UNIQUE(first_name, last_name, age)

GO
CREATE OR ALTER PROCEDURE removeCandidateKeyDancer
AS
	ALTER TABLE Dancer
		DROP CONSTRAINT if exists DANCER_CANDIDATE_KEY
	


---------------------------------
-- f) add / remove a foreign key
---------------------------------
GO
CREATE OR ALTER PROCEDURE newForeignKeyEmployee
AS
	ALTER TABLE Employee
		add CONSTRAINT EMPLOYEE_FOREIGN_KEY FOREIGN KEY(instructor_id) REFERENCES Instructor(instructor_id)

GO
CREATE OR ALTER PROCEDURE removeForeignKeyEmployee
AS
	ALTER TABLE Employee
		DROP CONSTRAINT EMPLOYEE_FOREIGN_KEY


----------------------------
-- g) create / drop a table
----------------------------
GO
CREATE OR ALTER PROCEDURE addEmployee
AS
	CREATE TABLE Employee (
		employee_id INT not null,
		first_name VARCHAR(50) not null,
		last_name VARCHAR(50),
		salary INT not null,
		CONSTRAINT EMPLOYEE_PRIMARY_KEY PRIMARY KEY(employee_id),
		instructor_id INT NOT NULL
	)

GO
CREATE OR ALTER PROCEDURE dropEmployee
AS
	DROP TABLE if exists Employee


/*
	a table that contains the current version of the database schema
*/
CREATE TABLE versionTable (
	version INT
)

INSERT INTO versionTable 
VALUES
	(1) -- this is the initial version

-- a table that contains the initial version, the version after the execution of the procedure 
-- and the procedure that changes the table in this way
CREATE TABLE procedureTable (
	initial_version INT,
	final_version INT,
	procedure_name VARCHAR(MAX),
	PRIMARY KEY (initial_version, final_version)
)

INSERT INTO procedureTable
VALUES
	(1, 2, 'setPointsFromPrizeDecimal'),
	(2, 1, 'setPointsFromPrizeInt'),
	(2, 3, 'addInstructorNameToWorkshop'), 
	(3, 2, 'removeInstructorNameFromWorkshop'),
	(3, 4, 'addDefaultToInstructorStyle'),
	(4, 3, 'removeDefaultFromInstructorStyle'),
	(4, 5, 'addEmployee'),
	(5, 4, 'dropEmployee'),
	(5, 6, 'addSalaryAndNamePKEmployee'),
	(6, 5, 'removeSalaryAndNamePKEmployee'),
	(6, 7, 'newCandidateKeyDancer'),
	(7, 6, 'removeCandidateKeyDancer'),
	(7, 8, 'newForeignKeyEmployee'),
	(8, 7, 'removeForeignKeyEmployee')


-- procedure to bring the database to the specified version
GO
CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT) 
AS
    DECLARE @curr INT
    DECLARE @var VARCHAR(MAX)
    SELECT @curr = version
    FROM versionTable

    IF @newVersion > (SELECT MAX(final_version)
                      FROM procedureTable)
        raiserror ('BAD VERSION', 10, 1)

    IF @newVersion < (SELECT MIN(final_version)
                      FROM procedureTable)
        raiserror ('BAD VERSION', 10, 1)

    WHILE @curr > @newVersion
        BEGIN
            SELECT @var=procedure_name FROM procedureTable WHERE initial_version=@curr AND final_version=@curr - 1
            EXEC (@var)
            SET @curr = @curr - 1
        END

    WHILE @curr < @newVersion
        BEGIN
            SELECT @var=procedure_name FROM procedureTable WHERE initial_version=@curr AND final_version=@curr + 1
            EXEC (@var)
            SET @curr = @curr + 1
        END

    UPDATE versionTable SET version = @newVersion


EXEC goToVersion 1

SELECT *
FROM versionTable

SELECT *
FROM procedureTable
