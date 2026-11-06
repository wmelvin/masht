# masht

**M**arkdown **as** **HT**ML

Reads a Markdown file and writes a HTML of the same name with a `AS.html` suffix.

PyPI: [masht](https://pypi.org/project/masht/)

```console
USAGE: masht [-h] [--stylesheet FILE] [filename.md ...]
```

The generated HTML links to a stylesheet named `style.css` by default. Use `--stylesheet FILE` to link to a different file name.

Uses the [mistune](https://pypi.org/project/mistune/) Markdown parser ([documentation](https://mistune.lepture.com/en/latest/)).
