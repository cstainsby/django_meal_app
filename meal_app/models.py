from django.db import models

# Create your models here.
units_of_measurement = ["tsp", "tbsp", "fl oz", "cup", 
                        "pint", "quart" "gallon", "ml", 
                        "liter", "lb", "oz", "mg", "g", "kg"]

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

# this table is intended to just be a list of each ingredient availible to all users
class Ingredient(models.Model):
  name = models.CharField(max_length=50)

  UnitOfMeasurement = models.TextChoices("UnitOfMeasurement", units_of_measurement)
  unit_of_measurement = models.CharField(max_length=10, blank=True)

  price_per_unit = models.FloatField()

  def __str__(self):
    if unit_of_measurement:
      return self.name + " (" + str(price_per_unit) + " per " + unit_of_measurement + ")"
    else:
      return self.name

class Recipe(models.Model):
  recipe_name = models.CharField(max_length=50)
  recipe_author = models.CharField(max_length=50)
  date_posted = models.DateField()
  time_to_cook = models.DurationField()
  description_of_meal = models.CharField(max_length=250)
  meal_instructions = models.CharField(max_length=700)
  
  #TODO add nutrition info and servings/caloric info

# each cook can have multiple recipes and each recipe can have 
# multiple cooks who can cook it warrenting its many-to-many status
class CookRecipeJunction(models.Model):
  UserID = models.ForeignKey(User, on_delete=models.CASCADE)
  RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)

# each Recipe can have multiple ingredients and each ingredient can have multiple recipes
# with this junction I will also include amount needed for each ingredient
class RecipeIngredientJunction(models.Model):
  IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  ammount = models.FloatField()



#TODO: for later implementation add groups

# Groups are used to organize group cooking efforts

