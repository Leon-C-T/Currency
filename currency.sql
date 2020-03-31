CREATE database currency;

USE currency;

CREATE table currencylist(
    Cur_ID INT(10) AUTO_INCREMENT PRIMARY KEY,
    Fiatname VARCHAR(10) NOT NULL,
    Crypname VARCHAR(10) NOT NULL,
    Price DECIMAL(20,5) NOT NULL
);
