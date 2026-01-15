/*



Prefix · Infix · Postfix Conversion
======================================


What is Operator & Operand
============================

Expression:


a + b
• Operator → +
• Operands → a , b



Priority Order (Operator Precedence)
=======================================

^            → 3   (Highest)
*   /        → 2
+   -        → 1   (Lowest)


Priority flows from top → down





Expression Notations
=======================

Prefix
------

OPERATOR Operand Operand

Example:

* + p q - m n


Infix
--------
Operand OPERATOR Operand

Example:

(p + q) * (m - n)



Postfix
-----------
Operand Operand OPERATOR

Example:

p q + m n - *



Stack Notes (Very Important)
===============================

• If stack top has lower priority
and incoming operator has higher priority
→ PUSH into stack

• If stack top has higher or equal priority
and incoming operator has lower priority
→ POP higher priority operator first
→ then PUSH incoming operator




*/