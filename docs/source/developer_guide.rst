Contributing Guide
==================
windIO was started under IEA Wind Task 37 and has been additionally supported by IEA Wind Task 55
as well as other community-based groups, research organization, and private companies.
Being a collaborative effort, it is important to establish a common understanding of the
rules, responsibilities, and expectations from all stakeholders.
**This document outlines the processes and guidelines for contributing to windIO.**

The windIO repository includes JSON schemas, YAML and NetCDF files that describe examples
of wind energy systems conforming to the schemas, Python code for working with the schemas
and input files, source files for web-based documentation,
and various other files that serve as infrastructure.
Changes to anything that is tracked with git in the windIO repository is considered a contribution,
and these guidelines apply.


Code of Conduct
~~~~~~~~~~~~~~~
As members of the wind energy community, we all agree that the advancement of wind
energy technologies is critical for the sustainability of our planet.
This shared goal should be reflected in our interactions with each other.
Remember that we're all on the same team despite differences in our day to day stressors and needs.

Two principles should guide our conduct:

- `Think that you might be wrong. <https://en.wikipedia.org/wiki/Cromwell%27s_rule>`_
- `Assume good faith. <https://en.wikipedia.org/wiki/Wikipedia:Assume_good_faith>`_


Contribution management
~~~~~~~~~~~~~~~~~~~~~~~
Contributions are tracked with `git <https://docs.github.com/en/get-started/start-your-journey/about-github-and-git#about-git>`_
and coordinated with `GitHub <https://docs.github.com/en/get-started/start-your-journey/about-github-and-git#about-github>`_.

In general, a version of the `git-flow <https://nvie.com/posts/a-successful-git-branching-model/>`_
model is used to navigate parallel development efforts.
Here's a brief summary:

- Day to day work happens on feature branches on the principle repository or forks. The feature
  branches may be unstable, and there's no expectation that they are complete.
  These branches should have a simple name that is indicative of the scope of the work such as
  ``feature/support_supersonic_tipspeeds``.
- The ``main`` branch absorbs completed feature branches through pull requests.
  This branch is expected to be stable and available for general use. However, breaking changes
  are allowed since the previous release.
- A tag is added to a commit on the ``main`` branch to note a released version of windIO.
  Tags typically have a version number such as ``v1.2.3``.

Pull requests
-------------
Once a set of changes is ready for review, the author should submit a pull request.
This signals to the windIO community that a change is coming, and it triggers the review
process to begin.
It is the responsibility of the pull request author to convince the reviewers that the change
is reasonable, complete and an improvement to windIO.

Some guidelines:

- The pull request description should explain the context, motivation, and justification
  for accepting the change.
- Executable code should be covered by tests.
- Data or reference models should include links to their published sources.
- The pull request's source branch can live either on the main repository or on a fork.

.. Consider this checklist as a starting point to ensuring a pull request is complete:

.. - Executable code is covered by the following tests:
..   - Test 1
..   - Test 2
.. - New components are documented in:
..   - Location 1
..   - Location 2

Reviews
-------
The review process is as critical to the success of windIO as the code contributions themselves.
The objective of code reviews is to ensure that windIO stays within its intended scope
and satisfies its requirements in a stable and sustainable manner.

Reviews should consider the following:

- Code style and formatting
- Validation: did we make the right thing?
- Verification: did we make the thing right?
- How will someone not involved in this pull request understand this
  change in two months or two years?
- How does this change impact the complexity of windIO?

.. Code progress and stability
.. ---------------------------
.. By default, windIO should be more adaptable / more conservative to change.


.. If adaptable:
.. Non-breaking changes should be evaluated for meeting scope and stability.
.. However, completeness and rigor are not critical.

.. If conservative:
.. Any change should be fully reviewed for scope, whole system impact, completeness, and rigor.


Roles, Responsibilities and Expectations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The collaborative development process involves various people with distinct roles, and 
a single person may participate as multiple roles.
In the context of windIO, the following are identified:

- **Contributor**: Adds to or modifies content in the windIO repository.
- **Reviewer**: Reviews and critiques changes by contributors from the domain perspective.
- **Maintainer**: Manages the repository by supporting the review process, managing issues,
  and generally ensuring the quality of the repository.

All roles are required to work together in the development of windIO, and
authorship of a change is given to contributors, reviewers, and maintainers.
Contributors should drive the progress of windIO, reviewers should ensure quality and
control, and maintainers should serve as a facilitators and enablers.
There is an implicit tension between these roles, and an effective development process
requires maintaining a balance.

Contributor Responsibilities
----------------------------
Contributors are responsible for communicating their intention to make a change through
a GitHub Issue or Discussion, and relevant people should be tagged directly for feedback.
After accepting feedback and updating the proposal, the contributor is responsible for
implementing the change and submitting a pull request.

It is the responsibility of the contributor to fully describe the change,
the motivation behind it, and the impact on windIO and the adjacent ecosystem.
The contributor should work with maintainers to establish a timeline for review and
incorporating feedback.
They should also keep a pull request up to date with the latest changes in the target branch.
While the maintainer will ultimately determine whether a pull request is complete, contributors
should push the process by providing information and requesting additional reviews.

**Summary: Contributors should strive to make high quality changes and create pull requests that encourage an approval from reviewers.**

Reviewer Responsibilities
-------------------------
Reviewers are responsible for providing feedback on the pull request from the perspective
of the domain included in the change.
For example, changes to a given area of the ontology should be reviewed by a domain expert
in that area who understands the contextual impacts.
Approving a change indicates agreement with the change, and it implies that the reviewer,
in addition to the contributor, is a relevant person to contact for future questions.

After being assigned to a pull request, a reviewer should coordinate with the contributor and
maintainers to establish a reasonable review timeline.

**Summary: Reviewers should strive to provide meaningful and constructive feedback that helps the contributor make quality changes and supports the objectives of the windIO project.**


Maintainer Responsibilities
---------------------------
Maintainers are responsible for ensuring that the windIO repository and processes around 
and within it continue to serve the windIO community well.
While the contributor and reviewer roles are activated by a specific pull request,
the maintainer role is always active.
Maintainers should keep a high level perspective of the project scope and intent, the
repository infrastructure, and the processes used to develop windIO.
This includes managing issues and discussions, reviewing pull requests, and ensuring that
the repository infrastructure is up to date.
Maintainers should also work with contributors and reviewers to keep the development process
moving forward.
They are responsible for ultimately merging a pull request.

While a pull request is active, maintainers should ensure the following:

- An appropriate reviewer is listed
- Conflicting works in progress are flagged
- A tentative timeline for review, design iteration, and merge is established

Otherwise, maintainers should consider the following:

- Dependencies are up to date
- Documentation sites are functioning
- Tests are running, passing, and addressing the intended targets
- Issues and discussions are engaging the relevant people
- Whether gaps or conflicts have emerged from individual development efforts

**Summary: Maintainers should steer the collaborative development process and provide reviews that support the objectives of the windIO project.**


Sequence
--------
Here's a typical sequence of events for a contribution:

0. **Identify a need**: *Contributors* identify and characterize a need for a change in windIO.
   Ideally, this need is discussed with domain experts within the windIO community through a
   GitHub Issue or Discussion.
1. **Implement a change**: *Contributors* implement the change in a feature branch.
2. **Submit a pull request**: When ready for review, *contributors* create a pull request
   to the windIO repository. A change is ready for review when it is complete, tested,
   and documented. The pull request should include the context, description and motivation for
   a description of the change.
3. **Review and Iteration**: *Reviewers* and *maintainers* provide feedback on the pull request.
   *Contributors* update the pull request to address feedback. This often occurs over multiple
   cycles, and it is rare for a pull request to be accepted without changes.
4. **Merge**: Once the pull request is approved by *reviewers* and the *contributor* signals
   that it is ready to merge, a *maintainer* does final checks and merges the pull request into
   the main branch. The change is now part of windIO.
