/*



⚡ Lazy Loading in React – Complete Guide

🚀 What is Lazy Loading?
lll Lazy loading is a performance optimization technique where components are loaded only when needed.
    Instead of bundling the entire app upfront, we split it and load pieces dynamically.

💡 Example: If a user never visits the "About" page, why load that code on the homepage?


🔍 Skills Tested
React.lazy() and Suspense
Code Splitting
Build Optimization (Vite / Webpack)
Performance Tuning


⚙️ Code Example:

import React, { lazy, Suspense } from "react";

const About = lazy(() => import('./pages/About'));

function App() {
  return (
    <div>
      <h1>My App</h1>
      <Suspense fallback={<p>Loading...</p>}>
        <About />
      </Suspense>
    </div>
  );
}


export default App;


✅ lll  Suspense handles the loading UI while the component is being fetched.
✅ lll  fallback prop defines what to render during the load delay.







npm create vite@latest

📦 Vite and Lazy Loading (React)  
🧪lll Development Mode – npm run dev
Vite serves each module separately on demand.

    lll Lazy loading still works, 
but:
    lll You/We won’t see "code-split chunks" clearly in DevTools.
    lll because Files are loaded individually (ES Modules).



🏗️ lll Production Mode – npm run build
Vite uses Rollup under the hood to:

   lll Bundle your/our app
   lll Minify, optimize, and split the code



✅ Creates a dist/ folder containing:

Asset Type	Description
*.js	                  Optimized JavaScript chunks (split if lazy)
*.css	                  Minified CSS files
*.png / *.svg	          Assets with hashed names for caching
index.html	              Main HTML entry point
Code-Split Files	      Separate .js chunks for lazy-loaded components



🔎 To Preview the Production Build

npm run preview
Open DevTools → Network tab → JS
Navigate to a lazy-loaded route


💡 You’ll now see separate JS files like:
About.8e24bf78.js
Contact.3a2ff1a9.js



✅ These files are loaded only when needed – this is lazy loading in action!



🧠 Why It Matters
Less JavaScript on initial load
Faster first paint
Only downloads the code the user actually uses














⚠️ Important Rule: Use Default Exports for Lazy Components
React.lazy() expects a default export:

// ✅ Works
export default function About() { ... }
If you're using named exports:


export function About() { ... } // ❌ won't work directly
Then you must do:


const About = lazy(() => import('./About').then(module => ({ default: module.About })));


🔁 Summary: Why Use Lazy Loading?
    ✅ Reduces initial bundle size
    ✅ Improves page load performance
    ✅ Enhances user experience on slower networks
    ✅ Helps in code splitting and reducing unused JavaScript








*/