from ll import egll

link = egll.head
for i in range(8):
    link = link.next
egll.tail.next = link

# Assuming egll has at least one element.
t1 = t2 = egll.head
t2 = t2.next
while t1 and t2:
    if t1 == t2:
        print 'loop detected! starts at %d' % (egll.tail.next.value)
        exit() # Cannot continue on to print since infinite.
    t1 = t1.next
    if t2.next:
        t2 = t2.next.next
    else:
        break

egll.prt()
