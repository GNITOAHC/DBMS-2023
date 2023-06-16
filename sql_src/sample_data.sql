-- Employee
-- INSERT INTO Employee (Ssn, Name, Sex) VALUES (123, 'John', 'male');
INSERT INTO Employee
VALUES (1, 'John', 'male');
INSERT INTO Employee
VALUES (2, 'Emily', 'female');
INSERT INTO Employee
VALUES (3, 'Sarah', 'female');
INSERT INTO Employee
VALUES (4, 'Michael', 'male');
INSERT INTO Employee
VALUES (5, 'Jessica', 'female');
INSERT INTO Employee
VALUES (6, 'David', 'male');
INSERT INTO Employee
VALUES (7, 'Jennifer', 'female');
INSERT INTO Employee
VALUES (8, 'Daniel', 'male');
INSERT INTO Employee
VALUES (9, 'Michelle', 'female');
INSERT INTO Employee
VALUES (10, 'Andrew', 'male');
-- Location
INSERT INTO `Location`
VALUES ('SY', 'ShengYang', 'Xinyi', 'TPE', 1);
INSERT INTO `Location`
VALUES ('Taipei 101', 'Shifu', 'Xinyi', 'TPE', 2);
INSERT INTO `Location`
VALUES ('NTU', 'Roosevelt', 'Daan', 'TPE', 3);
INSERT INTO `Location`
VALUES ('Gongguan', 'Xinhai', 'Daan', 'TPE', 4);
INSERT INTO `Location`
VALUES ('Ximending', 'Wuchang', 'Wanhua', 'TPE', 5);
INSERT INTO `Location`
VALUES (
        'Longshan Temple',
        'Guangzhou',
        'Wanhua',
        'TPE',
        6
    );
INSERT INTO `Location`
VALUES (
        'Shilin Night Market',
        'Danjin',
        'Shilin',
        'TPE',
        7
    );
INSERT INTO `Location`
VALUES (
        'Beitou Hot Springs',
        'Guizhou',
        'Beitou',
        'TPE',
        8
    );
INSERT INTO `Location`
VALUES (
        'Keelung Night Market',
        'Ren 2nd',
        'Renai',
        'KEE',
        9
    );
INSERT INTO `Location`
VALUES ('Yehliu Geopark', 'Gangdong', 'Wanli', 'KEE', 10);
-- Bike
-- INSERT INTO Bike (Serial_num, Factory, Is_broken, Is_using, Maintenance_record, Maintenance_Employee, Park_loc) VALUES (789, 'Giant', 0, 0, 0, 1, 'SY');
INSERT INTO Bike
VALUES (789, 'Giant', 0, 0, 0, 1, 'SY');
INSERT INTO Bike
VALUES (456, 'Trek', 0, 1, 0, 1, 'SY');
INSERT INTO Bike
VALUES (123, 'Merida', 0, 0, 0, 1, 'SY');
INSERT INTO Bike
VALUES (125, 'Scott', 0, 0, 0, 2, 'Taipei 101');
INSERT INTO Bike
VALUES (214, 'Giant', 0, 1, 0, 2, 'Taipei 101');
INSERT INTO Bike
VALUES (346, 'Trek', 1, 0, 0, 2, 'Taipei 101');
INSERT INTO Bike
VALUES (753, 'Specialized', 0, 1, 0, 3, 'NTU');
INSERT INTO Bike
VALUES (151, 'Cannondale', 0, 0, 0, 3, 'NTU');
INSERT INTO Bike
VALUES (457, 'Scott', 0, 0, 0, 3, 'NTU');
INSERT INTO Bike
VALUES (478, 'Fuji', 0, 0, 0, 4, 'Gongguan');
INSERT INTO Bike
VALUES (958, 'Bianchi', 0, 1, 0, 4, 'Gongguan');
INSERT INTO Bike
VALUES (182, 'Raleigh', 0, 0, 0, 4, 'Gongguan');
INSERT INTO Bike
VALUES (503, 'Diamondback', 0, 1, 0, 5, 'Ximending');
INSERT INTO Bike
VALUES (215, 'Specialized', 0, 0, 0, 5, 'Ximending');
INSERT INTO Bike
VALUES (405, 'Cannondale', 0, 0, 0, 5, 'Ximending');
INSERT INTO Bike
VALUES (281, 'Scott', 0, 1, 0, 6, 'Longshan Temple');
INSERT INTO Bike
VALUES (529, 'Giant', 1, 0, 0, 6, 'Longshan Temple');
INSERT INTO Bike
VALUES (129, 'Trek', 0, 0, 0, 6, 'Longshan Temple');
INSERT INTO Bike
VALUES (947, 'Fuji', 0, 1, 0, 7, 'Shilin Night Market');
INSERT INTO Bike
VALUES (
        392,
        'Bianchi',
        0,
        0,
        0,
        7,
        'Shilin Night Market'
    );
INSERT INTO Bike
VALUES (
        403,
        'Raleigh',
        0,
        0,
        0,
        7,
        'Shilin Night Market'
    );
INSERT INTO Bike
VALUES (
        204,
        'Diamondback',
        0,
        1,
        0,
        8,
        'Beitou Hot Springs'
    );
INSERT INTO Bike
VALUES (
        959,
        'Specialized',
        0,
        0,
        0,
        8,
        'Beitou Hot Springs'
    );
INSERT INTO Bike
VALUES (
        48,
        'Cannondale',
        0,
        0,
        0,
        8,
        'Beitou Hot Springs'
    );
INSERT INTO Bike
VALUES (11, 'Scott', 0, 1, 0, 9, 'Keelung Night Market');
INSERT INTO Bike
VALUES (7, 'Giant', 0, 0, 0, 9, 'Keelung Night Market');
INSERT INTO Bike
VALUES (67, 'Trek', 0, 0, 0, 9, 'Keelung Night Market');
INSERT INTO Bike
VALUES (938, 'Fuji', 0, 1, 0, 10, 'Yehliu Geopark');
INSERT INTO Bike
VALUES (208, 'Bianchi', 1, 0, 0, 10, 'Yehliu Geopark');
INSERT INTO Bike
VALUES (408, 'Raleigh', 1, 0, 0, 10, 'Yehliu Geopark');
-- User
-- INSERT INTO User (CardID, Name, Rent_bike_serial) VALUES (1000, 'Alice', 456);
INSERT INTO User
VALUES (1000, 'Alice', 456);
INSERT INTO User
VALUES (1001, 'Bob', 214);
INSERT INTO User
VALUES (1002, 'Charlie', 753);
INSERT INTO User
VALUES (1003, 'David', 958);
INSERT INTO User
VALUES (1004, 'Eve', 503);
INSERT INTO User
VALUES (1005, 'Frank', 281);
INSERT INTO User
VALUES (1006, 'Grace', 947);
INSERT INTO User
VALUES (1007, 'Henry', 204);
INSERT INTO User
VALUES (1008, 'Ivy', 11);
INSERT INTO User
VALUES (1009, 'Jack', 938);
-- Ensurance
-- INSERT INTO Ensurance (CardID, Type, Amount) VALUES (1000, 1, 78000);
INSERT INTO Ensurance
VALUES (1000, 1, 78000);
INSERT INTO Ensurance
VALUES (1001, 1, 325000);
INSERT INTO Ensurance
VALUES (1002, 1, 520000);
INSERT INTO Ensurance
VALUES (1003, 1, 147000);
INSERT INTO Ensurance
VALUES (1004, 1, 624000);
INSERT INTO Ensurance
VALUES (1005, 1, 255000);
INSERT INTO Ensurance
VALUES (1006, 1, 862000);
INSERT INTO Ensurance
VALUES (1007, 1, 42000);
INSERT INTO Ensurance
VALUES (1008, 1, 96000);
INSERT INTO Ensurance
VALUES (1009, 1, 710000);
-- Rent_History
-- INSERT INTO Rent_History (Start_loc, Stop_loc, Bike_serial, User_cardID, History_serial, Cost, Time) VALUES ('SY', 'Taipei 101', 125, 1000, 1, 50, 60);
INSERT INTO Rent_History
VALUES ('SY', 'Taipei 101', 125, 1000, 1, 50, 60);
INSERT INTO Rent_History
VALUES ('Taipei 101', 'SY', 789, 1001, 2, 40, 45);
INSERT INTO Rent_History
VALUES ('NTU', 'Taipei 101', 214, 1002, 3, 55, 75);
INSERT INTO Rent_History
VALUES ('Gongguan', 'NTU', 151, 1003, 4, 30, 25);
INSERT INTO Rent_History
VALUES ('Ximending', 'Gongguan', 478, 1004, 5, 25, 20);
INSERT INTO Rent_History
VALUES (
        'Longshan Temple',
        'Ximending',
        503,
        1005,
        6,
        35,
        30
    );
INSERT INTO Rent_History
VALUES (
        'Shilin Night Market',
        'Longshan Temple',
        281,
        1006,
        7,
        60,
        55
    );
INSERT INTO Rent_History
VALUES (
        'Beitou Hot Springs',
        'Shilin Night Market',
        947,
        1007,
        8,
        45,
        50
    );
INSERT INTO Rent_History
VALUES (
        'Keelung Night Market',
        'Beitou Hot Springs',
        204,
        1008,
        9,
        40,
        35
    );
INSERT INTO Rent_History
VALUES (
        'Yehliu Geopark',
        'Keelung Night Market',
        11,
        1009,
        10,
        65,
        70
    );