#Imports
import streamlit as st
import re

st.write("Depression Detection Based on Twitter Data")

input = st.text_input("Enter a message for depression evaluation (within 40 characters)")

st.write("Only input text please! No links, no emojis!")

#preprocessing text

#Expand contractions
import contractions
contr_func = lambda x : [contractions.fix(word) for word in x.split()]
input = contr_func(input)

#join list back to string with spaces in between
input = ' '.join(input)

#remove mentions, hashtags, punctuation in that order
input = input.replace('@[A-Za-z0-9_]+', '')
input = input.replace('#[A-Za-z0-9_]+', '')
input = input.replace('[^\w\s]','')

#turn all to lowercase
input = input.lower()

#lemmatizer
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
lemm_func = lambda x: ' '.join([lmtzr.lemmatize(word,'v') for word in x.split() ])

#padding and tokenizing

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#hyperparams
vocab_size = 5000
embedding_dim = 50
max_length = 40
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<OOV>'

#import tokenizer from pickle
import pickle 

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

text_seq = tokenizer.texts_to_sequences([input])
pad_seq = pad_sequences(text_seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)

#Predicting

#import model
model = tf.keras.models.load_model('lstm_100char_w2vembed_twitdepression.h5')

#predict on sequence
pred_func = lambda x: model.predict(x)
pred_prob = pred_func(pad_seq)
pred_prob = pred_prob[0][0]
pred_prob = pred_prob * 100
pred_prob = round(pred_prob, 2)

#output probability
st.write(str(pred_prob) + ' percent chance to be depressed')