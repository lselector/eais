# HTML & CSS Skill

Guidelines for HTML and CSS development in this project.

## HTML Rules

### Semantic Structure
- Use semantic HTML5 elements: `<header>`, `<nav>`, `<main>`, 
  `<section>`, `<article>`, `<footer>`
- Use `<h1>` only once per page (in header)
- Use heading hierarchy properly: h1 → h2 → h3 (no skipping)
- Use `<ul>` or `<ol>` for lists, not divs with line breaks

### Accessibility
- All images must have `alt` attributes
- Links must have descriptive text (not "click here")
- Use `title` attribute for icon-only links
- External links should have `target="_blank"` with 
  `rel="noopener"` for security

### Document Structure
- Include proper `<!DOCTYPE html>` declaration
- Set `lang="en"` on html element
- Include meta viewport for responsive design
- Include meta description for SEO

### Example HTML Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" 
          content="width=device-width, initial-scale=1.0">
    <title>Page Title - Site Name</title>
    <meta name="description" content="Page description">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>...</header>
    <main>...</main>
    <footer>...</footer>
    <script src="navigation.js"></script>
</body>
</html>
```

## CSS Rules

### File Organization
- All styles go in `styles.css` (no inline styles)
- Do not put `<style>` blocks in HTML files
- Group related styles together with comments

### Naming Conventions
- Use lowercase with hyphens: `.nav-links`, `.content-section`
- Use descriptive class names that indicate purpose
- Avoid overly generic names like `.box` or `.container1`

### Responsive Design
- Mobile-first approach when possible
- Use media queries for breakpoints
- Common breakpoint: `@media (max-width: 768px)`
- Use relative units (rem, em, %) over fixed pixels

### CSS Structure Order
Organize properties in this order:
1. Layout (display, position, flex, grid)
2. Box model (width, height, margin, padding)
3. Typography (font, text, color)
4. Visual (background, border, shadow)
5. Animation (transition, animation)

### Example CSS
```css
/* Navigation styles */
.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-color);
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: var(--accent-color);
}
```

### CSS Variables
- Define colors and common values as CSS variables
- Place variables in `:root` selector
- Use meaningful variable names

```css
:root {
    --primary-color: #2c3e50;
    --accent-color: #3498db;
    --text-color: #333;
    --background-color: #fff;
}
```

## Best Practices

### Performance
- Minimize CSS specificity conflicts
- Avoid `!important` unless absolutely necessary
- Use shorthand properties when appropriate

### Maintainability
- Comment major sections of CSS
- Keep selectors simple (max 3 levels deep)
- Remove unused CSS when refactoring

### Consistency
- Use consistent spacing (2 or 4 spaces for indentation)
- Keep line length reasonable (under 80 characters)
- Maintain consistent formatting throughout