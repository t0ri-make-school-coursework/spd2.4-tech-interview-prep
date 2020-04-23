Rotate a given linked-list counter-clockwise by k nodes, where k is the given integer.

1. What clarifying questions would you ask?
Will the linked-list always be more than k nodes long? If no, what should happen when that occurs?
Is it a doubly linked-list?
What built-in methods do the LinkedList and LinkedListNode class have?
Is k always positive?
Do I have access to the head and tail references?
2. What reasonable assumptions could you state?
... I do have access to head and tail references
The linkedlist will always be at least k nodes long
3. What are 2-3 ways you can simplify the problem?
- rotate by one node at a time

4. Brainstorm 2-3 ways to approach the problem.
- for _ in k ap
5. Choose one idea and write pseudocode for it.
for each num in range k:
    get current node from head
    get last node from tail
    set ll head to current node next
    set ll tail to current node
    set last node next to ll tail
    set ll tail next to None