"""Main entry point for the application."""

##############################################################################
# Python imports.
from argparse import ArgumentParser, Namespace
from inspect import cleandoc
from operator import attrgetter

##############################################################################
# Local imports.
from . import __doc__, __version__
from .complexitty import Complexitty
from .mandelbrot import colour_maps


##############################################################################
def get_args() -> Namespace:
    """Get the command line arguments.

    Returns:
        The arguments.
    """

    # Build the parser.
    parser = ArgumentParser(
        prog="complexitty",
        description=__doc__,
        epilog=f"v{__version__}",
    )

    # Add --version
    parser.add_argument(
        "-v",
        "--version",
        help="Show version information",
        action="version",
        version=f"%(prog)s v{__version__}",
    )

    # Add --license
    parser.add_argument(
        "--license",
        "--licence",
        help="Show license information",
        action="store_true",
    )

    # Add --bindings
    parser.add_argument(
        "-b",
        "--bindings",
        help="List commands that can have their bindings changed",
        action="store_true",
    )

    # Add --colour-map
    parser.add_argument(
        "-c",
        "--colour-map",
        "--color-map",
        help="Set the colour map",
        type=str,
        choices=colour_maps(),
    )

    # Add --max-iteration
    parser.add_argument(
        "-i",
        "--max-iteration",
        help="Set maximum iterations",
        type=int,
    )

    # Add --multibrot
    parser.add_argument(
        "-m",
        "--multibrot",
        help="Set the 'multibrot' value",
        type=int,
    )

    # Add --x-position
    parser.add_argument(
        "-x",
        "--x-position",
        help="Set the X position",
        type=float,
    )

    # Add --x-position
    parser.add_argument(
        "-y",
        "--y-position",
        help="Set the Y position",
        type=float,
    )

    # Add --zoom
    parser.add_argument(
        "-z",
        "--zoom",
        help="Set the zoom level",
        type=float,
    )

    # Add --theme
    parser.add_argument(
        "-t",
        "--theme",
        help="Set the theme for the application (set to ? to list available themes)",
    )

    # Finally, parse the command line.
    return parser.parse_args()


##############################################################################
def show_bindable_commands() -> None:
    """Show the commands that can have bindings applied."""
    from rich.console import Console
    from rich.markup import escape

    from .screens import Main

    console = Console(highlight=False)
    for command in sorted(Main.COMMAND_MESSAGES, key=attrgetter("__name__")):
        if command().has_binding:
            console.print(
                f"[bold]{escape(command.__name__)}[/] [dim italic]- {escape(command.tooltip())}[/]"
            )
            console.print(
                f"    [dim italic]Default: {escape(command.binding().key)}[/]"
            )


##############################################################################
def show_themes() -> None:
    """Show the available themes."""
    for theme in sorted(Complexitty(Namespace(theme=None)).available_themes):
        if theme != "textual-ansi":
            print(theme)


##############################################################################
def main() -> None:
    """Main entry point."""
    args = get_args()
    if args.license:
        print(cleandoc(Complexitty.HELP_LICENSE))
    elif args.bindings:
        show_bindable_commands()
    elif args.theme == "?":
        show_themes()
    else:
        Complexitty(args).run()


##############################################################################
if __name__ == "__main__":
    main()


### __main__.py ends here
