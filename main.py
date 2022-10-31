
from flask import Flask,render_template,jsonify,request
from models.utlis import Sales_Data


app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("sample.html")

@app.route("/prediction",methods = ['POST','GET'])
def get_sales():
    if request.method == 'GET':
        Item_Weight = float(request.args.get("Item_Weight"))
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year = int(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")

        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Type = request.args.get("Item_Type")
        Outlet_Type = request.args.get("Outlet_Type")

        OBJ = Sales_Data(Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,
        Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type,Outlet_Type)

        sales = OBJ.get_predicted_sales()
        print("Predicted Sales : ",sales.round(3))

        return render_template("sample.html",prediction = sales)

    else:
        Item_Weight = float(request.form.get("Item_Weight"))
        Item_Visibility = float(request.form.get("Item_Visibility"))
        Item_MRP = float(request.form.get("Item_MRP"))
        Outlet_Identifier = request.form.get("Outlet_Identifier")
        Outlet_Establishment_Year = int(request.form.get("Outlet_Establishment_Year"))
        Outlet_Size = request.form.get("Outlet_Size")
        Outlet_Location_Type = request.form.get("Outlet_Location_Type")

        Item_Fat_Content = request.form.get("Item_Fat_Content")
        Item_Type = request.form.get("Item_Type")
        Outlet_Type = request.form.get("Outlet_Type")

        OBJ = Sales_Data(Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,
        Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type,Outlet_Type)

        sales = OBJ.get_predicted_sales()
        print("Predicted Sales : ",sales.round(3))

        return render_template("sample.html",prediction = sales.round(3) )

if __name__ =="__main__":
    app.run(debug=True)