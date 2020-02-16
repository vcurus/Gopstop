import time
import random

codes = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
а = ord('А')
print()


def dsa (a):
    
    for i in range(а, а + 32):       
    time.sleep(0.3)
    print(f'{chr(155)}{random.choice(codes)}m{chr(i)}', end=' ', flush=True)


dsa(a)
print('\x1b[0m')