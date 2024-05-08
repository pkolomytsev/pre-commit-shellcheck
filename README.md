# pre-commit-shellcheck

This package provides a pip-installable [shellcheck][1] binary (mostly for
pre-commit purposes). It uses a custom build-backend, [pre-commit-download][2],
so downloading the executable is done during the wheel build process.

Inspired by [shellcheck-py][3].

## Installation

<!-- markdownlint-disable MD013 -->

```bash
pip install git+https://github.com/pkolomytsev/pre-commit-shellcheck.git@v0.10.0.1
```

<!-- markdownlint-enable MD013 -->

## Usage

As a regular executable from your environment:

```bash
shellcheck -V
```

As a [pre-commit][4] hook:

```yaml
repos:
  - repo: https://github.com/pkolomytsev/pre-commit-shellcheck
    rev: v0.10.0.1
    hooks:
      - id: shellcheck
```

[1]: https://www.shellcheck.net/
[2]: https://github.com/pkolomytsev/pre-commit-download
[3]: https://github.com/shellcheck-py/shellcheck-py
[4]: https://pre-commit.com/
