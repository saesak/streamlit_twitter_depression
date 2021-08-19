'''
Future update list for this app:

Ordered in urgency / ease of implementation

Change number of characters from 40 to 100 or something more reasonable

https://towardsdatascience.com/how-you-can-quickly-build-ml-web-apps-with-streamlit-62f423503305
Like shown above in the link, implement a thing where you can explain the results by showing them
the entire vector and its weights

Instead of taking in tokenized sentences, have it take in word2vec vectors raw
so it doesn't have to compensate for tokens it doesn't know. But this would cause me
to take in 195 extra mb of weight for the word2vec glove-50 twitter model. 

Get a better amount of samples and retrain the LSTM on better data



'''