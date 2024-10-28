#!/bin/sh
sudo rm -f ./sql/test.db 
cd sql/schema
goose sqlite3 ../test.db up