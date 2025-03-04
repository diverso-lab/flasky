import click
import subprocess
from dotenv import load_dotenv
import os
from datetime import datetime


@click.command(
    "db:dump", help="Creates a dump of the MariaDB database with credentials from .env."
)
@click.argument("filename", required=False)
def db_dump(filename):
    load_dotenv()

    mariadb_hostname = os.getenv("MARIADB_HOSTNAME")
    mariadb_user = os.getenv("MARIADB_USER")
    mariadb_password = os.getenv("MARIADB_PASSWORD")
    mariadb_database = os.getenv("MARIADB_DATABASE")

    # Generate default filename if not provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dump_{timestamp}.sql"
    else:
        # Ensure filename has .sql extension
        if not filename.endswith(".sql"):
            filename += ".sql"

    # Build the mysqldump command
    dump_cmd = f"mysqldump -h{mariadb_hostname} -u{mariadb_user} -p{mariadb_password} \
        {mariadb_database} > {filename}"

    # Execute the command
    try:
        subprocess.run(dump_cmd, shell=True, check=True, executable="/bin/bash")
        click.echo(
            click.style(f"Database dump created successfully: {filename}", fg="green")
        )
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"Error creating database dump: {e}", fg="red"))
