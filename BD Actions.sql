# add a new donor: Tom Hardy, tommy.h@th.com, born on march 17th 1977,
INSERT INTO blood_donor (donor_firstname, donor_lastname, donor_email, birth_date) values ('Mahesh', 'Sindhu', 'msindhu@mail.com', '1977-03-17');

select * from blood_donor;

# who made a new donation at september 26th 2015, B Rh-, 450 ml, for Ogólnopolski Bank Komórek Macierzystych S.A.
INSERT INTO blood_donation (donation_date, blood_type_donation, blood_quantity_donation, id_donor, id_bank) values ('2015-09-26', 'B Rh-', '450', 26, 1);

select * from blood_donation;

# age of donors
SELECT 
    id_donor AS 'id',
    donor_firstname AS 'first name',
    donor_lastname AS 'last name',
    birth_date AS 'birth date',
    (YEAR(CURDATE()) - YEAR(birth_date)) AS wiek,
    donor_email AS 'e-mail'
FROM
    blood_donor;


# amount of AB Rh+ type blood donated between february and august
SELECT 
    id_donor as 'donor id',
    blood_type_donation as 'blood type',
    donation_date as 'donation date',
    (blood_quantity_donation) AS 'ml'
FROM
    blood_donation
WHERE
    blood_type_donation = 'AB Rh+'
        AND ((MONTH(donation_date) > 02)
        AND (MONTH(donation_date) < 08));

# donors born before 1970

SELECT 
    donor_firstname AS 'first name',
    donor_lastname AS 'last name',
    birth_date AS 'birth date'
FROM
    blood_donor
WHERE
    YEAR(birth_date) < 1970;

# amount of donors with 0 Rh- type blood, who made donation in 2015

SELECT 
    blood_type_donation AS 'blood type',
    blood_quantity_donation AS 'blood quantity',
    id_donor AS 'donor'
FROM
    blood_donation
WHERE
	YEAR(donation_date) = 2015
    and blood_type_donation = '0 Rh-';

# view donor, blood type, quantity and donation date

SELECT 
	id_donor AS 'donor',
	blood_type_donation AS 'blood type',
    blood_quantity_donation AS 'blood quantity',
    DATE_FORMAT(donation_date, '%d.%m.%Yr.') AS 'donation date'
FROM
    blood_donation
ORDER BY donor;
    
# add new request

INSERT INTO blood_request (request_type, request_quantity, request_date, id_facility, id_bank) values ('B Rh-', 2000, '2017-08-04', 7, 2);

# search for request from august 4th 2017

SELECT 
    id_request AS 'request id',
    request_type AS 'blood type',
    request_quantity AS 'quantity (ml)',
    request_date AS 'request date'
FROM
    blood_request
WHERE
    request_date = '2017-08-04';

# add new transport

INSERT INTO blood_transport (transport_date, blood_type, transport_quantity, id_facility) values ('2017-08-04', 'B Rh-', 2000, 7);

# search for transport from august 4th 2017
    
SELECT 
    id_transport AS 'transport id',
    transport_date AS 'date of transport',
    blood_type AS 'blood type',
    transport_quantity AS 'quantity (ml)'
FROM
    blood_transport
WHERE
    transport_date = '2017-08-04';
    
# search for all transports with A Rh- blood type

SELECT 
    id_transport AS 'transport id',
    transport_date AS 'date of transport',
    blood_type AS 'blood type',
    transport_quantity AS 'quantity (ml)'
FROM
    blood_transport
WHERE
    blood_type = 'A Rh-'
ORDER BY transport_date;
    
# sum quantity all B Rh- transports in 2016
    
SELECT 
    blood_type AS 'blood type',
    SUM(transport_quantity) AS 'summary'
FROM
    blood_transport
WHERE
    blood_type = 'B Rh-';
    
# count all donations

select count(*) as 'all donations' from blood_donation;

# count all donations with 0 Rh+ blood type

SELECT 
    COUNT(*) AS 'all donations'
FROM
    blood_donation
WHERE
    blood_type_donation = '0 Rh+';

# update donor email adress to 'abc@gmail.xyz for donor id = 15'

UPDATE blood_donor 
SET 
    donor_email = 'abc@gmail.xyz'
WHERE
    id_donor=15;
        
# show informations about donor whose last name is singh

SELECT 
    id_donor AS 'donor id',
    donor_firstname AS 'first name',
    donor_lastname AS 'last name',
    donor_email AS 'email adress'
FROM
    blood_donor
WHERE
    donor_lastname = 'singh';
        
# what was the largest transport for each blood type, what was the quantity of it and when it happened? order by quantity descending

SELECT 
    blood_type AS 'blood type',
    MAX(transport_quantity) AS 'quantity',
    id_transport AS 'transport id',
    transport_date AS 'date of transport'
FROM
    blood_transport
GROUP BY blood_type
ORDER BY quantity desc;

# 1st view blood type A Rh-

CREATE VIEW ARhmin AS
    SELECT 
        id_donor,
        donation_date,
        blood_type_donation,
        blood_quantity_donation
    FROM
        blood_donation
    WHERE
        blood_type_donation = 'A Rh-';

# alter 1st view blood type A Rh-

alter view ARhmin as 
	select 
		id_donor as 'donor id',
        donation_date as 'donation date',
        blood_type_donation as 'blood type',
        blood_quantity_donation as 'quantity (ml)'
	FROM
        blood_donation
    WHERE
        blood_type_donation = 'A Rh-';

# show 1st view

select * from ARhmin;

# dropping 1st view

drop view ARhmin;

# donors view

CREATE VIEW donors AS
    SELECT 
        id_donor as 'donor id',
        birth_date as 'birth date',
        (YEAR(CURDATE()) - YEAR(birth_date)) AS 'age',
        donor_firstname as 'first name',
        donor_lastname as 'last name'
    FROM
        blood_donor;

# show donors view

select * from donors;

# donations view

CREATE VIEW donations AS
    SELECT 
        id_donation as 'donation id',
        id_donor as 'donor id',
        donation_date as 'donation date',
        blood_type_donation as 'blood type',
        blood_quantity_donation as 'quantity (ml)'
    FROM
        blood_donation;

# show donations view

select * from donations;

# requests view

CREATE VIEW requests AS
    SELECT 
        id_request as 'donation id',
		id_facility as 'facility id',
        request_type as 'blood type',
        request_quantity as 'quantity (ml)',
        request_date as 'request date'
    FROM
        blood_request;

# show requests view

select * from requests;

# medical facility view

CREATE VIEW facility AS
    SELECT 
        id_facility as 'facility id',
		facility_name as 'facility name',
        facility_adress as 'facility adress'
    FROM
        med_facility;

# show medical facility view

select * from facility;

SELECT 
    id_donor AS 'donor id',
    id_donation AS 'donation id',
    donation_date AS 'donation date',
    blood_type_donation AS 'blood type',
    id_bank AS 'bank id',
    donor_firstname AS 'donor first name',
    donor_lastname AS 'donor last name',
    birth_date AS 'donor birth date',
    donor_email AS 'donor email'
FROM
    blood_donor
        NATURAL RIGHT JOIN
    blood_donation
ORDER BY id_donor; 

# triggers