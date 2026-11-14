"""food-picture-01 entry: writes one food picture to /output/entry.png.

A steaming bowl of tonkotsu ramen on a dark wooden table, chopsticks
lifting glossy noodles from the creamy broth, a halved jammy egg with
a golden yolk, chashu pork, green onions and nori, steam catching
warm window light. Deterministic: the program copies the image held
in this repository, with no network, no randomness and no clock, so
two runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    src = os.path.join(HERE, "entry.png")
    # The sandbox writes to /output; a local run can point elsewhere
    # with MAKEFUN_OUTPUT_DIR (the kit's starter uses the same knob).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)

if __name__ == "__main__":
    main()
