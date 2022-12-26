import urllib
import os
import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
st.set_page_config(page_title='dogs vs cats', page_icon='🐶')
st.title("Classificador de Gatos ou Cachorros")


if not os.path.isfile('network.h5'):
        urllib.request.urlretrieve('https://github.com/Giuseppe31-s/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/raw/main/Machine_Learning/network.h5', 'network.h5')
else:
    pass
network = tf.keras.models.load_model('network.h5')
image = st.file_uploader('Carregue a imagem do seu pet', type=['jpg','png','jpeg'])

def classificador(image,*args):
    im = Image.open(image)
    im = im.resize((128, 128))
    im = np.expand_dims(im, axis=0)
    im = np.array(im)
    im = im / 255
    pred = np.argmax(network.predict([im]), axis=-1)
    results = {
        0: 'Gato',
        1: 'Cachorro'
    }
    return results[int(pred)]




if image is not None:
    if st.button('Classificar',type = 'primary',on_click= classificador, kwargs={'image':image}):
        st.subheader(f'Essa imagem foi classificada como {classificador(image)}')
        st.image(image)

else:
    st.write('Coloque uma imagem para começar')




