USE DanceStudio;


-- *************************** INSERT ***************************

INSERT INTO Dancer
    (dancer_id, first_name, last_name, age, class, no_prizes)
VALUES
    (1, 'Irina', 'Scortar', 20, 'D', 15),
    (2, 'Carina', 'Ciubancan', 23, 'A', 21),
    (3, 'Andra', 'Dumitru', 23, 'S', 22),
    (4, 'Daria', 'Mesesan', 20, 'B', 19),
    (5, 'Mara', 'Dumitru', 15, 'E', 11),
    (6, 'Paul', 'Scortar', 16, 'D', 13),
    (7, 'Mihnea', 'Covaci', 23, 'S', 22),
    (8, 'Arthur', 'Engi', 21, 'A', 23),
    (9, 'Darius', 'Dobranis', 24, 'S', 26),
    (10, 'Alex', 'Pop', 17, 'E', 12),
    (11, 'Raluca', 'Suciu', 25, 'E', 11),
    (12, 'Rares', 'Capusan', 20, 'D', 15),
    (13, 'Evelin', 'Dulf', 21, 'C', 17),
    (14, 'Catalin', 'Gabor', 20, 'C', 18),
    (15, 'Andrei', 'Vaida', 22, 'B', 21),
    (16, 'Samira', 'Varga', 26, 'E', 10),
    (17, 'David', 'Maris', 19, 'H', 8),
    (18, 'Carla', 'Maris', 19, 'H', 8),
    (19, 'Maria', 'Andreescu', 17, 'D', 12),
    (20, 'Cosmin', 'Lupu', 22, 'C', 14),
    (21, 'Maria', 'Pirv', 18, 'D', 17),
    (22, 'Razvan', 'Terec', 20, 'C', 19),
    (23, 'Marius', 'Muica', 12, 'H', 5),
    (24, 'Emma', 'Serban', 19, 'C', 14);

DELETE from Dancer
WHERE dancer_id = 22 or dancer_id = 23 or dancer_id = 24

UPDATE Dancer set fans = 2
UPDATE Dancer set fans = 10 WHERE class = 'A' or class = 'S'
UPDATE Dancer set fans = 8 WHERE class = 'B' or class = 'C'
UPDATE Dancer set fans = 6 WHERE class = 'D' or class = 'E'

SELECT *
FROM Dancer D2
WHERE D2.class = 'H'

SELECT *
FROM Dancer D2
WHERE D2.fans = 2


INSERT INTO DancerPair
    (dancer1_id, dancer2_id, dance_pair_id, competition_level, age_group, style)
VALUES
    (6, 1, 1, 'D', '19-35', 'both'),
    (8, 2, 2, 'A', '19-35', 'ballroom'),
    (7, 3, 3, 'S', '19-35', 'both'),
    (10, 5, 4, 'E', '16-18', 'latin'),
    (12, 11, 5, 'D', '19-35', 'both'),
    (18, 17, 6, 'H', '19-35', 'ballroom'),
    (22, 24, 7, 'C', '19-35', 'latin');

UPDATE DancerPair
    set dancer1_id = 17, dancer2_id = 18
WHERE
    dance_pair_id = 6
     
INSERT INTO Instructor
    (instructor_id, first_name, last_name, competition_level, style, phone_no)
VALUES
    (1, 'Istvan', 'Both', 'D', 'both', 0712274529),
    (2, 'Krisztina', 'Both', 'D', 'both', 0794759670),
    (3, 'Alice', 'Rusznyak', 'A', 'ballroom', 0722189567),
    (4, 'Raul', 'Moldovan', 'S', 'latin', 0728905732),
    (5, 'Cristina', 'Tatar', 'S', 'latin', 0789980215);

INSERT INTO Instructor
VALUES
    (6, 'Andra', 'Dumitru', 'S', 'both', 0729889564),
    (7, 'Mihnea', 'Covaci', 'S', 'both', 0714264321),
    (8, 'Carina', 'Ciubancan', 'A', 'ballroom', 0725667384);

INSERT INTO DanceGroup
    (group_id, no_participants, level_group)
VALUES
    (1, 3, 'beginners'),            /* H class */
    (2, 9, 'intermmediate'),        /* E and D class */
    (3, 7, 'advanced'),             /* C and B class */
    (4, 4, 'performance')          /* A and S class */

INSERT INTO TrainingCamp
    (camp_id, group_id, duration_days, camp_theme)
VALUES
    (1, 1, 5, 'The basics of slow walz'),
    (2, 1, 4, 'Best approach to an efficient leading'),
    (3, 4, 7, 'Intensive competition endurance'),
    (4, 2, 5, 'Let us Jive!'),
    (5, 3, 4, 'Passo Doble'),
    (6, 3, 5, 'Tango'),
    (7, 4, 3, 'Viennese Walz'),
    (8, 1, 5, 'Cha-Cha-Cha');

INSERT INTO Prize
    (prize_id, prize_name, points)
VALUES
    (1, 'Floris', 2),
    (2, 'Attitude', 5),
    (3, 'Feeling Dance', 6),
    (4, 'Potaissa', 5),
    (5, 'Happy Feeet', 2),
    (6, 'National', 7),
    (7, 'International', 20),
    (8, 'Local', 4);

INSERT INTO Wins
    (dancer_id, prize_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 8),
    (2, 3),
    (2, 4),
    (2, 7),
    (15, 6),
    (20, 5);

DELETE from Wins

INSERT INTO Sponsor
    (sponsor_id, sponsor_name)
VALUES
    (1, 'Supadance'),
    (2, 'Royals'),
    (3, 'Borsec'),
    (4, 'BijouxBrigitte'),
    (5, 'Lidl');
INSERT INTO Sponsor
VALUES
    (6, 'Gesteredi'),
    (7, 'Paolo'),
    (8, 'Swarovski');

INSERT INTO Sponsors
    (dancer_id, sponsor_id, sum_of_money)
VALUES
    (2, 1, 550), 
    (3, 2, 600),
    (7, 5, 450),
    (8, 1, 500),
    (9, 3, 600),
    (15, 4, 200),
    (4, 5, 300),
    (20, 4, 100);

INSERT INTO Costume
    (costume_id, dancer_id, size)
VALUES
    (1, 1, 'S'),
    (2, 1, 'M'),
    (3, 2, 'XS'),
    (4, 2, 'XS'),
    (5, 3, 'M'),
    (6, 4, 'L'),
    (7, 5, 'S'),
    (8, 6, 'XS'),
    (9, 6, 'S'),
    (10, 7, 'M'),
    (11, 8, 'S'),
    (12, 9, 'M'),
    (13, 10, 'S'),
    (14, 10, 'XS'),
    (15, 11, 'XS'),
    (16, 12, 'XS'),
    (17, 13, 'L');

INSERT into Costume
VALUES
    (18, 1, 'S'),
    (19, 1, 'M');

INSERT INTO Shoes
    (shoes_id, dancer_id, size, brand)
VALUES
    (1, 1, '5', 'Supadance'),
    (2, 1, '4.5', 'Aida'),
    (3, 1, '5', 'RayRose'),
    (4, 23, '6.5', 'Paoul'),
    (5, 23, '6.5', 'RayRose');

INSERT INTO Teaches
    (instructor_id, group_id)
VALUES
    (2, 1),
    (1, 2),
    (4, 3),
    (3, 3),
    (5, 2),
    (1, 4),
    (3, 4);

-- Referential integrity constraint:
--      this will generate error because there is no group with id 6
/*
INSERT INTO Teaches
    (instructor_id, group_id)
VALUES
    (2, 6);
*/

INSERT into Competition
    (competition_id, city, date_competiton, organiser, no_participants)
VALUES
    (1, 'Cluj-Napoca', '2022-11-18', 'Attitude', 100),
    (2, 'Oradea', '2022-12-09', 'Feeling Dance', 150),
    (3, 'Turda', '2023-01-09', 'Potaissa', 100),
    (4, 'Cluj-Napoca', '2023-01-16', 'Crystal Top', 200),
    (5, 'Baia-Mare', '2023-02-02', 'Happy Feet', 170),
    (6, 'Bucuresti', '2023-02-26', 'National', 250),
    (7, 'Targu-Mures', '2023-03-15', 'DanceArt', 200),
    (8, 'Oradea', '2023-04-01', 'Apollo', 250),
    (9, 'Cluj-Napoca', '2023-05-12', 'Passo Doble', 200),
    (10, 'Oradea', '2023-05-13', 'Feeling Dance', 130);

UPDATE Competition
    SET ranking = 'national'
WHERE competition_id % 3 = 0


UPDATE Competition
    SET ranking = 'local'
WHERE no_participants <= 150

UPDATE Competition
    SET ranking = 'international'
WHERE city = 'Cluj-Napoca'

UPDATE Competition
    SET ranking = 'european'
WHERE ranking <> 'local' or ranking <> 'national' or ranking <> 'international'


INSERT INTO ParticipatesInCompetition
    (dancer1_id, dancer2_id, competition_id, dance_pair_id)
VALUES
    (6, 1, 1, 1),
    (6, 1, 3, 1),
    (6, 1, 8, 1),
    (8, 2, 1, 2),
    (8, 2, 5, 2),
    (7, 3, 1, 3),
    (7, 3, 2, 3),
    (7, 3, 3, 3),
    (7, 3, 7, 3),
    (10, 5, 4, 4),
    (10, 5, 5, 4),
    (12, 11, 6, 5),
    (12, 11, 7, 5),
    (12, 11, 8, 5),
    (17, 18, 5, 6),
    (22, 24, 1, 7),
    (22, 24, 4, 7),
    (22, 24, 9, 7);

INSERT INTO Workshop
    (workshop_id, instructor_id, topic)
VALUES
    (1, 3, 'Footwork'),
    (2, 5, 'Samba flexibility'),
    (3, 3, 'Effortless posture'),
    (4, 2, 'Facial expression'),
    (5, 3, 'Step speed in Jive');
INSERT INTO Workshop
VALUES
    (6, 3, 'Step speed Quickstep'),
    (7, 3, 'Posture in Quickstep');
INSERT INTO Workshop
VALUES
    (7, 2, 'Quickstep');

INSERT INTO Dancer
    (dancer_id, first_name, last_name, age, class, no_prizes)
VALUES
    (25, 'Ana', 'Pop', 22, NULL, 12),
    (26, 'Andrei', 'Pop', 22, NULL, 13);



-- *************************** UPDATE ***************************


UPDATE Dancer
    SET age = 21
WHERE age = 20;
/*
UPDATE Dancer
    SET age = 20
WHERE age = 21;
*/


-- update the number of participants to 10, where the group_id is 3
UPDATE DanceGroup
    SET no_participants = 10
WHERE group_id = 3;
/*
UPDATE DanceGroup
    SET no_participants = 7
WHERE group_id = 3;
*/


-- update the sum of money to 400 where the sponsor has id 1
UPDATE Sponsors
    SET sum_of_money = 400
WHERE sponsor_id = 1;
/*
UPDATE Sponsors
    SET sum_of_money = 100
WHERE sponsor_id = 1;
*/


-- Irina Scortar:       20 => 21
-- David Maris:         19 => 20
-- Carla Maris:         19 => 20
-------------------------
-- used IN, AND BETWEEN  |
-------------------------
UPDATE Dancer
    SET age = age + 1
WHERE last_name IN('Scortar', 'Dumitru', 'Maris') AND age BETWEEN 19 and 22;


-- Emma Serban:         NULL => D
-- Ana Pop:             NULL => D
-- Andrei Pop:          NULL => D
----------------
-- used IS NULL |
----------------
UPDATE Dancer
    SET class='D'
WHERE class IS NULL;



-- *************************** DELETE ***************************

DELETE FROM Workshop
WHERE workshop_id = 5;
/*
INSERT INTO Workshop
VALUES
    (5, 3, 'Step speed in Jive');
*/

DELETE FROM ParticipatesInCompetition
WHERE dance_pair_id = 1;

-- delete the dancers whose first names contain the word 'Delete'
-------------
-- used LIKE |
-------------
INSERT into Dancer
VALUES
    (30, 'ToDelete', 'THIS', 22, NULL, 12),
    (31, 'DeleteNow', 'THIS', 22, NULL, 13);

DELETE FROM Dancer
WHERE first_name LIKE '%Delete%';



-- ************************************ QUERIES ************************************


-- a. 2 queries with the union operation; use UNION [ALL] and OR;

    -- The dancer Irina Scortar (id = 1) makes the inventary only of her costumes and her shoes
    -- first 4 are her costumes, next 3 are her shoes
SELECT C.costume_id
FROM Costume C
WHERE C.dancer_id = 1
UNION ALL
SELECT S.shoes_id 
FROM Shoes S 
WHERE S.dancer_id = 1;

    -- The instructor Alice Rusznyak Alice prepares for her conferences and workshops
    -- the ones with prefix 'C:' are conference presentations, the other ones are workshops
SELECT C.presentation_name
FROM Conference C
WHERE C.instructor_id = 3
UNION
SELECT W.topic
FROM Workshop W
WHERE W.instructor_id = 3;

    -- Select all the instructors whose topic of workshop is related to quickstep 
    -- or whose conference presentation is related to walz, eliminating duplicates
    -- used DISTINCT
SELECT DISTINCT  I.first_name, I.last_name
FROM Instructor I, Workshop W, Conference C
WHERE (I.instructor_id = W.instructor_id AND W.topic like '%Quickstep%') OR 
        (I.instructor_id = C.instructor_id AND C.presentation_name like '%Walz%');


-- b. 2 queries with the intersection operation; use INTERSECT and IN;

    -- All entities who are both dancers and instructors
SELECT D.first_name, D.last_name
FROM Dancer D
INTERSECT
SELECT I.first_name, I.last_name
FROM Instructor I;

    -- All entities who are both dancers and instructors (alternative with IN)
SELECT D.first_name, D.last_name
FROM Dancer D 
WHERE D.first_name IN (SELECT I.first_name FROM Instructor I);


-- c) two queries with the difference operation; use EXCEPT and NOT IN

    -- Female Dancers ids who are in class H or E, but ar not in a DancePair
SELECT D.dancer_id
FROM Dancer D
WHERE D.class = 'H' OR D.class = 'E'
EXCEPT
SELECT DP.dancer2_id
from DancerPair DP;

    -- Female Dancers ids who are in class H or E, but ar not in a DancePair (alternative with NOT IN)
SELECT D.dancer_id
FROM Dancer D
WHERE (D.class = 'H' OR D.class = 'E') AND D.dancer_id NOT IN (
    select DP.dancer2_id
    from DancerPair DP
);




-- d) 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL JOIN (one query per operator); 
--    one query will join at least 3 tables, while another one will join at least two m:n relationships

    -- INNER JOIN
    -- Get for each instructor the workshop topics they have
SELECT W.instructor_id, I.first_name, W.topic
FROM Instructor I INNER JOIN Workshop W on W.instructor_id = I.[instructor_id]
ORDER BY I.first_name

    -- LEFT JOIN        (tables are: Instructor, Workshop, Conference)
    -- Print all the instructor ids and their workshops and conferences, 
    -- including the ones that have no workshops or conferences
    -- first column = first_name, second column = id if in Workshop, third column = id if in Conference
SELECT I.first_name, W.workshop_id, C.conference_id, C.instructor_id
from Instructor I
LEFT JOIN Workshop W ON I.instructor_id = W.instructor_id
LEFT JOIN Conference C ON I.instructor_id = C.instructor_id

    -- RIGHT JOIN
    -- Print all costumes with their corresponding owner
    -- include instructors that do not teach any group
SELECT Dancer.dancer_id, Dancer.first_name, Costume.costume_id
From Costume
RIGHT JOIN Dancer on Dancer.dancer_id = Costume.dancer_id

/*
    SELECT DG.group_id
    FROM DanceGroup DG
    RIGHT JOIN Teaches T ON T.group_id = DG.group_id
    RIGHT JOIN Instructor I ON I.instructor_id = T.instructor_id
*/

    -- FULL JOIN
    -- Print all sponsors who sponsor at least one dancer
    -- include dancers with no sponsor, sponsors with no one to sponsor, dancers with and without prizes
    -- join at least two many-to-many relationships
SELECT S.sponsor_name, D.first_name, P.prize_name
FROM Sponsor S
FULL JOIN Sponsors Ss ON Ss.sponsor_id = S.sponsor_id
FULL JOIN Dancer D ON SS.dancer_id = D.dancer_id
FULL JOIN Wins W ON D.dancer_id = W.dancer_id
FULL JOIN Prize P ON P.prize_id = W.prize_id




-- e) 2 queries with the IN operator and a subquery in the WHERE clause; 
--    in at least one case, the subquery should include a subquery in its own WHERE clause

    -- Print the name of male dancers who are in a dancePair that take part in a competition
SELECT D.first_name, D.last_name
FROM Dancer D
WHERE D.dancer_id IN (

    SELECT DP.dancer1_id
    FROM DancerPair DP
    INNER JOIN ParticipatesInCompetition PARTICIPATES ON DP.dance_pair_id = PARTICIPATES.dance_pair_id
    INNER JOIN Dancer DNCR ON PARTICIPATES.dancer1_id = DP.dancer1_id
    WHERE PARTICIPATES.dance_pair_id IN (

        SELECT DP2.dance_pair_id
        FROM DancerPair DP2
        INNER JOIN ParticipatesInCompetition PC2 ON PC2.dance_pair_id = DP2.dance_pair_id
        INNER JOIN Competition C ON C.competition_id = PC2.competition_id
    )
)

    -- Print the name of female dancers who are in a dancePair that take part in a competition
SELECT D.first_name, D.last_name
FROM Dancer D
WHERE D.dancer_id IN (

    SELECT DP.dancer2_id
    FROM DancerPair DP
    INNER JOIN ParticipatesInCompetition PARTICIPATES ON DP.dance_pair_id = PARTICIPATES.dance_pair_id
    INNER JOIN Dancer DNCR ON PARTICIPATES.dancer2_id = DP.dancer2_id
    WHERE PARTICIPATES.dance_pair_id IN (

        SELECT DP2.dance_pair_id
        FROM DancerPair DP2
        INNER JOIN ParticipatesInCompetition PC2 ON PC2.dance_pair_id = DP2.dance_pair_id
        INNER JOIN Competition C ON C.competition_id = PC2.competition_id
    )
)




-- f) 2 queries with the EXISTS operator and a subquery in the WHERE clause

    -- Print dancers that have costumes
    -- increment by 2 the number of fans because they like the costumes
SELECT D.first_name, D.last_name, D.fans + 2 AS NewFans
FROM Dancer D
WHERE EXISTS (
    SELECT *
    FROM Dancer D2
    INNER JOIN Costume C ON D2.dancer_id = C.dancer_id
    WHERE D2.dancer_id = D.dancer_id
)

    -- Print dancers that have shoes
    -- increment by 1 the number of fans because they like the shoes
                -- before incrementation: 6
                -- after incrementation: 7
SELECT D.first_name, D.last_name, D.fans + 1 AS NewFans
FROM Dancer D
WHERE EXISTS (
    SELECT *
    FROM Dancer D2
    INNER JOIN Shoes S ON D2.dancer_id = S.dancer_id
    WHERE D2.dancer_id = D.dancer_id
)




-- g) 2 queries with a subquery in the FROM clause

    -- Print the male dancers who are at least 17 years old and are in a dance pair
                -- Alex, David, Arthur, Rares, Razvan, Mihnea
SELECT d.first_name, d.last_name, d.age
FROM (
    SELECT *
    FROM Dancer D
    WHERE NOT D.age < 17
)d WHERE d.dancer_id IN (
    SELECT DP.dancer1_id
    from DancerPair DP
)
ORDER by age ASC

    -- Print the female dancers who are at most 21 years old and are in a dance pair
                -- Irina, Carla, Emma, Mara
SELECT d.first_name, d.last_name, d.age
FROM (
    SELECT *
    FROM Dancer D
    WHERE NOT D.age > 21
)d WHERE d.dancer_id IN (
    SELECT DP.dancer2_id
    from DancerPair DP
)
ORDER by age desc




-- h) 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 
--   2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX

    -- GROUP BY:
    -- show the number of costumes for each dancer
SELECT C.dancer_id, COUNT(*) AS count
from Costume C
GROUP BY C.dancer_id

    -- GROUP BY and HAVING:
    -- list all classes of dancers which have at least 4 dancers
                -- E, D, C
SELECT  D.class, COUNT(D.class) number_of_dancers_with_class
From Dancer D
GROUP BY D.class
HAVING COUNT(D.class) > 3
ORDER BY D.class DESC

    -- GROUP BY and HAVING with subquery:
    -- Print the dancers with the most prizes
                -- Irina and Carina (both 3)
SELECT D.dancer_id, D.first_name, COUNT(*) AS prizes
from Dancer D INNER JOIN Wins W ON D.dancer_id = W.dancer_id 
INNER JOIN Prize P ON P.prize_id = W.prize_id
GROUP BY D.dancer_id, D.first_name
HAVING COUNT(*) = (
    select MAX(T.C)
    from (
        select COUNT(*) C
        from Dancer D2 
        INNER JOIN Wins W2 ON D2.dancer_id = W2.dancer_id 
        INNER JOIN Prize P2 ON P2.prize_id = W2.prize_id
        GROUP BY D2.dancer_id, D2.first_name
    )T
)

    -- GROUP BY and HAVING with subquery:
    -- select the sum of money of all sponsors grouped by the dancer they sponsor,
    -- where the dancer_id is valid (there exists a dancer with that ID) 
SELECT Ss.sponsor_id, Ss.dancer_id, (Ss.sum_of_money) AS investment
FROM Sponsors Ss
GROUP BY Ss.dancer_id, Ss.sponsor_id, Ss.sum_of_money
HAVING Ss.dancer_id in (
    select dancer_id FROM Dancer
)
ORDER BY Ss.sponsor_id asc





-- i. 4 queries using ANY and ALL to introduce a subquery in the WHERE clause (2 queries per operator); 
--    rewrite 2 of them with aggregation operators, and the other 2 with IN / [NOT] IN.

    -- find the top 3 competitions which have more participants than the competition from Oradea 
    -- with the least participants (ANY)
SELECT top 3 C.*
from Competition C
WHERE C.no_participants > ANY (
    select C2.no_participants
    from Competition C2
    WHERE C2.city = 'Oradea'
)
ORDER BY C.no_participants desc

    -- rewritten with an aggregation operator (MIN instead of ANY)
SELECT top 3 C.*
from Competition C
WHERE C.no_participants > (
    select MIN(C2.no_participants)
    from Competition C2
    WHERE C2.city = 'Oradea'
)
ORDER BY C.no_participants desc

    -- find all the participants for the competitions in 2023 (ANY)
SELECT PC.dance_pair_id, PC.dancer1_id, PC.dancer2_id, PC.competition_id
from ParticipatesInCompetition PC
where PC.competition_id = ANY (
    select C.competition_id
    from Competition C
    WHERE C.date_competiton >= '2023-01-01'
)
ORDER BY competition_id

    -- rewritten with IN
SELECT PC.dance_pair_id, PC.dancer1_id, PC.dancer2_id, PC.competition_id
from ParticipatesInCompetition PC
where PC.competition_id IN (
    select C.competition_id
    from Competition C
    WHERE C.date_competiton >= '2023-01-01'
)
ORDER BY competition_id

    -- find the top 50% of dancers for which the number of prizes is more 
    -- than the number of prizes of the dancers with an id greater than 20 (ALL)
                -- Andra has 22 prizes, Darius and Arthur have more than her
                -- only they are shown because the dancer with max nr. of prizes with id>20 is Razvan Terec (19 prizes)
                -- the number of dancers with this property is 6, so 3 is 50% of them
SELECT TOP 50 PERCENT D.*
FROM Dancer D
WHERE D.no_prizes > ALL (
    select D2.no_prizes
    from Dancer D2
    WHERE D2.dancer_id > 20
)
ORDER BY D.no_prizes DESC

    -- rewritten with an aggregation operator (MAX instead of ALL)
SELECT TOP 50 PERCENT D.*
FROM Dancer D
WHERE D.no_prizes > (
    select MAX(D2.no_prizes)
    from Dancer D2
    WHERE D2.dancer_id > 20
)
ORDER BY D.no_prizes DESC

    -- find all dancers who are not instructors and have class greater than D (ALL) 
                -- (should not show Andra, Mihnea, Carina)
SELECT D.*
from Dancer D
WHERE D.class LIKE '%C%' or D.class LIKE '%B%' or D.class LIKE '%S%'
                    AND D.first_name <> ALL (
    select I.first_name
    FROM Instructor I
)
ORDER BY D.first_name

    -- rewritten using NOT IN
                -- (should not show Andra, Mihnea, Carina)
SELECT D.*
from Dancer D
WHERE D.class LIKE '%C%' or D.class LIKE '%B%' or D.class LIKE '%S%'
                    AND D.first_name not in (
    select I.first_name
    FROM Instructor I
)
ORDER BY D.first_name
