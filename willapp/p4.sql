CREATE TABLE "will" (
  "id" serial PRIMARY KEY,
  "user_name" varchar,
  "user_address" varchar,
  "user_phone" varchar,
  "user_tax_id" varchar,
  "created_when" timestamptz
);

CREATE TABLE "asset" (
  "id" serial PRIMARY KEY,
  "will_id" serial,
  "name" varchar,
  "description" varchar,
  "quantity" int,
  "location" varchar
);

CREATE TABLE "inheritor" (
  "id" serial PRIMARY KEY,
  "name" varchar,
  "address" varchar,
  "phone" varchar,
  "tax_id" varchar,
  "active" boolean
);

CREATE TABLE "inheritor_group" (
  "id" serial PRIMARY KEY,
  "inheritor_id" serial,
  "grouping_key" varchar,
  "priority" int
);

CREATE TABLE "distribution" (
  "id" serial PRIMARY KEY,
  "asset_id" serial,
  "inheritor_group_id" serial,
  "percentage" real,
  "distributed" boolean
);

ALTER TABLE "asset" ADD FOREIGN KEY ("will_id") REFERENCES "will" ("id");

ALTER TABLE "inheritor_group" ADD FOREIGN KEY ("inheritor_id") REFERENCES "inheritor" ("id");

ALTER TABLE "distribution" ADD FOREIGN KEY ("asset_id") REFERENCES "asset" ("id");

ALTER TABLE "distribution" ADD FOREIGN KEY ("inheritor_group_id") REFERENCES "inheritor_group" ("id");

-- class Cheese(models.Model):
--     name = models.CharField(max_length=100)
--     origin_country = models.CharField(max_length=100)
--     type = models.CharField(max_length=100)
