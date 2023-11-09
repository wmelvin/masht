import sys
from textwrap import dedent

from masht import md_to_html

# def test_failure():
#     assert False


def test_a_markdown_file(tmp_path, monkeypatch):
    md = tmp_path / "test.md"
    md.write_text(
        dedent(
            """
            # Heading 1

            ## Heading 2

            ### Heading 3

            [bogusoft](https://www.bogusoft.com/)

            List of:
            - stuff
            - fluff
            - snuff

            ---

            """
        )
    )

    assert md.exists()

    monkeypatch.setattr(sys, "argv", ["masht.py", str(md)])

    md_to_html.main()

    assert md.with_suffix(".md.AS.html").exists()
