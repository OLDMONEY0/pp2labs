CREATE OR REPLACE PROCEDURE add_new_phonebooks(
    new_names[11] 
	new_phones[11]
)
AS $$

BEGIN
        FOR cnt in 1..11 LOOP
			INSERT INTO phonebook(name, phone)
			VALUES(new_names[cnt], new_phones[cnt]);
		END LOOP;
END;
LANGUAGE plpgsql;

