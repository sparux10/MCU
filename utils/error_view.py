from django.http import JsonResponse

def handler404(request,exeception):
    message = ('Oops! Path no found')
    response = JsonResponse(data={'error': message})
    response.status_code = 404
    return response