# Batteries

SQLite application to keep track of the usage and inventory of batteries in every home device that uses batteries. Access to the database is made through a Python layer.

## Modules
This application uses the `sqlite3` Python module to create a conneciton with the database, and the `tabulate` module to pretty-print the reports in table format. Both modules are imported at the beggining of our `batteries.py` file.

## Main Steps

1. Create an sqlite database: `sqlite3 batteries.db` from the terminal command prompt.
2. If you have a persistent database already created and want to access it, just go to the sqlite3 command prompt by typing `sqlite3`, and then `.open batteries.db`.
3. Create a table: it is better to put all your tables and triggers in a schema.sql file. You can then load them with `.read schema.sql` from the sqlite command prompt.

## To insert info in tables
### With a csv file 
First import it into a temp file: `.import --csv devices.csv temp` and then merge the temp file into the table: 
```
INSERT INTO "devices" ("name", "type", "battery_type", "battery_qty") 
SELECT "name", "type", "battery_type", "battery_qty"
FROM temp;
```   
### Manually
```
INSERT INTO "batteries" ("kind", "inventory") 
VALUES
('AAA', 26),
('AA', 19),
('123', 0),
('9V', 1),
('CR2032', 12)
;
```

## Fixing Mistakes
If you make changes to the structure of a table, you can remove it from the database with `DROP TABLE tablename`. They you can read your schema file again to update to the new structure.

You can delete all the rows on a table with `DELETE FROM "tablename"`.

You can update an individual record with `UPDATE "batteries" SET "inventory" = 19 WHERE "id" = 2;`

You can delete an individual record with `DELETE FROM "changes" WHERE "device_id" = 15;`.

## Outputs
You can view the individual tables with SELECT. For a neat table view type `.mode table` from the sqlite command prompt.

You can print all the outputs with `.read queries.sql`.

You can also use the Python layer to access the queries without having to type SQLite commands.

## Python Layer
After the first iteration of the program, I decided to create an interface in Python to capture information from the user rather than writing the SQLite queries by hand every time. It provides a simple menu with five different options:

```
Menu:
0. Print reports
1. Add new device
2. Replace batteries
3. Add batteries to inventory
4. Exit program
```

You type your preferred option and start answering the prompts. The Python layer will then take that information and interact with SQLite to make the necessary changes to the database.

To start the program type `python3 batteries.py` from the bash command prompt. 

It is a good idea to choose option 0 at the begginning and at the end of updating the database, so you can make sure the expected changes were recorded.