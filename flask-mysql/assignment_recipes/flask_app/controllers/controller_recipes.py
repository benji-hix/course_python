from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_recipe, model_user


# ----------------- post-validation, redirect to landing page ---------------- #
@app.route('/recipes')
def landing():
    # ensure one can only reach landing page after logging in
    if not session['logged_in']:
        return redirect('/')
    user = model_user.User.login(session['user_id'])
    session['user_name'] = user.first_name
    #! insert additional data/class methods
    all_recipes = model_recipe.Recipe.read_recipes_with_user()

    return render_template('all-recipes.html', user=user, all_recipes=all_recipes)

# ------------------------------ read one recipe ----------------------------- #
@app.route('/recipes/<int:pk>')
def read_recipe(pk):
    recipe = model_recipe.Recipe.read_recipe(pk)
    return render_template('recipe-view.html', recipe = recipe)

# ---------------------------- create recipe page ---------------------------- #
@app.route('/recipe-create')
def create_recipe():
    if not session['logged_in']:
        return redirect('/')
    model_recipe.Recipe.clear_recipe_session()
    return render_template('recipe-create.html')

#* ------------------------------- submit recipe ------------------------------ #
@app.route('/submit-recipe', methods=['POST'])
def submit_recipe():
    if not session['logged_in']:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipe-create')
    recipe_id = model_recipe.Recipe.create_recipe(request.form)
    return redirect('/recipes')

# ----------------------------- edit recipe page ----------------------------- #
@app.route('/recipes/edit/<int:pk>')
def update_recipe(pk):
    if not session['logged_in']:
        return redirect('/')
    recipe = model_recipe.Recipe.read_recipe(pk)
    session['recipe_id'] = pk
    return render_template('recipe-edit.html')

#* --------------------------- submit recipe update --------------------------- #
@app.route('/submit-update', methods = ['POST'])
def submit_update():
    if not session['logged_in']:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipes/edit/' + str(session['recipe_id']))
    model_recipe.Recipe.update_recipe(request.form)
    return redirect('/recipes')
# ------------------------------ delete recipe ------------------------------ #
@app.route('/recipes/delete/<int:pk>')
def delete_recipe(pk):
    if not session['logged_in']:
        return redirect('/')
    model_recipe.Recipe.delete_recipe(pk)
    return redirect('/recipes')
