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

1. plenary discussions/meetings;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
2. discussions within parts of the group;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
3. reading documentation;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
4. configuration and setup;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
5. analyzing code/output;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
6. writing documentation;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
7. writing code;
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:
8. running code:
    * E-Joon Ko:
    * Jakob Berggren:
    * Niklas Tomsic:
    * Caroline Borg:

For setting up tools and libraries (step 4), enumerate all dependencies
you took care of and where you spent your time, if that time exceeds
30 minutes.

## Overview of issue(s) and work done.

Title: Low pylint score

Issue: https://github.com/keon/algorithms/issues/761
PR: 

Pylint is the go-to program for checking whether a Python program is adhering to the [PEP8](https://www.python.org/dev/peps/pep-0008/)-standard. The algorithms project scores really low.

A run of the pylint linter results in a little under 4000 warnings across the entire code-base. Correcting these should not in any way affect the outcome of functions, but would instead improve readability, reduce dead code, and reduce the use of deprecated functions. [TODO: E-Joon, write the score improvement. Maybe link to the branch?]


Title: Tree planting algorithm

Issue: https://github.com/keon/algorithms/issues/768
PR: https://github.com/keon/algorithms/pull/770

A tree planting algorithm utilizing dynamic programming.

This pull request adds the above algorithm with corresponding passing test cases to the repository. The affected code is restricted to a module used to test algorithms using dynamic programming.


Title: Algorithm for calculating the least amount of perfect squares needed to sum a given integer

Issue: https://github.com/keon/algorithms/issues/767
PR: https://github.com/keon/algorithms/pull/769

An algorithm for calculating the least amount of perfect squares needed to sum a given integer.

This pull request adds the above algorithm with corresponding passing test cases to the repository. The affected code is restricted to a module used to test math algorithms.

[TODO: Add the pytest logs after all our issues are done.]

Title:

URL:

Summary in one or two sentences

Scope (functionality and code affected).

## Requirements for the new feature or requirements affected by functionality being refactored

Optional (point 3): trace tests to requirements.

## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).

## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

This project strenghtened our main take-away from the last project, and made us appreciate the value of a well-documented onboarding experience even more. The difference between not knowing whether the failing tests should fail or not, and the exact steps to set-up, install, test, or uninstall the project is very real, and having experienced two projects at the very extremes of onboarding has been a humbling experience.

Another take-away is that you really shouldn't trust the Canvas deadlines-tab since it doesn't necessarily reflect the actual deadlines.

How did you grow as a team, using the Essence standard to evaluate yourself?

According to the Essence checklist on p.52, we achieved the 'Formed' state even before the first assignment was handed in. The group adopted regular meetings early on where we discussed what had been done, current issues that group members were having, and what neeeded to be done. This, combined with establishing project leaders already during the first meeting, led to a well-defined but adaptable and scrum-like setup for each of the projects. We did not achieve 'Collaborating' during the first project as we didn't really get to know each-other until after that assignment. A reason for this probably being the first assignment being so easily divided between group members.

Discounting that we lost a member after the assignment, 'Collaboration' was met towards the end of assignment 2. This was when we started doing regular pair-programming sessions as well as discussing issues over text char during off-time. Now, at the end of assignment 4, we feel that we've reached 'Performing'. Aside from the mis-hap of missing the original deadline, we've reached a state where we have an active and honest flow of communication between all active members. Our dynamic division of work has reduced extraneous work to nil, and we've gained the ability to adapt to unforeseeable events such as 'sudden deadline at work' and 'prolonged internet outage'. At the time of writing this, we still have another assignment left (More on refactoring), and as such we can't consider the group 'Adjourned' just yet.

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?
