from django.http import HttpResponse
def html(request):
    s='''
    <html>
        <head>
        </head>
        <body>
        test
        </body>
    
    </html>
    
    
    '''
    return HttpResponse(s)