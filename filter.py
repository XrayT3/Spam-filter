from corpus import Corpus
from trainingcorpus import TrainingCorpus

all_words = {}
spam_words = {}
probability_spam = 0
count_spams = 0
count_emails = 0

class MyFilter:

    def train(self, email_adress):
        global all_words, spam_words, probability_spam, count_spams, count_emails
        hemails_with_body = TrainingCorpus(email_adress).hams()
        semails_with_body = TrainingCorpus(email_adress).spams()
        hwords = TrainingCorpus(email_adress).get_words(hemails_with_body)
        swords = TrainingCorpus(email_adress).get_words(semails_with_body)
        all_words = TrainingCorpus(email_adress).all_words(hwords, swords) # all words with their count
        spam_words = TrainingCorpus(email_adress).spam_words(swords) # spam words with their count
        count_spams = TrainingCorpus.count_spams(email_adress) # count of all spam's emails
        count_emails = TrainingCorpus.count_emails(email_adress) # count of all emails
        probability_spam = count_spams / count_emails # probability that email is spam
        pass

    def test(self, email_adress):
        global all_words, spam_words, probability_spam, count_spams, count_emails
        # part without train
        if probability_spam == 0:
            html_words = ['<html>', '<p>', '</a>', '<br>', '<head>', '<meta>', '<title>', '<body>']
            fnames_with_body = Corpus(email_adress).emails()
            f = open(str(email_adress + '/!prediction.txt'), 'w', encoding="utf-8")
            for fname in fnames_with_body:
                for word in html_words:
                    if word in fname[1]: # if word there are in email's body -> It's SPAM!
                        f.write(str(fname[0] + ' SPAM\n'))
                        break
                    f.write(str(fname[0] + ' OK\n')) # Else it's probably ham =\
            f.close()
        # part with train
        else:
            fnames_with_body = Corpus(email_adress).emails()
            f = open(str(email_adress + '/!prediction.txt'), 'w', encoding="utf-8")
            for fname in fnames_with_body:
                email_words = TrainingCorpus.get_words_from_email(fname[1])
                probability_spam_words = []
                for word in email_words:
                    # skip empty words and about know nothing
                    if (word not in all_words) or (word == ''):
                        continue
                    if word not in spam_words:
                        probability_spam_word = 0
                    if word in spam_words:
                        # Bayes' theorem. What is the probability that email is spam, if it has this word
                        probability_spam_word = ( spam_words[word]/count_spams * probability_spam) / (all_words[word]/count_emails)
                    probability_spam_words.append(probability_spam_word)
                # Final probability that email is spam
                probability_spam_email = sum(probability_spam_words)/len(probability_spam_words) *100
                if probability_spam_email > 70:
                    f.write(str(fname[0] + ' SPAM\n'))
                else:
                    f.write(str(fname[0] + ' OK\n'))
            f.close()
