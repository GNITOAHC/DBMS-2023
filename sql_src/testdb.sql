-- MySQL dump 10.13  Distrib 8.0.33, for macos13.3 (arm64)
--
-- Host: localhost    Database: Youbike
-- ------------------------------------------------------
-- Server version	8.0.33
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */
;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */
;
/*!50503 SET NAMES utf8mb4 */
;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */
;
/*!40103 SET TIME_ZONE='+00:00' */
;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
;
drop database if exists Youbike;
create database Youbike;
use Youbike;
--
-- Table structure for table `Bike`
--

DROP TABLE IF EXISTS `Bike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `Bike` (
    `Serial_num` int NOT NULL,
    `Factory` varchar(60) NOT NULL,
    `Is_broken` tinyint(1) NOT NULL,
    `Is_using` tinyint(1) NOT NULL,
    `Maintenance_record` int NOT NULL,
    `Maintenance_Employee` int NOT NULL,
    `Park_loc` varchar(20) NOT NULL,
    PRIMARY KEY (`Serial_num`),
    KEY `fk_Bike_Maintenance_Employee` (`Maintenance_Employee`),
    KEY `fk_Bike_Park_loc` (`Park_loc`),
    CONSTRAINT `fk_Bike_Maintenance_Employee` FOREIGN KEY (`Maintenance_Employee`) REFERENCES `Employee` (`Ssn`),
    CONSTRAINT `fk_Bike_Park_loc` FOREIGN KEY (`Park_loc`) REFERENCES `Location` (`Name`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `Bike`
--

LOCK TABLES `Bike` WRITE;
/*!40000 ALTER TABLE `Bike` DISABLE KEYS */
;
INSERT INTO `Bike`
VALUES (456, 'Giant', 0, 0, 0, 123, 'SY');
/*!40000 ALTER TABLE `Bike` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `Employee` (
    `Ssn` int NOT NULL,
    `Name` varchar(20) NOT NULL,
    `Sex` varchar(10) NOT NULL,
    PRIMARY KEY (`Ssn`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */
;
INSERT INTO `Employee`
VALUES (123, 'John', 'male');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `Ensurance`
--

DROP TABLE IF EXISTS `Ensurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `Ensurance` (
    `CardID` int NOT NULL,
    `Type` int NOT NULL,
    `Amount` int NOT NULL,
    PRIMARY KEY (`CardID`, `Type`),
    CONSTRAINT `fk_Ensurance_CardID` FOREIGN KEY (`CardID`) REFERENCES `User` (`CardID`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `Ensurance`
--

LOCK TABLES `Ensurance` WRITE;
/*!40000 ALTER TABLE `Ensurance` DISABLE KEYS */
;
INSERT INTO `Ensurance`
VALUES (789, 1, 100);
/*!40000 ALTER TABLE `Ensurance` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `Location`
--

DROP TABLE IF EXISTS `Location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `Location` (
    `Name` varchar(20) NOT NULL,
    `Street` varchar(30) NOT NULL,
    `District` varchar(30) NOT NULL,
    `City` varchar(30) NOT NULL,
    `Control_Employee` int NOT NULL,
    PRIMARY KEY (`Name`),
    KEY `fk_Location_Control_Employee` (`Control_Employee`),
    CONSTRAINT `fk_Location_Control_Employee` FOREIGN KEY (`Control_Employee`) REFERENCES `Employee` (`Ssn`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `Location`
--

LOCK TABLES `Location` WRITE;
/*!40000 ALTER TABLE `Location` DISABLE KEYS */
;
INSERT INTO `Location`
VALUES ('SY', 'ShengYang', 'Xinyi', 'TPE', 123),
('Taipei 101', 'Shifu', 'Xinyi', 'TPE', 123);
/*!40000 ALTER TABLE `Location` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `Rent_history`
--

DROP TABLE IF EXISTS `Rent_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `Rent_history` (
    `Start_loc` varchar(30) NOT NULL,
    `Stop_loc` varchar(30) NOT NULL,
    `Bike_serial` int NOT NULL,
    `User_cardID` int NOT NULL,
    `History_serial` int NOT NULL,
    `Cost` int NOT NULL,
    `Time` int NOT NULL,
    PRIMARY KEY (
        `Start_loc`,
        `Stop_loc`,
        `Bike_serial`,
        `User_cardID`,
        `History_serial`
    ),
    KEY `fk_Rent_history_Stop_loc` (`Stop_loc`),
    KEY `fk_Rent_history_Bike_serial` (`Bike_serial`),
    KEY `fk_Rent_history_User_cardID` (`User_cardID`),
    CONSTRAINT `fk_Rent_history_Bike_serial` FOREIGN KEY (`Bike_serial`) REFERENCES `Bike` (`Serial_num`),
    CONSTRAINT `fk_Rent_history_Start_loc` FOREIGN KEY (`Start_loc`) REFERENCES `Location` (`Name`),
    CONSTRAINT `fk_Rent_history_Stop_loc` FOREIGN KEY (`Stop_loc`) REFERENCES `Location` (`Name`),
    CONSTRAINT `fk_Rent_history_User_cardID` FOREIGN KEY (`User_cardID`) REFERENCES `User` (`CardID`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `Rent_history`
--

LOCK TABLES `Rent_history` WRITE;
/*!40000 ALTER TABLE `Rent_history` DISABLE KEYS */
;
INSERT INTO `Rent_history`
VALUES ('SY', 'Taipei 101', 456, 789, 111, 50, 60);
/*!40000 ALTER TABLE `Rent_history` ENABLE KEYS */
;
UNLOCK TABLES;
--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!50503 SET character_set_client = utf8mb4 */
;
CREATE TABLE `User` (
    `CardID` int NOT NULL,
    `Name` varchar(20) NOT NULL,
    `Rent_bike_serial` int DEFAULT NULL,
    PRIMARY KEY (`CardID`),
    KEY `fk_User_Rent_bike_serial` (`Rent_bike_serial`),
    CONSTRAINT `fk_User_Rent_bike_serial` FOREIGN KEY (`Rent_bike_serial`) REFERENCES `Bike` (`Serial_num`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;
--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */
;
INSERT INTO `User`
VALUES (789, 'Alice', NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */
;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */
;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */
;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */
;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
;
-- Dump completed on 2023-05-17 15:33:38