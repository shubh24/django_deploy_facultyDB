from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forms import ArticleForm,JobForm,AcadsForm,MyForm,FunkyForm
#from forms import ModelFormWithFileField
from models import Profile,Job,Acads,Papers
from django.core.context_processors import csrf
from reportlab.pdfgen import canvas
from django.forms.formsets import formset_factory
from reportlab.lib.pagesizes import letter
from io import BytesIO
import csv
from django.db.models.loading import get_model

@login_required
def create(request, profile_id):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
	    print request.POST
            a = form.save()
            
	    jform = JobForm()
	    args = {}
	    args.update(csrf(request))
	    args['form'] = jform
	    args['profile_id'] = profile_id
	    return render_to_response('job.html', args)
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['profile_id'] = profile_id
    
    return render_to_response('create_profile.html', args)

def profiles(request):
    args = {}
    args.update(csrf(request))
    	
    args['profiles'] = Profile.objects.all()

    return render_to_response('profiles.html', args) 

def profile(request, profile_id=1):   
    rc = RequestContext(request, {'profile': Profile.objects.get(id=profile_id),'job' : Job.objects.get(id=profile_id) ,'acads' : Acads.objects.get(id=profile_id), 'papers' : Papers.objects.get(publication='ACM')})
    return render_to_response('profile.html',context_instance=rc)

@login_required
def report(request):
	model = Profile
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	writer = csv.writer(response)

	headers = []
	for field in model._meta.fields:
		headers.append(field.name)
	writer.writerow(headers)

	for obj in Profile.objects.all():
		row = []
		for field in headers:
			val = getattr(obj, field)
			if type(val) == unicode:
				val = val.encode("utf-8")
			print val,field			
			row.append(val)
		writer.writerow(row)
	return response
@login_required
def reportProf(request, profile_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()	 

    model = Profile
    
    
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
 
    pro = Profile.objects.get(id=profile_id)
    j = Job.objects.get(id=profile_id)
    a = Acads.objects.get(id=profile_id)
    pa = Papers.objects.filter()
    print pa

    line = 0	
    headers = []	
    for field in model._meta.fields:
	headers.append(field.name)

    for field in headers:
	val = getattr(pro, field)
	if field != 'id':
		p.drawString(30,800-20*line,field + ': ' + str(val))
		line += 1

    headers = []
    for field in Job._meta.fields:
	headers.append(field.name)

    for field in headers:
	val = getattr(j, field)
	if field != 'id' and field != 'profile':
		p.drawString(30,800-20*line,field + ': ' + str(val))
		line += 1

    headers = []
    for field in Acads._meta.fields:
	headers.append(field.name)
    for field in headers:
	val = getattr(a, field)
	if field != 'id' and field != 'profile':
		p.drawString(30,800-20*line,field + ': ' + str(val))
		line += 1

    headers = []
    for field in Papers._meta.fields:
	headers.append(field.name)
    for field in headers:
	for x in pa:
		val = getattr(x, field)
		if field != 'id' and field != 'profile':
			p.drawString(30,800-20*line,field + ': ' + str(val))
			line += 1

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def makePdf(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()	 

    model = Profile
    headers = []
    for field in model._meta.fields:
	headers.append(field.name)
    
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
 
    line = 0
    for obj in Profile.objects.all():
	line += 1
	string = ""
	for field in headers:
		if field == 'name' or field == 'psrn':		
			val = getattr(obj, field)
			if type(val) == unicode:
				val = val.encode("utf-8")
		
			string = string + ' ' + str(val)		
	p.drawString(30,800-50*line,string)
	

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def filters(request):
	form = MyForm()
	return render(request,'filters.html',{'form': form})

@login_required    
def generatedReport(request):
    if request.method == 'POST':
	f = MyForm(request.POST,request.FILES)
	if f.is_valid():	    
	    search = f.cleaned_data['Search']
	    sign = f.cleaned_data['Name'] 
	    response = HttpResponse(content_type='application/pdf')
	    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	    buffer = BytesIO()	 

	    model = Profile
	    headers = []
	    for field in model._meta.fields:
		headers.append(field.name)
	    
	    p = canvas.Canvas(buffer)
	    p.setLineWidth(.3)
	    p.setFont('Helvetica', 12)
	 
	    line = 0
	    for obj in Profile.objects.all():
		line += 1
		string = ""
		for field in headers:
			if field == 'name':		
				val = getattr(obj, field)
				if type(val) == unicode:
					val = val.encode("utf-8")
				if (((val <= search) and (int(sign) == 1)) or ((val == (search)) and (int(sign) == 2)) or ((val >= (search)) and (int(sign) == 3))):
					string = string + ' ' + str(val)		
		p.drawString(30,800-50*line,string)
	

	    # Close the PDF object cleanly, and we're done.
	    p.showPage()
	    p.save()

	    pdf = buffer.getvalue()
	    buffer.close()
	    response.write(pdf)
	    return response



@login_required
def job(request, profile_id):
	if request.method == 'POST':
		form = JobForm(request.POST, request.FILES)
		if form.is_valid():
		    found_user = Profile.objects.get(id=profile_id)
		    a = form.save()
		    a.profile = found_user
		    a.save()

		    aform = AcadsForm()
	     	    args = {}
		    args.update(csrf(request))		    
		    args['form'] = aform
		    args['profile_id'] = profile_id
		    return render_to_response('acads.html', args)
	else:
		form = JobForm()
		
	args = {}
	args.update(csrf(request))
	    
	args['form'] = form
	args['profile_id'] = profile_id
	return render_to_response('job.html', args)

@login_required
def acads(request, profile_id):
	if request.method == 'POST':
		form = AcadsForm(request.POST, request.FILES)
		if form.is_valid():
		    found_user = Profile.objects.get(id=profile_id)
		    a = form.save()
		    a.profile = found_user
		    numberOfForms = form.cleaned_data.get('papersPublished')
		    a.save()
		    
		    form = FunkyForm(request.POST,request.FILES)
		    FunkyFormSet = formset_factory(FunkyForm,extra=numberOfForms, max_num=numberOfForms)
		    formset = FunkyFormSet()
	     	    args = {}
		    args.update(csrf(request))		    
		    args['formset'] = formset
		    args['form'] = form
		    args['profile_id'] = profile_id
		    return render_to_response('createPapers.html', args)
	else:
		form = AcadsForm()
		
	args = {}
	args.update(csrf(request))
	    
	args['form'] = form
	args['profile_id'] = profile_id
	return render_to_response('acads.html', args)


@login_required
def createPapers(request, profile_id):
	if request.method == 'POST':
		
		FunkyFormSet = formset_factory(FunkyForm,extra=3, max_num=3)
		formset = FunkyFormSet(request.POST)		
		#form = FunkyForm(request.POST, request.FILES)
	        for f_form in formset:
			if f_form.is_valid():
			    found_user = Profile.objects.get(id=profile_id)
			    a = f_form.save()
			    a.profile = found_user
			    print a
			    a.save()
	    	return HttpResponseRedirect('/all/')
	else:
		FunkyFormSet = formset_factory(FunkyForm, extra=10, max_num=10)
		formset = FunkyFormSet()
	        form = FunkyForm()
	args = {}
	args.update(csrf(request))
	    
	args['formset'] = formset
	args['form'] = form
	args['profile_id'] = profile_id
	return render_to_response('createPapers.html', args)
