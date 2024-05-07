"""Entry points and all that."""

import os
import subprocess  # noqa: S404
import sys

import importlib_resources


def get_pkg_resource(pkg_name: str, res_relpath: str) -> str:
    """Get a path to the package resource.

    :param pkg_name: the package name
    :param res_relpath: the resource relative path the package root
    :return: a path to the package resource
    """
    with importlib_resources.as_file(
        importlib_resources.files(pkg_name).joinpath(res_relpath),
    ) as pkg_file:
        return str(pkg_file)


def get_self_resource(res_relpath: str) -> str:
    """Get a path to the package resource of this library.

    :param res_relpath: the resource relative path the package root
    :return: a path to the package resource
    """
    return get_pkg_resource("pre_commit_shellcheck", res_relpath)


def shellcheck(*argv) -> int:
    """Call the installed shellcheck.

    :param argv: shellcheck command line arguments
    :return: exit code
    """
    bin_path = get_self_resource("bin")
    exec_path = os.path.join(bin_path, "shellcheck")
    if sys.platform == "win32":
        exec_path = f"{exec_path}.exe"
    proc = subprocess.run([exec_path, *argv])  # noqa: S603
    return proc.returncode


def entry() -> int:
    """Shellcheck entry point.

    :return: exit code (0 - ok, other - error)
    """
    return shellcheck(*sys.argv[1:])
