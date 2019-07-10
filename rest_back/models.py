from django.db import models
import random
import string

# Create your models here.
class BoardList(models.Model):
    tag = models.CharField(primary_key=True, max_length=8, default='Auto set')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.tag = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        super(BoardList, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{} ~ {}".format(self.tag, self.title)
