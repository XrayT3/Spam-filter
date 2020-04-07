import os

class Corpus:

    def __init__(self, email_adress):
        self. email_adress = email_adress

    def emails(self):
        emails = []
        fnames = os.listdir(self.email_adress)
        for fname in fnames:
            if (fname[0]== '!'):
                continue
            file= open(str(self.email_adress + '/' + fname), 'r', encoding="utf-8")
            body = file.read() 
            file.close()
            emails.append((fname, body))
        return emails
