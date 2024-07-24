import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


app = Flask(__name__)

def get_estimated_price(location,sqft,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    xp= np.zeros(len(__data_columns))
    xp[0]= sqft
    xp[1]= bath
    xp[2]=bhk
    if loc_index >= 0:
       xp[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    pass


def load_saved_artifacts():
    print("loading saved artifacts....start")
    global __data_columns
    global __locations
    
    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    with open('./artifacts/bengaluru_house_prices_model.pkl', 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_saved_artifacts()  
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000,3,2))
    print(get_estimated_price('1st Phase JP Nagar', 1000,2,2))
    print(get_estimated_price('Kalhalli', 1000,3,2))# other location
