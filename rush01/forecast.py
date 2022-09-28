import numpy as np
import pickle
import joblib
# import sys

class Forecast:
    """
    Predicting the rating or the class
    """
    def __init__(self, list_of_ingredients):
        """
        Put here any fields that you think you will need.
        """
        self.ingredients = list_of_ingredients
        self.names = np.loadtxt('data/ingr.csv', dtype='object', delimiter=',')
        self.X = self.preprocess()
        self.reg = joblib.load('data/model_reg.joblib')
        self.clf = pickle.load(open('data/gs_vot_cl.sav', 'rb'))

    def preprocess(self):
        """
The method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
        vector = np.zeros(self.names.shape)
        for ing in self.ingredients:
            vector[self.names == ing] = 1.
        return vector.reshape(1, -1)

    def predict_rating(self):
        """
The method returns the rating for the list of ingredients using the regression model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.
        """
        rating = self.reg.predict(self.X)
        self.reg_rating = rating
        if self.reg_rating < 2:
            text = "You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"
        elif self.reg_rating < 4:
            text = "You might find it tasty and in our opinion, it is so-so idea to have a dish with that list of ingredients"
        else:
           text = "You might find it tasty and in our opinion, it is a great idea to have a dish with that list of ingredients!"
        rating = rating[0]
        return text

    def predict_rating_category(self):
        """
The method returns the rating category for the list of ingredients using the classification model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.
        """
        rating = self.clf.predict(self.X)
        self.clf_rating = rating
        if self.clf_rating < 2:
            text = "You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"
        elif self.clf_rating < 4:
            text = "You might find it tasty and in our opinion, it is so-so idea to have a dish with that list of ingredients"
        else:
           text = "You might find it tasty and in our opinion, it is a great idea to have a dish with that list of ingredients!"
        rating = rating[0]
        return text

# if __name__ == '__main__':
#     f = Forecast(sys.argv[1:])
#     f.preprocess()
#     print(f.predict_rating())
#     print(f.predict_rating_category())