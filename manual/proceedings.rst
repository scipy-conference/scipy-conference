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
the proceedings (this is optional).

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

Reviewers (in 2013, the programme committee was asked, but wider solicitation
will probably be necessary) leave comments on the pull requests, and work with
the authors until papers reach the required standard for publication.  Ideally,
two reviewers should sign off on each paper.  Once the paper is ready for
inclusion in the proceedings, reviewers "sign off", giving the go-ahead to the
proceedings chairs to merge the papers.

It is not expected of reviewers to build the papers themselves; for this
purpose a build server is available, currently hosted at

http://stefan.pythonanywhere.com

with source code at

https://github.com/scipy-conference/procbuild

Old review guidelines are here (this should be reworked for 2014 with relation
to the new PR workflow):

https://github.com/scipy-conference/scipy_proceedings/blob/master/reviews/review-template.rst

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
  in the proceedings. When the reveiwer(s) deem it ready for inclusion, they
  can simply add a comment along the lines of "@stefanv The paper is ready to
  be merged.".

  The deadline for inclusion is June 14th, so please complete your
  communications with the author by then.

  Questions about this process should be addressed to Stéfan van der Walt
  <email> and Jarrod Millman <email>.

  Thank You,
  Katy Huff and Matt McCormick


Putting everything together
---------------------------
Ideally, the final proceedings should be available the week following the
conference.  In 2013, we managed to have a draft version ready on the last day.

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

Technical notes
---------------
- All improvements to the toolchain should be made on the master branch and
  thereafter merged back into the current proceedings (e.g. 2013 branch).
