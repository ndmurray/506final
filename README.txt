SI 506 SAMPLE README

Your readme should include ALL of the following in order to earn full points for it.

You should include these README instructions and fill in your answers below/beside the questions.

You may submit this .txt file edited, or a .PDF if you want to format it more (just like the project plan).


* In ~2-3 sentences, what does your project do?

This project pulls data on articles from the New York Times (NYT) and Wall Street Journal (WSJ) APIs based on user provided search keyword, start date, and end date. The application pulls a maximum of 20 articles from each source (less if only so many meet the search criteria within the provided dates). It then produces a csv file designed to supply a scatter plot with date published on the x access and "emotional score" on the y axis, comparing the emotional scores over time of individual articles from the WSJ and NYT. Emotional scores are calclauted based on the words found in the abstracts of articles from each source.

e.g. "If you fill out secret_data.py with your Facebook information as instructed below, and run the program, the project will find the most common word in your last 25 FB posts and create a CSV file of songs from a search on iTunes that comes from that word."

You should not say "Option 1" or "Option 2" -- tell us what YOUR project does, whatever that is.


* What files (by name) are included in your submission? List them all! MAKE SURE YOU INCLUDE EVERY SINGLE FILE YOUR PROGRAM NEEDS TO RUN, as well as a sample of its output file.


* What Python modules must be pip installed in order to run your submission? List them ALL (e.g. including requests, requests_oauthlib... anything someone running it will need!). Note that your project must run in Python 3.


* Explain SPECIFICALLY how to run your code. We should very easily know, after reading this:
    - What file to run (e.g. python SI506_finalproject.py). That's what we expect -- but tell us specifically, just in case.

    - Anything else (e.g. "There will be a prompt asking you to enter a word. You'll definitely get good data if you enter the word 'mountains', but you can try anything", or "You need to fill out secret_data.py with the Facebook key and secret" -- if you have to do something like this, you should include the FULL INSTRUCTIONS, just like we did. Not enough to say "just like PS9". Provide text or a link to tell someone exactly what to do to fill out a file they need to include.

    - Anything someone should know in order to understand what's happening in your program as it runs

    - If your project requires secret data of YOUR OWN, and won't work with OURS (e.g. if you are analyzing data from a private group that is just yours and not ours), you must include the secret data we need in a file for us and explain that you are doing that. (We don't expect this to happen, but if it does, we still need to be able to run your program in order to grade it.)

* Where can we find all of the project technical requirements in your code? Fill in with the requirements list below.
-- NOTE: You should list (approximately) every single line on which you can find a requirement. If you have requirements written in different files, you should also specify which filename it is in! For example, ("Class definition: 26" -- if you begin a class definition on line 26 of your Python file)
It's ok to be off by a line or 2 but you do need to give us 100% of this information -- it makes grading much easier!

REQUIREMENTS LIST:
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):
    * If you relied upon FB data and did not cache it, say so here:
* Define at least 2 classes, each of which fulfill the listed requirements:
* Create at least 1 instance of each class:
* Invoke the methods of the classes on class instances:
* At least one sort with a key parameter:
* Define at least 2 functions outside a class (list the lines where function definitions begin):
* Invocations of functions you define:
* Create a readable file:
END REQUIREMENTS LIST

* Put any citations you need below. If you borrowed code from a 506 problem set directly, or from the textbook directly, note that. If you borrowed code from a friend/classmate or worked in depth with a friend/classmate, note that. If you borrowed code from someone else's examples on a website, note that.

* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of how many lines, how many columns, which headers...?

* Make sure you include a SAMPLE version of the file this project outputs (this should be in your list of submitted files above!).

* Is there anything else we need to know or that you want us to know about your project? Include that here!
