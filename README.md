# README

1. Download all parquet files files

```sh
$ wget -i dl.txt
```

2. Setup python project

```sh
$ poetry install
```

3. Create sqlite file (file will be found in `./db.sqlite`)

```sh
$ poetry run alembic upgrade head
```

4. Run CLI, see cli.py

```sh
$ poetry run python3 cli.py import_profiles
$ poetry run python3 cli.py import_<...>
```