use elibrary;

CREATE TABLE `users` (
  `firstname` varchar(100) not NULL,
  `lastname` varchar(100) not NULL,
  `username` varchar(100) not NULL,
  PRIMARY KEY (`id`)
);

create table `userbooks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) not null,
  `bookid` int not null,
  PRIMARY KEY (`id`),
  FOREIGN KEY (bookid) REFERENCES books(id)
);

insert into `users` (`firstname`,`lastname`,`username`)
values ('Roman','P','roman'),
('Larry', 'Page', 'larry'),
('Elon', 'Musk', 'elon');