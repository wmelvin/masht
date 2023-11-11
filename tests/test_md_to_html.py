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

            List using asterisk:

            * stuff
            * fluff
            * fuzz

            ---

            """
        )
    )

    assert md.exists()

    monkeypatch.setattr(sys, "argv", ["masht.py", str(md)])

    md_to_html.main()

    ht = md.with_suffix(".md.AS.html")

    assert ht.exists()

    #  Open the test-output file in the default browser.
    # import webbrowser as wb
    # wb.open_new_tab(f"file://{ht}")


def test_a_markdown_file_with_list_not_preceeded_by_blank_line(tmp_path, monkeypatch, capsys):
    md = tmp_path / "test-lists.md"
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

            List using asterisk:
            * stuff
            * fluff
            * fuzz

            ---
            """
        )
    )

    assert md.exists()

    monkeypatch.setattr(sys, "argv", ["masht.py", str(md)])

    md_to_html.main()

    ht = md.with_suffix(".md.AS.html")

    assert ht.exists()

    captured = capsys.readouterr()

    assert "WARNING: Lists should be preceeded by a blank line. At line 17." in captured.out

    #  Open the test-output file in the default browser.
    # import webbrowser as wb
    # wb.open_new_tab(f"file://{ht}")
