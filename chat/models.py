from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Friends(models.Model):
    id1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='first')
    id2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='second')

class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='receiver')
    msg = models.CharField(max_length=300)
    sent_at = models.DateTimeField(auto_now_add=True)

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='senderReq')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='receiverReq')
