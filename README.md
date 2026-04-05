# recipecard
A collection of recipes.

## Structure
- `index.html`: The main index page that lists all recipes automatically.
- `recipes/`: Folder containing individual recipe HTML files.
- `generate_index.py`: Script to regenerate the index.html when new recipes are added.

## Adding a New Recipe
1. Create a new HTML file in the `recipes/` folder with the recipe content.
2. Run `python3 generate_index.py` to update the index automatically.