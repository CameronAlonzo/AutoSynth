from api import AutoSynthAPI
from augment import Noise
# Tabular
print("Tabular Data: \n")
tabular_api = AutoSynthAPI('tabular', n_samples=10, n_features=10)
augmentor = Noise(1)
X, y = tabular_api.generate_data(augment=True, augmentor=augmentor)
#print(X.head())

# Generating images
image_api = AutoSynthAPI('image', n_images=5, image_size=(32, 32))
images = image_api.generate_data()
#for img in images:
#    img.show()


# Generating text data
print("Text Data \n")
text_api = AutoSynthAPI('text', n_sentences=5, sentence_length=12)
sentences = text_api.generate_data(augment=True, augmentor=augmentor)
print(sentences)