-------------------------------------------------------------------------------------------
--Trigger Name: INSERT_RENT_DETAILS
--This trigger updates the availability flag in the car table 
--when the car is rented then it updates the booking status in the booking table when the booking is confirmed
-------------------------------------------------------------------------------------------
DELIMITER $$
CREATE TRIGGER INSERT_RENT_DETAILS
BEFORE INSERT ON GRADE_REPORT 
FOR EACH ROW
BEGIN
    DECLARE message VARCHAR(255);
    IF(!CHECK_AVAILABILITY(NEW.REGISTRATION_NUMBER))
    THEN 
        SET message=CONCAT('YOU HAVE TO WAIT FOR SOME TIME IN ORDER TO RENT THE CAR ',NEW.REGISTRATION_NUMBER); 
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT=message;
    ELSE 
      UPDATE CAR_DETAILS SET AVAILABILITY_FLAG='N' WHERE REGISTRATION_NUMBER=NEW.REGISTRATION_NUMBER;
      UPDATE BOOKING_DETAILS SET BOOKING_STATUS='B' WHERE BOOKING_ID=NEW.BOOKING_ID;
    END IF;
END$$
DELIMITER ;




