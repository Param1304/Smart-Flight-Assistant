# from django.shortcuts import render
# from django.http import JsonResponse 
# from django.views.decorators.csrf import csrf_exempt
# import json, os 
# import yaml
# from .models import FlightDelayPrediction
# import pandas as pd
# import plotly.express as px
# from plotly.offline import plot
# import warnings

# # Suppress FutureWarning from pandas for Plotly groupby operations
# warnings.filterwarnings("ignore", category=FutureWarning, message=".*get_group.*")

# # Load the dataset once at server startup
# try:
#     df = pd.read_csv(r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\flights_sample_3m.csv")
#     print("Dataset loaded successfully. Unique airlines:", df['AIRLINE'].unique())
# except Exception as e:
#     print(f"Error loading dataset: {e}")
#     df = pd.DataFrame()  # Fallback to empty DataFrame if loading fails

# def home(request):
#     return render(request, 'home.html')

# import joblib, torch
# from pytorch_tabular import TabularModel
# import pandas as pd 
# from django.shortcuts import render 
# from django.http import JsonResponse
# def load_cpu(file_path):
#     with open(file_path, 'rb') as f:
#         return torch.load(f, map_location=torch.device('cpu'))
# encoder = joblib.load(r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\flight_cat_encoder.pkl")
# model_dir = r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\ft_transformer_model"
# tabular_model = TabularModel.load_model(model_dir)
# cat_cols = ['Airline', 'Origin', 'Dest']
# cont_cols = ['DayOfWeek', 'Month', 'HOUR', 'IS_WEEKEND', 'Year', 'DayOfMonth']
# all_cols = cat_cols + cont_cols

# def predict_delay(inputs):
#     df = pd.DataFrame([inputs])
#     preds = tabular_model.predict(df)
#     prediction_value = preds.iloc[0, 0]
#     return prediction_value

# @csrf_exempt
# def delay_predictor(request):
#     if request.method == 'POST':
#         try:
#             inputs = {
#                 "Airline": request.POST.get('airline'),
#                 "Origin": request.POST.get('origin'),
#                 "Dest": request.POST.get('dest'),
#                 "Month": int(request.POST.get('month')),
#                 "HOUR": int(request.POST.get('hour')),
#                 "IS_WEEKEND": int(request.POST.get('is_weekend')),
#                 "DayOfMonth": int(request.POST.get('day_of_month')),
#                 "DayOfWeek": int(request.POST.get('day_of_week')),
#             }
#             prediction = predict_delay(inputs)
#             FlightDelayPrediction.objects.create(
#                 airline=inputs["Airline"],
#                 origin=inputs["Origin"],
#                 destination=inputs["Dest"],
#                 month=inputs["Month"],
#                 hour=inputs["HOUR"],
#                 is_weekend=bool(inputs["IS_WEEKEND"]),
#                 day_of_month=inputs["DayOfMonth"],
#                 day_of_week=inputs["DayOfWeek"],
#                 prediction_result=prediction
#             )
#             if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#                 return JsonResponse({'predicted_delay': float(prediction)})
#             else:
#                 return render(request, 'delay_predictor.html', {'prediction': prediction})
#         except Exception as e:
#             print("Error in delay predictor:", e)
#             if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#                 return JsonResponse({'error': str(e)}, status=400)
#             else:
#                 return render(request, 'delay_predictor.html', {'error': str(e)})
    
#     return render(request, 'delay_predictor.html')

# import math
# import requests
# def get_distance_from_lat_lon_in_km(lat1, lon1, lat2, lon2):
#     R = 6371
#     dLat = math.radians(lat2 - lat1)
#     dLon = math.radians(lon2 - lon1)
#     a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
#         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
#         math.sin(dLon / 2) * math.sin(dLon / 2)
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     return R * c

# def live_tracking(request):
#     center_lat = 20.0
#     center_lon = 72.0
#     range_km = 500.0
#     map_div = None

#     if request.method == 'POST':
#         try:
#             center_lat = float(request.POST.get('lat', center_lat))
#             center_lon = float(request.POST.get('lon', center_lon))
#             range_km = float(request.POST.get('range', range_km))
#         except ValueError:
#             pass

#         params = {'access_key': 'cbd04b2f0534995dafc014f8bbcffc85', 'flight_status': 'active'}
#         api_result = requests.get('http://api.aviationstack.com/v1/flights', params=params)
#         api_response = api_result.json()

#         flights = []
#         for flight in api_response.get('data', []):
#             live = flight.get('live')
#             if live and not live.get('is_ground', True):
#                 lat = live.get('latitude')
#                 lon = live.get('longitude')
#                 if lat and lon:
#                     distance = get_distance_from_lat_lon_in_km(center_lat, center_lon, lat, lon)
#                     if distance <= range_km:
#                         flights.append({
#                             "Airline": flight['airline'].get('name', 'Unknown'),
#                             "Flight": flight['flight'].get('iata', 'N/A'),
#                             "From": flight['departure'].get('airport', 'Unknown'),
#                             "To": flight['arrival'].get('airport', 'Unknown'),
#                             "Latitude": lat,
#                             "Longitude": lon
#                         })

#         df = pd.DataFrame(flights)

#         if df.empty:
#             map_div = "<p>No live flights in the area.</p>"
#         else:
#             fig = px.scatter_geo(df,
#                                 lat='Latitude',
#                                 lon='Longitude',
#                                 text='Flight',
#                                 hover_name='Airline',
#                                 hover_data=['From', 'To'],
#                                 title="Live Flights in Your Region",
#                                 projection="natural earth")
#             fig.update_geos(
#                 center=dict(lat=center_lat, lon=center_lon),
#                 lataxis_range=[center_lat - 5, center_lat + 5],
#                 lonaxis_range=[center_lon - 5, center_lon + 5]
#             )
#             fig.update_layout(height=600, margin={"r":0,"t":50,"l":0,"b":0})
#             map_div = plot(fig, output_type='div', include_plotlyjs=False)

#     return render(request, 'live_tracking.html', {
#         'map_div': map_div,
#         'lat': center_lat,
#         'lon': center_lon,
#         'range': range_km
#     })

# from math import radians, sin, cos, sqrt, atan2
# airport_dict = {
#     'Atlanta': (33.6407, -84.4277),
#     'Los Angeles': (33.9416, -118.4085),
#     'JFK New York': (40.6413, -73.7781),
#     'Heathrow London': (51.4700, -0.4543),
#     'San Francisco': (37.7749, -122.4194),
#     'Chicago': (41.8781, -87.6298),
#     'Washington DC': (38.9072, -77.5),
#     'Dallas': (32.7767, -96.7970),
#     'Denver': (39.7392, -104.9903),
#     'Miami': (25.7617, -80.1918),
#     'Houston': (29.7604, -95.3698),
#     'Phoenix': (33.4484, -112.0740),
#     'Philadelphia': (39.9526, -75.1652),
#     'Boston': (42.3601, -71.0589),
#     'San Diego': (32.7157, -117.1611),
#     'San Jose': (37.3382, -121.8863),
#     'Seattle': (47.6062, -122.3321),
#     'Orlando': (28.5383, -81.3792),
#     'Portland': (45.5152, -122.6750),
#     'Las Vegas': (36.1699, -115.1398),
# }
# def haversine_distance(lat1, lon1, lat2, lon2):
#     R = 6371
#     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
#     dlat = lat2 - lat1
#     dlon = lon2 - lon1
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     return R * c

# def co2_footprint(request):
#     co2_emission = None
#     distance = None
#     error = None
#     if request.method == 'POST':
#         origin_code = request.POST.get('origin')
#         dest_code = request.POST.get('dest')
#         if origin_code and dest_code and origin_code in airport_dict and dest_code in airport_dict:
#             origin_coords = airport_dict[origin_code]
#             dest_coords = airport_dict[dest_code]
#             distance = haversine_distance(*origin_coords, *dest_coords)
#             co2_emission_per_passenger = distance * 0.09
#             co2_emission = round(co2_emission_per_passenger, 2)
#         else:
#             error = "Invalid airport codes or missing input. Please try again."
#     return render(request, 'co2_footprint.html', {
#         'co2_emission': co2_emission,
#         'distance': distance,
#         'error': error,
#         'airports': airport_dict.keys()
#     })

# def delay_analysis(request):
#     return render(request, 'delay_analysis.html')

# def about(request):
#     return render(request, 'about.html')

# def statistics(request):
#     return render(request, 'statistics.html')

# def compare_airlines(request):
#     error = None 
#     graphs = None 
#     airlines = [
#         'United Air Lines Inc.',
#         'Delta Air Lines Inc.',
#         'American Airlines Inc.',
#         'Republic Airline',
#         'SkyWest Airlines',
#         'Horizon Air'
#     ]
#     if request.method == 'POST':
#         airline1 = request.POST.get('airline1')
#         airline2 = request.POST.get('airline2')
#         print(f"Selected airlines: {airline1}, {airline2}")  # Debug print
#         if not airline1 or not airline2 or airline1 == airline2:
#             error = "Please select two different airlines."
#         elif airline1 not in airlines or airline2 not in airlines:
#             error = "Invalid airline selection."
#         else:
#             try:
#                 df_filtered = df[df['AIRLINE'].isin([airline1, airline2])].copy()
#                 print(f"Filtered DataFrame shape: {df_filtered.shape}")  # Debug print
#                 if df_filtered.empty:
#                     error = "No data available for the selected airlines."
#                 else:
#                     df_filtered['DEP_DELAY'] = pd.to_numeric(df_filtered['DEP_DELAY'], errors='coerce')
#                     df_filtered['ARR_DELAY'] = pd.to_numeric(df_filtered['ARR_DELAY'], errors='coerce')
#                     df_filtered['CANCELLED'] = pd.to_numeric(df_filtered['CANCELLED'], errors='coerce')
#                     df_filtered['TAXI_OUT'] = pd.to_numeric(df_filtered['TAXI_OUT'], errors='coerce')
#                     df_filtered['TAXI_IN'] = pd.to_numeric(df_filtered['TAXI_IN'], errors='coerce')
#                     # Average delay
#                     delay_data = df_filtered.groupby('AIRLINE')[['DEP_DELAY', 'ARR_DELAY']].mean().fillna(0)
#                     delay_data['TOTAL_DELAY'] = delay_data[['DEP_DELAY', 'ARR_DELAY']].sum(axis=1)
#                     delay_plot = plot(px.bar(delay_data.reset_index(), x='AIRLINE', y='TOTAL_DELAY',
#                                         title="Average Delay Comparison", labels={'TOTAL_DELAY': 'Average Delay (min)'},
#                                         color='AIRLINE'), output_type='div', include_plotlyjs=False)
#                     print(f"Delay plot HTML length: {len(delay_plot)}")  # Debug print
                    
#                     # Cancellation rate
#                     cancellation_data = df_filtered.groupby('AIRLINE')['CANCELLED'].mean() * 100
#                     cancellation_plot = plot(px.bar(cancellation_data.reset_index(), x='AIRLINE', y='CANCELLED',
#                                                 title="Cancellation Rate Comparison", labels={'CANCELLED': 'Cancellation Rate (%)'},
#                                                 color='AIRLINE'), output_type='div', include_plotlyjs=False)
#                     print(f"Cancellation plot HTML length: {len(cancellation_plot)}")  # Debug print
                    
#                     # Wait time (approximated as taxi out + taxi in time)
#                     wait_time_data = df_filtered.groupby('AIRLINE')[['TAXI_OUT', 'TAXI_IN']].mean().fillna(0)
#                     wait_time_data['TOTAL_WAIT'] = wait_time_data[['TAXI_OUT', 'TAXI_IN']].sum(axis=1)
#                     wait_time_plot = plot(px.bar(wait_time_data.reset_index(), x='AIRLINE', y='TOTAL_WAIT',
#                                             title="Average Wait Time Comparison", labels={'TOTAL_WAIT': 'Average Wait Time (min)'},
#                                             color='AIRLINE'), output_type='div', include_plotlyjs=False)
#                     print(f"Wait time plot HTML length: {len(wait_time_plot)}")  # Debug print

#                     graphs = {
#                         'delay_plot': delay_plot,
#                         'cancellation_plot': cancellation_plot,
#                         'wait_time_plot': wait_time_plot
#                     }
#             except Exception as e:
#                 error = f"Error processing data: {str(e)}"
#                 print(f"Error: {e}")
#     return render(request, 'compare_airlines.html', {
#         'error': error,
#         'graphs': graphs,
#         'airlines': airlines
#     })

from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json, os 
import yaml
from .models import FlightDelayPrediction
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import warnings

# Suppress FutureWarning from pandas for Plotly groupby operations
warnings.filterwarnings("ignore", category=FutureWarning, message=".*get_group.*")

# Load the dataset once at server startup
try:
    df = pd.read_csv(r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\flights_sample_3m.csv")
    print("Dataset loaded successfully. Unique airlines:", df['AIRLINE'].unique())
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = pd.DataFrame()  # Fallback to empty DataFrame if loading fails

def home(request):
    return render(request, 'home.html')

import joblib, torch
from pytorch_tabular import TabularModel
import pandas as pd 
from django.shortcuts import render 
from django.http import JsonResponse
def load_cpu(file_path):
    with open(file_path, 'rb') as f:
        return torch.load(f, map_location=torch.device('cpu'))
encoder = joblib.load(r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\flight_cat_encoder.pkl")
model_dir = r"C:\Users\Param\OneDrive\文档\DSA_SEM_VI\Group_Project\ft_transformer_model"
tabular_model = TabularModel.load_model(model_dir)
cat_cols = ['Airline', 'Origin', 'Dest']
cont_cols = ['DayOfWeek', 'Month', 'HOUR', 'IS_WEEKEND', 'Year', 'DayOfMonth']
all_cols = cat_cols + cont_cols

def predict_delay(inputs):
    df = pd.DataFrame([inputs])
    preds = tabular_model.predict(df)
    prediction_value = preds.iloc[0, 0]
    return prediction_value

@csrf_exempt
def delay_predictor(request):
    if request.method == 'POST':
        try:
            inputs = {
                "Airline": request.POST.get('airline'),
                "Origin": request.POST.get('origin'),
                "Dest": request.POST.get('dest'),
                "Month": int(request.POST.get('month')),
                "HOUR": int(request.POST.get('hour')),
                "IS_WEEKEND": int(request.POST.get('is_weekend')),
                "DayOfMonth": int(request.POST.get('day_of_month')),
                "DayOfWeek": int(request.POST.get('day_of_week')),
            }
            prediction = predict_delay(inputs)
            FlightDelayPrediction.objects.create(
                airline=inputs["Airline"],
                origin=inputs["Origin"],
                destination=inputs["Dest"],
                month=inputs["Month"],
                hour=inputs["HOUR"],
                is_weekend=bool(inputs["IS_WEEKEND"]),
                day_of_month=inputs["DayOfMonth"],
                day_of_week=inputs["DayOfWeek"],
                prediction_result=prediction
            )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'predicted_delay': float(prediction)})
            else:
                return render(request, 'delay_predictor.html', {'prediction': prediction})
        except Exception as e:
            print("Error in delay predictor:", e)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': str(e)}, status=400)
            else:
                return render(request, 'delay_predictor.html', {'error': str(e)})
    return render(request, 'delay_predictor.html')

import math
import requests
def get_distance_from_lat_lon_in_km(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def live_tracking(request):
    center_lat = 20.0
    center_lon = 72.0
    range_km = 500.0
    map_div = None

    if request.method == 'POST':
        try:
            center_lat = float(request.POST.get('lat', center_lat))
            center_lon = float(request.POST.get('lon', center_lon))
            range_km = float(request.POST.get('range', range_km))
        except ValueError:
            pass

        params = {'access_key': 'cbd04b2f0534995dafc014f8bbcffc85', 'flight_status': 'active'}
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params=params)
        api_response = api_result.json()

        flights = []
        for flight in api_response.get('data', []):
            live = flight.get('live')
            if live and not live.get('is_ground', True):
                lat = live.get('latitude')
                lon = live.get('longitude')
                if lat and lon:
                    distance = get_distance_from_lat_lon_in_km(center_lat, center_lon, lat, lon)
                    if distance <= range_km:
                        flights.append({
                            "Airline": flight['airline'].get('name', 'Unknown'),
                            "Flight": flight['flight'].get('iata', 'N/A'),
                            "From": flight['departure'].get('airport', 'Unknown'),
                            "To": flight['arrival'].get('airport', 'Unknown'),
                            "Latitude": lat,
                            "Longitude": lon
                        })

        df = pd.DataFrame(flights)

        if df.empty:
            map_div = "<p>No live flights in the area.</p>"
        else:
            fig = px.scatter_geo(df,
                                lat='Latitude',
                                lon='Longitude',
                                text='Flight',
                                hover_name='Airline',
                                hover_data=['From', 'To'],
                                title="Live Flights in Your Region",
                                projection="natural earth")
            fig.update_geos(
                center=dict(lat=center_lat, lon=center_lon),
                lataxis_range=[center_lat - 5, center_lat + 5],
                lonaxis_range=[center_lon - 5, center_lon + 5]
            )
            fig.update_layout(height=600, margin={"r":0,"t":50,"l":0,"b":0})
            map_div = plot(fig, output_type='div', include_plotlyjs=False)

    return render(request, 'live_tracking.html', {
        'map_div': map_div,
        'lat': center_lat,
        'lon': center_lon,
        'range': range_km
    })

from math import radians, sin, cos, sqrt, atan2
airport_dict = {
    'Atlanta': (33.6407, -84.4277),
    'Los Angeles': (33.9416, -118.4085),
    'JFK New York': (40.6413, -73.7781),
    'Heathrow London': (51.4700, -0.4543),
    'San Francisco': (37.7749, -122.4194),
    'Chicago': (41.8781, -87.6298),
    'Washington DC': (38.9072, -77.5),
    'Dallas': (32.7767, -96.7970),
    'Denver': (39.7392, -104.9903),
    'Miami': (25.7617, -80.1918),
    'Houston': (29.7604, -95.3698),
    'Phoenix': (33.4484, -112.0740),
    'Philadelphia': (39.9526, -75.1652),
    'Boston': (42.3601, -71.0589),
    'San Diego': (32.7157, -117.1611),
    'San Jose': (37.3382, -121.8863),
    'Seattle': (47.6062, -122.3321),
    'Orlando': (28.5383, -81.3792),
    'Portland': (45.5152, -122.6750),
    'Las Vegas': (36.1699, -115.1398),
}
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def co2_footprint(request):
    co2_emission = None
    distance = None
    error = None
    if request.method == 'POST':
        origin_code = request.POST.get('origin')
        dest_code = request.POST.get('dest')
        if origin_code and dest_code and origin_code in airport_dict and dest_code in airport_dict:
            origin_coords = airport_dict[origin_code]
            dest_coords = airport_dict[dest_code]
            distance = haversine_distance(*origin_coords, *dest_coords)
            co2_emission_per_passenger = distance * 0.09
            co2_emission = round(co2_emission_per_passenger, 2)
        else:
            error = "Invalid airport codes or missing input. Please try again."
    return render(request, 'co2_footprint.html', {
        'co2_emission': co2_emission,
        'distance': distance,
        'error': error,
        'airports': airport_dict.keys()
    })

def delay_analysis(request):
    return render(request, 'delay_analysis.html')

def about(request):
    return render(request, 'about.html')

def statistics(request):
    return render(request, 'statistics.html')

def compare_airlines(request):
    error = None 
    graphs = None 
    airlines = [
        'United Air Lines Inc.',
        'Delta Air Lines Inc.',
        'American Airlines Inc.',
        'Republic Airline',
        'SkyWest Airlines Inc.',
        'Horizon Air',
        'Southwest Airlines Co.',
        'Endeavor Air Inc.'
    ]
    if request.method == 'POST':
        airline1 = request.POST.get('airline1')
        airline2 = request.POST.get('airline2')
        print(f"Selected airlines: {airline1}, {airline2}")  # Debug print
        if not airline1 or not airline2 or airline1 == airline2:
            error = "Please select two different airlines."
        elif airline1 not in airlines or airline2 not in airlines:
            error = "Invalid airline selection."
        else:
            try:
                df_filtered = df[df['AIRLINE'].isin([airline1, airline2])].copy()
                print(f"Filtered DataFrame shape: {df_filtered.shape}")  # Debug print
                if df_filtered.empty:
                    error = "No data available for the selected airlines."
                else:
                    df_filtered['DEP_DELAY'] = pd.to_numeric(df_filtered['DEP_DELAY'], errors='coerce')
                    df_filtered['ARR_DELAY'] = pd.to_numeric(df_filtered['ARR_DELAY'], errors='coerce')
                    df_filtered['CANCELLED'] = pd.to_numeric(df_filtered['CANCELLED'], errors='coerce')
                    df_filtered['TAXI_OUT'] = pd.to_numeric(df_filtered['TAXI_OUT'], errors='coerce')
                    df_filtered['TAXI_IN'] = pd.to_numeric(df_filtered['TAXI_IN'], errors='coerce')
                    
                    delay_data = df_filtered.groupby('AIRLINE')[['DEP_DELAY', 'ARR_DELAY']].mean().fillna(0)
                    delay_data['TOTAL_DELAY'] = delay_data[['DEP_DELAY', 'ARR_DELAY']].sum(axis=1)
                    delay_fig = px.bar(delay_data.reset_index(), x='AIRLINE', y='TOTAL_DELAY',
                                    title="Average Delay Comparison", labels={'TOTAL_DELAY': 'Average Delay (min)'},
                                    color='AIRLINE')
                    delay_plot = delay_fig.to_html(full_html=False, include_plotlyjs=False)
                    print(f"Delay plot HTML length: {len(delay_plot)}")  
                    
                    # Cancellation rate
                    cancellation_data = df_filtered.groupby('AIRLINE')['CANCELLED'].mean() * 100
                    cancellation_fig = px.bar(cancellation_data.reset_index(), x='AIRLINE', y='CANCELLED',
                                            title="Cancellation Rate Comparison", labels={'CANCELLED': 'Cancellation Rate (%)'},
                                            color='AIRLINE')
                    cancellation_plot = cancellation_fig.to_html(full_html=False, include_plotlyjs=False)
                    print(f"Cancellation plot HTML length: {len(cancellation_plot)}")  # Debug print
                    
                    # Wait time (approximated as taxi out + taxi in time)
                    wait_time_data = df_filtered.groupby('AIRLINE')[['TAXI_OUT', 'TAXI_IN']].mean().fillna(0)
                    wait_time_data['TOTAL_WAIT'] = wait_time_data[['TAXI_OUT', 'TAXI_IN']].sum(axis=1)
                    wait_time_fig = px.bar(wait_time_data.reset_index(), x='AIRLINE', y='TOTAL_WAIT',
                                        title="Average Wait Time Comparison", labels={'TOTAL_WAIT': 'Average Wait Time (min)'},
                                        color='AIRLINE')
                    wait_time_plot = wait_time_fig.to_html(full_html=False, include_plotlyjs=False)
                    print(f"Wait time plot HTML length: {len(wait_time_plot)}")  # Debug print

                    graphs = {
                        'delay_plot': delay_plot,
                        'cancellation_plot': cancellation_plot,
                        'wait_time_plot': wait_time_plot
                    }
            except Exception as e:
                error = f"Error processing data: {str(e)}"
                print(f"Error: {e}")
    return render(request, 'compare_airlines.html', {
        'error': error,
        'graphs': graphs,
        'airlines': airlines
    })