# -*- coding: utf-8 -*-

import random

a = unicode(raw_input(u'Write text: '))
a = a.split()
z = []
for i in a:
    i = list(i)
    b = i[1:-1]
    random.shuffle(b)
    i[1:-1] = b
    i.append(' ')
    i = ''.join(i)
    z.append(i)
z = ''.join(z)
print z
