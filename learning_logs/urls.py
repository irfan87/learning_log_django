from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # page that shows all topics
    path('topics/', views.topics, name='topics'),
    # page that shows a topic based on topic_id
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for edit a current entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]