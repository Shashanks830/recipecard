# recipecard
A collection of recipes with a consistent, professional design.

## Structure
- `index.html`: The main index page that lists all recipes automatically.
- `recipes/`: Folder containing individual recipe HTML files.
- `recipes/styles.css`: Shared CSS file with all common styling for recipe pages.
- `recipes/template.html`: Template file for creating new recipes.
- `generate_index.py`: Script to regenerate the index.html when new recipes are added.

## Creating a New Recipe
1. Copy `recipes/template.html` to a new file (e.g., `recipes/new-recipe.html`).
2. Replace the content placeholders (e.g., `{{RECIPE_TITLE}}`) with your recipe details.
3. Customize the color theme by modifying the CSS variables in the `<style>` tag (you only need to define the four color variables).
4. Run `python3 generate_index.py` to add the new recipe to the index automatically.

## How the CSS Works
- **styles.css**: Contains all common styles and responsive design rules. This file is shared by all recipes.
- **Per-recipe color variables**: Each recipe HTML file has a small `<style>` section that defines only the four color variables:
  - `--primary-color`: Main color (e.g., #e67e22 for orange, #e74c3c for red)
  - `--secondary-color`: Secondary color (e.g., #f1c40f for yellow)
  - `--accent-color`: Accent color (e.g., #27ae60 for green)
  - `--darker-shade`: Darker shade of primary color for backgrounds

This separation makes it easy to:
- Maintain consistency across all recipes
- Update styles globally by editing one CSS file
- Create new recipes quickly with different color themes