SI 506 SAMPLE README

Your readme should include ALL of the following in order to earn full points for it.

You should include these README instructions and fill in your answers below/beside the questions.

You may submit this .txt file edited, or a .PDF if you want to format it more (just like the project plan).


* In ~2-3 sentences, what does your project do?

This project pulls data on articles from the New York Times (NYT) and Wall Street Journal (WSJ) APIs based on user provided search keyword, start date, and end date. The application pulls a maximum of 10 articles from each source (less if only so many meet the search criteria within the provided dates). It then produces a csv file designed to supply a scatter plot with date published on the x access and "emotional score" on the y axis, comparing the emotional scores over time of individual articles from the WSJ and NYT. Emotional scores are calclauted based on the words found in the abstracts of articles from each source.


* What files (by name) are included in your submission? List them all! MAKE SURE YOU INCLUDE EVERY SINGLE FILE YOUR PROGRAM NEEDS TO RUN, as well as a sample of its output file.

Main python executable: SI506_finalproject.py
negative word list: negative_words.txt
positive word list: positive_words.txt
Sample output file: output_data.csv
Readme: README.txt (this same file you're looking at)
cache file (not necessary, program creates it, although included in case it's work points): SI506finalproject_cache.json


* What Python modules must be pip installed in order to run your submission? List them ALL (e.g. including requests, requests_oauthlib... anything someone running it will need!). Note that your project must run in Python 3.

Modules required include json, requests, sys


* Explain SPECIFICALLY how to run your code. We should very easily know, after reading this:
    - What file to run (e.g. python SI506_finalproject.py). That's what we expect -- but tell us specifically, just in case.

    Run SI506_finalproject.py, please :).

    - Anything else (e.g. "There will be a prompt asking you to enter a word. You'll definitely get good data if you enter the word 'mountains', but you can try anything", or "You need to fill out secret_data.py with the Facebook key and secret" -- if you have to do something like this, you should include the FULL INSTRUCTIONS, just like we did. Not enough to say "just like PS9". Provide text or a link to tell someone exactly what to do to fill out a file they need to include.

    There will be three prompts, each will tell you what to do:
    1. Enter a search term
    2. Enter start date of query in format YYYY-MM-DD
    3. Enter end date of query in format YYYY-MM-DD

    - Anything someone should know in order to understand what's happening in your program as it runs

    The program will print some statements that confirm it has found data either online or in the cache, and how many articles it's pulled for both sources. It should be 10 articles for each sourcde

    - If your project requires secret data of YOUR OWN, and won't work with OURS (e.g. if you are analyzing data from a private group that is just yours and not ours), you must include the secret data we need in a file for us and explain that you are doing that. (We don't expect this to happen, but if it does, we still need to be able to run your program in order to grade it.)

* Where can we find all of the project technical requirements in your code? Fill in with the requirements list below.
-- NOTE: You should list (approximately) every single line on which you can find a requirement. If you have requirements written in different files, you should also specify which filename it is in! For example, ("Class definition: 26" -- if you begin a class definition on line 26 of your Python file)
It's ok to be off by a line or 2 but you do need to give us 100% of this information -- it makes grading much easier!

REQUIREMENTS LIST:
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):

Function to get & cache NYT data: line 176
Invocation of this function: line 259

Function to get & cache WSJ data: line 209
Invocation of this function: line 278

* Define at least 2 classes, each of which fulfill the listed requirements:

Article_NYT class: line 27
Article_WSJ class: line 73

* Create at least 1 instance of each class:

Create list of Article_NYT classes: line 259 (happens within the nyt_format function (this function is defined on line 129),
which is invoked in the get_nyt_data function)
Create list of WSJ classes: line 278 (happens within the wsj_format function (this function is defined on line 138)

* Invoke the methods of the classes on class instances:

Invoke the emo_score method, which itself inoves the positive_count and negative_count methods, both of which invoke the abstract_list method: lines 300, and 305

* At least one sort with a key parameter: 

sort NYT articles descending by emo score: line 265

sort WSJ articles descending by emo score: line 281

Sort

* Define at least 2 functions outside a class (list the lines where function definitions begin):

nyt_format, this format NYT articles into list of NYT_Article objects: line 129

wsj_format, this formats articles into list of WSJ_Article objects: line 138

* Invocations of functions you define:

nyt_format invoked within get_nyt_data function on line 259
wsj_format invoked within get_wsj_data finction on line 278

* Create a readable file:

output csv file created beginning line 295, ending line 305

END REQUIREMENTS LIST

* Put any citations you need below. If you borrowed code from a 506 problem set directly, or from the textbook directly, note that. If you borrowed code from a friend/classmate or worked in depth with a friend/classmate, note that. If you borrowed code from someone else's examples on a website, note that.

positive and negative words lists:

;   Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
;       Proceedings of the ACM SIGKDD International Conference on Knowledge 
;       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
;       Washington, USA, 
;   Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
;       and Comparing Opinions on the Web." Proceedings of the 14th 
;       International World Wide Web conference (WWW-2005), May 10-14, 
;       2005, Chiba, Japan.

* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of how many lines, how many columns, which headers...?

This program will create output_data.csv, a csv file that contains the necessary data to build a scatter plot that compares over time (based on the start and end date entered by the user), emotional scores of 20 New York Times and 20 Wall Street Journal Articles. You will see in that file the columns necessary to do this

-query: The search term used to query the data
-source: Article source, will be either NYT or WSJ
-title: Article title, based on API request (or cached data)
-author: Article author, based on API request (or cached data)
-published_on: the date the article was published. This field will determine the scatter plot item position on the x axi
-emo_score: the emotional score of the article, this will determine the scatter plot item's postion on the y axis
-description: the string method of the article class (either Article_NYT or Article_WSJ depending on the source). It gives a short human readable description of the article's metadata (title, author, source, published date, emotional score)



* Make sure you include a SAMPLE version of the file this project outputs (this should be in your list of submitted files above!).



* Is there anything else we need to know or that you want us to know about your project? Include that here!

Emotional scores are based on article "abstracts." For NYT articles this is the "snippet" field in their API response. For WSJ articles this is the "description" field in their API response.
