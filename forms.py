from django import forms

class TweetTag(forms.Form):
   tweet_tag = forms.CharField(max_length = 100)