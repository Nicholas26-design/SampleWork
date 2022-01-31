select 
    o.name,c.name 
    from sys.columns            c
        inner join sys.objects  o on c.object_id=o.object_id
    order by o.name,c.column_id
;
select 
     o.name as [Table], c.name as [Column]
     from sys.columns            c
         inner join sys.objects  o on c.object_id=o.object_id
     --where c.name = 'column you want to find'
     order by o.name,c.name
     
--https://stackoverflow.com/questions/2729126/how-to-find-column-names-for-all-tables-in-all-databases-in-sql-server     
