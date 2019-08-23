from django.shortcuts import render

from .models import Topic

# Create your views here.
# index view
def index(request):
    return render(request, 'learning_logs/index.html')

# topics view
def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    
    return render(request, 'learning_logs/topics.html', context)

# view single topic
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)