Suggested workflow for handling tutorials in SciPy conference
=============================================================

:Author: Francesc Alted
:Author: Dharhas Potina

Here are some guidelines for the tutorials workflow that we followed for
SciPy 2013.  Here you will find not only the tasks that we have done,
but also notes, suggestions and caveats for not replicating errors in
future releases of the conference.

Please see `manual/calendar.rst` for the actual dates when all the
actions in this workflow happened.


Announcing and inviting
-----------------------

* Conference announcement

* Call for submissions announcement.  This year, 3 different tracks
  (introductory, intermediate and advanced) were scheduled, and we
  decided to have 4 slots of 4 hours each per track.  See the details in
  `mailings/tutorials_announcement.rst`

* A couple of weeks later, send a reminder for the submissions.

* Besides the public announcements, we did send private invitations
  for a number of respected people in the community, and specially those
  with a reputation of being good teachers.

  Some invited people said that they were going to be busy, but
  generally they suggested good replacements.  See
  `http://redmine.scipy.org/issues/8` for the details of some of the
  invited people.

* After the deadline is over, we extended it for one additional week and
  sent a last public requirement for submissions.


Tutorial selection process
--------------------------

This includes some of the most critical tasks for the tutorial
organization, so take your time to understand it for ensuring an smooth
selection process.

* After the last deadline, the tutorial co-chairs should carefully study
  the proposals and, depending on the requirements and 'hot topics' for
  the conference, select the candidates that are best suited.  For the
  selection it is important that you do some research about the quality
  of the tutors as teachers, as this is a very important parameter for
  increasing the quality of the tutorial tracks.

* Take notes about the submissions because these are going to be
  important, specially for providing feedback in non-acceptance mails.
  In 2013 we had almost a 3:1 submission ratio, so better be ready for
  justifying the rejections, because you are going to do lots of them.
  This year we did not provided this feedback, and some submitters got
  very disappointed.

* For doing the preselection, it is important to get in touch with the
  general conference co-chairs, as they have a broader vision of the
  conference, and also past conferences, so they can provide a very nice
  insight on different aspects of the selection.

* Once the preselection is complete, send a mail to the selected tutors
  and ask for confirmation.  Be patient and wait until everybody
  confirmed.  This year we had a case that took several days to confirm.
  In this case it helps sending a last call and requiring him to confirm
  in less than 24 hours (this probably helps people waiting for company
  management approval).  He confirmed on-time.

* *Important*: Once the list of tutorials is confirmed and prior to
   making it public, *please please please*, send a non-acceptance
   message for non-selected submitters.  Here are the thoughts of
   Jonathan Rocher on how to write such a message:

    """
    Indeed, let's try to find a good balance between helping people
    understand if/how they can improve their submission in the future
    and not have to enter in a long argument to explain decisions that
    can just be topic-based.

    We could imagine storing in the manual a generic email explaining
    that there were many many more submissions than available slots and
    that, the selections were made in a large part based on subjects
    that best fit this year's themes for the conference as well as 2
    additional criteria:

    - the potential audience for the proposed topic
    - the coverage of the topic in past editions.

    We should add that even though their tutorial wasn't selected this
    year, they are encouraged to submit it again next year. <OPTIONAL
    ADDITIONAL COMMENT TO HELP THEM IMPROVE THEIR SUBMISSION: STRENGTHEN
    PART ??, PROVIDE MORE/BETTER EXERCISES, EMBED THEIR TOPIC IN A
    LARGER CONTEXT TO WIDEN THE POTENTIAL AUDIENCE, ADD MORE MATERIAL
    DEMONSTRATING MASTERY OF THE SUBMITTED TOPIC.>

    That means that when tutorials are reviewed, reviewers should be
    asked to provide such additional comment(s). Unless the submission
    was perfect, in which case we could say something like: "Your
    submission was found excellent, and should just be submitted again
    in the future".
    """

    [TBD: I think we should produce something concrete based on these
    guidelines]

* *After* the messages for rejection are sent, the list can be made
  public.  Do the proper announcements for this.

* It is important that chairs would not hurry up too much in this stage,
  because the selection is one of the most critical parts of the
  process.  Take your time for this, and our experience is that 2-3
  weeks for tackling the complete selections process would be fine.


Post-selection tasks
--------------------

[This section is in the works...]

Write up more detailed instructions for the actual event. Points to
remember:

* Have folks submit test scripts that check whether you have all the
  packages required.

* Encourage folks not to use development versions, have versions
  finalized before conference starts. This cause lots of issues last
  year.

* No helping audience install stuff during tutorial. This caused lots of
  delays in some tutorials last year. Maybe have a pre-tutorial install
  time?


.. Local Variables:
.. mode: rst
.. coding: utf-8
.. fill-column: 72
.. End:
