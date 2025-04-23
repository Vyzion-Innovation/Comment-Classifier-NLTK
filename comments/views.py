from django.shortcuts import render, redirect
from .models import Comment
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def comment_view(request):
    """Handles comment submission and classification."""
    if request.method == "POST":
        comment_text = request.POST.get("comment", "")
        if comment_text:
            sentiment_score = sia.polarity_scores(comment_text)["compound"]
            sentiment = "good" if sentiment_score >= 0 else "bad"
            Comment.objects.create(text=comment_text, sentiment=sentiment)
        return redirect("comment_form")

    # Fetch comments from DB
    good_comments = Comment.objects.filter(sentiment="good")
    bad_comments = Comment.objects.filter(sentiment="bad")

    return render(request, "comments/comment_form.html", {
        "good_comments": good_comments,
        "bad_comments": bad_comments,
    })
