#!/usr/bin/env python3
"""Fail when a tracked vault path is too long to survive a Windows download.

Windows File Explorer refuses to open a ZIP archive that contains any entry of
260 bytes or more, and GitHub prepends `networked-thinking-<version>/` to every
path in both the release and the branch archive. Windows also caps an extracted
path at 260 characters, and Explorer's "Extract All" nests the archive name
twice. A 171-byte budget keeps the vault openable, extractable, and clonable on
Windows even for a tag as long as v10.10.10.

Run directly, or via lefthook (pre-commit) and the path-length workflow.
"""
import argparse
import subprocess
import sys

DEFAULT_BUDGET = 171


def vault_paths():
    """Every path git would ship: tracked files plus new files not yet added.

    Untracked files count because a note that has just been written, and not
    yet staged, is exactly the case this check exists to catch. Ignored files
    are excluded, so scratch files do not trip it.
    """
    out = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        check=True,
        capture_output=True,
    ).stdout
    return sorted({p for p in out.decode("utf-8").split("\0") if p})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET)
    parser.add_argument("--quiet", action="store_true", help="print nothing on success")
    args = parser.parse_args()

    paths = vault_paths()
    if not paths:
        print("No files found; is this a git repository?", file=sys.stderr)
        return 1

    over = sorted(
        ((len(p.encode("utf-8")), p) for p in paths if len(p.encode("utf-8")) > args.budget),
        reverse=True,
    )

    if over:
        print(f"{len(over)} path(s) exceed the {args.budget}-byte budget:\n")
        for size, path in over:
            print(f"  {size:4d} bytes ({size - args.budget:+d})  {path}")
        print(
            "\nWindows cannot open a ZIP containing an entry of 260+ bytes, and"
            "\nGitHub adds a ~28-byte prefix to every path in the archive."
            "\n"
            "\nShorten the filename. For an atomic note, split the Definition's"
            "\nfirst sentence into two sentences rather than dropping words, so"
            "\nthe filename still matches the Definition exactly."
        )
        return 1

    if not args.quiet:
        longest = max(len(p.encode("utf-8")) for p in paths)
        print(
            f"Path length OK: {len(paths)} paths, "
            f"longest {longest} bytes, budget {args.budget}."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
