CREATE DATABASE IF NOT EXISTS stock_data;
USE stock_data;

CREATE TABLE sectors (
  id_sector SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  sector VARCHAR(100) NOT NULL,
  UNIQUE(sector)
  );

  CREATE TABLE symbol_sector (
  symbol varchar(100) NOT NULL PRIMARY KEY,
  id_sector SMALLINT,
  UNIQUE(symbol),
  FOREIGN KEY (id_sector) REFERENCES sectors(id_sector)
  );

  CREATE TABLE daily_data (
  row_id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  symbol VARCHAR(100),
  time_scraped DATETIME,
  price FLOAT(2),
  price_change FLOAT(2),
  percentage_change FLOAT(2),
  volume VARCHAR(100),
  avg_3_months_volume VARCHAR(100),
  UNIQUE(symbol, time_scraped),
  FOREIGN KEY (symbol) REFERENCES  symbol_sector(symbol)
  );

  CREATE TABLE financial_data (
  row_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  symbol VARCHAR(100),
  date_report DATETIME,
  net_income BIGINT,
  UNIQUE(symbol, date_report),
  FOREIGN KEY (symbol) REFERENCES  symbol_sector(symbol)
  );

  CREATE TABLE recommendations (
  symbol VARCHAR(100),
  date_recommendations DATETIME,
  type_recommendation VARCHAR(100),
  how_many INT,
  PRIMARY KEY(symbol, date_recommendations, type_recommendation),
  FOREIGN KEY (symbol) REFERENCES  symbol_sector(symbol)
  );
