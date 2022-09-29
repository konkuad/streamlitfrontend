import streamlit as st
import json
import random
import requests
import base64
import presets

st.title("This WAIFU doesn't exist")
st.write("#### But you can control what specs of waifu you want!")
generate_form = st.form(key='generate')
generate = generate_form.form_submit_button('Generate!')

names = [
    'Initial (4x4)',
    'Step #0 (8x8)',
    'Step #1 (16x16)',
    'Step #2 (32x32)',
    'Step #3 (64x64)',
    'Step #4 (128x218)',
]

cfg = {
    i:False 
    for i in range(len(names))
}

modulation_json = {
    i:{
        'id':512,
        'alpha':0
    }
    for i in range(len(names))
}

with st.sidebar:
    
    st.write('## Set up some parameters')
    
    include_original = st.checkbox('Include orginal')
    sample_size = st.slider(f'Sample Size', 1, 11, 3)   
    option = st.selectbox('Use presets',['none', 'lavender', 'sunset', 'golden', 'dark'])
    
    if option == 'none':
        random_ID = st.checkbox('Random ID')
        random_alpha = st.checkbox('Random Alpha')
        st.write('## Tweak the features!')

        for i, name in enumerate(names):
            cfg[i] = st.checkbox(f'Modulate {name}')

            if cfg[i]:
                ID = st.number_input(f'ID for layer - {name}', 0, 511, 0)
                ALPHA = st.slider(f'Alpha for layer - {name}', -100, 100, 0)    
                modulation_json[i] = {
                    'id':ID,
                    'alpha':ALPHA
                }
            else:
                modulation_json[i] = {
                    'id':512,
                    'alpha':0
                }
                
    else:
        random_ID = False
        random_alpha = False
        modulation_json = presets.get_presets()[option]

url = 'http://41f7-35-197-98-113.ngrok.io'

if generate:
    
    send_json = {}
    
    for s in range(sample_size):
    
        for i in range(len(names)):
            if random_ID:
                modulation_json[i]['id'] = random.randint(0,512)
            if random_alpha:
                modulation_json[i]['alpha'] = random.randint(0,201)-100
                
        send_json[s] = modulation_json
        
    topost = {
        'include_original':include_original,
        'data':send_json
    }
        
    post = requests.post(url, json=topost)
    get_json = json.loads(post.text)
    
    cols = st.columns(sample_size)
    for i, col in enumerate(cols):
       
        col.write(f'Waifu #{i+1}')
        base64_encoded = str.encode(get_json[f'new_{i}'])
        base64_decoded = base64.decodebytes(base64_encoded) 
        col.image(base64_decoded, use_column_width=True)
        
        if include_original:
            col.write('Original')
            base64_encoded = str.encode(get_json[f'original_{i}'])
            base64_decoded = base64.decodebytes(base64_encoded) 
            col.image(base64_decoded, use_column_width=True)
    
    download_json = st.download_button(
        label="Download Modulations as JSON",
        file_name="modulations.json",
        mime="application/json",
        data=json.dumps(send_json),
    )
    
    download_image = st.download_button(
        label="Download Generated Image",
        file_name="modulations.json",
        mime="application/json",
        data=json.dumps(send_json),
    )