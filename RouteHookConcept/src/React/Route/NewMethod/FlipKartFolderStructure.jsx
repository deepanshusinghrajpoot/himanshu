import React from 'react'



/*






✅ Where to use Simple Routing
✅ Where to use Deep Nested Routing
✅ Where to use Dynamic Routing

⚡️ Flipkart-like Folder Structure with Routing Strategy

/src
 ├── App.jsx
 ├── main.jsx
 ├── /layout
 │      ├── RootLayout.jsx     // Global Layout with Navbar/Footer
 │      └── AccountLayout.jsx  // Nested layout for user account section
 │
 ├── /components
 │      ├── Navbar.jsx
 │      ├── ProductCard.jsx
 │      ├── FilterSidebar.jsx
 │      ├── Footer.jsx
 │
 ├── /pages
 │      ├── Home.jsx                     // Simple Route (/)
 │      ├── Login.jsx                    // Simple Route (/login)
 │      ├── Signup.jsx                   // Simple Route (/signup)
 │
 │      ├── /products
 │      │      ├── Products.jsx          // Route: /products (All Products Page)
 │      │      ├── Electronics.jsx       // Deep Nested Route: /products/electronics
 │      │      ├── Fashion.jsx           // Deep Nested Route: /products/fashion
 │      │      ├── Laptop.jsx            // Deep Nested Route: /products/electronics/laptop
 │      │      ├── Phone.jsx             // Deep Nested Route: /products/electronics/phone
 │      │      └── ProductDetails.jsx    // Dynamic Route: /products/:productId
 │
 │      ├── /cart
 │      │      └── Cart.jsx              // Simple Route: /cart
 │
 │      ├── /checkout
 │      │      └── Checkout.jsx          // Simple Route: /checkout
 │
 │      ├── /account
 │      │      ├── Account.jsx           // Nested Layout Start: /account
 │      │      ├── Orders.jsx            // Deep Nested Route: /account/orders
 │      │      ├── Profile.jsx           // Deep Nested Route: /account/profile
 │      │      └── Address.jsx           // Deep Nested Route: /account/address
 │
 │      └── NotFound.jsx                 // 404 Route






✅ Routing Breakdown


Simple Routing
URL	Page
/	                      Home.jsx
/login	                  Login.jsx
/signup	                  Signup.jsx
/cart	                  Cart.jsx
/checkout	              Checkout.jsx



Deep Nested Routing
URL	Page
/products	                              Products.jsx (list all) with <Outlet />
/products/electronics	                  Electronics.jsx  with <Outlet/>
/products/electronics/laptop	          Laptop.jsx
/products/electronics/phone	              Phone.jsx
/account	                              Account Layout with <Outlet>
/account/orders	                          Orders.jsx
/account/profile	                      Profile.jsx
/account/address	                      Address.jsx


Dynamic Routing
URL Example	Page
/products/12345	    ProductDetails.jsx (single product by ID)
/products/abc123	ProductDetails.jsx (dynamic by slug/ID)



You can use:
<Route path="products/:productId" element={<ProductDetails />} />





⚡️ Notes
✅ You can nest <Outlet /> inside /account for private sections.
✅ /products/:productId works for every product detail page.
✅ Deep nesting keeps product categories structured.
✅ Simple routes for public pages like Home, Login, etc.



💡 Real Flipkart Example
✅ /products/electronics/laptop → List of Laptops (Nested)
✅ /products/electronics/phone → List of Phones (Nested)
✅ /products/12345 → Specific product details (Dynamic Route)
✅ /account/orders → User orders (Deep Nested inside /account)











*/




const FlipKartFolderStructure = () => {
  return (
    <div>FlipKartFolderStructure</div>
  )
}

export default FlipKartFolderStructure