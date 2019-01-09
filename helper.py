
import io
import torch
import torch.nn as nn
from torchvision import models, transforms
from collections import OrderedDict
from PIL import Image
def get_model():
    checkpoint = 'plantDensenet121.pt'
    model = models.densenet121(pretrained = True)

    for param in model.parameters():
        param.required_grad = False

    classifier = nn.Sequential(OrderedDict([
                                    ('fc1',nn.Linear(1024,512)),
                                    ('relu',nn.ReLU()),
                                    ('fc2',nn.Linear(512,38)),
                                    ('output',nn.LogSoftmax(dim=1))]))
    model.classifier = classifier
    model.load_state_dict(torch.load(checkpoint, map_location = 'cpu'), strict = False)
    model.eval()
    return model

def get_tensor(image_bytes):
	img_transforms = transforms.Compose([transforms.Resize(300),
                                       transforms.CenterCrop(224),
                                       transforms.ToTensor(),
                                       transforms.Normalize([.485,.456,.406],
                                                            [.229,.224,.225])])
	image = Image.open(io.BytesIO(image_bytes))
	return img_transforms(image).unsqueeze(0)
