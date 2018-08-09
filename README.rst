semanticdiff
============

semanticdiff is a library for making diffs out of human language text, useful
when you want to make a diff that should be shown to humans, such as diffing
any form of written document.

It uses Google's diff_match_patch library to make somewhat semantically aware
diffs of text, and combines this with tools to help you with diffing of text
that has HTML or XML type formatting, used for example by xmldiff.

semanticdiff aims to have 100% test coverage, and the initial releases will
also run on Python 2.7, but this may change soon, Python 3 is the main target.


Quick usage
-----------

If you diff human language text with Pythons standard library ``difflib`` you
often get diffs that aren't useful::

  >>> import difflib
  >>> sm = difflib.SequenceMatcher()
  >>> old = "This is sample text"
  >>> new = "Those are samples boxes"
  >>> sm.set_seqs()
  >>> sm.get_opcodes()
  [('equal', 0, 2, 0, 2),
   ('replace', 2, 3, 2, 3),
   ('equal', 3, 4, 3, 4),
   ('insert', 4, 4, 4, 5),
   ('equal', 4, 5, 5, 6),
   ('replace', 5, 7, 6, 9),
   ('equal', 7, 14, 9, 16),
   ('insert', 14, 14, 16, 17),
   ('equal', 14, 15, 17, 18),
   ('replace', 15, 16, 18, 21),
   ('equal', 16, 17, 21, 22),
   ('replace', 17, 19, 22, 23)]

This is a list of very small changes, many of them being only one character
long. Let's print this out so it's easier to see, there is a handy function
for that, mostly usable for debugging.

    >>> import semanticdiff
    >>> semanticdiff.print_diff(sm.get_opcodes())
    = Th
    / i/o
    = s
    + e
    =
    / is/are
    =  sample
    + s
    =
    / t/box
    = e
    / xt/s

What we want is a more reasonable diff that changes words, not just a few
characters here and there:

  >>> from semanticdiff import diff
  >>> old = "This is sample text"
  >>> new = "Those are samples boxes"
  >>> diffs = semanticdiff.diff_text(old, new)
  >>> semanticdiff.print_diff(diffs)
  = Th
  - is is sample text
  + ose are samples boxes'

There is also support for HTML and XML

  >>> from semanticdiff import diff, patch, prepare, unprepare
  >>> old = prepare(u'This   is \nformatted text ')
  >>> old
  u'This is formatted text'
  >>> new = prepare(u'This is  \n<b>formatted</b> text')
  >>> new
  u'This is \U000f0000 text'
  >>> diff = diff(old, new)
  >>> diff
  [Delete(8, 17, 8, 8), Insert(8, 8, 8, 9)]
  >>> result = patch(old, diff)
  >>> result == new
  True
  >>> unprepare(result)
  u'This is \U000f0000 text'
