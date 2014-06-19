# TODO list:

## Implement regex flags

 - Ignore case
 - Locale
 - Multi line
 - Dot all
 - Unicode
 - Verbose



## Implement better interactive mode

You should be able to change all flags in this mode.

Somehow support multiline input in this mode. Possible solution could be to do what git does, open nano/editor and then write multiline regex and on close, read the contents and use that

Retry mode. If you for example have a minor typo in the last regex and you want to reuse it it should be possible to have the data prefilled to enable easy edit.



## Implement test code

 - Core
 - interactive mode [probably doc tests]
 - cli
 - regex works the way it shold
 - regex flags



## Travis CI integration

Add all possible versions and see where it fails.

It should be targeted for python3 only but if it supports any other older versions that is extra.
