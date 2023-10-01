from django.shortcuts import render
from .models import model
import numpy as np

def home(request):
    return render(request, 'home.html')

def symptom_input(request):
    symptoms = ['Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering',
                'Chills', 'Joint Pain', 'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Muscle Wasting',
                'Vomiting', 'Burning Micturition', 'Spotting Urination', 'Fatigue', 'Weight Gain',
                'Anxiety', 'Cold Hands And Feets', 'Mood Swings', 'Weight Loss', 'Restlessness',
                'Lethargy', 'Patches In Throat', 'Irregular Sugar Level', 'Cough', 'High Fever',
                'Sunken Eyes', 'Breathlessness', 'Sweating', 'Dehydration', 'Indigestion', 'Headache',
                'Yellowish Skin', 'Dark Urine', 'Nausea', 'Loss Of Appetite', 'Pain Behind The Eyes',
                'Back Pain', 'Constipation', 'Abdominal Pain', 'Diarrhoea', 'Mild Fever', 'Yellow Urine',
                'Yellowing Of Eyes', 'Acute Liver Failure', 'Fluid Overload', 'Swelling Of Stomach',
                'Swelled Lymph Nodes', 'Malaise', 'Blurred And Distorted Vision', 'Phlegm',
                'Throat Irritation', 'Redness Of Eyes', 'Sinus Pressure', 'Runny Nose', 'Congestion',
                'Chest Pain', 'Weakness In Limbs', 'Fast Heart Rate', 'Pain During Bowel Movements',
                'Pain In Anal Region', 'Bloody Stool', 'Irritation In Anus', 'Neck Pain', 'Dizziness',
                'Cramps', 'Bruising', 'Obesity', 'Swollen Legs', 'Swollen Blood Vessels',
                'Puffy Face And Eyes', 'Enlarged Thyroid', 'Brittle Nails', 'Swollen Extremeties',
                'Excessive Hunger', 'Extra Marital Contacts', 'Drying And Tingling Lips',
                'Slurred Speech', 'Knee Pain', 'Hip Joint Pain', 'Muscle Weakness', 'Stiff Neck',
                'Swelling Joints', 'Movement Stiffness', 'Spinning Movements', 'Loss Of Balance',
                'Unsteadiness', 'Weakness Of One Body Side', 'Loss Of Smell', 'Bladder Discomfort',
                'Foul Smell Of Urine', 'Continuous Feel Of Urine', 'Passage Of Gases', 'Internal Itching',
                'Toxic Look (Typhos)', 'Depression', 'Irritability', 'Muscle Pain', 'Altered Sensorium',
                'Red Spots Over Body', 'Belly Pain', 'Abnormal Menstruation', 'Dischromic  Patches',
                'Watering From Eyes', 'Increased Appetite', 'Polyuria', 'Family History', 'Mucoid Sputum',
                'Rusty Sputum', 'Lack Of Concentration', 'Visual Disturbances', 'Receiving Blood Transfusion',
                'Receiving Unsterile Injections', 'Coma', 'Stomach Bleeding', 'Distention Of Abdomen',
                'History Of Alcohol Consumption', 'Fluid Overload', 'Blood In Sputum', 'Prominent Veins On Calf',
                'Palpitations', 'Painful Walking', 'Pus Filled Pimples', 'Blackheads', 'Scurring',
                'Skin Peeling', 'Silver Like Dusting', 'Small Dents In Nails', 'Inflammatory Nails', 'Blister',
                'Red Sore Around Nose', 'Yellow Crust Ooze']
    if request.method == 'POST':
        selected_symptoms = request.POST.getlist('symptoms')
        binary_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
        binary_vector_2d = np.array(binary_vector).reshape(1, -1)
        diagnosis = model.predict(binary_vector_2d)
        return render(request, 'diagnosis.html', {'diagnosis': diagnosis[0]})
    else:
        return render(request, 'symptom_input.html', {'symptoms': symptoms})