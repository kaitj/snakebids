from __future__ import annotations

from typing import TYPE_CHECKING

from snakebids.paths._templates import spec_func
from snakebids.paths.utils import BidsPathSpec, find_entity, get_spec_path, load_spec

# <AUTOUPDATE>
# The code between these tags is automatically generated. Do not
# manually edit
# To update, run::
#
#       poetry run poe update_bids
#

if not TYPE_CHECKING:
    __all__ = ["v0_0_0", "latest", "LATEST"]  # noqa:F822

    def __dir__():
        return __all__


_SPECS = ["v0_0_0"]
LATEST = "v0_0_0"
# </AUTOUPDATE>


def __getattr__(name: str):
    """Allow dynamic retrieval of latest spec."""
    if name == "latest":
        name = LATEST

    if name not in _SPECS:
        msg = f"module '{__name__}' has no attribute '{name}'"
        raise AttributeError(msg)

    spec_config = load_spec(get_spec_path(name))

    spec = spec_config["spec"]

    def get_spec(subject_dir: bool = True, session_dir: bool = True) -> BidsPathSpec:
        if not subject_dir:
            find_entity(spec, "subject")["dir"] = False

        if not session_dir:
            find_entity(spec, "session")["dir"] = False

        return spec

    get_spec.__doc__ = spec_func.format_doc(spec_config)
    get_spec.__name__ = name

    return get_spec
