-- Set view to table mode
.mode table

-- View all the devices
SELECT * FROM "devices" ORDER BY "type";

-- View the battery inventory
SELECT "id", "kind", "inventory", "usage" FROM "batteries" 
JOIN (SELECT "battery_type", SUM("battery_qty") AS "usage" FROM "devices"
GROUP BY "battery_type"
) 
ON "batteries"."kind" = "battery_type"
;

-- View all the changes
SELECT "device_id", "name", "date" 
FROM "changes" JOIN "devices" 
ON "changes"."device_id" = "devices"."id";