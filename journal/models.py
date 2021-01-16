from django.db import models

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField(blank=True)
    content = models.TextField()
    author = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    tags = models.TextField(blank=True)
    designation = models.CharField(max_length=100, blank=True)
    disclosures = models.TextField(blank=True)
    content_choices = ["HTML", "markdown"]
    content_choices = [(i, i) for i in content_choices]
    content_type = models.CharField(max_length=50, choices=content_choices)
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

    def __str__(self):
        return self.title
