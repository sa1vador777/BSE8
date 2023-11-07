#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: tuple, n: int) -> int:
    inp: list = sorted(inp, reverse=True)
    return inp.index(n) + 1


if __name__ == "__main__":
    print(main(inp=tuple(range(21)), n=19))
