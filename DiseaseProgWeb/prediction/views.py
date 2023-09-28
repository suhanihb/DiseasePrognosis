from django.shortcuts import render
from .models import model  

def home(request):
    return render(request, 'home.html')

def symptom_input(request):
    if request.method == 'POST':
        # Handle form submission
        symptoms = request.POST.getlist('symptoms')
        
        # Use your trained model for predictions
        diagnosis = model.predict(symptoms)  # Adjust this line based on your model input format
        
        # Pass the diagnosis to the template
        return render(request, 'diagnosis.html', {'diagnosis': diagnosis})
    else:
        # Display the symptom input form
        return render(request, 'symptom_input.html')

def diagnosis(request):
    return render(request, 'diagnosis.html')
