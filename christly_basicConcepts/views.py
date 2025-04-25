from django.shortcuts import render
from django.http import HttpResponse

from joblib import load
model = load("./christ_savedModel.h5")

# Create your views here.

def index(request):
    if request.method == "POST":
        sepal_length = request.POST["gtljc_sepal_length"]
        sepal_width = request.POST["gtljc_sepal_width"]
        petal_length = request.POST["gtljc_petal_length"]
        petal_width = request.POST["gtljc_petal_width"]

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        print(y_pred)

        if y_pred[0] == 0:
            y_pred = "Setosa"
        elif y_pred[0] == 1:
            y_pred = "Versicolor"
        else:
            y_pred = "Virginica"

        return render(request, template_name="christly_basicConcepts/index.html", context={
            "y_pred" : y_pred
    })

    return render(request, template_name="christly_basicConcepts/index.html", context={
        
    })
