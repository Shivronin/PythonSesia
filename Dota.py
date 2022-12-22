import itertools
import time

it = itertools.cycle(['Д'] + ['о'] + ['т'] + ['а'] + [' '] + ['г'] + ['о'] + ['в'] + ['н'] + ['о'] + ['\b \b'] * 10)
for x in range(40):
    time.sleep(.2)  # выполнение функции
    print(next(it), end='', flush=True)
print('\nСаня иди нахуй!')