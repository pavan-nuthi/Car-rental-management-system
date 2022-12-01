-------------------------------------------------------------------------------------------
--Function Name: CHECK_AVAILABILITY
--This function checks if the given car is booked.
-------------------------------------------------------------------------------------------
DELIMITER $$
CREATE FUNCTION CHECK_AVAILABILITY(REGISTRATION_NUM VARCHAR(7))
RETURNS INTEGER
BEGIN
  IF((SELECT AVAILABILITY_FLAG FROM CAR_DETAILS WHERE REGISTRATION_NUMBER=REGISTRATION_NUM)='A') THEN
    RETURN 1;
  ELSE
    RETURN 0;
  END IF;
END$$
DELIMITER ;

