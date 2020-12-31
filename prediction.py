import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import string


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
        X.append(col)
    # print(X)

    # num = pd.read_csv(
    #     "F:/My Projects/Stock Market Chat Box Python/dataset/test.csv")

    y = dataset.iloc[-201:-1, 8].values
    # print(X)
    # print(y)
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y)

    ################################################################################
    # plt.scatter(X, y, color='red')
    # plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
    # plt.title('Median Graph of previous Days (not to scale, just a prediction)')
    # plt.xlabel('Days')
    # plt.ylabel('Price Variation')
    # plt.show()
    ################################################################################

    # stock_pred_array = {str(lin_reg_2.predict(poly_reg.fit_transform([[201]]))), str(
    #     lin_reg_2.predict(poly_reg.fit_transform([[202]])))}

    # print(stock_pred_array)
    stock_pred_array2 = "Tomorrow's Predicted Value of " + stock_name + " is: " + \
        str(lin_reg_2.predict(poly_reg.fit_transform([[201]]))) + "\n" + "Day After Tomorrow's Predicted Value of " + \
        stock_name + " is: " + \
        str(lin_reg_2.predict(poly_reg.fit_transform([[202]]))) + "\n"

    ################################################################################
    # predicting for day 21 and 22
    # print("Today expected Close : ", end=" ")
    # print(str(lin_reg_2.predict(poly_reg.fit_transform([[201]]))))
    # if []
    # print("Tomorrow expected Close : ", end=" ")
    # print(lin_reg_2.predict(poly_reg.fit_transform([[202]])))
    # stores the data in json_result variable
    # json_result2 = json.loads(stock_pred_array)
    ################################################################################

    # print(stock_pred_array2)

    return{
        stock_pred_array2  # return the array of predicted stocks
    }
