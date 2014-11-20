from django.shortcuts import render_to_response


def sample_html(request):
    return render_to_response('home.html')