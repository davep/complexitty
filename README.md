# Complexitty

[![Complexitty](https://raw.githubusercontent.com/davep/complexitty/refs/heads/main/.images/complexitty-social-banner.png)](https://complexitty.davep.dev/)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/davep/complexitty/code-checks.yaml)](https://github.com/davep/complexitty/actions)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/davep/complexitty/latest)](https://github.com/davep/complexitty/commits/main/)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/davep/complexitty)](https://github.com/davep/complexitty/issues)
[![GitHub Release Date](https://img.shields.io/github/release-date/davep/complexitty)](https://github.com/davep/complexitty/releases)
[![PyPI - License](https://img.shields.io/pypi/l/complexitty)](https://github.com/davep/complexitty/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/complexitty)](https://github.com/davep/complexitty/blob/main/pyproject.toml)
[![PyPI - Version](https://img.shields.io/pypi/v/complexitty)](https://pypi.org/project/complexitty/)

## Introduction

Complexitty is a simple terminal-based application that lets you explore the
classic Mandelbrot set in full character-based glory. It is the successor to
and replacement for
[`textual-mandelbrot`](https://github.com/davep/textual-mandelbrot).

## Installing

### pipx

The package can be installed using [`pipx`](https://pypa.github.io/pipx/):

```sh
$ pipx install complexitty
```

### uv

The application can be installed using [`uv`](https://docs.astral.sh/uv/getting-started/installation/):

```sh
uv tool install complexitty
```

If you don't have `uv` installed you can use [uvx.sh](https://uvx.sh) to
perform the installation. For GNU/Linux or macOS or similar:

```sh
curl -LsSf uvx.sh/complexitty/install.sh | sh
```

or on Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://uvx.sh/complexitty/install.ps1 | iex"
```

### Going faster

Complexitty has a (currently experimental) installation option to make it go
faster using [Numba](http://numba.pydata.org). If you want to try this out,
install it as `complexitty[faster]` rather than `complexitty`.

## Using Complexitty

Once you've installed Complexitty using one of the above methods, you can
run the application using the `complexitty` command.

The best way to get to know Complexitty is to read the help screen, once in the
main application you can see this by pressing <kbd>F1</kbd>.

![Complexitty help](https://raw.githubusercontent.com/davep/complexitty/refs/heads/main/.images/complexitty-help.png)

For more information and details on configuring Complexitty, see [the online
documentation](https://complexitty.davep.dev/).

## Getting help

If you need help, or have any ideas, please feel free to [raise an
issue](https://github.com/davep/complexitty/issues) or [start a
discussion](https://github.com/davep/complexitty/discussions).

## TODO

See [the TODO tag in
issues](https://github.com/davep/complexitty/issues?q=is%3Aissue+is%3Aopen+label%3ATODO)
to see what I'm planning.

[//]: # (README.md ends here)
