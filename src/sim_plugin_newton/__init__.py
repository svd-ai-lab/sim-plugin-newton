"""Newton driver plugin for sim-cli.

Distributed as an out-of-tree plugin; discovered by sim-cli via the
``sim.drivers`` entry-point group. Bundled skill files (under
``_skills/``) are exposed via the ``sim.skills`` entry-point group, and
lightweight metadata via ``sim.plugins``.
"""
from importlib.resources import files

from .driver import NewtonDriver

skills_dir = files(__name__) / "_skills"

plugin_info = {
    "name": "newton",
    "summary": "Newton driver for sim (v1: one-shot subprocess).",
    "homepage": "https://github.com/svd-ai-lab/sim-plugin-newton",
    "license_class": "oss",
    "solver_name": "Newton",
}

__all__ = ["NewtonDriver", "skills_dir", "plugin_info"]
