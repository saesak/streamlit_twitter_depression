This is a streamlit deployed ML app that judges whether your statement entered is depressed or not. 

This dataset was based on about 7000 tweets that were scraped from twitter. 

Explanation of files:

lstm_100char_w2vembed_twitdepression.h5 is the file containing the model pretrained through Kaggle.
streamlit_app.py contains streamlit GUI code as well as the preprocessing and prediction code for inputs inputted by the user.
tokenizer.pickle is the tokenizer used to tokenize incoming user inputs for use in the model. 
future_updates.py is a file used to document future updates I have incoming for this streamlit app. 
tf_env is a virtual environment file that contains my dependencies. 