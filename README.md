# recipecard
A collection of recipes.

## Structure
- `index.html`: The main index page that lists all recipes automatically.
- `recipes/`: Folder containing individual recipe HTML files.
- `recipes/template.html`: Template file for creating new recipes.
- `generate_index.py`: Script to regenerate the index.html when new recipes are added.

## Adding a New Recipe
1. Copy `recipes/template.html` to a new file (e.g., `recipes/new-recipe.html`).
2. Replace the placeholders in the HTML (e.g., {{RECIPE_TITLE}}) with your recipe details.
3. Adjust the color variables in the CSS `:root` section for a unique theme (replace the default hex values).
4. Run `python3 generate_index.py` to update the index automatically.

## Color Themes
Each recipe can have its own color theme by changing the CSS variables in `:root`:
- `--primary-color`: Main color (default: #e67e22 for orange)
- `--secondary-color`: Secondary color (default: #f1c40f for yellow)
- `--accent-color`: Accent color (default: #27ae60 for green)
- `--darker-shade`: Darker shade of primary for gradients (default: #d35400)