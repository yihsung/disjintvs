# Disjoint Intervals

There are two classes in `disjintv.py`:

* `class DisjIntvs()`: this is the main class maintains a set of disjoint intervals. It has two methods:
  1. `add()`: add an interval to the exisiting intervals.
  2. `remove()`: remove an interval from the existing intervals.

* `class Operator()`: this is an interface for running a batch of commands. The actions are given as a sequence of arrays: `[z, a, b]`, where `z` is the command: `z=1` means add and `z=0` means remove; `a, b` represent the interval `[a, b]`. The operator contains two methods:
  1. `run()`: run the commands.
  2. `result()`: print out the intervals.



