#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click


@click.command()
@click.option("--pg-user", default="root", help="PostgreSQL user")
@click.option("--pg-pass", default="root", help="PostgreSQL password")
@click.option("--pg-host", default="localhost", help="PostgreSQL host")
@click.option("--pg-port", default=5432, type=int, help="PostgreSQL port")
@click.option("--pg-db", default="ny_taxi", help="PostgreSQL database name")
@click.option("--target-table", default="green_trip_data", help="Target table name")
@click.option("--year", default="2025", help="Target table name")
@click.option("--month", default="11", help="Target table name")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, year, month):
    url = (
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
    )

    engine = create_engine(
        f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )

    df = pd.read_parquet(url, engine="pyarrow")

    df.to_sql(name=target_table, con=engine, if_exists="replace", index=False)

    engine.dispose()


if __name__ == "__main__":
    run()
