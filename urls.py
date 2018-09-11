from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name ='home.html'), name="home"),
    url(r'^tweet_by_word',TemplateView.as_view(template_name = 'tweet_by_word.html'),name="tweet_by_word_input"),
    url(r'^text_analysis',TemplateView.as_view(template_name = 'text_analysis.html'),name="text_analysis"),
    url(r'^tweets/', views.tweet_by_word, name='tweet_by_word_print'),
    url(r'^admin/', admin.site.urls),

]