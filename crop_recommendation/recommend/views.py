from django.shortcuts import render
import pickle
import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import OneHotEncoder

# def recommend_crop(request):
#     if request.method == 'POST':
#         # Fetch the input data from the form
#         district = request.POST['district']
#         soil_color = request.POST['soil_color']
#         nitrogen = float(request.POST['nitrogen'])
#         phosphorus = float(request.POST['phosphorus'])
#         potassium = float(request.POST['potassium'])
#         ph = float(request.POST['ph'])
#         rainfall = float(request.POST['rainfall'])
#         temperature = float(request.POST['temperature'])

#         # Load model and encoder
#         try:
#             with open('crop_recommendation_model.pkl', 'rb') as file:
#                 model_data = pickle.load(file)
#             model_crop = model_data['model']
#             encoder = model_data['encoder']
#         except FileNotFoundError:
#             return render(request, 'recommend/index.html', {'error': 'Model file not found.'})

#         # Prepare the input data in the same structure as the training data
#         input_data = pd.DataFrame(
#             [[nitrogen, phosphorus, potassium, ph, rainfall, temperature, district, soil_color]],
#             columns=['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature', 'District_Name', 'Soil_color']
#         )

#         # Perform OneHotEncoding for categorical features
#         input_data_encoded = encoder.transform(input_data[['District_Name', 'Soil_color']])

#         # Predict the crop using the trained model
#         predicted_crop = model_crop.predict(input_data_encoded)
        
#         # Get recommended fertilizer
#         recommended_fertilizer = P1[P1['Crop'] == predicted_crop[0]]['Fertilizer'].values[0]

#         # Pass recommendation to the results page
#         return render(request, 'recommend/results.html', {
#             'crop': predicted_crop[0],
#             'fertilizer': recommended_fertilizer
#         })
    
#     # If the request is GET, show the form again
#     return render(request, 'recommend/index.html')
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def recommend_crop(request):
    # Load the data (P1 should be a DataFrame, replace with your actual data loading method)
    P1 = pd.read_csv('crop_recommendation.csv')  # Adjust the path to your dataset
    
    if request.method == 'POST':
        # Fetch the input data from the form
        district = request.POST['district']
        soil_color = request.POST['soil_color']
        nitrogen = float(request.POST['nitrogen'])
        phosphorus = float(request.POST['phosphorus'])
        potassium = float(request.POST['potassium'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])
        temperature = float(request.POST['temperature'])

        # Load model and encoder
        try:
            with open('crop_recommendation_model.pkl', 'rb') as file:
                model_data = pickle.load(file)
            model_crop = model_data['model']
            encoder = model_data['encoder']
        except FileNotFoundError:
            return render(request, 'recommend/index.html', {'error': 'Model file not found.'})

        # Prepare the input data in the same structure as the training data
        input_data = pd.DataFrame(
            [[nitrogen, phosphorus, potassium, ph, rainfall, temperature, district, soil_color]],
            columns=['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature', 'District_Name', 'Soil_color']
        )

        # Perform OneHotEncoding for categorical features
        input_data_encoded = encoder.transform(input_data[['District_Name', 'Soil_color']])

        # Predict the crop using the trained model
        predicted_crop = model_crop.predict(input_data_encoded)
        
        # Get recommended fertilizer
        recommended_fertilizer = P1[P1['Crop'] == predicted_crop[0]]['Fertilizer'].values[0]

        # Pass recommendation to the results page
        return render(request, 'recommend/results.html', {
            'crop': predicted_crop[0],
            'fertilizer': recommended_fertilizer
        })
    
    # If the request is GET, show the form again
    return render(request, 'recommend/index.html')
