import numpy as np
import pandas as pd

import pickle
import json
try:
    import config
except:
    pass



class Sales_Data():

    def __init__(self,Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,
        Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type,Outlet_Type):

        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = "Item_Fat_Content_" + Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_Type = "Item_Type_" + Item_Type
        self.Item_MRP = Item_MRP
        self.Outlet_Identifier = Outlet_Identifier
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = "Outlet_Type_" + Outlet_Type


    def load_model (self):

    #     with open (config.MODEL_FILE_PATH,"rb") as f:
    #         self.model = pickle.load(f)

    #     with open (config.JSON_FILE_PATH,"r") as f:
    #         self.json_data = json.load(f)


        try:
            with open(config.MODEL_FILE_PATH,"rb")as f:
             self.model = pickle.load(f)

        except:
             with open("lin_model.pkl","rb")as f:
              self.model = pickle.load(f)

        try:
            with open(config.JSON_FILE_PATH,"r")as f:
             self.json_data = json.load(f)
        except:
            with open("project_data.json","r")as f:
             self.json_data = json.load(f)



    def get_predicted_sales(self):
        self.load_model()

        Item_Fat_Content_index = self.json_data["columns"].index(self.Item_Fat_Content)
        Item_Type_index = self.json_data["columns"].index(self.Item_Type)
        Outlet_Type_index = self.json_data["columns"].index(self.Outlet_Type)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.Item_Weight
        array[1] = self.Item_Visibility
        array[2] = self.Item_MRP
        array[3] = self.json_data["Outlet_Identifier"][self.Outlet_Identifier]
        array[4] = self.Outlet_Establishment_Year
        array[5] = self.json_data["Outlet_Size"][self.Outlet_Size]
        array[5] = self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        array[Item_Fat_Content_index] = 1
        array[Item_Type_index] = 1
        array[Outlet_Type_index] = 1

        predicted_sale = self.model.predict([array])[0]
        return predicted_sale

if __name__ == "__main__":

    Item_Weight = 9.300000
    Item_Visibility = 0.016047
    Item_MRP = 249.809200
    Outlet_Identifier = "OUT049"
    Outlet_Establishment_Year = 1999.000000
    Outlet_Size = "Medium"
    Outlet_Location_Type = "Tier 2"

    Item_Fat_Content = "Regular"
    Item_Type = "Dairy"
    Outlet_Type = "Supermarket Type2"


    OBJ = Sales_Data(Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,
        Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type,Outlet_Type)

    sales = OBJ.get_predicted_sales()
    print("Predicted Sales : ",sales.round(3))