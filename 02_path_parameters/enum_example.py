from enum import Enum
from fastapi import FastAPI

#  This example shows how to use an Enum for path parameters in FastAPI.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/models/{model_name}") # path parameter for model_name
async def get_model(model_name: ModelName): # get model_name using the Enum ModelName

    # compare the model_name with the Enum values
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}