class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        copies = {}

        cur = head

        # Create all copied nodes
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        # Assign next and random pointers
        while cur:
            copies[cur].next = copies.get(cur.next)
            copies[cur].random = copies.get(cur.random)
            cur = cur.next

        return copies[head]