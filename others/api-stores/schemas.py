from pydantic import BaseModel
class Store(BaseModel):
    id : int
    name : str
    opening_time : str
    closing_time : str
    address : str
    number : str
    payment_method : str
    image_url : str