from ll import egll

def remove_duplicates(link):
    head = link.head
    count = dict()
    while head is not None:
        count[head.value] = count.get(head.value, 0) + 1
        head = head.next

    head = link.head
    while head is not None:
        if count[head.value] > 1:
            count[head.value] -= 1
            temp = head
            head = head.next
            link.delete(link.head, temp)
        else:
            head = head.next

egll.prt()
remove_duplicates(egll)
egll.prt()
