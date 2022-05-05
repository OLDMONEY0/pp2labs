CREATE OR REPLACE PROCEDURE delete_one_phonebook(
    delete_column VARCHAR
)
AS $$

BEGIN
    DELETE FROM phonebook
        WHERE name = delete_column or phone = delete_column;

END;
$$
LANGUAGE plpgsql;