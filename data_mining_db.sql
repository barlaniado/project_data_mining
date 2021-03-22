CREATE TABLE `companies` (
  `company_no` int NOT NULL auto_increment,
  `symbol` varchar(10) NOT NULL,
  `sector` varchar(20) NOT NULL,
  PRIMARY KEY (`company_no`),
  UNIQUE KEY `symbol` (`symbol`)
  );
  
CREATE TABLE `daily_data` (
  `company_no` int NOT NULL auto_increment,
  `time` datetime NOT NULL,
  `price` float NOT NULL,
  `price_change` float NOT NULL,
  `percentage` float NOT NULL,
  `volume` float NOT NULL,
  `avg_vol`	float NOT NULL,
  PRIMARY KEY (`company_no`),
  CONSTRAINT FOREIGN KEY (`company_no`) REFERENCES `companies` (`company_no`) ON DELETE CASCADE
);

CREATE TABLE `financials_data` (
  `company_no` int NOT NULL auto_increment,
  `time` date NOT NULL,
  `price` float NOT NULL,
  `net_income` float NOT NULL,	
  PRIMARY KEY (`company_no`),
  CONSTRAINT FOREIGN KEY (`company_no`) REFERENCES `companies` (`company_no`) ON DELETE CASCADE
);