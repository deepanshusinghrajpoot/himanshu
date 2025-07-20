import React from 'react'


/*

⚡️ React Router — Nested Routing Example
1️⃣ Basic Project Structure
bash
Copy
Edit
/src
 ├── App.jsx
 ├── main.jsx
 ├── /layout
 │      └── RootLayout.jsx
 ├── /pages
 │      ├── Home.jsx
 │      ├── About.jsx
 │      ├── Products.jsx
 │      ├── ProductDetails.jsx
 │      ├── Contact.jsx
 ├── /components
 │      └── Navbar.jsx
2️⃣ App.jsx — Define Nested Routes
jsx
Copy
Edit
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
import RootLayout from "./layout/RootLayout";
import Home from "./pages/Home";
import About from "./pages/About";
import Products from "./pages/Products";
import ProductDetails from "./pages/ProductDetails";
import Contact from "./pages/Contact";

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<RootLayout />}>

        <Route index element={<Home />} />
        <Route path="about" element={<About />} />

        {/* Products Route with Nested Child Route }
        <Route path="products" element={<Products />}>
          <Route path=":productId" element={<ProductDetails />} />
        </Route>

        <Route path="contact" element={<Contact />} />

      </Route>
    )
  );

  return <RouterProvider router={router} />;
};

export default App;
3️⃣ RootLayout.jsx — Common Layout with <Outlet />
jsx
Copy
Edit
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
4️⃣ Navbar.jsx — Navigation
jsx
Copy
Edit
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
5️⃣ Products.jsx — Parent Route with Nested <Outlet />
jsx
Copy
Edit
import { Link, Outlet } from "react-router-dom";

const Products = () => {
  return (
    <div>
      <h2>Products Page</h2>
      <ul>
        <li><Link to="1">Product 1</Link></li>
        <li><Link to="2">Product 2</Link></li>
      </ul>

      <Outlet />
    </div>
  );
};

export default Products;





6️⃣ ProductDetails.jsx — Access Dynamic productId
jsx
Copy
Edit
import { useParams } from "react-router-dom";

const ProductDetails = () => {
  const { productId } = useParams();

  return (
    <div>
      <h3>Details for Product ID: {productId}</h3>
    </div>
  );
};

export default ProductDetails;









✅ Summary
Nested Route: <Route path="products" element={<Products />}> contains a child <Route path=":productId" ... />

Inside Products.jsx, <Outlet /> renders the nested ProductDetails based on URL

Access dynamic params using useParams()


 */
const DynamicRouting = () => {
  return (
    <div>DynamicRouting</div>
  )
}

export default DynamicRouting