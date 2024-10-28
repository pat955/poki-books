./scripts/reqs.sh
sqlc generate

./scripts/gopy_build.sh
./scripts/migrate.sh
./scripts/autolint.sh
./scripts/test.sh
