import React from 'react'




/*


✅ Q1. What is the role of DOCTYPE in HTML?

✔ <!DOCTYPE html> tells the browser which version of HTML to use.
✔ It ensures the browser renders the page in standards-compliant mode rather than quirks mode.
✔ Prevents inconsistent behavior across browsers.

Example:

<!DOCTYPE html>
<html>
  <head></head>
  <body></body>
</html>
✅ Modern HTML uses <!DOCTYPE html> for HTML5.





✅ Q2. What are Meta Tags? What are their types?
✔ Meta tags provide metadata (information about the page) to browsers and search engines.
✔ They reside in the <head> section and do not display on the page.

Common Meta Tags:

Meta Type	                     Purpose
charset	                         Defines character encoding (e.g., UTF-8)
viewport	                     Enables responsive design for devices
description	                     Brief description for SEO
keywords	                     Keywords for SEO (less used today)
author	                         Specifies the author of the document



Example:

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Portfolio of Deepanshu Singh">
<meta name="keywords" content="React, MERN, JavaScript">
<meta name="author" content="Deepanshu Singh">




✅ Q3. Difference between <div> and <span>?
Aspect	                   <div>	                                <span>
Display Type	           Block-level element	                    Inline element
Usage	                   Structural grouping	                    Styling small content
Layout Effect	           Breaks to new line	                    Stays within the line




✅ Q4. What are Semantic Elements in HTML? Is <div> semantic?
✔ Semantic elements clearly describe their meaning both to the browser and developer.
✔ Improves accessibility and SEO.

Examples of Semantic Elements:
<header>, <main>, <section>, <article>, <footer>, <nav>, <aside>, <address>

✔ <div> is non-semantic, used for layout without conveying specific meaning.





✅ Q5. Difference between Block-Level and Inline Elements
Feature	                  Block-Level Elements	                         Inline Elements
Layout	                  Start on a new line	                         Do not break to new line
Width	                  Occupies full available width	                 Only occupies necessary width
Examples	              <div>, <p>, <section>, <h1>	                 <span>, <a>, <strong>, <img>





✅ One-Liner Ready Answers for Quick Interviews
✔ DOCTYPE ensures correct HTML rendering mode
✔ Meta tags add page metadata for SEO & functionality
✔ <div> = block container, <span> = inline container
✔ Semantic elements provide meaning, <div> is not semantic
✔ Block elements break lines, Inline elements stay within lines










✅ Q6. Difference between Absolute and Relative URLs
Aspect	              Absolute URL	                                                                  Relative URL
Definition	          Complete path to a resource, including protocol and domain	                  Partial path relative to current document
Usage	              Links to external websites or full resource address	                          Links within the same website or project
Example	              https://www.google.com/images/logo.png	                                      images/logo.png or ../assets/logo.png


Absolute URL Example

<a href="https://www.openai.com/">Visit OpenAI</a>
<img src="https://cdn.site.com/images/banner.jpg">
✔ Points to a resource on a different website or complete external path.


Relative URL Example

<a href="/about.html">About Us</a>
<img src="images/profile.png">
✔ Refers to resources within the same domain or project folder.
✔ Easier for internal linking and better during website migrations.

✅ Quick Interview One-Liner
"Absolute URLs contain the full web address, ideal for external links, while Relative URLs point to resources relative to the current page, ideal for internal navigation."









✅ Q7. What are HTML Form Elements and Their Main Attributes?
✔ Forms are used to collect user input in web pages.

🔹 Common Form Elements & Attributes
Element	Purpose	Important Attributes
<form>	Container for form controls	action, method
<label>	Defines label for inputs	for (associates label with input id)
<input>	User input field	type, name, id, value, placeholder
<textarea>	Multi-line text input	name, rows, cols, placeholder
<button>	Clickable button	type (e.g., submit, reset, button)
<select>	Dropdown menu	name
<option>	Dropdown options	value

✅ Example Form with Attributes
html
Copy
Edit
<form action="/submit" method="POST">
   <label for="username">Username:</label>
   <input type="text" id="username" name="username" placeholder="Enter name">

   <label for="password">Password:</label>
   <input type="password" id="password" name="password">

   <button type="submit">Submit</button>
</form>
✔ action — Where form data is sent
✔ method — HTTP method (GET or POST)
✔ label for — Connects label to input
✔ type, name — Define input behavior and key for data

✅ Q8. What is SEO? What are 5 HTML Best Practices for SEO?
✔ SEO (Search Engine Optimization) improves a website's visibility on search engines like Google, increasing traffic and ranking.
✔ HTML structure plays a key role in SEO.

🔹 Top 5 HTML Best Practices for SEO
Practice	                                       Benefit
1. Use Semantic HTML	                           Helps search engines understand content
2. Optimize Page <title>	                       Improves click-through rates, defines page purpose
3. Use <meta name="description">	               Adds summary for search snippets
4. Proper Heading Hierarchy (<h1> to <h6>)	       Organizes content, boosts SEO
5. Use alt Attributes for Images	               Improves accessibility & image indexing




✅ Example for SEO Optimization

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Best React Developer - Deepanshu Singh</title>
    <meta name="description" content="Portfolio of Deepanshu Singh, React & MERN Stack Developer">
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
    </header>
    <img src="profile.jpg" alt="Profile picture of Deepanshu Singh">
</body>
</html>

Quick SEO One-Liner for Interviews
"SEO ensures your website ranks higher by using semantic HTML, optimized titles, descriptions, headings, and image alt tags."






✅ Basic HTML Questions:
1. What is HTML?
HTML (HyperText Markup Language) is the standard markup language used to create and structure web pages.

2. What is the difference between HTML and HTML5?
HTML5 is the latest version of HTML with new semantic elements, multimedia support (audio/video), APIs (Canvas, Web Storage), and better performance.

3. What are semantic elements?
Semantic elements clearly describe their meaning in a human- and machine-readable way (e.g., <header>, <footer>, <article>, <section>).

4. What is the purpose of the <DOCTYPE html> tag?
It informs the browser about the HTML version being used (HTML5 uses <!DOCTYPE html>).







✅ HTML5 New Features:
5. List some new tags introduced in HTML5.
<header>, <footer>, <section>, <article>, <nav>, <figure>, <figcaption>, <aside>, <main>, <mark>, <time>.

6. What are HTML5 form input types?
text, email, number, url, date, range, color, tel, search, datetime-local, month, week, time.

7. What is the difference between <canvas> and <svg>?
<canvas> draws graphics via JavaScript and is pixel-based.
<svg> draws vector-based graphics (XML-based).

8. What is localStorage and sessionStorage?
localStorage: Stores data with no expiration (until cleared).
sessionStorage: Stores data for the session (cleared when tab closes).







✅ Advanced HTML5 Questions:
9. What is the use of data-* attributes?
Custom data attributes used to store extra information without affecting layout or style (e.g., <div data-id="123">).

10. Difference between id and class attributes?
id: Unique, one element per page.
class: Reusable, can be applied to multiple elements.


11. What is the difference between <div> and <section>?
<div> is a generic container. <section> is a semantic container representing a standalone section.


12. What is the difference between <b> vs <strong> and <i> vs <em>?
<b> and <i> are for styling (bold/italic).
<strong> and <em> have semantic meaning (importance/emphasis).








✅ Multimedia and APIs:

13. How to embed video/audio in HTML5?
<video controls src="video.mp4"></video>
<audio controls src="audio.mp3"></audio>

14. What is the use of the Geolocation API?
Allows a website to access user location (via navigator.geolocation.getCurrentPosition()).

15. What is the difference between defer and async?
async: Script runs as soon as it’s downloaded (not in order).
defer: Script runs after HTML parsing completes (in order).






✅ Best Practices and Miscellaneous:
16. Why use semantic tags?
Improves accessibility.
Helps SEO.
Makes code more readable.

17. What is the difference between <link> and <@import>?
<link> is faster and preferred for CSS.
@import is slower, used inside CSS files.

18. Can HTML5 work without CSS and JS?
Yes, HTML structures the content; CSS styles it, and JavaScript adds interactivity.









*/



const Top10Html = () => {
  return (
    <div>Top10Html</div>
  )
}

export default Top10Html