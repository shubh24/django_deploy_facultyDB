from django.db import models

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
    profile = models.ForeignKey(Profile,default=lambda: Profile.objects.get(id=1))
    underGrad = models.CharField(max_length=20)
    postGrad = models.CharField(max_length=20)
    designation = models.CharField(max_length=12)
    #join_date = models.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    specializations = models.CharField(max_length=100)
    currentResearch = models.CharField(max_length=100)
    jobExperience = models.IntegerField(max_length=2)
    ResearchStudents = models.IntegerField(max_length = 3)

    def __unicode__(self):
	return self.designation

class Acads(models.Model):
    profile = models.ForeignKey(Profile,default=lambda: Profile.objects.get(id=1))
    papersPublished = models.IntegerField(max_length=4)    
    booksPublished = models.IntegerField(max_length=4)
    
    def __unicode__(self):
	return self.profile

class Papers(models.Model):
	profile = models.ForeignKey(Profile,default=lambda: Profile.objects.get(id=1))
        paperTitle = models.CharField(max_length=400)
	publication = models.CharField(max_length=30)
	publishDate = models.CharField(max_length=30)

	def __unicode__(self):
		return self.paperTitle

