from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Example without Template render
# def index(request):
#   text = """<h1> Wow This is Great !</h1>"""
#   return HttpResponse(text)

# Example with Template render
def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def author(request):
  template = loader.get_template('mysecond.html')
  
  #passing values to view in Dictionay format
  context = {
    'firstname': 'Vijay',
    'lastname': 'Kumar',
    'gender': 'Male'
  }
  return HttpResponse(template.render(context))
  # The other syntax or way
  #return render(request, 'mysecond.html', {'firstname': "sssss"})
