CREATE OR REPLACE FUNCTION get_phonebook_option(n integer)
  RETURNS TABLE(name VARCHAR, phone VARCHAR) 
AS
$$
#variable_conflict use_column
BEGIN
    RETURN QUERY
	SELECT name, phone
		FROM phonebook
		ORDER BY name
		LIMIT n OFFSET 2;
END;
$$
LANGUAGE plpgsql;
