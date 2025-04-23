from django.db import models

class Comment(models.Model):
    text = models.TextField()  # Store the comment text
    sentiment = models.CharField(max_length=10)  # Either 'good' or 'bad'
    created_at = models.DateTimeField(auto_now_add=True)  # Store the timestamp

    def __str__(self):
        return f"{self.text} ({self.sentiment})"
