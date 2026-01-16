# JavaScript Skill

Guidelines for JavaScript development in this project.

## General Rules

### Code Style
- Use ES6+ syntax (const, let, arrow functions, template literals)
- Prefer `const` over `let`, avoid `var`
- Use meaningful variable and function names
- Keep functions small and focused (single responsibility)

### File Organization
- Place scripts at end of `<body>` for performance
- Use separate `.js` files (no inline `<script>` blocks)
- One main purpose per JavaScript file

## DOM Manipulation

### Element Selection
- Prefer `querySelector` and `querySelectorAll`
- Cache DOM references when used multiple times
- Use descriptive variable names for elements

```javascript
// Good
const navLinks = document.querySelector('.nav-links');
const hamburger = document.querySelector('.hamburger');

// Avoid
const x = document.querySelector('.nav-links');
```

### Event Handling
- Use `addEventListener` instead of inline handlers
- Remove event listeners when no longer needed
- Use event delegation for dynamic content

```javascript
// Good
hamburger.addEventListener('click', toggleMenu);

// Avoid (inline in HTML)
// <button onclick="toggleMenu()">
```

## Functions

### Function Declarations
- Use arrow functions for short callbacks
- Use regular functions for methods and constructors
- Add brief comments for complex logic

```javascript
// Arrow function for callback
items.forEach(item => processItem(item));

// Regular function for named functionality
function toggleMenu() {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
}
```

### Function Length
- Keep functions under 25 lines when possible
- Extract complex logic into helper functions
- Each function should do one thing well

## Error Handling

### Defensive Coding
- Check if elements exist before manipulating
- Use try-catch for operations that might fail
- Provide fallbacks for missing features

```javascript
// Check element exists
const element = document.querySelector('.my-element');
if (element) {
    element.classList.add('active');
}

// Try-catch for risky operations
try {
    const data = JSON.parse(jsonString);
} catch (error) {
    console.error('Failed to parse JSON:', error);
}
```

## Best Practices

### Performance
- Minimize DOM queries (cache references)
- Use `requestAnimationFrame` for animations
- Debounce scroll and resize handlers

### Accessibility
- Ensure keyboard navigation works
- Manage focus appropriately
- Support screen readers with ARIA when needed

### Browser Compatibility
- Test in major browsers (Chrome, Firefox, Safari)
- Use feature detection when needed
- Avoid bleeding-edge features without fallbacks

## Example: Navigation Toggle

```javascript
// navigation.js - Mobile menu toggle functionality

document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    if (!hamburger || !navLinks) return;
    
    hamburger.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInside = hamburger.contains(event.target) 
                           || navLinks.contains(event.target);
        
        if (!isClickInside && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });
});
```

## Console and Debugging

### Development
- Use `console.log` for debugging during development
- Remove or comment out debug logs before committing
- Use `console.error` for actual error conditions

### Production
- Minimize console output in production code
- Keep error logging for critical issues
- Consider using a logging utility for complex apps

## Comments

### When to Comment
- Explain "why" not "what" (code shows what)
- Document non-obvious behavior
- Add TODO comments for future improvements

```javascript
// Close menu on outside click to improve UX
document.addEventListener('click', handleOutsideClick);

// TODO: Add keyboard support for accessibility
```