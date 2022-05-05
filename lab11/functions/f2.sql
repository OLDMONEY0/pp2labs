CREATE OR REPLACE PROCEDURE add_new_phonebook(
    new_name varchar,
    new_phone varchar
)
AS $$

#variable_conflict use_column
BEGIN
    IF EXISTS (SELECT name, phone FROM phonebook where new_name = name) THEN
        UPDATE phonebook 
        SET name = new_name, phone = new_phone 
        WHERE name = new_name;
    ELSE
        INSERT INTO phonebook(name, phone) 
        VALUES(new_name, new_phone);
    END IF;
            
END;

$$
LANGUAGE plpgsql;