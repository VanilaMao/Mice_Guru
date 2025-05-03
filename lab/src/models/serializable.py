import json
import dataclasses
from models.location import Point
class Serializable:
    def serialize(self):
        pass
    
    def deserialize(self,data):
        pass
        
class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o) 

class PointClassDecoder(json.JSONDecoder):
    def __init__(self,*args,**kwargs):
        super().__init__(object_hook=self.dataclass_hook,*args,**kwargs)
    
    def dataclass_hook(self, obj:any)->any:
        if isinstance(obj,dict):
            if "x" in obj and "y" in obj:
                return Point(x=obj["x"],y=obj["y"])
        return obj
