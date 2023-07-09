from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class MailingList(models.Model):
    name = models.CharField(max_length=100)
    clients = models.ManyToManyField(Client, related_name='mailing_lists')


class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)


class MailingLog(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
