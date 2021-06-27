create schema if not exists "posts";

create table if not exists "posts"."post"
(
    "id"           serial primary key,
    "title"        varchar,
    "content"      varchar,
    "picture_blob" bytea
);

create  table if not exists "posts"."users"

(
    "id"        serial primary key,
    "id_token"  varchar default null,
    "name"      varchar,
    "email"     varchar unique,
    "photo_url" varchar

)
