import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def prediction_stock(predstock):
    stock_name = predstock
    file_path = "F:/My Projects/Stock Market Chat Box Python/dataset/" + stock_name + ".csv"
    dataset = pd.read_csv(file_path)

    rows, cols = (200, 1)
    X = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(i+1)
        X.append(col)  # creates a 2D array of digits (1 to 200)
    # print(X)

    y = dataset.iloc[-201:-1, 8].values

    # print(y)
    # creates polinomial relation between x and y with degree 4 ( for best results)
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    # creats object of imported LinearRegression function.
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y)

    stock_pred_string = "Tomorrow's Predicted Value of " + stock_name + " is: " + \
        str(lin_reg_2.predict(poly_reg.fit_transform([[201]]))) + "\n" + "Day After Tomorrow's Predicted Value of " + \
        stock_name + " is: " + \
        str(lin_reg_2.predict(poly_reg.fit_transform([[202]]))) + \
        "\n"  # this string concatinates the stock name and then predicted value.

    # print(stock_pred_array2)

    return{
        stock_pred_string  # return the string of predicted stocks data
    }
