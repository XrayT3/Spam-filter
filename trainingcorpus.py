import email
import os
from utils import read_classification_from_file

class TrainingCorpus:
    
    def __init__(self, email_adress):
        self.email_adress = email_adress

    def is_ham(self, email_soubor):
        truth = read_classification_from_file(str(self.email_adress + '/!truth.txt') )
        for email in truth:
            if email == email_soubor and truth[email] == 'SPAM':
                return False
            if email == email_soubor and truth[email] == 'OK':
                return True

    def is_spam(self, email_soubor):
        truth = read_classification_from_file(str(self.email_adress + '/!truth.txt') )
        for email in truth:
            if (email == email_soubor) and (truth[email] == 'SPAM'):
                return True
            if (email == email_soubor) and (truth[email] == 'OK'):
                return False

    def spams(self):
        spams = []
        fnames = os.listdir(self.email_adress)
        for fname in fnames:
            if TrainingCorpus.is_spam(self, fname):
                file= open(str(self.email_adress + '/' + fname), 'r', encoding="utf-8")
                body = file.read() 
                file.close()
                spams.append((fname, body))
        return spams

    def hams(self):
        hams = []
        fnames = os.listdir(self.email_adress)
        for fname in fnames:
            if TrainingCorpus.is_ham(self, fname):
                file= open(str(self.email_adress + '/' + fname), 'r', encoding="utf-8")
                body = file.read() 
                file.close()
                hams.append((fname, body))
        return hams

    def get_words(self, emails):
        words = []
        for email in emails:
            lines = email[1].split('\n')
            for line in lines:
                line = line.strip('')
                line = line.strip(',')
                line = line.strip('\n')
                words += line.split(' ')
        return words

    def get_words_from_email(email1):
        switch = 0
        words = []
        lines = email1.split('\n')
        for line in lines:
            # skip the first part of the letter (addressee, date and etc.)
            if 'Date:' in line:
                switch = 1
                continue
            if switch == 0:
                continue 
            line = line.strip('')
            line = line.strip(',')
            line = line.strip('\n')
            words += line.split(' ')
        return words

    def count_spams(email_adress):
        truth = read_classification_from_file(str(email_adress + '/!truth.txt'))
        count_spam = 0
        for email in truth:
            if truth[email] == 'SPAM':
                count_spam += 1
        return count_spam

    def count_emails(email_adress):
        truth = read_classification_from_file(str(email_adress + '/!truth.txt'))
        count_emails = len(truth)
        return count_emails

    def all_words(self, ham_words, spam_words):
        all_words = {}
        for word in ham_words:
            if word not in all_words:
                all_words[word] = 1
            else:
                all_words[word] += 1
        for word in spam_words:
            if word not in all_words:
                all_words[word] = 1
            else:
                all_words[word] += 1
        return all_words

    def spam_words(self, swords):
        spam_words = {}
        for word in swords:
            if word not in spam_words:
                spam_words[word] = 1
            else:
                spam_words[word] += 1
        return spam_words
