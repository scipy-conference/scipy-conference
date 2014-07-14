Suggested Workflow for Handling Sprints at SciPy Conference
===========================================================

:Author: Corran Webster

Here are some guidelines for the sprint workflow, based on the experiences
from SciPy 2013.  


Announcing
----------

* Some time after the conference announcement, send out a call for submissions
  for sprints.  This should point to a submission form on the website where
  anyone can submit a sprint proposal.  Sprint proposals should be brief: a
  few sentences about the project and the goals of the sprint.

* In parallel, around the time of the call for submissions, informally approach
  various major projects in the scientific python community to encourage
  participation.

* About a month later, send a reminder announcement, listing sprints which have
  already been planned.

* In the announcements, indicate that there will be a "how to sprint"
  introductory lesson during the sprints.  Approach potential teachers for this
  session well before the conference.

* In the conference schedule, ensure that there are times and locations
  indicated for an organizational meeting at the start (to determine which
  groups should use which spaces, and to announce goals) and after that the
  "how to sprint" session.  These require about 1 hour and 2 hours
  respectively.

* just before the conference, an e-mail should be sent to sprint coordinators
  asking them to be prepared to say a few words about their sprint at the
  organizational meeting (or to delegate that responsibility to someone).


Sprint Selection
----------------

Sprints should be inclusive and proposals should generally be approved.The
submission form on the website was moderated, but mainly to prevent spam.  In
the case of two sprint proposals which are very close in nature, it may be
appropriate to encourage the proposers to collaborate on a joint sprint, but
this was not an issue at the 2013 sprints.

Sprint proposals should be swiftly approved as they are proposed and appear
on the website to encourage potential attendees.  The aim is to have a
reasonable collection of sprints described on the website well before
conference registration deadlines.

There should be no deadline for proposing sprints.  Reasonable sprint proposals
should be accepted right up to the day of the sprints.


Running the Sprints
-------------------

Rooms for sprinters need to be set up with desks and power strips.  Open
floor-plan rooms are preferable to 'lecture-style' rooms, where available,
and ideally sprinters should be able to arrange furniture to facilitate
collaboration.

At the AT&T Conference Center at UT in Austin, rooms 103, 104, 107 and 108 are
ideal.  The smaller breakout rooms work well for individuals who wish to work
on their own projects, or smaller sub-groups who wish to work un-interupted.

Organization Meeting
~~~~~~~~~~~~~~~~~~~~

This should be in a large room that can hold all participants.

At the start of the first day of sprints, prepare a whiteboard with a list
of all the proposed sprints, the sprint coordinators, and space for a room
allocation.

After an introduction, the sprint co-chairs should invite sprint coordinators
to briefly describe their aims for the sprint, and perhaps how sprinters may
be able to contribute.  These descriptions should not require or use slides or
demos.  The aim is essentially for sprint coordinators to have an opportunity
to "advertise" for un-decided sprinters.

Following this, get a feel for the size of each sprint by show of hands.  This
should allow the co-chairs to start to sketch out a distribution of sprints
in the available spaces.  Several sprints can usually share a room, and
co-chairs should endeavour to ensure that groups which may have synergies are
in the same room, as much as possible.  Listen to sprint coordinator's
preferences as well.

Following this, people can start work as needed.

The location of sprints should be recorded and posted on a noticeboard
for latecomers.

"How to sprint" Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~

This should be aimed at participants who are new to contributing to open-source
projects.  You can probably assume familiarity with Python and the scientific
Python stack, but not with version control and the process of open-source
development.

The purpose of the talk is to prepare people to participate.  Topics which
should be included are:

* tools you need: Python environment, compilers, version control, project
  website/central repo
* development installation: using `setup.py develop` (and in the future,
  possibly venv) and `setup.py build_ext --inplace`
* building documentation
* running tests
* github accounts, getting and installing git
* issue trackers (particularly on github), how to report bugs, and reasonable
  expectations for responses
* the github development cycle: forking github repos, cloning a repo locally,
  branching, doing work, pushing and pulling, making a pull-request
* ettiquette and expectations

Ideally the lecture should have live demonstrations, and if students can follow
along that's even better.  The purpose is to teach skills, and that is done best
by doing.

Given the prevalence of Git and GitHub, it makes sense to focus examples on
these as a matter of practicality.

Feedback from coordinators is that having a gap between when they start
sprinting and when "newbie" sprinters join them is valuable as they have a
chance to plan and start work without having to split attention towards the
newer sprinters.

The Main Sprint Session
~~~~~~~~~~~~~~~~~~~~~~~

Beyond the initial meetings, there isn't too much that the sprint co-chairs
need to do: sprints are largely run by coordinators, and the role of the
co-chairs is to support and facilitate as needed.  Co-chairs should be the
first point of contact between coordinators and the conference committee.






