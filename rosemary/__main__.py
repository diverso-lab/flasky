from rosemary.cli import check_working_dir, cli, load_commands


def main():
    check_working_dir()
    load_commands(cli)
    cli()


if __name__ == "__main__":
    main()
