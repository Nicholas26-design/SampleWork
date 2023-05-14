---SQL:

--Temp Tables:

IF OBJECT_ID('tempdb..##TempTable') IS NOT NULL
    DROP TABLE ##TempTable
select CPT.Column_Name
INTO ##TempTable
from table CPT

--Finding columns in the database:

SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME like '%location%'
ORDER BY TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME


  
--Seeing when the table was last updated /Refreshed:

SELECT OBJECT_NAME(OBJECT_ID) AS TableName,
 last_user_update,*
FROM sys.dm_db_index_usage_stats
WHERE database_id = DB_ID( 'Database_name')
AND OBJECT_ID=OBJECT_ID('Table_name')

