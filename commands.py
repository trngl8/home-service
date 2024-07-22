import click
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext




@click.command("show-environment-configuration")
@with_appcontext
def show_environment_configuration():
    """
    Shows environment configuration
    """
    for key, value in current_app.config.items():
        click.echo(f"{key}: {value}")


@click.command("show-order-requests")
@with_appcontext
def show_order_requests():
    """
    Shows all the order requests
    """
    db_path = current_app.config["DATABASE"]
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM realty")
        rows = cursor.fetchall()

        for row in rows:
            click.echo(row)
    finally:
        cursor.close()
        connection.close()
