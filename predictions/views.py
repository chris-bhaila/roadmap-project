from django.shortcuts import render


def predict(request):
    return render(request, 'placeholder.html', {'page_title': 'Career Prediction'})


def prediction_result(request):
    return render(request, 'placeholder.html', {'page_title': 'Prediction Result'})
