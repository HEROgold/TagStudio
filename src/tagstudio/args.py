from argparse import Namespace

from herogold.argparse import Actions, Argument

from tagstudio.core.constants import VERSION, VERSION_BRANCH


class TagStudio(Namespace):
    """TagStudio launcher arguments. For use with `python -m tagstudio`."""

    open = Argument(
        "--open",
        type_=str,
        help="Path to a TagStudio Library folder to open on start.",
    )
    settings_file = Argument(
        "--settings-file",
        type_=str,
        help="Path to a TagStudio .toml global settings file to use.",
    )
    cache_file = Argument(
        "--cache-file",
        type_=str,
        help="Path to a TagStudio .ini or .plist cache file to use.",
    )
    debug = Argument(
        "debug",
        action=Actions.STORE_TRUE,
        help="Reveals additional internal data useful for debugging.",
    )
    version = Argument(
        "--version",
        action=Actions.VERSION,
        help="Displays TagStudio version information.",
        default=f"TagStudio v{VERSION} {VERSION_BRANCH}",
    )
    browse = Argument(
        "--browse",
        action=Actions.STORE_TRUE,
        help="Jumps to entry browsing on startup.",
    )
    external_preview = Argument(
        "--external-preview",
        action=Actions.STORE_TRUE,
        help="Outputs current preview thumbnail to a live-updating file.",
    )
