#!/bin/sh
cd sql/schema 
goose sqlite3 ../test.db reset
goose sqlite3 ../test.db up