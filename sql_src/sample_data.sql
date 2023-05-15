INSERT INTO Employee (Ssn, Name, Sex) VALUES (123, 'John', 'male');

INSERT INTO Location (Name, Street, District, City, Control_Employee) VALUES ('SY', 'ShengYang', 'Xinyi', 'TPE', 123);
INSERT INTO Location (Name, Street, District, City, Control_Employee) VALUES ('Taipei 101', 'Shifu', 'Xinyi', 'TPE', 123);

INSERT INTO Bike (Serial_num, Factory, Is_broken, Is_using, Maintenance_record, Maintenance_Employee, Park_loc) VALUES (456, 'Giant', 0, 0, 0, 123, 'SY');

INSERT INTO User (CardID, Name, Rent_bike_serial) VALUES (789, 'Alice', 456);

INSERT INTO Ensurance (CardID, Type, Amount) VALUES (789, 1, 100);

INSERT INTO Rent_History (Start_loc, Stop_loc, Bike_serial, User_cardID, History_serial, Cost, Time) VALUES ('SY', 'Taipei 101', 456, 789, 111, 50, 60);