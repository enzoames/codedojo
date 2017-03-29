from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from models import DojoMember

# VIEWS
# Takes in a web request and returns a response (http request)

# This function returns all the data inside our database table DojoMember
def Member(request):
    member = DojoMember.objects.all()
    return render(request, 'dojoteam/dojoteam.html', {'member': member})


# We need to query down to the member we are trying to obtain. Can not return entire table of members
# def EnzoClicked(request):
#     instance = get_object_or_404(DojoMember, f_name="Enzo")
#     context = {
#         'instance': instance,
#     }
#     return render(request, 'dojoteam/enzo.html', context)

def memberClicked(request, f_name):
    print f_name
    instance = get_object_or_404(DojoMember, f_name=f_name)
    context = {
        'instance': instance,
    }
    return render(request, 'dojoteam/Enzo.html' , context)