/*
   
   ================================== React Routing =====================================
    
   1. React Routing
   2. Link & NavLink Tags
   3. UseNavigate Hook
   4. Nested Routes
   5. Custom 404 Page
   6. React Router Loader
   7. Route Parameters and Dynamic Routing
   8. React Router Error Element
   

   ************************** What is page routing ********************************


   ************************** What is React Router ********************************

   React Router is a javaScript framework that allow us to handle client and server side routing in the react application.
   It enable the creation of single page web or mobile application that allow navigation without refreshing the web page.
   
   It mean when we using react router and when navigate the web page from one page to onother then web page not reload.
   The react router is powerfull tool that can be use to create complex and dynamic web application.
   




   ----------------- Implement react router in react project ------------------------
   install package:- npm i react-router-dom

   first:- import BrowserRouter from react-router-dom and wrap App component inside the main.jsx from BrowserRouter to get suport of brouser routing.
   second:- import Routes, Route from react-router-dom inside the App Component and wrap Route(self cloging tag) using Routes.
            And in Route tag we provide two item  (1) path='' , (2) element={}
   third:- import Link from react-router-dom and wrap the tag eg:- <Link to='path' ><li>Home</li></Link> and provide path
   

   ----------------- Implement react router in react project(NEW METHOD) ------------------------         
   this NEW METHOD is implemented new folder:- frontends and inside the frontends folder

   first:-  import createBrowserRouter, createRoutesFromElements, Route, RouterProvider from react-router-dom inside the App component and use

   const App = () => {
      const router = createBrowserRouter(
            createRoutesFromElements(
                <Route path='/' element={<RootLayout />} >
                    <Route index element={<Home />} />
                    <Route path='about' element={<About />} />
                </Route>
            )
      )

      return (
                <RouterProvider router={router} />
      )

    }

    second:- frontends/src/layout/RootLayout :- import outlet from react-router-dom
      
         const RootLayout = () => {
              return (
                         <div>
                              <Navebar />
                              <Outlet />
                         </div>
              )
         }
     
    
    third:-  import Link from react-router-dom
             <ul>
                  <Link to='/' ><li>Home</li></Link>
                  <Link to='/about' ><li>About</li></Link>
                  <Link to='/products' ><li>Products</li></Link>
                  <Link to='/contact' ><li>Contact</li></Link>
             </ul>




    ************************** Difference in Link & NavLink Tag  ********************************
    
    when we use Link tag then in console convert itself anchor tag and it not contain any extra class after click
    <Link to='/' ><li>Home</li></Link> => console = <a href="/" data-discover="true"><li>Home</li></a>
    
    when we use NavLink tag then in console convert itself anchor tag and it contain an active extra class after click
    <Link to='/' ><li>Home</li></Link> => console = <a href="/" data-discover="true"><li>Home</li></a>


    ************************** Routing with useNavigate Hook ********************************
    
    when we click Link and NavLink tag it is starte forword way to navigate b/w route

    But some the you want to navigate programaticaly lick redirecting after
    - form submition
    - navigating based on user action
    - implementing back button
    - passing state b/w route

    In these condition we can use useNavigate Hook



    first:- import useNavigate hook from react-router-dom where we want to use 
     
    const Navbar = () => {
       
        const navigate = useNavigate();

        return (
            <button onClick={()=> navigate('/useState')} >Get Started</button>
        )  
    }



    useNavigate hook have one more feature

    when we nagvigate then navigation history store in history stack

    It is use to replace current location inside history stack or navigate to forword and backword in history stack 
     
    <button onClick={()=> navigate('/contact',{replace: true})} >Get Started</button>

    Here previous location is replace to contact



    ************************** NESTED ROUTE ********************************

    nested routes are powerfull feature :- see inside the frontends folder

    first:- frontends/src/layout/ContactLayout :- import Outlet from react-router-dom

          const Contactlayout = () => {
                 return (
                           <div>
                               <Contact />
                               <Outlet />
                           </div>
                 )
           }
    
    Second:- frontends/App

    const router = createBrowserRouter(
          createRoutesFromElements(
             <Route path='/' element={<RootLayout />} >
                  <Route index element={<Home />} />
                  <Route path='contact' element={<ContactLayout />} >
                      <Route path='info' element={<ContactInfo />} />
                      <Route path='info' element={<ContactForm />} />
                  </Route>
             </Route>
          )
    )

    ************************** CREATE 404 PAGE ********************************

    using that route which is not exist then reach to 404 page on our website 
    404 page can also help to truble shoot problem in our website by providing information about error that occur.  

   
    ************************** REACT ROUTER LOADER ********************************
    
    react router loader is function that use to fetch data for a route before it is render

    


*/