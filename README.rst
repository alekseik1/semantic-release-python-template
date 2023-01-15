Semantic release test project
=============================

This project aims to show how Semantic Release can be configured with Python.


Drawbacks
---------

The major problem of Semantic Release is that is cannot run if master/main branch has new commits.
This makes it complicated to release from a trunk with high commit cadence.
See `Issue <https://github.com/semantic-release/semantic-release/issues/1208>`_ for discussion.

My solution is pretty dumb:

1. Create a new branch ``release`` and keep trunk as the main target branch.
2. Push & merge PR into trunk.
3. Once you want to make a release, merge directly/open PR intro ``release`` branch, then **wait** till release pipeline is finished.
4. (Optional) Merge ``release`` branch with changelog back into ``trunk`` (to update trunk's changelog).