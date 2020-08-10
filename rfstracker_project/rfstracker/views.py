
from django.shortcuts import render,get_object_or_404, redirect
from rfstracker import models
from rfstracker import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',{})
@login_required
def sales(request):
    return render(request,'sales.html',{})

@login_required
def displaysalesdb(request):
    entries = models.Salesdb.objects.all()
    context = {'entries':entries}
    return render(request,'sales.html',context)
@login_required
def displaydetailsdb(request, pk):
    entries = models.Detailsdb.objects.filter(rfsnumber=pk)
    rfsnumber = models.Salesdb.objects.get(pk=pk)
    context = {'entries':entries,"pk":pk, "rfsnumber":rfsnumber}
    return render(request,'details.html',context)
@login_required
def addsalesdb(request):
    if request.method == "POST":
        form = forms.Salesdbform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/displaysalesdb')
        else:
            return render(request,'addsales.html',{"form":form,"invalidmsg":"invalid"})
    else:
        form = forms.Salesdbform()
        return render(request,'addsales.html',{"form":form})

@login_required
def editsalesdb(request, pk):
    item = get_object_or_404(models.Salesdb, pk=pk)

    if request.method == 'POST':
        form = forms.Salesdbform(request.POST,instance=item)
        if form.is_valid():

            form.save()
            return redirect('/displaysalesdb')
        else:
            return render(request,'editsales.html',{"form":form,"invalidmsg":"invalid"})
    else:
        form = forms.Salesdbform(instance=item)
        return render(request,'editsales.html',{"form":form})

@login_required
def deletesalesdb(request, pk):
    models.Salesdb.objects.filter(id=pk).delete()

    entries = models.Salesdb.objects.all()
    context = {'entries':entries}
    return render(request,'sales.html',context)

@login_required
def addprogress(request,pk):

    if request.method == 'POST':
        form = forms.Detailsdbform(request.POST, request.FILES)
        print("post reached")
        if form.is_valid():
            form.save()
            formdetailsqueue = form.cleaned_data['queue']
            print("form valid")
            #update queue status from subtable to main table
            models.Salesdb.objects.filter(pk=pk).update(queue=formdetailsqueue)

            #display back the subtable
            return displaydetailsdb(request,pk)
        else:
            print("form invalid")
            return render(request,'addprogress.html',{"form":form,"invalidmsg":"Form Invalid"})
    else:
        form = forms.Detailsdbform()

        # to update the rfs number into sub table automoatically mapping to corresponding rfs number clicked in the main table
        maintablerfsnumber = models.Salesdb.objects.get(pk=pk)
        form.fields['rfsnumber'].initial = maintablerfsnumber
        #form.fields['rfsnumber'].widget.attrs['readonly'] = "readonly"


        return render(request,'addprogress.html',{"form":form})
@login_required
def viewdetails(request, lpk, fpk):
    item = get_object_or_404(models.Detailsdb, pk=lpk)

    if request.method == 'POST':
        print("requested method is POST")
    else:
        print("requested method is GET")
        form = forms.Detailsdbform(instance=item)
        return render(request,'viewdetails.html',{'form':form, 'fpk':fpk})


## To be completed
@login_required
def search(request):
    if request.method == 'POST':
        form = forms.Salesdbform(request.POST)
        if form.is_valid():
            rfsnumber = form.cleaned_data['']
            item = get_object_or_404(models.Salesdb, rfsnumber=rfsnumber)
