# Allganize Types Overview

This is collection of stub packages for Type checkers (Pyright, ...).
Type checkers will use the type information by [PEP 561](https://peps.python.org/pep-0561/#type-checker-module-resolution-order).

## How to update/ add stub package?

1. Generate stub files or write some stub files. Please refer to [Pyright Generating Type Stubs](https://github.com/microsoft/pyright/blob/main/docs/type-stubs.md#generating-type-stubs)

   ```
   pyright --createstub [import-name]
   ```

   and update the generated draft stub files if need.

   or write by [PEP 561](https://peps.python.org/pep-0561/).

2. Create `{import-name}-stubs` directory in this repository and update `packages` of `[tool.poetry]` section in build config, `pyproject.toml`.
   (Please refer to [PEP 621](https://peps.python.org/pep-0621/) and [poetry docs](https://python-poetry.org/docs/) for `pyproject.yaml`)
