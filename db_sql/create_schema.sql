create schema if not exists "posts";

create table if not exists "posts"."post"
(
    "id"           serial primary key,
    "title"        varchar,
    "content"      varchar,
    "picture_blob" bytea
);

create table if not exists "posts"."users"

(
    "id"        serial primary key,
    "id_token"  varchar default null,
    "name"      varchar,
    "email"     varchar unique,
    "photo_url" varchar

);

create table if not exists "posts"."comments"
(
    "id"      serial primary key,
    "user_id" integer references "posts"."users" (id),
    "post_id" integer references "posts"."post" (id),
    "content" varchar
);

create table if not exists "posts"."likes"
(
    "id"        serial primary key,
    "timestamp" varchar,
    "user_id"   integer references "posts"."users" (id),
    "post_id"   integer references "posts"."post" (id)
)

