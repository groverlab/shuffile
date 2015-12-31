# shuffile

Randomizes the order of files in a directory.  For setting the order of class presentations without getting blamed by someone.

Motivation
----------

Every quarter that I teach a class involving student projects, there eventually comes a time when I have a folder on my computer full of PowerPoint files from the students, like this:

  * Adams.ppt
  * Baker.ppt
  * Carlos.ppt
  * Donaldson.ppt
  * ...

and the students need to present these slides to the rest of the class, and the question arises, what's the presentation order?  And I never have a good answer.  If the students have named the files after their last names, then the default order in the Finder on my Mac is alphabetical order by student last name, which seems unfair to the Andersons and Adamses of the world.  So occasionally I'd toggle the column header and use reverse alphabetical order, but the Zimmermans and Zamoras of the world object.  Once I clicked on the "File size" column header and the students presented in order of their file size from smallest to largest; this seemed more fair than alphabetical order but it meant that all the presentations with embedded movies came last, and with PowerPoint being PowerPoint, most of those movies won't play on my Mac, and the class presentations end on a bummer.

I finally decided that the only way I could set the presentation order without being blamed by someone was to set a truly random order, and I wrote this tiny Python program.

Usage
-----

Here's how you use it.  For maximum effect, run in front of class.

   `python shuffile.py directory_path`

where "directory_path" is the full path of the directory containing files to be shuffled.  The list of files is shuffled randomly (using python's [`random.shuffle`](https://docs.python.org/2/library/random.html#random.shuffle) function), and to lock-in the new order, numbers are added to the beginnings of the filenames.  So for the example shown above, the files might be shuffled and renamed

* 01Carlos.ppt
* 02Adams.ppt
* 03Donaldson.ppt
* 04Baker.ppt
* ...

Then just sort the files alphabetically (well, numerically) in Finder and you're good to go - come on down, Ms. Carlos, you're the next contestant on *The Presentation Is Right*!

Known issues
------------

* Written to work on a Mac; not tested on PC.

* Prefix number is zero-padded to two digits, so this will probably only work correctly for classes with fewer than 100 students (which happily is true of all the classes I teach).  But if you need more students, just increase the 2 in `zfill(2)` to something larger.

* This'll happily rename all the files in whatever directory you specify, so be careful not to specify the wrong directory.  It won't recurse into subdirectories though.


