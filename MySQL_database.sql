CREATE DATABASE `books` -- create a new database schema named books

  --this is the 1st table named book_detils
  --cuurently has 4 columns wherein book_type column is limited to 4 possible values.
CREATE TABLE `book_details` (
  `Book_Name` varchar(45) NOT NULL,
  `Author_Name` varchar(45) NOT NULL DEFAULT 'Unknown',
  `Book_Type` enum('Manga','Comic Book','Graphic Novel','Novel') NOT NULL COMMENT 'Manga, Novel, Comic, Light Novel.',
  `Year_Published` year NOT NULL,
  PRIMARY KEY (`Book_Name`,`Author_Name`)
) ENGINE=InnoDB 

  --this is the 2nd table named calendar
  --this counts up from year 2000 to 2024 and the week number column counts upwards from 1 to 52 each year
  --to do, currrently week number column does not roll back to 1 when the year changes.
CREATE TABLE `calendar` (
  `Week_Number` int NOT NULL,
  `Week_start_date` datetime NOT NULL,
  `Week_end_date` datetime NOT NULL,
  `Year` year NOT NULL,
  PRIMARY KEY (`Week_Number`)
) ENGINE=InnoDB 
