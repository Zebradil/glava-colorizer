import colorsys
import sys


def generate_hsv(h: float, s: float) -> tuple:
    return ((h + 1) * 180, (s + 1) / 2, 100)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line == "" or line.startswith(";"):
            continue
        t, h, s = line.split()
        if not is_int(t):
            continue
        h = float(h)
        s = float(s)
        hsv = generate_hsv(h, s)
        rgb = colorsys.hsv_to_rgb(*hsv)
        out = rgb_to_hex(*map(int, rgb))
        print("{} {}".format(t, out), file=sys.stderr)
        print(out, flush=True)
