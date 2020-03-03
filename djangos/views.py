from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    output = '<html>'
    output += '  <head>'
    output += '    <title>Django Projects by Yashbeer</title>'
    output += '  </head>'
    output += '  <body>'
    output += '  <center><h1>Projects by Yashbeer</h1></center>'
    output += '  <center><a href="/api/movies/">Movie Rating by Fynd</a></center>'
    output += '  </body>'
    output += '</html>'
    return HttpResponse(output)