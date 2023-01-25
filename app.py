# https://laptopvalueestimator.onrender.com/     live server

import pandas as pd
import streamlit as slt
import numpy as np

import pickle
pickled_file= open('pipe.pkl', 'rb')
lr = pickle.load(pickled_file)
pickled_file.close()

df = pd.read_csv('traineddata.csv', encoding='latin1')

slt.title('LAPTOP VALUE ESTIMATOR')
# slt.subheader('----*developed by Joshi.Inc*-----')

company = slt.selectbox('BRAND', df['COMPANY'].unique())

type = slt.selectbox('Type', df['TYPENAME'].unique())

ram = slt.selectbox('RAM ( in GB )', [2,4,6,8,12,16,24,32,64])

clock_speed = slt.number_input('CLOCK SPPED (in GHz)  ---normally ranges from 0.8 to 3.8 GHz')

opsys = slt.selectbox("Operating System", df['OS'].unique())


weight = slt.number_input('Weight (in kg) ---normally ranges from 0.5 to 4.5 kg---')

touchscreen = slt.selectbox("Touchscreen", ['Yes','No'])

ips = slt.selectbox("IPS", ['Yes','No'])

processor = slt.selectbox('Processor/ CPU', df['PROCESSOR'].unique())

screen_size = slt.number_input('Screen Size(inches) ---normally ranges from 11 to 19 inches---')
screen_resolution = slt.selectbox('Screen Resolution', ['3200x1800','1600x900','1366x768','1920x1080', '3840x2160', '2880x1800'])

gpu = slt.selectbox('GPU', df['GPU COMPANY'].unique())

ssd = slt.selectbox('SSD (in GB)', [0,8,128,256,512,1024])
hdd = slt.selectbox('HDD (in GB)', [0,128,256,512,1024, 2048])                                                    



if slt.button('ESTIMATE VALUE'):
    if opsys == 'Mac'and company != "Apple":
        slt.title("Mac doesn't support with laptops of other brands except 'Apple'")
    else:
        try:    
            if ips == 'Yes':
                ips=1
            else:
                ips=0
            if touchscreen=='Yes':
                touchscreen=1
            else:
                touchscreen=0

            x_res= int(screen_resolution.split('x')[0])
            y_res= int(screen_resolution.split('x')[1])
            ppi = ((x_res**2)+(y_res**2))**0.5/(screen_size)

            new_feature = np.array([company,type, ram, opsys, weight, touchscreen, ips, ppi, clock_speed,  processor, hdd, ssd, gpu])
            new_feature.reshape(1,13)

            pred_price = int(np.exp(lr.predict([new_feature])[0]))
            slt.title(f'The price of this laptop as per our prediction should range between: \$_{str(pred_price-100)}_  and \$_{str(pred_price+100)}_ ')
        except:
            print("Please fill all of the boxes...")
