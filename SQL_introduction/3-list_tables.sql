-- List all tables from the specified database without extra headers
SELECT table_name AS 'Tables_in_hbtn_test_db_0'
FROM information_schema.tables
WHERE table_schema = DATABASE();
