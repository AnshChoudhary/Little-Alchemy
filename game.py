from flask import Flask, render_template, request
import os

app = Flask(__name__)

elements = []
recipes = []

@app.route("/")
def index():
    # Get the current page number
    page = int(request.args.get('page', 1))

    # Get the elements for the current page
    elements_page = elements[(page-1) * 8:page * 8]

    # Render the index page
    return render_template('index.html', elements=elements_page, page=page)

@app.route("/combine", methods=['POST'])
def combine():
    # Get the elements to combine
    elements_to_combine = request.form.getlist('elements')

    # Check if the elements are valid
    if not all(element in elements for element in elements_to_combine):
        return "Invalid element(s) selected.", 400

    # Get the resulting element
    resulting_element = combine_elements(elements_to_combine)

    # Add the resulting element to the list of elements
    elements.append(resulting_element)

    # Redirect to the index page
    return redirect(url_for('index'))

def combine_elements(elements):
    # Get all the recipes that use the given elements
    recipes_for_elements = [recipe for recipe in recipes if set(elements).issubset(recipe[0])]

    # If there are no recipes, then the combination is invalid
    if not recipes_for_elements:
        return None

    # Get the first recipe
    recipe = recipes_for_elements[0]

    # Return the resulting element
    return recipe[1]

if __name__ == "__main__":
    # Load the elements and recipes from the data file
    data = open("Recipes.dat", "r").read()
    elements, recipes = tuple(data.split("\n-\n"))
    elements = elements.split("\n")
    r = []
    rkeys = []
    for x in recipes.split("\n"):
        com = set(x.split("=")[0].split("+"))
        res = [x.split("=")[1]]
        if com in rkeys:
            r[[x[0] for x in r].index(com)][1].append(res[0])
        else:
            rkeys.append(com)
            r.append([com, res])
    recipes = r

    # Start the Flask application
    app.run()