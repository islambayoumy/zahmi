from django.shortcuts import render, HttpResponseRedirect, redirect


def events_list(request):
    return render(request, 'website/events.html')

def event_details(request, event_id):
    args = {'event': event_id}
    return render(request, 'website/event-details.html', args)

