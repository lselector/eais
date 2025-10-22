# eAIs Website

A professional static website for eAIs - Enterprise AI Solutions.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Professional blue gradient theme with liquid design
- **Pure HTML/CSS/JavaScript**: No frameworks or dependencies required
- **Hamburger Menu**: Mobile-friendly navigation that converts to hamburger menu on small screens
- **Interactive Slideshow**: Browse through project demonstrations and services
- **Contact Form**: Client-side form validation (ready for backend integration)

## Pages

1. **Home (index.html)**: Main landing page with service overview and demos
2. **About (about.html)**: Company information, team members, and values
3. **Services (services.html)**: Detailed description of all services offered
4. **Contact (contact.html)**: Contact form and company information
5. **Slides (slides.html)**: Interactive slideshow of projects and demonstrations

## File Structure

```
website/
├── index.html          # Home page
├── about.html          # About page
├── services.html       # Services page
├── contact.html        # Contact page
├── slides.html         # Slides/demos page
├── styles.css          # All CSS styles
├── navigation.js       # Navigation functionality
├── server.py           # Python HTTP server
├── README.md           # This file
└── images/             # Image assets
    ├── Lev.jpg
    ├── Dima.jpg
    ├── RAG_demo.png
    ├── diagram.png
    ├── icon-linkedin.svg
    ├── icon-github.svg
    └── icon-youtube.svg
```

## Running the Website

### Option 1: Using Python Server (Recommended)

The included Python server will run the website on port 3000:

```bash
cd website
python server.py
```

Then open your browser to: http://localhost:3000

### Option 2: Using Python's Built-in HTTP Server

```bash
cd website
python -m http.server 3000
```

Then open your browser to: http://localhost:3000

### Option 3: Using Node.js http-server

If you have Node.js installed:

```bash
cd website
npx http-server -p 3000
```

### Option 4: Open Directly in Browser

You can also open `index.html` directly in your browser, though some features may work better with a local server.

## Design Features

### Color Scheme
- Primary Blue: #0066cc
- Secondary Blue: #0099ff
- Dark Blue: #003366
- Light Blue: #e6f2ff
- Accent Blue: #00ccff

### Responsive Breakpoints
- Desktop: > 768px
- Tablet: 481px - 768px
- Mobile: ≤ 480px

### Navigation
- Desktop: Horizontal navigation bar
- Mobile: Hamburger menu (≤ 768px)
- Active page highlighting
- Smooth transitions

## Customization

### Changing Colors
Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-blue: #0066cc;
    --secondary-blue: #0099ff;
    /* ... other colors ... */
}
```

### Adding New Pages
1. Create a new HTML file based on existing page templates
2. Add navigation link in the header of all pages
3. Update the navigation.js if needed

### Modifying Content
All content is in the HTML files. Simply edit the text within the HTML tags.

## Browser Compatibility

- Chrome/Edge: ✓ Fully supported
- Firefox: ✓ Fully supported
- Safari: ✓ Fully supported
- Mobile browsers: ✓ Fully supported

## Technologies Used

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript (ES6+)
- Python 3 (for local server)

## Notes

- The contact form currently uses client-side JavaScript for demonstration
- In production, you would need to add backend functionality to handle form submissions
- All images should be placed in the `images/` directory
- The website is fully static and can be hosted on any web server or CDN

## License

Copyright © 2025 eAIs - Enterprise AI Solutions. All rights reserved.
