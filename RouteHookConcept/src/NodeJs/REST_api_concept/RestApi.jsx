import React from 'react'



/*




🚀 REST API – Best Possible Explanation (Node.js Focus, Interview Perfect)


🟦 What is a REST API?
----------------------

lll “A REST API (Representational State Transfer API) is a way for two systems communicate 
over HTTP using a set of architectural rules—like statelessness, uniform interfaces, and resource-based operations. 
REST treats everything as a resource and allows clients to perform actions on those resources using standard HTTP methods.”



✅ 1. Statelessness (Very Simple Explanation)
..................................................

lll “Stateless means the server does not remember anything about the client.
     Every request must contain everything needed.”

🟦 Example:

If you login once, the server does NOT remember it.
So every request must send the token again.

➡️ Server does not store session → Client provides data every time.



✅ 2. Uniform Interface
.........................

lll “Uniform interface means the API follows one standard way to access all resources.”

🟦 Example:

We always use:

GET → to fetch

POST → to create

PUT → to update

DELETE → to remove

No matter which resource it is: users, products, orders, anything.

➡️ Same rules for all API endpoints → easy to understand and predictable.





✅ 3. Resource-Based Operations (Very Simple Explanation)
..........................................................

lll “Everything is treated as a resource, and each resource has its own URI.”

🟦 Example:

/users → Users resource

/products → Products resource

/orders/10 → Order with ID 10

We perform actions on these resources using HTTP methods.
We don’t use verbs in the URL — only nouns.

➡️ Focus is on resources, not actions.



⭐ Ultra-Simple One-Liner (Super Interview Friendly)**
.......................................................

Statelessness → Server doesn’t remember anything; client sends info every time.
Uniform Interface → Same standard way to access all resources.
Resource-Based → Everything is a resource accessed via a URI.








🟦 REST HTTP Methods – With Clean Examples
-------------------------------------------            

..... is use to 

| Method     | Meaning                     | Example           |
| ---------- | --------------------------- | ----------------- |
| **GET**    | Fetch a resource            | `GET /users`      |
| **POST**   | Create a resource           | `POST /users`     |
| **PUT**    | Fully update a resource     | `PUT /users/1`    |
| **PATCH**  | Partially update a resource | `PATCH /users/1`  |
| **DELETE** | Remove a resource           | `DELETE /users/1` |



🟦 Important REST API Concepts in Node.js
------------------------------------------

1. Route Handling
..................

“Routes map HTTP methods to controller functions.”

app.get('/users', getUsers);


2. Controllers
..............

“Controllers contain the business logic for handling a request.”

const getUsers = (req, res) => {
  res.json({ message: "All Users" });
};



3. Middleware
.............

“Middleware handles tasks like authentication, validation, error handling, and parsing data before the request reaches the controller.”

app.use(express.json());



4. Status Codes
...............

lll “REST APIs use proper status codes to clearly indicate the result of the request.”

Code	Meaning
200     OK	
201     Created	
400     Bad Request	
401     Unauthorized	
404     Not Found	
500     Internal Server Error




🟦 One-Shot Interview Explanation (Best Version – 30 to 40 seconds)

“REST API is an architectural style where the server exposes resources using unique URIs, 
and clients interact with those resources using standard HTTP methods like GET, POST, PUT, PATCH, and DELETE. 
REST is stateless, meaning every request must contain all the information the server needs. In Node.js, 
we build REST APIs using routes, controllers, and middleware. Data is exchanged in JSON format, 
proper status codes are used to indicate results, and consistent error handling makes the API predictable. 
Authentication is usually done using JWT. Overall, REST provides a simple, scalable, and standardized way 
for communication between client and server.”




*/










const RestApi = () => {
  return (
    <div>RestApi</div>
  )
}

export default RestApi