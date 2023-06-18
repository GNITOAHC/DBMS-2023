drop database if exists Youbike;
create database Youbike;
use Youbike;
CREATE TABLE `User` (
    `CardID` int NOT NULL,
    `Name` varchar(20) NOT NULL,
    `Rent_bike_serial` int,
    PRIMARY KEY (`CardID`)
);
CREATE TABLE `Bike` (
    `Serial_num` int NOT NULL,
    `Factory` varchar(60) NOT NULL,
    `Is_broken` bool NOT NULL,
    `Is_using` bool NOT NULL,
    `Maintenance_record` int NOT NULL,
    `Maintenance_Employee` int NOT NULL,
    `Park_loc` varchar(20) NOT NULL,
    PRIMARY KEY (`Serial_num`)
);
CREATE TABLE `Location` (
    `Name` varchar(20) NOT NULL,
    `Street` varchar(30) NOT NULL,
    `District` varchar(30) NOT NULL,
    `City` varchar(30) NOT NULL,
    `Control_Employee` int NOT NULL,
    PRIMARY KEY (`Name`)
);
CREATE TABLE `Employee` (
    `Ssn` int NOT NULL,
    `Name` varchar(20) NOT NULL,
    `Sex` varchar(10) NOT NULL,
    PRIMARY KEY (`Ssn`)
);
CREATE TABLE `Ensurance` (
    `CardID` int NOT NULL,
    `Type` int NOT NULL,
    `Amount` int NOT NULL,
    PRIMARY KEY (`CardID`, `Type`)
);
CREATE TABLE `Rent_history` (
    `Start_loc` varchar(30) NOT NULL,
    `Stop_loc` varchar(30) NOT NULL,
    `Bike_serial` int NULL,
    `User_cardID` int NOT NULL,
    `History_serial` int NOT NULL,
    `Cost` int NOT NULL,
    `Time` int NOT NULL,
    PRIMARY KEY (
        `Start_loc`,
        `Stop_loc`,
        `User_cardID`,
        `History_serial`
    )
);
ALTER TABLE `User`
ADD CONSTRAINT `fk_User_Rent_bike_serial` FOREIGN KEY(`Rent_bike_serial`) REFERENCES `Bike` (`Serial_num`);
ALTER TABLE `Bike`
ADD CONSTRAINT `fk_Bike_Maintenance_Employee` FOREIGN KEY(`Maintenance_Employee`) REFERENCES `Employee` (`Ssn`);
ALTER TABLE `Bike`
ADD CONSTRAINT `fk_Bike_Park_loc` FOREIGN KEY(`Park_loc`) REFERENCES `Location` (`Name`);
ALTER TABLE `Location`
ADD CONSTRAINT `fk_Location_Control_Employee` FOREIGN KEY(`Control_Employee`) REFERENCES `Employee` (`Ssn`);
ALTER TABLE `Ensurance`
ADD CONSTRAINT `fk_Ensurance_CardID` FOREIGN KEY(`CardID`) REFERENCES `User` (`CardID`);
ALTER TABLE `Rent_history`
ADD CONSTRAINT `fk_Rent_history_Start_loc` FOREIGN KEY(`Start_loc`) REFERENCES `Location` (`Name`);
ALTER TABLE `Rent_history`
ADD CONSTRAINT `fk_Rent_history_Stop_loc` FOREIGN KEY(`Stop_loc`) REFERENCES `Location` (`Name`);
ALTER TABLE `Rent_history`
ADD CONSTRAINT `fk_Rent_history_User_cardID` FOREIGN KEY(`User_cardID`) REFERENCES `User` (`CardID`);
