# Disjoint Intervals

### Formats 

* **Format of Intervals:** the format of an interval is`[a,b)` with `a <= b`. Remark that `[a,a)` is valid and it is an *empty set*.

* **Format of Commands:** in order to focus on problem solving, we simplify the input. The format of a command consists of three numbers `[z, a, b]`, where `z` is the command: `z=1` means *add* and `z=0` means *remove*; `a, b` represent the interval `[a, b)`. 

----

### Classes 

There are two classes in `disjintv.py`:

* `class DisjIntvs(intvs)`: this is the main class maintains a set of disjoint intervals. `intvs` is the default set of disojint intervals. The class has two methods:
  1. `add(a,b)`: add `[a,b)`  to the exisiting intervals.
  2. `remove(a,b)`: remove `[a,b)` from the existing intervals.

* `class Operator(intvs, acts)`: this is an interface for running a batch of commands. `intvs` is the initial set of disjoint intervals. It is set as `[]` as default; `acts` is a sequence of commands. The class contains three methods:
  1. `run()`: run the commands.
  2. `result()`: return the current set of intervals.
  3. `gen_randtest()`: generate a set of commands for testing.

----

### Parameters

* `class Operator()`: in `gen_randtest`, `TESTCMDS` is the number of commands in one test batch; `UPPBDD` is the upperbound of the randomly generated intervals.
* `main section`: `ROUNDS` is the round of *random tests*.

