CREATE OR REPLACE FUNCTION get_phonebook(n varchar)
  RETURNS TABLE(name VARCHAR, phone VARCHAR) AS
$$
#variable_conflict use_column
BEGIN
  RETURN QUERY

  SELECT name, phone FROM phonebook;

END; $$

LANGUAGE plpgsql;