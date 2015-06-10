from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from resources.serializers import UserSerializer, GroupSerializer


# Create your views here.
def resourcedef(request):
    context = RequestContext(request)
    return render_to_response('resource-def.html', {}, context)

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {}, context)


#Django REST API classes
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer