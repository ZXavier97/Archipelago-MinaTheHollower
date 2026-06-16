"""CLI: validate an edges.csv. Exit 0 if clean, 1 if any problems.

Usage:
    python -m worlds.mina_the_hollower.tools.validate_edges path/to/edges.csv
"""
import argparse
import pathlib
import sys

try:  # standalone-first so the tooling never needs to boot the Archipelago stack
    import edge_schema as es
except ModuleNotFoundError:  # running via `python -m worlds.mina_the_hollower.tools...`
    from worlds.mina_the_hollower.tools import edge_schema as es

AREAS_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "locations"


def known_area_names() -> set[str]:
    """Area module names = the .py files in areas/ (excluding dunder files)."""
    return {
        p.stem.removesuffix("_edges")
        for p in AREAS_DIR.glob("*.py")
        if not p.stem.startswith("__")
    }


def main(argv: "list[str] | None" = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Mina edges.csv")
    parser.add_argument("csv", type=pathlib.Path)
    args = parser.parse_args(argv)

    edges = es.read_edges_csv(args.csv)
    errors = es.validate_rows(edges, known_area_names())

    unresolved = es.unresolved_to_regions(edges)
    if unresolved:
        print(f"{len(unresolved)} unresolved to_region(s) (never a from_region "
              f"- typo, truncation, or edge into an unmigrated area):")
        for r in unresolved:
            print(f"  ? {r}")

    if errors:
        print(f"{len(errors)} problem(s) in {args.csv}:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(edges)} edges, no problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
