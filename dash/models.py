from django.db import models
from django import forms

class Profile(models.Model):
    psrn = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=40)
    fax = models.CharField(max_length=12)
    biodata = models.FileField(upload_to = '.')

    def __unicode__(self):
    	return self.psrn

class Job(models.Model):
    psrn = models.CharField(max_length=20)
    underGrad = models.CharField(max_length=20)
    postGrad = models.CharField(max_length=20)
    designation = models.CharField(max_length=12)
    specializations = models.CharField(max_length=100)
    currentResearch = models.CharField(max_length=100)
    jobExperience = models.IntegerField(max_length=2)
    ResearchStudents = models.IntegerField(max_length = 3)

    def __unicode__(self):
    	return self.psrn

class Acads(models.Model):
    psrn = models.CharField(max_length=20)
    papersPublished = models.IntegerField(max_length=4)
    
    def __unicode__(self):
    	return self.psrn

class Papers(models.Model):
    psrn = models.CharField(max_length=20)
    paperTitle = models.CharField(max_length=400)
    co_author = models.CharField(max_length=30)
    conference = models.CharField(max_length=30)
    publication = models.CharField(max_length=30)
    sjr = models.CharField(max_length=30)    
    volume = models.CharField(max_length=30)
    page = 	models.CharField(max_length=6)
    publishDate = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.psrn

class Books_Count(models.Model):
    psrn = models.CharField(max_length=20)
    booksPublished = models.IntegerField(max_length=4)
    
    def __unicode__(self):
    	return self.psrn

    
class Books(models.Model):
    psrn = models.CharField(max_length=20)
    title = models.CharField(max_length=400)
    co_author = models.CharField(max_length=30)
    publication = models.CharField(max_length=30)
    publishDate = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.psrn


class Awards(models.Model):
    psrn = models.CharField(max_length=20)
    award = models.CharField(max_length=400)
    recognition = models.CharField(max_length=30)
    organisation = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.psrn

class Course_Count(models.Model):
    psrn = models.CharField(max_length=20)
    coursesTaken = models.IntegerField(max_length=4)
    
    def __unicode__(self):
    	return self.psrn


class Course(models.Model):
    psrn = models.CharField(max_length=20)
    course = models.CharField(max_length=400)
    organisation = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.psrn

class ResearchAgency_Count(models.Model):
    psrn = models.CharField(max_length=20)
    grants = models.IntegerField(max_length=4)
    
    def __unicode__(self):
    	return self.psrn

class ResearchAgency(models.Model):
    psrn = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    organisation = models.CharField(max_length=30)
    supervisor = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

    def __unicode__(self):
        return self.psrn

