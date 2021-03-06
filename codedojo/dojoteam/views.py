from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from models import DojoMember

# VIEWS
# Takes in a web request and returns a response (http request)

# This function sends information of table DojoMember to the dojoteam.html so it can be displayed
def Member(request):
    member = DojoMember.objects.all()
    return render(request, 'dojoteam/dojoteam.html', {'member': member})


# This method gets called when a name is clicked in /dojoteam, it opens the members personal page
def memberClicked(request, f_name):
    print f_name
    instance = get_object_or_404(DojoMember, f_name=f_name)
    context = {
        'instance': instance,
    }
    return render(request, 'dojoteam/{}.html'.format(f_name), context)