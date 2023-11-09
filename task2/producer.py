#!/usr/bin/env python3

import random
import time

def gen_exp():
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    operator = random.choice(['+', '-', '*', '/'])
    return f"{x} {operator} {y}"

def main():
    random.seed()
    N = random.randint(120, 180)
    
    for _ in range(N):
        exp = gen_exp()
        print(exp, flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()
