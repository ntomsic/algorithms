# Report for assignment 4 Group 19

This is the report markdown file of assignment 4 by Group 19. The members for this group assignment are: E-Joon Ko, Niklas Tomsic, Caroline Borg, and Jakob Berggren.

## Project

Name: Algorithms (Pythonic Data Structures and Algorithms)

URL: https://github.com/keon/algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Onboarding experience

For this assignment, our group decided to choose a new project compared to the project chosen in assignment 3. This decision was made because this new project had well defined issues which seemed clear to solve and was done in Python 3 which our group was more comfortable with. Meanwhile our previous project Jsoniter (http://jsoniter.com/java-features.html) had vague issues, making it hard for us to determine how to approach the assignment. The decision to change projects was done after a few hours of trying to get the old project to pass all existing unit tests. As described in our previous report, the onboarding experience of Jsoniter was lackluster at best, and we grew tired of trying to find the exact combination of dependencies required to pass the unit tests and actually begin assignment 4.

The onboarding experience for Algorithms was a lot smoother than Jsoniter due to couple of reasons. First off, being able to run unittests on this project was as simple as importing the project and simply running unittest in the relevant directory. Compared to Algorithms, Jsoniter required us to use a IDE such as Intellij to easily work with Maven and have the correct dependencies for the project, which took a while and didn't work properly even after we tweaked some of the Maven dependencies. Therefore, overall the onboarding experience with Algorithms has been easy and straightforward.

Algorithms also has a much better documentation present in it's readme file compared to Jsoniter, as it has detailed instructions on how to test, install, and uninstall the software. It also has a long detailed list of every single function present in the project, making navigation and comprehension easy for the group.
## Effort spent

For each team member, how much time was spent in

1. **plenary discussions/meetings:**
    * E-Joon Ko: 2 hour.
    * Jakob Berggren: 2 hour.
    * Niklas Tomsic: 2 hour.
    * Caroline Borg: 2 hour.
2. **discussions within parts of the group:**
    * E-Joon Ko: 3 hour.
    * Jakob Berggren: 3 hour.
    * Niklas Tomsic: 3 hour.
    * Caroline Borg: 3 hour.
3. **reading documentation:**
    * E-Joon Ko: 1 hour.
    * Jakob Berggren: 1 hour.
    * Niklas Tomsic: 1 hour.
    * Caroline Borg: 1 hour.
4. **configuration and setup:**
    * E-Joon Ko: less than 30 minutes.
    * Jakob Berggren: less than 30 minutes.
    * Niklas Tomsic: less than 30 minutes.
    * Caroline Borg: less than 30 minutes.
5. **analyzing code/output:**
    * E-Joon Ko: 4 hours
    * Jakob Berggren:
    * Niklas Tomsic: 1 hour
    * Caroline Borg: 1 hour
6. **writing documentation:**
    * E-Joon Ko: 4 hours
    * Jakob Berggren:
    * Niklas Tomsic: 4 hour (including making PRs etc.)
    * Caroline Borg: 1 hour ( -||- )
7. **writing code:**
    * E-Joon Ko: 4 hours
    * Jakob Berggren:
    * Niklas Tomsic: 4 hours
    * Caroline Borg: 4 hours
8. **running code:**
    * E-Joon Ko: 2 hours
    * Jakob Berggren:
    * Niklas Tomsic: 1 hour
    * Caroline Borg: 1 hour


## Overview of issue(s) and work done.

### Title: Low pylint score

Issue: https://github.com/keon/algorithms/issues/761

Pylint is the go-to program for checking whether a Python program is adhering to the
[PEP8](https://www.python.org/dev/peps/pep-0008/)-standard. The algorithms project scores really low
with a score of 6.53/10.

A run of the pylint linter results in a little under 4000 warnings across the entire code-base.
Correcting these should not in any way affect the outcome of functions, but would instead improve readability,
reduce dead code, and reduce the use of deprecated functions. It is also important to ensure that improving the code
does not interfere with the performance of all the tests.

   * **Original score: 6.53/10:** https://github.com/ntomsic/algorithms/tree/master
   * **Commit 1: 7.04/10:** https://github.com/ntomsic/algorithms/commit/f97b23418e408e352c5ba8d28616b667aa7e43ab
   * **Commit 2: 7.17/10:** https://github.com/ntomsic/algorithms/commit/a7695e69f456d325e05dc12084b6d28c5d2e3aa3
   * **Commit 3: 7.37/10:** https://github.com/ntomsic/algorithms/commit/4c4af54f025fca82ad988914b8089b0e8e49419e
   * **Commit 4: 7.46/10:** https://github.com/ntomsic/algorithms/commit/3e922e914fb9463872ea20d87fc418c426ed3ad9
   * **Commit 5: 7.61/10:** https://github.com/ntomsic/algorithms/commit/a30ddb6e5c3d9eb497873e00c192820ffd579f93
   * **Commit 6: 8.06/10:** https://github.com/ntomsic/algorithms/commit/cdd2b2924d82c4926ca8bb518b5596d3b5e8f472
   * **Commit 7: 8.41/10:** https://github.com/ntomsic/algorithms/commit/6e032dd83c9941449a5e0937028d0ec928b5e7ae
   * **Commit 8: 8.63/10:** https://github.com/ntomsic/algorithms/commit/0ea1f53f89517c6aa18986b57d6f15de2799517a
   * **Commit 9: 8.65/10:** https://github.com/ntomsic/algorithms/commit/78110d54f172db4987c207463489ad0d5608d68b

#### Commit 1: Reformatting the entire directory (Ctrl + Alt + L)

By using the Jetbrain IDE for Python (Pycharm), we were able to reformat the code with respect to the Python standards
with the command (Ctrl + Alt + L). This command can be used for a line, multiple lines, files, and even directories to
reformat all the code. Reformatting can include improvements such as: Optimizing imports. Proper spacing between classes,
functions, and definitions. Proper formatting of code statements and comments.

#### Commit 2-3: Removing/editing redundant if/elif cases, removing unnecessary parentheses, and removing trailing whitespaces

There were many cases in which an else or elif case were unnecessary due to the previous case having a guaranteed return.

There were also many unnecessary parentheses which could be safely removed without affecting the test results.

Finally, there were a lot of trailing whitespaces which could be safely removed.

#### Commit 4: Editing non-used variables

There were a lot of cases in which variables (specifically in for loops) were not being used. In python, unused variable
can instead be assigned as "don't care" like so: _.

#### Commit 5-8: Changing variable names to conform to standard Python naming style, editing lines that are too long, optimizing if cases through simplification.

Variables names were changed so that they conformed to the standard Python naming style, such as variable names conforming
to the snake_case style, and constant variables conforming to the UPPER_CASE style.

Some lines (Mostly comments) were over a hundred character long, and therefore could be split up so that every line did not
exceed 100 characters.

Finally, a lot of if cases could either be optimized or simplified to either make the code more readable, or to improve
code complexity through refactoring.

#### Commit 9: Final Touches

Some final touches were made for more difficult and sensitive code scenarios which easily affected the test results.

### Title: Tree planting algorithm

Issue: https://github.com/keon/algorithms/issues/768
PR: https://github.com/keon/algorithms/pull/770

A tree planting algorithm utilizing dynamic programming.

This pull request adds the above algorithm with corresponding passing test cases to the repository. The affected code is restricted to a module used to test algorithms using dynamic programming.


### Title: Least amount of perfect squares algorithm

Issue: https://github.com/keon/algorithms/issues/767
PR: https://github.com/keon/algorithms/pull/769

An algorithm for calculating the least amount of perfect squares needed to sum a given integer. Even if there are relatively litte code there are some advanced mathematical theorems that are required to calculate the correct result of the algorithm such as [Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem) and [Legendre's three-square theorem](https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem) which made the whole process a lot harder than it looks. If you just look at the finished code the few lines of code do not reflect the whole thought proccess surrounding the problem solving and verification of the solution.

This pull request adds the above algorithm with corresponding passing test cases to the repository. The affected code is restricted to a module used to test math algorithms.

## Requirements for the new feature or requirements affected by functionality being refactored

### Title: Low Pylint score
**Requirement 1:** Improve Pylint score from original score by at least 1.0.
   * After running Pylint on the Algorithms directory, the code in whatever way should be improved by atleast 1.0 points
   to be considered improved substantially for the issue to be determined fixed.

**Requirement 2:** Pass all test (Or at least have tests results be consistent with the Master Branch) after Linting.
   * All the tests in the "tests" directory should be tested regularly with the linting and improvement process to ensure
   that the codes are not affected in such a way that it affects the test results. Basically the code should overall be
     improved without affecting the test results.

### Title: Tree planting algorithm

**Requirement 1:** Correct input and output
   * The function should take in a list of integers, and then two additional integers. It should return a float.

**Requirement 2:** Correct result for first test
   * The function should return the correct result for the test_simple test found in /tests/test_dp.py.

**Requirement 3:** Correct result for second test
   * The function should return the correct result for the test_simple2 test found in /tests/test_dp.py.

**Requirement 4:** Passing the Kattis testsuite
   * The function should pass the [Kattis testsuite](https://open.kattis.com/problems/aspenavenue) for this algorithm.

### Title: Least amount of perfect squares algorithm

**Requirement 1:** Correct result for perfect squares.
   * The first requirement is that the algorithm works for perfect square input. Essentially if the square root of the input rounded to the nearest integer has to be the input, eg. 9 = 3<sup>2</sup>

**Requirement 2:** Correct result for four perfect squares.
   * The second requirement is that the agorithm works for four squares in accordance to [Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem). eg. 960 = 24<sup>2</sup> + 16<sup>2</sup> + 8<sup>2</sup> + 8<sup>2</sup>

**Requirement 3:** Correct result for three perfect squares.
   * The third requirement is that the algorithm works for three squares in accordance to [Legendre's three-square theorem](https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem). eg. 600 = 20<sup>2</sup> + 14<sup>2</sup> + 2<sup>2</sup>

**Requirement 4:** Correct result for two perfect squares.
   * The fourth requirement is that the algorithm works for two perfect squares. eg. 500 = 20<sup>2</sup> + 10<sup>2</sup>

**Requirement 5:** All tests pass
   * The final requirement is that all tests pass for the algorithm. These new tests are placed in /tests/test_math.py and everything in this folder should pass.

## Code changes

### Patch

#### Title: Low Pylint score
``` 
git checkout linting 
git diff 0ea1f53f89517c6aa18986b57d6f15de2799517a^ HEAD 
```

#### Title: Tree planting algorithm

``` 
git diff 40f240a46573dcb7559d0557eaa6a768d976ba46 d5b397ab89e48935f0afc0af4d4fa1c078e9bd1e
```

#### Title: Least amount of perfect squares algorithm

``` 
git diff 40f240a46573dcb7559d0557eaa6a768d976ba46 c2043dcc18f437352e7455c32a2fa0b1ffc275df
```

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).

#### Title: Low Pylint score

Before
```
$ python -m pytest
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 366 items

tests\test_array.py ............................                         [  7%]
tests\test_automata.py .                                                 [  7%]
tests\test_backtrack.py .........................                        [ 14%]
tests\test_bfs.py ...                                                    [ 15%]
tests\test_bit.py .............................                          [ 23%]
tests\test_compression.py .....                                          [ 24%]
tests\test_dfs.py ........                                               [ 27%]
tests\test_dp.py .....................                                   [ 32%]
tests\test_graph.py ..............                                       [ 36%]
tests\test_heap.py .....                                                 [ 37%]
tests\test_histogram.py .                                                [ 38%]
tests\test_iterative_segment_tree.py .........                           [ 40%]
tests\test_linkedlist.py ............                                    [ 43%]
tests\test_map.py .......................                                [ 50%]
tests\test_maths.py ....................................                 [ 60%]
tests\test_matrix.py .............                                       [ 63%]
tests\test_ml.py ..                                                      [ 64%]
tests\test_monomial.py ........                                          [ 66%]
tests\test_polynomial.py .......                                         [ 68%]
tests\test_queues.py .....                                               [ 69%]
tests\test_search.py .............                                       [ 73%]
tests\test_set.py .                                                      [ 73%]
tests\test_sort.py ...................                                   [ 78%]
tests\test_stack.py ..........                                           [ 81%]
tests\test_strings.py .................................................. [ 95%]
...                                                                      [ 95%]
tests\test_tree.py ...........                                           [ 98%]
tests\test_unix.py F.F.                                                  [100%]


=========================== short test summary info ===========================
FAILED tests/test_unix.py::TestUnixPath::test_full_path - AssertionError: 'D:...
FAILED tests/test_unix.py::TestUnixPath::test_simplify_path - AssertionError:...
================== 2 failed, 364 passed, 3 warnings in 7.00s ==================
```
After
```
$ python -m pytest
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 366 items

tests\test_array.py ............................                         [  7%]
tests\test_automata.py .                                                 [  7%]
tests\test_backtrack.py .........................                        [ 14%]
tests\test_bfs.py ...                                                    [ 15%]
tests\test_bit.py .............................                          [ 23%]
tests\test_compression.py .....                                          [ 24%]
tests\test_dfs.py ........                                               [ 27%]
tests\test_dp.py .....................                                   [ 32%]
tests\test_graph.py ..............                                       [ 36%]
tests\test_heap.py .....                                                 [ 37%]
tests\test_histogram.py .                                                [ 38%]
tests\test_iterative_segment_tree.py .........                           [ 40%]
tests\test_linkedlist.py ............                                    [ 43%]
tests\test_map.py .......................                                [ 50%]
tests\test_maths.py ....................................                 [ 60%]
tests\test_matrix.py .............                                       [ 63%]
tests\test_ml.py ..                                                      [ 64%]
tests\test_monomial.py ........                                          [ 66%]
tests\test_polynomial.py .......                                         [ 68%]
tests\test_queues.py .....                                               [ 69%]
tests\test_search.py .............                                       [ 73%]
tests\test_set.py .                                                      [ 73%]
tests\test_sort.py ...................                                   [ 78%]
tests\test_stack.py ..........                                           [ 81%]
tests\test_strings.py .................................................. [ 95%]
...                                                                      [ 95%]
tests\test_tree.py ...........                                           [ 98%]
tests\test_unix.py F.F.                                                  [100%]


=========================== short test summary info ===========================
FAILED tests/test_unix.py::TestUnixPath::test_full_path - AssertionError: 'D:...
FAILED tests/test_unix.py::TestUnixPath::test_simplify_path - AssertionError:...
================== 2 failed, 364 passed, 3 warnings in 7.41s ==================
```

#### Title: Tree planting algorithm
Before
```
$ python -m pytest tests/test_dp.py
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 21 items

tests\test_dp.py .....................                                   [100%]

============================= 21 passed in 0.36s ==============================
```
After
```
$ python -m pytest tests/test_dp.py
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 23 items

tests\test_dp.py .......................                                 [100%]

============================= 23 passed in 0.57s ==============================
```

#### Title: Least amount of perfect squares algorithm
Before
```
$ python -m pytest tests/test_maths.py
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 36 items

tests\test_maths.py ....................................                 [100%]

============================= 36 passed in 3.51s ==============================
```

After
```
$ python -m pytest tests/test_maths.py
============================= test session starts =============================
platform win32 -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: ****
collected 37 items

tests\test_maths.py .....................................                [100%]

============================= 37 passed in 3.79s ==============================
```



## UML class diagram and its description

### Key changes/classes affected

## Overall experience

### What are your main take-aways from this project? What did you learn?

This project strengthened our main take-away from the last project, and made us appreciate the value of a well-documented onboarding experience even more. The difference between not knowing whether the failing tests should fail or not, and the exact steps to set-up, install, test, or uninstall the project is very real, and having experienced two projects at the very extremes of onboarding has been a humbling experience.

Another take-away is that you really shouldn't trust the Canvas deadlines-tab since it doesn't necessarily reflect the actual deadlines.

### How did you grow as a team, using the Essence standard to evaluate yourself?

According to the Essence checklist on p.52, we achieved the 'Formed' state even before the first assignment was handed in. The group adopted regular meetings early on where we discussed what had been done, current issues that group members were having, and what neeeded to be done. This, combined with establishing project leaders already during the first meeting, led to a well-defined but adaptable and scrum-like setup for each of the projects. We did not achieve 'Collaborating' during the first project as we didn't really get to know each-other until after that assignment. A reason for this probably being the first assignment being so easily divided between group members.

Discounting that we lost a member after the assignment, 'Collaboration' was met towards the end of assignment 2. This was when we started doing regular pair-programming sessions as well as discussing issues over text char during off-time. Now, at the end of assignment 4, we feel that we've reached 'Performing'. Aside from the mis-hap of missing the original deadline, we've reached a state where we have an active and honest flow of communication between all active members. Our dynamic division of work has reduced extraneous work to nil, and we've gained the ability to adapt to unforeseeable events such as 'sudden deadline at work' and 'prolonged internet outage'. At the time of writing this, we still have another assignment left (More on refactoring), and as such we can't consider the group 'Adjourned' just yet.

