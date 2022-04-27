from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chat.models import Thread

# Create your views here.


@login_required(login_url="/account/loginform")
def chatPage(request):
    threads = (
        Thread.objects.byUser(user=request.user)
        .prefetch_related("chatmessage_thread")
        .order_by("timestamp")
    )
    context = {"Threads": threads}

    return render(request, "chat/chat.html", context)