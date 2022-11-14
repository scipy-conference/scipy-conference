Notes from the SciPy 2023 BoF
=============================

Notes from the Birds of a Feather session on Friday, July 15, 2022, to gather feedback for SciPy 2022 and ideas for SciPy 2023.

Keynote
-------

* Andrej Karpathy (director of artificial intelligence tesla)
* Someone from CZI/Chan Zuckerberg Biohub
* Someone who has the history of SciPy/stack
* Sarah Hooker - fairness in AI
* Joy Buolamwini
* Rachel Thomas?
* History of computing
* Historian of science or technology
* Katy Huff (Department of Energy)
* Matthew Brett
* Nadia (Eghbal) Asparouhova 
* Kyle Cranmner
    * Matthew Feickert contact
* Josh Bloom
* Joseph DeRisi, or someone from the Chan Zuckerberg Biohub. 
    * They were instrumental in the early covid testing capacity in California and the US. Learned about him in Michael Lewis' The Premonition.
* Brad Voytek at UCSD
    * Very cool neuro work, mostly in Python
    * `https://voyteklab.com/ <https://voyteklab.com/&sa=D&source=editors&ust=1668443480169558&usg=AOvVaw3DKon2dFiLg6OBvrTWkFnS>`_
    * `https://voyteklab.com/code <https://voyteklab.com/code&sa=D&source=editors&ust=1668443480169829&usg=AOvVaw0c-fdsUOPtFNAh0tmGkOCx>`_
    * and a course taught with Ashely Juavinett on Neural Data Science
    * `https://github.com/BIPN162 <https://github.com/BIPN162&sa=D&source=editors&ust=1668443480170144&usg=AOvVaw0ggki2PRR3KG2MhwjORGj3>`_
    * https://voyteklab.com/data%20science/neural-data-science/
* Olivia Guest
    * `https://oliviaguest.com/ <https://oliviaguest.com/&sa=D&source=editors&ust=1668443480170573&usg=AOvVaw0F0POPG687WHG21XZFaBwn>`_
    * has a ton of good, provocative ideas about the relationships between theory <-> models <-> code
    * `https://www.youtube.com/watch?v=67X0TpnQeO0&t=4s <https://www.youtube.com/watch?v%3D67X0TpnQeO0%26t%3D4s&sa=D&source=editors&ust=1668443480170955&usg=AOvVaw2m3dQ--nfAkjAGyeZ5ObXR>`_
    * topic editor at JOSS on comp. cog. Neuro and has been very involved with initiatives like ReScience C

Tracks and Mini-Symposia
------------------------

* Machine Learning needs to be a track, otherwise it takes over all the other tracks
* A track not in English. Spanish?
    * Live captioned/live translated. 
* Physics & Astronomy
* Social Sciences / Computational Social Science & Digital Humanities
    * Matthias Bussonier has a contact who could be chair
* Education summit (pycon) - how to teach scientific stack
* Teen Track
* Maintainers Track / Community track
    * Building your community
    * Governance
    * Packaging and sharing
* Life sciences / Neurology
* Shorter talks: 20+5 or 15+3
* BoFs and Lightning Talks all of Friday

Tutorials
---------

* Topics
    * Invite specific presenters to force balance
* Feedback
    * Machine learning in particular (GPU resource donation); cloud compute and resources
    * Binder is used heavily; should we donate to them?
    * Which tutorial is advanced/beginner? Not clear this year
        * Have a learner persona for each tutorial
* Guidance for tutorial presenters, recommendations about what is successful
* Binder driven tutorials eliminates problems
    * Reviewing is easier to do with binder as well
    * Should we "mandate" this?
    * Matthew Feickert
        * RE: using Binder, the PyHEP conferences use Binder each year. I'm the contact for PyHEP to Binder and the workflow that they have requested we useis:
        * Have a representative of your org come to the Jupyter/Binder monthly meetings and make a request
        * Have a representative of your org make the PRs to update pod allocations for the days that are needed about a day before and then remove them when they are done
        * If you can, try to monitor usage to ensure that that you aren't going to overwhelm the resources you requested
        * They don't want money but they want you to explicitly mention that you're using them and show slides

Hybrid
------

* Funneling questions through Slack levels the playing field
    * Ask in person - can clarify question or have a dialogue
    * Alternate between in person and in slack
    * Many conflicting ideas/feedback on this topic
* In-person, online, and interaction between the two
* Pre-recorded talks, played/broadcasted in a dedicated room, with presenter in-person to answer questions
    * Presenter can also respond to slack questions during the talk if the talk is pre recorded
    * First time we did virtual, we did prerecorded and elected to not do it the next year because it was very disengaging
* Not engaging to have people just sitting and watching a screen
    * Need a person or a dialogue in the room
* Virtual poster session concurrently with live poster session
    * Some posters did not get any feedback on the posters they worked hard to make
    * Hard to know where the virtual session was and where to "put" the posters
* Rethinking model
    * Neuromatch conference - distributed local meetings - watch party to go gather and watch together `xref <https://anneurai.net/2022/01/20/2046/&sa=D&source=editors&ust=1668443480176069&usg=AOvVaw1ov2uGb8lJHleKIeU4-FII>`_ (see bof-virtual-vs-hybrid)
* Would a poster session in gather town work for virtual posters?
    * Linux was terrible on gather town (crashed everytime tried to open/close a poster)

Diversity Efforts
-----------------

* Accessibility - live captioning/translation
    * Sponsor for this specifically

General Feedback
----------------

* Younger or less polished tutorials so people aren't afraid to be first time presenters
    * Example: Lightning talks in years past were created 10 min before the talk; this year a lot of them were polished so newcomers may expect to have to prepare well in advance (intimidating)
    * As a follow-up to @Matthias Bussonnier's comments about re-lowering the bar so that folks feel comfortable to create "crappy" last-minute lightning talks, perhaps offering one lightning talk session that is not recorded and posted to YouTube could help there. People might feel less pressure to create a polished talk.
* Give a talk or BoF or mini-symposia
    * Help people getting started on speaking or presenting at SciPy
* Feedback mechanism for all
    * How did you do on the tutorials; posters; BoFs etc.
    * Pass this information onto future chairs
* Historical trends should be considered (not the same people over and over)
* Badges with names on both sides
    * Github handle and twitter handle
    * Avatar as well
* Pronoun stickers that are much more visible
* Maintainers track should be able to submit to proceedings
* Mini-sprint track mid-week (can't stay through the weekend)
    * History breadcrumb - sprints used to be at the start but those leading the sprints were giving the talks/tutorials so the sprints never happened
    * Sprints moved to end of conference for this reason
* Diversity luncheon elevated to keynote not a lunch
* Just repeating the idea here of updating / maintaining the docs to help with knowledge transfer `https://github.com/scipy-conference/scipy-conference <https://github.com/scipy-conference/scipy-conference&sa=D&source=editors&ust=1668443480178429&usg=AOvVaw3780mbQ1Illc6F6IV_VjH1>`_ (this haven't been touched for 3 years)
    * Maybe this could also include
    * Calendars
    * Checklists
    * And maybe this could be a thing we do at a "SciPy 2023 kickoff sprint" in early fall
* Should we re-visit the "mini-symposia" naming convention?
    * Drop the name call it track; some cross cutting and some distinct

BoFs
----

* PyCon "open spaces" idea (throw a topic on the board and discuss)
* Mixture of both (pre-selected and open spaces)
* More BoFs submitted than what we had sessions for
    * Can you do a "grassroots" approach; even if you didn't get selected as an "official" BoF gather and meet (free rooms)

Mentorship Program
------------------

* 69 participants (virtual + in person)
* Some in person connected with virtual attendees
* Good to have some people connect at the start of the conference if they didn't know anyone coming 
* Send out a survey to gather feedback
* Mentors came back and said they had good sessions

