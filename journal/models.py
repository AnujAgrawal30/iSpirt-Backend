from django.db import models

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Article(models.Model):
    name = models.CharField(max_length=200)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    content = models.TextField()
    author = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    tags = models.TextField()
    designation = models.CharField(max_length=100)
    disclosures = models.TextField()
    status_choices = ["Working Paper", "Final"]
    status_choices = [(i, i) for i in status_choices]
    status = models.CharField(max_length=50, choices=status_choices)
    peer_choices = ["Yes", "No", "Under Review"]
    peer_choices = [(i, i) for i in peer_choices]
    peer_reviewed = models.CharField(max_length=50, choices=peer_choices)
    affiliation_choices = ["Volunteer", "Fellow", "Unaffiliated"]
    affiliation_choices = [(i, i) for i in affiliation_choices]
    affiliation = models.CharField(max_length=50, choices=affiliation_choices)
    external_funding = models.BooleanField(default=False)
