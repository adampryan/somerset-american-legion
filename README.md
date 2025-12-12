# Somerset American Legion Post 228 Website

A complete, modern website for Somerset American Legion Post 228.

## Project Structure

```
somerset-american-legion/
├── index.html              # Home page
├── about.html              # About page
├── contact.html            # Contact page with form
├── history.html            # History page
├── membership.html         # Membership overview
├── hall-rental.html        # Hall rental information
├── ... (additional pages)
├── css/
│   └── style.css           # Main stylesheet
├── js/
│   └── main.js             # JavaScript functionality
└── images/
    └── (add your images here)
```

## Setup Instructions

1. **Upload to your web host** - Upload all files to your web hosting provider (e.g., GoDaddy, Bluehost, etc.)

2. **Add Images** - Add the following images to the `images/` folder:
   - `legion-emblem.png` - American Legion emblem (can be downloaded from legion.org)
   - `hero-1.jpg`, `hero-2.jpg`, `hero-3.jpg` - Hero slider images (1920x600px recommended)
   - Any additional photos for the gallery

3. **Update Content** - Edit the HTML files to update:
   - Officer names and positions
   - Event dates and details
   - Hall rental rates
   - Any other post-specific information

4. **Configure Forms** - The contact and application forms need a backend to process submissions. Options:
   - Use a form service like Formspree, Netlify Forms, or Google Forms
   - Set up server-side processing (PHP, etc.)
   - Contact your web host for form handling options

## Features

- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **Modern Styling** - Patriotic color scheme with professional typography
- **Easy Navigation** - Dropdown menus for organized content
- **Hero Slider** - Automatic image slider on the home page
- **Contact Forms** - Ready-to-use forms (requires backend setup)
- **Google Maps** - Embedded map showing post location
- **Social Media** - Links to Facebook and Twitter

## Customization

### Colors
Edit the CSS variables in `css/style.css`:
```css
:root {
    --navy: #1a2744;
    --red: #a50000;
    --gold: #c9a227;
    /* ... */
}
```

### Fonts
The site uses Google Fonts:
- **Cinzel** - Headings (elegant, classic feel)
- **Source Sans 3** - Body text (clean, readable)

### Adding Pages
Use the existing pages as templates. Key elements:
1. Copy an existing page structure
2. Update the `<title>` and meta description
3. Update the page header and breadcrumb
4. Add your content
5. Link to the new page in the navigation

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Credits

- Font Awesome icons (https://fontawesome.com)
- Google Fonts (https://fonts.google.com)
- Google Maps embed

## Contact

Somerset American Legion Post 228
55 Roosevelt Avenue
Somerset, MA 02726
Phone: 508-679-2380
Email: somersetamericanlegion@gmail.com

---

*"Still Serving America!"*
