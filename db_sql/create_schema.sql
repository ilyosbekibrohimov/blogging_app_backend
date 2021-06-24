create schema if not exists "posts";

create table if not exists "posts"."post"
(
    "id"           serial primary key,
    "title"        varchar,
    "content"      varchar,
    "picture_blob" bytea
)

