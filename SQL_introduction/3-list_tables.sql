-- Lists all tables from the specified database
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = DATABASE();
