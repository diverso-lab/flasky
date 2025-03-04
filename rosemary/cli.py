import os
import sys
import importlib
import click


def check_working_dir():
    working_dir = os.getenv("WORKING_DIR", "").strip()

    if not working_dir:
        return

    if working_dir in ["/app", "/vagrant", "/app/", "/vagrant/"] and not os.path.exists(
        working_dir
    ):

        print(
            f"⚠️  WARNING: WORKING_DIR is set to '{working_dir}', but the directory does not exist."
        )

        if working_dir in ["/app", "/app/"]:
            print(
                "📌 It looks like your `.env` file is configured for Docker, "
                "but you are running Rosemary locally."
            )
        elif working_dir in ["/vagrant", "/vagrant/"]:
            print(
                "📌 It looks like your `.env` file is configured for Vagrant, "
                "but you are running Rosemary locally."
            )

        print("\n💡 How to fix this issue:\n")
        print(
            "  Option 1️⃣  Update your `.env` file and set WORKING_DIR=\"\" to run locally. "
            "Don't forget to type `source .env` to reload the environment variables."
        )

        if working_dir in ["/app", "/app/"]:
            print(
                "  Option 2️⃣  Start the correct environment: use `docker exec -it web_app_container bash` "
                "to access the container, then run `rosemary` inside."
            )
        elif working_dir in ["/vagrant", "/vagrant/"]:
            print(
                "  Option 2️⃣  Start the correct environment: use `vagrant ssh` to access the virtual machine, "
                "then run `rosemary` inside."
            )

        print("")

        sys.exit(1)


class RosemaryCLI(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = super().get_command(ctx, cmd_name)
        if rv is None:
            click.echo(f"No such command '{cmd_name}'.")
            click.echo("Try 'rosemary --help' for a list of available commands.")
        return rv


def load_commands(cli_group, commands_dir="rosemary/commands"):
    """
    Dynamically import all commands in the specified directory and add them to the CLI group.
    """
    commands_path = os.path.abspath(commands_dir)
    for file in os.listdir(commands_path):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"rosemary.commands.{file[:-3]}"
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, click.Command):
                    cli_group.add_command(attr)


@click.group(cls=RosemaryCLI)
def cli():
    """A CLI tool to help with project development."""
