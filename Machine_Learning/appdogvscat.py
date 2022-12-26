import tensorflow
import streamlit as st
from PIL import Image
from keras.models import load_model
import numpy as np
st.set_page_config(page_title='dogs vs cats', page_icon='🐶')
st.title("Classificador de Gatos ou Cachorros")

network = load_model('network.h5')
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




