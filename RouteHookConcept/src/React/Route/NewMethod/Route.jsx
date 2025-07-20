import React from 'react'


/*




🚀 React Router DOM (New Method) — Step by Step Setup




1️⃣ Installation
npm install react-router-dom





2️⃣ Project Structure Example

/frontends
 ├── /src
       ├── App.jsx
       ├── main.jsx
       ├── /layout
             └── RootLayout.jsx
       ├── /pages
             ├── Home.jsx
             ├── About.jsx
             ├── Products.jsx
             ├── Contact.jsx
       ├── /components
             └── Navbar.jsx





3️⃣ App.jsx — Router Setup

import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import RootLayout from "./layout/RootLayout";
import Home from "./pages/Home";
import About from "./pages/About";
import Products from "./pages/Products";
import Contact from "./pages/Contact";

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<RootLayout />}>
        <Route index element={<Home />} />
        <Route path="about" element={<About />} />
        <Route path="products" element={<Products />} />
        <Route path="contact" element={<Contact />} />
      </Route>
    )
  );

  return <RouterProvider router={router} />;
};

export default App;





4️⃣ RootLayout.jsx — Common Layout with <Outlet />

import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";

const RootLayout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export default RootLayout;





5️⃣ Navbar.jsx — Navigation Links

import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <ul>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/about">About</Link></li>
      <li><Link to="/products">Products</Link></li>
      <li><Link to="/contact">Contact</Link></li>
    </ul>
  );
};

export default Navbar;





6️⃣ Sample Pages (Home.jsx, About.jsx, etc.)

const Home = () => <h1>Home Page</h1>;
export default Home;
Similarly create About.jsx, Products.jsx, Contact.jsx.





7️⃣ main.jsx — Application Entry Point

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(<App />);










✅ Key Notes for Interviews
createBrowserRouter is part of React Router v6.4+
It provides advanced routing with better code splitting and data loading
<Outlet /> renders the nested child routes inside the layout
RouterProvider injects the router into your application







 */

const Route = () => {
  return (
    <div>Route</div>
  )
}

export default Route