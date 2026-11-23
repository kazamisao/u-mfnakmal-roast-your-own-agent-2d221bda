import os

TEXT = (
    "My agent announces every plan like a Nobel acceptance speech, then "
    "delivers it one loading bar at a time: genius-level confidence, "
    "permanently buffering."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
