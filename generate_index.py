import os
import re

recipes = []
for file in os.listdir('recipes'):
    if file.endswith('.html'):
        with open(f'recipes/{file}', 'r') as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content)
            if match:
                title = match.group(1)
                recipes.append((title, file))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Index</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #d4af37;
            text-align: center;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            margin: 15px 0;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }}
        a {{
            text-decoration: none;
            color: #8b4513;
            font-size: 20px;
            font-weight: bold;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Recipe Collection</h1>
        <ul>
"""

for title, file in sorted(recipes):
    html += f'            <li><a href="recipes/{file}">{title}</a></li>\n'

html += """        </ul>
    </div>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)