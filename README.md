# Spam-filter
Program filters emails and can learn on other emails

File `utils.py` gets address of the file with information about which email is spam and which is not.  
Format of this file: `name OK` or `name SPAM`. Every email is on new line.  
Result of `utils.py` is dictionary, where key is the name of the email and the value is `OK` or `SPAM`

File `corpus.py` gets directory of emails and returns array of tuples.  
Tuples contain name of the email and its body. Example (name, body).

File `trainingcorpus.py` implements learning function. The function can count spam/ham emails, count bad and good words. It helps to determine later whether an email is good or bad.

Main file is `filter.py`.  
Function `train` can learn, but the program can work without it.
Function `test` gets directory of emails and creates file `prediction.txt` with the result.
