======================
Conference Proceedings
======================

Overview
--------

The peer-reviewed conference proceedings aims to provide some academic rigor to
the conference, helping attendees from academia or research institutes to
attend as well as publish their software-related work.  It also captures a part
of the event in writing and provides a useful overview of prevalent ideas and
how they change over time.

Tools
-----
Papers for the proceedings are written in ReStructuredText and converted to
IEEE Computer Society format using the tools at:

https://github.com/scipy-conference/scipy_proceedings.git

This repository also provides utilities for building a full proceedings website
with index and BiBTeX citations.

Submission
----------
After accepted talks are announced, speakers are invited to submit papers to
the proceedings (submitting a paper is optional).

The proceedings is **not intended as an advertising venue**, and strong
preference is given to papers describing work done under an open license--this
should be communicated clearly to authors.

Papers are submitted as pull requests onto the appropriate branch of the
proceedings repository mentioned above (typically the branch is the current
year).  Author instructions are here:

https://github.com/scipy-conference/scipy_proceedings/blob/master/README.md

An example paper, illustrating the syntax used, is here:

https://github.com/scipy-conference/scipy_proceedings/blob/master/papers/00_vanderwalt/00_vanderwalt.rst

Review process
--------------
The proceedings review process developed over the years, starting with
traditional (blind) review, then becoming non-blind and published, and
eventually culminating in 2013 in a fully open conversation on GitHub.

Reviewers (in 2013, the programme committee was asked, but in 2014 the
proceedings chair solicited outside that group as well) leave comments
on the pull requests, and work with the authors until papers reach the
required standard for publication.  Ideally, two reviewers should sign
off on each paper.  Once the paper is ready for inclusion in the
proceedings, reviewers "sign off", giving the go-ahead to the
proceedings chairs to merge the papers.

Before, papers were assigned to reviewers, but in 2014 reviewers got
to choose which papers they wanted to review.  Where there were gaps,
the proceedings chair made individual review requests.

It is not expected of reviewers to build the papers themselves; for this
purpose a build server is available:

https://github.com/scipy-conference/procbuild

Note that the build server scans all pull requests whose titles are
prefixed with "Paper:".

Old review guidelines are here (this should be reworked for 2014 with relation
to the new PR workflow):

https://github.com/scipy-conference/scipy_proceedings/blob/master/reviews/review-template.rst

At the bottom of this document, find the 2014 instructions to
reviewers, as well as the 2013 invitation to the program committee.

Putting everything together
---------------------------
Ideally, the final proceedings should be available a month or so after the
conference.  In 2013 and 2014, we managed to have draft versions ready
on the last day of the conference, but the actual publication happened
much later.

After all PRs are merged:

1. Comment out the lines in ``publisher/_static/status.sty`` to remove the
   watermark.
2. Update ``scipy_proc.json`` with conference info, committee member names,
   sponsored students, etc.
3. After the conference, add `:video:` links to all papers.
4. ``cd publisher && make proceedings-html``

This should produce a website along with paper PDFs.

- Depends on ``recode`` and ``pdfannotextractor`` (``texlive-latex-extra``
  package).
- Due to a bug in the Debian packaging of ``pdfannotextractor``, you may have
  to execute ``pdfannotextractor --install`` to fetch the PDFBox library.

Afterwards
----------
Split out the current year's proceedings branch into a new repository under the
``scipy-conference`` organization.  This preserves the proceedings, as
well as slimming down the main repository.

::

  git checkout 20xx
  git remote add 20xx_proc git@github.com:scipy-conference/scipy_proceedings_20xx
  git push 20xx_proc master

Finally, delete the branch::

  git push origin :20xx

Technical notes
---------------
- All improvements to the toolchain should be made on the master branch and
  thereafter merged back into the current proceedings (e.g. 2015 branch).

Communications
--------------

Instructions to 2019 reviewers:

    Dear colleague,

    Thank you for volunteering to review full papers for the 2019 SciPy conference (https://www.scipy2019.scipy.org/). As the proceedings co-chairs, it is our honor to invite you to review "Paper", which can be found at URL.

    Briefly, your goal is to to help this paper reach a point where it is easily readable, understandable, and verifiable. Some papers may be here already; other may be in want of revisions. You are asked to submit an initial review to this effect by June 11th, and work with the author through June 25th, or until you feel the paper is ready for inclusion in the proceedings. More detailed instructions can be found in the README  (https://github.com/scipy-conference/scipy_proceedings#instructions-for-reviewers).

    You can find the latest PDFs of all the papers at https://procbuild.scipy.org.

    Please don't hesitate to contact us with any questions.

    Yours,

    The SciPy 2019 Proceedings Chairs
      Chris Calloway
      David Lippa
      Dillon Niederhut
      David Shupe


Instructions to 2017 reviewers::

    Dear Dillon Niederhut,

    Thank you for volunteering to review full papers for the 2017 SciPy
    conference (scipy2017.scipy.org). As the proceedings co-chairs, it is our
    honor to invite you to review the full paper submissions that we have
    received. Your expertise is of particular interest this year.

    Due to the extraordinary efforts of the Program Committee and the authors
    themselves, there are 19 proceedings submissions to review.  Since many
    hands make light work, we would be grateful for your expertise and will
    list you as a member of the proceedings review committee in the published
    proceedings. You are encouraged to review any of the submissions that seem
    interesting to you.

    You can find the latest PDFs of the papers at
    https://zibi.bids.berkeley.edu:7001 .

    If a paper is outdated, just click on its sync button. Review comments can
    be made directly on the pull request (the paper title links to the pull
    request at https://github.com/scipy-conference/scipy_proceedings/pulls).

    Reviewers are asked to work with the authors directly in the GitHub pull
    request (i.e. comment, wait for update from author, comment) until the
    paper is ready for inclusion in the proceedings.  This decision should be
    based on the technical expertise of the reviewer as well as the guidance
    found here:
    https://github.com/scipy-conference/scipy_proceedings/blob/master/review_criteria.md.
    When you deem it ready for inclusion, you can simply add a comment along
    the lines of "@proceedings, The paper is ready to be merged.".

    We would like to ask that you please complete your comprehensive review by
    June 21st. Additional communication with the author can and should continue
    during their revisions. However, a final ready/unready decision must be
    made by July 7th. We recognize this is a tight turn around, but are
    striving this year to have the proceedings available during the conference
    - we hope you can help!

    Please don't hesitate to contact us with any questions.


Instructions to 2014 reviewers::

  Dear colleagues

  Thank you very much for volunteering your time to review papers for
  the SciPy 2014 Proceedings!

  We've received 19 contributions this year, a perfect number to match
  the 19 reviewers.

  These reviews are somewhat different than the traditional ones you
  may be used to, in that we ask you to engage in a conversation with
  authors and guide them towards getting their paper accepted.

  The process is as follows:

  1) Go to https://bit.ly/scipy2014_proc and pick any two papers
  2) Click on the name of the paper to take you to the corresponding
     GitHub pull request
  3) Start a conversation by commenting on the author's paper.

  [You can also find a PDF of the paper at (1)]

  An example of a first comment could simply be "Dear @stefanv, I look
  forward to reviewing your paper."

  The final deadline (for authors) is July 5th, which is just more
  than two weeks from now.  Around that time, I will scan each pull
  request for a reviewer comment along the lines of

  "@stefanv The paper is now ready to be merged."

  If I don't see such a message, I will contact you to confirm that
  the paper should be rejected.

  Thanks again for your help; we're all excited to produce a fantastic
  2014 proceedings.

  Kind regards

  Stéfan van der Walt & James Bergstra
  on behalf of SciPy2014

  P.S. This is a bit of an experiment in "load balancing", so if you
       see that other reviewers are already active on a paper, please
       select another!

  P.P.S. It is certainly not your responsibility to do a review last
         minute, should the author only address concerns then.  If the
         author is non-responsive, there is no pressure to include the
         paper in the proceedings.

  P.P.P.S. Feel free to look at some review guidelines here for
           inspiration:

           https://github.com/scipy-conference/scipy_proceedings/blob/master/reviews/review-template.rst#specific-evaluation

Below is the 2013 invitation to members of the programme committee to review
the proceedings::

  Dear SciPy 2013 Program Committee,

  Thank you for being on the Program Committee this year! As a result of your
  efforts reviewing nearly 120 submissions, a full program for the conference
  is now available on the website and we have received a number of full papers
  to be published in the proceedings.

  There are only 15 full papers submitted and many hands make light work, so if
  you think you can manage to review at least one paper please fill in your
  name next to it as soon as possible on this google doc, so that we can keep
  track of review coverage:

  [link redacted]

  Then, once you've volunteered to review some papers, go to: https://stefan.pythonanywhere.com .

  There, you can find the latest PDF of the paper to review (if it is outdated,
  just click on "Build latest").  Comments on the review can be made directly
  on the github pull request (the paper title links to the pull request).

  Reviewers should work with the authors (i.e. comment on the pull request,
  wait for update from author, comment) until the paper is ready for inclusion
  in the proceedings. When the reviewer(s) deem it ready for inclusion, they
  can simply add a comment along the lines of "@stefanv The paper is ready to
  be merged.".

  The deadline for inclusion is June 14th, so please complete your
  communications with the author by then.

  Questions about this process should be addressed to Stéfan van der Walt
  <email> and Jarrod Millman <email>.

  Thank You,
  Katy Huff and Matt McCormick
