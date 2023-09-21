from django.shortcuts import render


def HelloView(request):
    data = {}
    if request.method == 'GET':
        data['name'] = request.GET.get('name')
        data['message'] = request.GET.get('message')

    return render(request, 'main/main.html', data)
