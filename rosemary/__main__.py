from rosemary.cli import check_working_dir, cli, load_commands


def main():
    """Punto de entrada principal de Rosemary."""
    check_working_dir()  # Verificar variables de entorno antes de ejecutar la CLI

    load_commands(cli)  # Asegurar que los comandos se cargan antes de ejecutar la CLI

    cli()  # Ejecutar la CLI normalmente


if __name__ == "__main__":
    main()
