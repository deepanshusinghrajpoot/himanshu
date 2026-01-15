/*






Introduction to Binary Trees
==============================

Definition
.............

A Binary Tree is a hierarchical data structure where
each node has at most two children:

Left child
Right child


Basic Terms
------------

Root
-----
The topmost node of the tree
Starting point of the tree

    A   ← Root

Children
---------
Nodes directly connected below a parent

      A
     / \
    B   C   ← B and C are children of A



Leaf Node
----------

A node with no children

      A
     / \
    B   C
         \
          D  ← Leaf nodes: B, D



Ancestors
---------
All nodes above a given node up to the root

      A
     /
    B
   /
  C

Ancestors of C → B, A












Types of Binary Trees
=======================

1. Full Binary Tree
--------------------

Definition
-----------
Every node has either 0 or 2 children
No node has only one child

Example
        A
       / \
      B   C
     / \
    D   E


✔ Valid
❌ Node with single child is not allowed





2. Complete Binary Tree
------------------------

Definition
-----------
All levels are completely filled
Last level is filled from left to right

Example
        A
       / \
      B   C
     / \  /
    D   E F


✔ Left filled first
❌ Right child without left is not allowed






3. Perfect Binary Tree
-------------------------

Definition
------------

All internal nodes have 2 children
All leaf nodes are at the same level

Example
            A
         /     \
        B       C
      /  \    /   \
     D    E  F     G


✔ Nodes = 2^h - 1
✔ Height is completely balanced








4. Balanced Binary Tree
------------------------

Definition
-----------

For every node:   |height(left) - height(right)| ≤ 1
Keeps tree height minimum

Example
        A
       / \
      B   C
     /
    D


✔ Height difference ≤ 1
Used in AVL Trees, Red-Black Trees






5. Degenerate Tree
--------------------

Definition
-----------
Each node has only one child
Tree behaves like a linked list

Example (Left Degenerate)
    A
   /
  B
 /
C
/
D


❌ Worst case
❌ Time complexity becomes O(n)






















*/