CREATE TABLE "devices" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "type" TEXT NOT NULL,
    "battery_type" TEXT NOT NULL,
    "battery_qty" NUMERIC,
    PRIMARY KEY("id") 
);


CREATE TABLE "batteries" (
    "id" INTEGER,
    "kind" TEXT NOT NULL UNIQUE,
    "inventory" NUMERIC,
    PRIMARY KEY("id"),
    FOREIGN KEY("kind") REFERENCES "devices"("battery_type")
);


CREATE TABLE "changes" (
    "device_id" INTEGER,
    "date" NUMERIC NOT NULL DEFAULT '2023-01-01',
    PRIMARY KEY("device_id", "date"),
    FOREIGN KEY("device_id") REFERENCES "devices"("id")
);


CREATE TRIGGER "update" 
AFTER INSERT ON "changes"
BEGIN
    UPDATE "batteries"
    SET "inventory" = "inventory" - (SELECT "battery_qty" FROM "devices" WHERE "id" = (SELECT "device_id" FROM "changes" WHERE "device_id" = NEW."device_id"))
    WHERE "kind" = (SELECT "battery_type" FROM "devices" WHERE "id" = (SELECT "device_id" FROM "changes" WHERE "device_id" = NEW."device_id"));
END;