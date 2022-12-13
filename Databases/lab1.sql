USE DanceStudio;

DROP TABLE Dancer;
DROP TABLE Instructor;
DROP TABLE DanceGroup;
DROP TABLE Prize;
DROP TABLE Costume;
DROP TABLE DancerPair;
DROP TABLE TrainingCamp;
DROP TABLE ParticipatesInCompetition;
DROP TABLE Teaches;
DROP TABLE Competition;
DROP TABLE Workshop;
DROP TABLE Wins;
DROP TABLE Sponsors;
DROP TABLE Sponsor;


CREATE TABLE Dancer(
    dancer_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(10) DEFAULT 'TBA',
    last_name VARCHAR(10) DEFAULT 'TBA',
    age TINYINT CHECK (age >= 3),
    class VARCHAR(5),
    no_prizes INT DEFAULT 0
);
ALTER TABLE Dancer
ALTER COLUMN class VARCHAR(50)

CREATE TABLE Instructor(
    instructor_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    competition_level VARCHAR(3) DEFAULT 'D',
    style VARCHAR(8),
    phone_no INT
);
ALTER TABLE Instructor
ALTER COLUMN competition_level VARCHAR(50)
ALTER TABLE Instructor
ALTER COLUMN style VARCHAR(50)

CREATE TABLE DanceGroup(
    group_id INT PRIMARY KEY NOT NULL,
    no_participants INT,
    level_group VARCHAR(10)
);
ALTER TABLE DanceGroup
drop column camp_id 

ALTER TABLE DanceGroup
ALTER COLUMN level_group varchar(15);

CREATE TABLE Prize(
    prize_id INT PRIMARY KEY NOT NULL,
    prize_name VARCHAR(20),
    points INT
);

CREATE TABLE Sponsor(
    sponsor_id INT PRIMARY KEY NOT NULL,
    sponsor_name VARCHAR(20)
);

/*
    1(sponsor):n(dancers)
    More dancers can have the same sponsor.
*/
CREATE TABLE Sponsors(
    dancer_id INT FOREIGN KEY REFERENCES Dancer(dancer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    sponsor_id INT FOREIGN KEY REFERENCES Sponsor(sponsor_id) ON DELETE CASCADE ON UPDATE CASCADE,
    sum_of_money INT,
    PRIMARY KEY(dancer_id, sponsor_id)
);

/*
    1(dancer):n(costumes)
    A dancer can have multiple costumes but a costume can be worn by only one dancer.
*/
CREATE TABLE Costume(
    costume_id INT,
    dancer_id INT,
    size CHAR(1),
    PRIMARY KEY(costume_id, dancer_id)
);

ALTER TABLE Costume
ALTER COLUMN size char(3);


/*
    1(dancer):n(costumes)
    A dancer can have multiple pairs of shoes but a pair of shoes can be worn by only one dancer.
*/
CREATE TABLE Shoes(
    shoes_id INT,
    dancer_id INT,
    size CHAR(3),
    brand CHAR(20),
    PRIMARY KEY(shoes_id, dancer_id)
);


/*
    1(group):n(camps)
    One group can go to more camps.
*/
CREATE TABLE TrainingCamp(
    camp_id INT,
    group_id INT FOREIGN KEY REFERENCES DanceGroup(group_id) ON DELETE CASCADE ON UPDATE CASCADE,
    duration_days TINYINT,
    camp_theme varchar(50),
    PRIMARY KEY(camp_id, group_id)
);


/*
    1(dancer):n(prizes)
    A dancer can win more prizes but a prize can be won by only one dancer.
*/
CREATE TABLE Wins(
    dancer_id INT FOREIGN KEY REFERENCES Dancer(dancer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    prize_id INT FOREIGN KEY REFERENCES Prize(prize_id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY(dancer_id, prize_id)
);

/*
    m(dancer1):n(dancer2)
    Any dancer can have more partners.
*/
CREATE TABLE DancerPair(
    dancer1_id INT DEFAULT 0,
    dancer2_id INT DEFAULT 0,
    dance_pair_id INT DEFAULT 0,
    competition_level VARCHAR(3),
    age_group TINYINT,
    style VARCHAR(20),
    PRIMARY KEY(dance_pair_id, dancer1_id, dancer2_id)
);
alter table DancerPair
alter COLUMN age_group varchar(6);

/*
    m(instructors):n(dancers)
    An instructor can teache multiple dancers and a dancer can be taught by multiple instructors.
*/
CREATE TABLE Teaches(
    instructor_id INT FOREIGN KEY REFERENCES Instructor(instructor_id) ON DELETE CASCADE on UPDATE CASCADE,
    group_id INT FOREIGN KEY REFERENCES DanceGroup(group_id) ON DELETE CASCADE on UPDATE CASCADE,
    PRIMARY KEY(instructor_id, group_id)
);

/*
    m(competition):n(dancers)
    A competition can have more dancers and a dancer can take part in more competitions.
*/
CREATE TABLE Competition(
    competition_id INT DEFAULT 0,
    city VARCHAR(20),
    date_competiton DATE,
    organiser VARCHAR(20),
    no_participants TINYINT DEFAULT 50,
    ranking varchar(20),
    PRIMARY KEY(competition_id)
);
alter table Competition
drop column no_participants;

/*
    m(dance pairs):n(competitions)
*/
CREATE TABLE ParticipatesInCompetition(
    dancer1_id INT DEFAULT 0,
    dancer2_id INT DEFAULT 0,
    competition_id INT FOREIGN KEY REFERENCES Competition(competition_id) ON DELETE CASCADE on UPDATE CASCADE,
    dance_pair_id INT,
    CONSTRAINT FK_DancerPair FOREIGN KEY(dance_pair_id, dancer1_id, dancer2_id) REFERENCES DancerPair(dance_pair_id, dancer1_id, dancer2_id),
    PRIMARY KEY(dance_pair_id, competition_id)
);


/*
    m(workshops):n(dancers)
    A workshop can have more dancers and a dancer can participate in more workshops.
*/
CREATE TABLE Workshop(
    workshop_id INT DEFAULT 0,
    instructor_id INT FOREIGN KEY REFERENCES Instructor(instructor_id) ON DELETE CASCADE ON UPDATE CASCADE,
    topic VARCHAR(20),
    PRIMARY KEY(workshop_id, instructor_id)
);

/*
    m(conferences):n(dancers)
    A conference can have more instructors and an instructor can take part in more conferences.
*/
CREATE TABLE Conference(
    conference_id INT DEFAULT 0,
    instructor_id INT FOREIGN key REFERENCES Instructor(instructor_id) ON DELETE CASCADE ON UPDATE CASCADE,
    presentation_name VARCHAR(30),
    PRIMARY KEY(conference_id, instructor_id)
);

/*
    1(instructor):n(members)
*/
CREATE TABLE Member(
    member_id INT PRIMARY KEY NOT NULL,
    instructor_id INT,
    member_name VARCHAR(50)
)
