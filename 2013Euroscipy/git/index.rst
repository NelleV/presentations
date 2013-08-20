
Create a repository
--------------------------------------------------------------------------------

In the project directory, initialize the git repository with::

  git init

This will enable git to keep track of changes in this folder, and subfolders
by creating a .git hidden folder containing the git skeleton.

Before continuing let's configure git. You will have to do this once per
computer you use::

  git config --global
  git config --global user.name "Your Name Comes Here"
  git config --global user.email you@yourdomain.com``
  git config --global core.editor vim
  git config color.ui auto

And you can check your configuration with::

  git config --list


Creating snapshots
--------------------------------------------------------------------------------

One of the main goal of version control is to save snapshots of your
directory. We call those snapshots commits. To each snapshot is associated
some metadata: the date the snapshot was taken, who took it, what files where
modified, the changes that were made on those files etc. Git will enable you
to track the changes made to the files, revert the entire project to a
previous snapshot, review changes made over time, view who modified a file.

Now that we know why we want to create a snapshot, let's see how to do this.
Right now, nothing in the project is tracked.
First let's create some directories and files in our directory.

.. code-block:: bash

   touch README

You now have a new file in the project folder. As mentionned before, git does
not track this file yet. First, you need to tell git this file exists::

  git add README


Now you can commit it::

  git commit -m "Added a README file"

At this point, you have one tracked file, and an initial commit.
Each file in the working directory can be in one of two states: tracked or
untracked. Any file you have not explicitely added at some point is untracked.
Tracked files can themselved be in different states: unmodified, modified or
staged.

.. image:: ../images/git_file_status_lifecycle.png

You can check the statuses of each file in your directory with the
command ``git status``. This command will display all untracked files, and
modified and staged files in your directory::

  touch AUTHORS
  git status

Note as the README file is not listed, while the AUTHORS file is there. Now
let's add the AUTHORS file. The AUTHORS file is now tracked, and staged::

  git add AUTHORS
  git status

``git add`` is also used to stage file. In fact, running ``git add`` on an
untracked file not only tracks it, but stages it. ``git commit`` will take a
snapshot of the staged files::

  git commit -m "Added the AUTHORS file"

And here is the second commit! Sometimes, you may want to look at the changes
you've made to a modified file::

  git diff

To look at the changes you've made in the staged files, simply use::

  git diff --cached

And to view the history of all commits::

  git log


Now, let's try to rm AUTHORS::

  rm AUTHORS CONTRIBUTORS
  git status

You can see that the ``AUTHORS`` file is in red, and marked as deleted. Yet,
running ``git add`` on this file doesn't move the change in the staging area.
To remove a file that has been tracked with git, use the ``git rm`` command.
In a similar fashion, ``git mv`` can be used to move a file.

Because to err is human, you may want to cancel some stages. Two scenarios may
occur: (1) you have staged a file you do not want to commit (2) you have made
some changes on a file you want to cancel.

First, let's assume you've staged a file you want to unstage::

  touch TODO
  git add TODO

To unstage it, run::

  git reset HEAD TODO

The syntax is ``git reset HEAD <filename>``. We will explain what HEAD is later
on.

In the second case, you've modified a file and you want to cancel the changes.
To do so, use ``git checkout <filename>``. If you run ``git status``, you can
notice git reminds you what command to use for which action.


Exercises:

  - Create a folder called GitTutorial
  - Inside it, initialize an empty git repository (``git init``)
  - Create an AUTHORS file, a TODO file and a README file.
  - Add the AUTHORS file to the staging area. (``git add``)
  - Check the status of the repository (``git status``)
  - Add the two other files to the staging area (``git add``)
  - Commit your changes (``git commit``).
  - Now rename the AUTHORS file to CONTRIBUTORS (``git mv``)
  - Add your name to the CONTRIBUTORS file.
  - Cancel the changes you've made to this file.


-----

Working with a distant repository with github
================================================================================

Up to now, we've been working locally on our computer. As researched and
computer scientist, you may want to share your work, (or better contribute to
an opensource project!). This is where github comes in handy. Github is a web
hosting plateform for git projects. Not only does it provide free git
repository for opensource projects (private ones can be purchased, or asked
for free for students and women), but it provides great tools to review code,
manage projects, release packages and publish documentation. Most of the
scientific python code **you** use are hosted on github.

Let's have a look at the interface. [DEMO]

Creating a new project on github yields a url. To use this new git repository,
we are going to associate to this url a name. To add a new remote Git
repository as a shortname you can reference easily, run ``git remote add
<shortname> <url>``::

  git remote add origin <github_url>

The <github_url> can be new referenced as origin. To check which remotes
you've added, run::

  git remote

or::

  git remote -v

Now that you've added this shortcut, you can push new changes to the remotes::

  git push origin master

And now, checkout your github repository !

You can also fetch changes from a github repository::

  git fetch origin

This will fetch all the changes of all branches from the remote (we will see
branches later one). Yet, it will not merge those changes with your work.

Sometimes, you may want to rename or remove a remote. To do so, run ``git
remote rename <old_remote_name> <new_remote_name>`` and ``git remote rm
<remote_name>``.

Branches
================================================================================

First let's try to understand what a branch is.
[See slides]

Let's now create a new branch and call it ``issue_53``. You can either use the
commands::

  git branch issue_53
  git checkout issue_53

or, a shortcut::

  git checkout -b issue_53

You can check which branch you created by running::

  git branch

The branch in green marked with an asterix is the branch you are currently
working on. Now let's add a new commit::

  vim AUTHORS
  git add AUTHORS
  git status
  git commit -m "Added a new author"

You've now created a new commit in branch ``issue_53``. You can easily go
back to the master branch by running::

  git checkout master

Checking out a branch will restore the tracked files to the state they were at
the last commit you created on the branch you are going back to. Note that if
you have uncommitted or staged changes, git will not permit to switch
branches.

To incorporate the changes of the branch ``issue_53`` into ``master``, you need
to merge ``issue_53`` in master. To do so, make sur you are in branch master
(using ``git branch``), and run the following command::

  git merge issue_53

You can use git log to check that the changes have been merged into master.
Once a branch has been merged, you can delete it::

  git branch -d issue_53

Remember how, in the previous section, we discussed how to fetch changes from
a remote repository using ``git fetch``? We also said fetching the changes did
not incorporate them into your working repository. So what does it do... Git
fetch updates a series of branch from a remote, let say ``origin``, by
creating and updating remote branches called ``origin/branch_name``.
If you wan to update your branch ``master`` with the changes you've pulled
into ``origin/master``, you need to merge ``origin/master`` onto ``master``::

  git merge origin/master

You can checkout the remote branches, but you should never (never ever
ever!!!) work in those branches.


Exercises:

  - Create a github accound.
  - Create a git project. **DO NOT ADD A README FILE, A .GITIGNORE FILE, OR
  ANYTHING THING TO THIS PROJECT THROUGH THE GITHUB INTERFACE**. This would
  create a commit and be quite annoying for the rest of the exercise.
  - Add a remote called origin to your local git repository (``git remote
  add``). Note that github tells you how to do this.
  - Push your changes to the remote (``git push``) and check your changes do
  appear on Github.
  - Now create a branch called ``fix``. Edit the README file (add a title to
  it), add it to the staging area and commit it.
  - Push this branch on the github repository:: ``git push origin fix``. This
  branch should appear in the github interface.
  - Now merge the changes back to your master branch.
