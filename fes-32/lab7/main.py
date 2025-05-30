import csv, time
import asyncio, aiofiles
import reactivex as rx
from reactivex import operators as ops


def default_func():
    with open('lab7/csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()

        print('default')

        count = 0
        for row in csv.reader(file):
            if 'Ukraine' in row:
                count += 1

        print(count)
        print(f'Time: {time.time() - start}')


async def async_func():

    async with aiofiles.open('lab7/csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()

        print('async')

        data = await file.readlines()
        count = 0

        for row in data:
            if 'Ukraine' in row:
                count += 1

        print(count)

        print(f'Time: {time.time() - start}')


async def rx_func():
    async with aiofiles.open('lab7/csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()

        print('rx')

        data = await file.readlines()

        observable = rx.from_(data)

        observable.pipe(
            ops.filter(lambda x: 'Ukraine' in x), ops.count()
        ).subscribe(lambda out: print(out))

        print(f'Time: {time.time() - start}')


default_func()
print()

asyncio.run(async_func())
print()

asyncio.run(rx_func())
