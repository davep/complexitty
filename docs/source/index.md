# Introduction

```{.textual path="docs/screenshots/basic_app.py" title="Complexitty" lines=70 columns=200}
```

Complexitty is a simple terminal-based application that lets you explore the
classic Mandelbrot set in full character-based glory.

## Installation

### pipx

The application can be installed using [`pipx`](https://pypa.github.io/pipx/):

```sh
pipx install complexitty
```

### uv

If you are a [`uv`](https://docs.astral.sh/uv/) user you can:

```sh
uv tool install complexitty
```

Also, if you do have uv installed, you can simply use
[`uvx`](https://docs.astral.sh/uv/guides/tools/):

```sh
uvx complexitty
```

to run `complexitty`.

### Homebrew

The package is available via [Homebrew](https://brew.sh). Use the following
commands to install:

```sh
brew tap davep/homebrew
brew install complexitty
```

## Running Complexitty

Once you've installed Complexitty using one of the [above
methods](#installation), you can run the application using the `complexitty`
command.

### Command line options

Complexitty has a number of command line options; they include:

#### `-b`, `--bindings`

Prints the application commands whose keyboard bindings can be modified,
giving the defaults too.

```sh
complexitty --bindings
```
```bash exec="on" result="text"
complexitty --bindings
```

#### `-c`, `--colour-map`, `--color-map`

Set the colour map to use in the plot.

#### `-h`, `--help`

Prints the help for the `complexitty` command.

```sh
complexitty --help
```
```bash exec="on" result="text"
complexitty --help
```

#### `-i`, `--max-iteration`

Set the maximum number of iterations for the plot's calculation.

#### `--license`, `--licence`

Prints a summary of [Complexitty's license](license.md).

```sh
complexitty --license
```
```bash exec="on" result="text"
complexitty --license
```

#### `-m`, `--multibrot`

Set the 'multibrot' parameter for the plot.

#### `-t`, `--theme`

Sets Complexitty's theme; this overrides and changes any previous theme choice made
[via the user interface](configuration.md#theme).

To see a list of available themes use `?` as the theme name:

```sh
complexitty --theme=?
```
```bash exec="on" result="text"
complexitty --theme=?
```

#### `-v`, `--version`

Prints the version number of Complexitty.

```sh
complexitty --version
```
```bash exec="on" result="text"
complexitty --version
```

#### `-x`, `--x-position`

Set the X position of the centre of the plot.

#### `-y`, `--y-position`

Set the Y position of the centre of the plot.

#### `-z`, `--zoom`

Set the amount of zoom to use for the plot.

## Getting help

A great way to get to know Complexitty is to read the help screen. Once in
the application you can see this by pressing <kbd>F1</kbd>.

```{.textual path="docs/screenshots/basic_app.py" title="The Complexitty Help Screen" press="f1" lines=50 columns=120}
```

### The command palette

Another way of discovering commands and keys in Complexitty is to use the
command palette (by default you can call it with
<kbd>ctrl</kbd>+<kbd>p</kbd> or <kbd>meta</kbd>+<kbd>x</kbd>).

```{.textual path="docs/screenshots/basic_app.py" title="The Complexitty Command Palette" press="ctrl+p" lines=50 columns=120}
```

## Questions and feedback

If you have any questions about Complexitty, or you have ideas for how it might be
improved, do please feel free to [visit the discussion
area](https://github.com/davep/complexitty/discussions) and [ask your
question](https://github.com/davep/complexitty/discussions/categories/q-a) or
[suggest an
improvement](https://github.com/davep/complexitty/discussions/categories/ideas).

When doing so, please do search past discussions and also [issues current
and previous](https://github.com/davep/complexitty/issues) to make sure I've not
already dealt with this, or don't have your proposed change already flagged
as something to do.

[//]: # (index.md ends here)
