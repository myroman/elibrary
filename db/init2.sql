CREATE DATABASE elibrary;
use elibrary;

CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `firstsentence` text,
  `published` int DEFAULT NULL,
  `createdat` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

insert into `books` (`author`,`title`,`published`)
values ('Leo Tolstoy', 'War and Peace', 1885),
('Erih Remark', '3 comrados', 1920),
('ernest hemingway', 'Farewell to the arms', 1942);