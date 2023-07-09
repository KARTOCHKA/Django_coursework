from django.shortcuts import render, redirect
from .models import Client, MailingList, Message


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        client = Client.objects.create(name=name, email=email)
        return redirect('client_list')
    return render(request, 'create_client.html')


def view_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'view_client.html', {'client': client})


def create_mailing_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        mailing_list = MailingList.objects.create(name=name)
        return redirect('mailing_list', mailing_list.id)
    return render(request, 'create_mailing_list.html')


def view_mailing_list(request, mailing_list_id):
    mailing_list = MailingList.objects.get(id=mailing_list_id)
    return render(request, 'view_mailing_list.html', {'mailing_list': mailing_list})


def view_mailing_logs(request, mailing_list_id):
    mailing_list = MailingList.objects.get(id=mailing_list_id)
    logs = mailing_list.mailinglog_set.all()
    return render(request, 'view_mailing_logs.html', {'mailing_list': mailing_list, 'logs': logs})


def send_message(request, mailing_list_id):
    if request.method == 'POST':
        subject = request.POST['subject']
        body = request.POST['body']
        mailing_list = MailingList.objects.get(id=mailing_list_id)
        message = Message.objects.create(subject=subject, body=body, mailing_list=mailing_list)
        # Code for sending the message to the mailing list
        return redirect('mailing_list', mailing_list_id)
    return render(request, 'send_message.html', {'mailing_list_id': mailing_list_id})

