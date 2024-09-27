from api import AutoSynthAPI

#Tabular
print("Tabular Data: \n")
tabular_api = AutoSynthAPI('tabular')
X, y = tabular_api.generate_data(n_samples=1000, n_features=10)
print(X.head())
print("\n")

# Generating images
print("Image Data \n")
image_api = AutoSynthAPI('image')
images = image_api.generate_data(n_images=5, image_size=(32, 32))
for img in images:
    img.show()
print("\n")

# Generating text data
print("Text Data \n")
text_api = AutoSynthAPI('text')
sentences = text_api.generate_data(n_sentences=5, sentence_length=12)
print(sentences)
print("\n")