import React from 'react'


/*



⚡️ React Router Deeply Nested Routing Example
Folder Structure

/src
 ├── App.jsx
 ├── /layout
 │      └── RootLayout.jsx
 ├── /pages
 │      ├── Home.jsx
 │      ├── Products.jsx
 │      ├── Electronics.jsx
 │      ├── Laptop.jsx
 ├── /components
 │      └── Navbar.jsx





1️⃣ App.jsx — Define Nested Routes

import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import RootLayout from "./layout/RootLayout";
import Home from "./pages/Home";
import Products from "./pages/Products";
import Electronics from "./pages/Electronics";
import Laptop from "./pages/Laptop";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>

      <Route index element={<Home />} />

      {/* Products with Nested Routes }
      <Route path="products" element={<Products />}>
        
        {/* Electronics inside Products *}
        <Route path="electronics" element={<Electronics />}>

          {/* Laptop inside Electronics *}
          <Route path="laptop" element={<Laptop />} />

        </Route>

      </Route>

    </Route>
  )
);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;





2️⃣ RootLayout.jsx

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
3️⃣ Navbar.jsx
jsx
Copy
Edit
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <ul>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/products">Products</Link></li>
      <li><Link to="/products/electronics">Electronics</Link></li>
      <li><Link to="/products/electronics/laptop">Laptop</Link></li>
    </ul>
  );
};

export default Navbar;





4️⃣ Products.js

import { Outlet } from "react-router-dom";

const Products = () => {
  return (
    <div>
      <h2>Products Page</h2>
      <Outlet />
    </div>
  );
};

export default Products;





5️⃣ Electronics.jsx

import { Outlet } from "react-router-dom";

const Electronics = () => {
  return (
    <div>
      <h3>Electronics Section</h3>
      <Outlet />
    </div>
  );
};

export default Electronics;







6️⃣ Laptop.jsx

const Laptop = () => {
  return (
    <div>
      <h4>Laptop Details Page</h4>
    </div>
  );
};

export default Laptop;




✅ Final URL Examples
URL	Renders
/                                         Home Page
/products	                              Products Page
/products/electronics	                  Electronics Section inside Products
/products/electronics/laptop	          Laptop Page inside Electronics inside Products




⚡️ Conclusion
Deep nested routes possible with <Outlet />
You can nest routes inside routes indefinitely
Layout structure remains clean




*/



const NestedRouting = () => {
  return (
    <div>NestedRouting</div>
  )
}

export default NestedRouting