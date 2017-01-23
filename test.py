#!/usr/bin/env python
from celery import chord, chain
from tasks import add, multiple, total_sum


result = chord(
    chain(
        add.s(i, i),
        multiple.s(i)
    )
    for i in xrange(10))(total_sum.s()).get()
print(result)
