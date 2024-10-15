#!/bin/sh
cd sql/schema 
goose sqlite3 ../poki_books.db reset
cd ..
cd ..
./scripts/migrate.sh