from helper import get_tensor, get_model
import json
model = get_model()

with open('mappings.json', 'r') as f:
    mappings = json.load(f)

with open('remidies.json', 'r') as f:
    remidies = json.load(f)

    
def get_disease_name(image_bytes):
	tensor = get_tensor(image_bytes)
	outputs = model.forward(tensor)
	_, prediction = outputs.max(1)
	category = prediction.item()
	disease = mappings[str(category)]

	return  disease, remidies[disease]