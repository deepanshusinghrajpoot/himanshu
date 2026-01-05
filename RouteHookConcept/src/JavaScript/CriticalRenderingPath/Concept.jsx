/*

✅ Critical rendering path:

   "The Critical Rendering Path starts by converting HTML into the DOM and CSS into CSSOM. 
   Since CSS is render-blocking, the browser pauses rendering until styles are fully parsed. 
   JavaScript can block HTML parsing unless deferred. Once DOM and CSSOM are complete, 
   the browser builds the Render Tree, calculates layout, paints the page, and finally composites
   the layers to display pixels on the screen."




 ---- Explaination:
  🏗️ "The Critical Rendering Path starts by converting HTML into the DOM..."
  ✔️ The browser reads your HTML and creates a DOM Tree — a structured representation of all the HTML elements on the page.

  🎨 "...and CSS into CSSOM."
  ✔️ Simultaneously (or after), the browser parses all linked or embedded CSS and builds the CSSOM Tree, representing styles.

  ⚠️ "Since CSS is render-blocking, the browser pauses rendering until styles are fully parsed."
  ✔️ Why? The browser cannot safely render anything until it knows what everything should look like. 
  ✔️ That’s why CSS blocks rendering — to prevent showing an unstyled flash.

  🚫 "JavaScript can block HTML parsing unless deferred."
  ✔️ If the browser encounters a <script> tag:

   Without async or defer, it pauses the DOM construction

   It downloads and runs the script immediately (it might change DOM)



  ✅ Use defer to avoid blocking:

  Scripts load in parallel but execute after DOM is ready

 🌲 "Once DOM and CSSOM are complete, the browser builds the Render Tree..."
 ✔️ The Render Tree merges DOM + CSSOM, but:

  Only includes visible elements

  Skips display: none

 📐 "...calculates layout..."
 ✔️ The browser figures out the position and size of each element on screen (this is the Layout or Reflow step).

 🖌️ "...paints the page..."
 ✔️ Then it paints pixels — text, colors, images, shadows — for everything based on the layout.

 🧩 "...and finally composites the layers to display pixels on the screen."
 ✔️ If there are multiple layers (e.g., using CSS transforms), the browser composites them together and sends it to the GPU for final rendering.







✅ Polished Explanation: async vs defer in JavaScript

 In HTML, the <script> tag can use two optional boolean attributes — async and defer — to load JavaScript files more efficiently without blocking HTML parsing.


 🧠 Default Behavior (No Attribute):
 
 
 When the browser encounters a <script> tag without async or defer:
         1. It pauses HTML parsing
         2. Fetches the script from the network
         3. Executes the script immediately
         4. Then resumes HTML parsing


 ⚡ async Attribute:
         1. Scripts are fetched asynchronously, in parallel with HTML parsing.
         2. As soon as the script is ready, HTML parsing pauses, and the script runs.
         3. Parsing resumes only after the script finishes executing.
         ✅ Good for scripts that don’t depend on or manipulate DOM, like analytics.
         🔸 Order of script execution is not guaranteed with async.


 ⏳ defer Attribute:
         1. Scripts are fetched in parallel with HTML parsing.
         2. But they are not executed immediately.
         3. Execution happens only after the entire HTML is parsed (i.e., when DOM is fully built).
         ✅ Best for scripts that need access to the full DOM.
        🔹 defer maintains script order, making it ideal for dependent scripts.


 📊 Summary Table:
           Attribute	    Download	    Execution	            Blocks HTML Parsing?	  Maintains Order?
           None	          Immediately   Immediately	          ✅ Yes	                ✅ Yes
           async	        Parallel	    As soon as ready	    ⚠️ Sometimes	         ❌ No
           defer	        Parallel	    After HTML parsed	    ❌ No	                ✅ Yes



           
----------- Example of async vs defer vs normal script in JavaScript

✅ 1. Without async or defer (Default Behavior)

<!DOCTYPE html>
<html>
  <head>
    <script src="app.js"></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>

          ⛔ What Happens:
                  1. Browser starts parsing HTML.
                  2. Encounters <script> — it pauses parsing.
                  3. Fetches and runs app.js immediately.
                  4. Once script finishes, it resumes parsing the rest of the HTML.
                 ⚠️ This can delay page rendering if the script is large or slow to load.


⚡ 2. Using async

<!DOCTYPE html>
<html>
  <head>
    <script src="analytics.js" async></script>
  </head>
  <body>
    <h1>Hello World</h1>
    <script src="main.js" async></script>
  </body>
</html>

         🚀 What Happens:
                 1. HTML parsing and script downloading happen in parallel.
                 2. As soon as any script finishes downloading, it executes immediately, pausing parsing.
                 3. Scripts may execute in any order (whichever finishes first).
                 ✅ Great for non-blocking scripts like analytics. ❌ Don’t use when script execution order matters.


⏳ 3. Using defer

<!DOCTYPE html>
<html>
  <head>
    <script src="lib.js" defer></script>
    <script src="main.js" defer></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>

         📌 What Happens:
                 1. Scripts are downloaded in parallel with HTML parsing.
                 2. All defer scripts are executed in order, but only after HTML is fully parsed.
                 3. DOM is ready when scripts run.
                ✅ Perfect for main app logic, DOM manipulations. ✅ Order is preserved.





*/