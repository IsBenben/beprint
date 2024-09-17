# BePrint -- A Python Package

> Make Your Python Print Statements Beautiful

## Introduction

**`beprint` (beautiful print)** is a simple package that can print messages in different colors and styles.

## Installation

Run the following command to install the package via pip:

```shell
pip install beprint
```

You can also clone the repository and run the following command to install the package:

```shell
pip install .
```

---------

```python
# Import the package
from beprint import *
beprint("Hello, world!")
```

## Features

- **Align Texts** - The package can align text using the `align` function. You can also use the `align_center`, `align_left`, `align_right`, and `align_stretch` functions to align text.
- **ANSI Codes** - The package uses ANSI escape codes to print messages in different colors and styles. Example: `Ansi.string('red').light().style('bold')`.
- **Code Highlight** - The package can highlight any code using the `highlight_code` function. This feature is powered by the `pygments` library.
- **Columns Layout** - The package can print messages in columns using the `beprint_columns` function.
- **Markdown Preview** - The package can preview markdown messages using the `beprint_md` function. This feature is powered by the `mistune` library.
- **Printing Objects** - The package can print objects with colors and styles using the `beprint` function.
- **Table** - The package can print messages in tables using the `Table` function. Base features: Add rows, columns, and pretty print.

You can find more information about the package in the *examples* folder.
