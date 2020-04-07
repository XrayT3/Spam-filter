# Spam-filter
Program filters emails and can learning on the other emails

File `utils.py` gets address of file with information which emails are spam and which are not.  
Format of this file: `name OK` or `name SPAM`. Every email on the own line.  
Result of `utils.py` is dictionary, where key is name of email and value is `OK` or `SPAM`

File `corpus.py` gets directory of emails and return array of tuples.  
Tuples have name of email and his body. Example (name, body).

File `trainingcorpus.py` implements learning function. Can count spam/ham emails, count bad and good words. It help in the future to make decision, bad or good email.

Main file is `filter.py`.  
Function `train` can learning, but program can work without this.
Function `test` gets directory of emails and make file `prediction.txt` with result.
