CREATE database currency;

USE currency;

CREATE table cryp2fiat(
    Cur_ID INT(10) AUTO_INCREMENT PRIMARY KEY,
    Fiatname VARCHAR(10) NOT NULL,
    Crypname VARCHAR(10) NOT NULL,
    Price DECIMAL(20,5) NOT NULL
);

CREATE table fiat2cryp(
    Cur_ID INT(10) AUTO_INCREMENT PRIMARY KEY,
    Crypname VARCHAR(10) NOT NULL,
    Fiatname VARCHAR(10) NOT NULL,
    Price DECIMAL(15,10) NOT NULL
);