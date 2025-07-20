import React from 'react'
import UseContextExample1 from './UseContextExample1'

const UseContext = () => {
  /*
     =================== useContext ===================

     useContext React Hook that allows you/us access data from any component without
     explicitly passing it down through props at every level.

     useContext is used to manage Global data in the React App.



      ************************************* suppose we have create a application *******************************************
      where we have footer profile and contact Compontent
      Problem:- pass phone number in footer component and also in Contact compontent

      if phone variable decleared in app component 

      So, we pass the data directly in the footer component using props
      But we not pass the data directly in Contact component 
      Means first pass the data in the profile component then pass in the Contact component

      So, It is very painfull when work with more nested component


      So, To Solve this problem useContext was introduce that allow us to create global data and we can access these data from any component 
      without passing through props at every component level
      
      
      ******************** We can use useContext Hook in three simple step ***************************************
      
      1. Creating the context
      2. Providing the context
      3. Consuming the context


      =====================================================================================================================   
      =                                                                                                         APP       =
      =                                                                                                                   =
      =                                                                            Data pass using props from App         =
      =     ==============================================================      <----------------------------------       =
      =     =     PROFILE                                                =                                                =
      =     =                                                            =                                                =
      =     =                                                            =                                                =
      =     =    ===========================     Data pass using props   =                                                =
      =     =    =   CONTACT               =       from Profile          =                                                =              
      =     =    =    +8400119700          =     <--------------------   =                                                =                                  
      =     =    ===========================                             =                                                =
      =     =                                                            =                                                =
      =     ==============================================================                                                =
      =                                                                                                                   =
      =                                                                                                                   =
      =                                                                                                                   =
      =                                                                                                                   =              
      =                                                                                                                   =
      =     ==============================================================        Data pass using props from App          =
      =     =                              FOOTER                        =      <----------------------------------       =
      =     =                                                            =                                                =              
      =     =           +8400119700                                      =                                                =        
      =     ==============================================================                                                =
      =                                                                                                                   =                                                                                                   =
      =                                                                                                                   =
      =                                                                                                                   =    
      =====================================================================================================================  
      
      
    

    The context API use to share any type of data including object, function, arrays 
    this makes it flexible solution for variaty of state management needs.

    Most common use of context API is

    Share to current theam of all it's component 
    or
    Share to authenticated user with all of our component in our application
    or
    share to the result of an API call with all of our component in our application
    
    that reduce the API call


  */



  return (
    <div>
         <h1>================ useContext Hook Example ===================</h1>
         <h3>------- Example 1 ---------</h3>
         <UseContextExample1 />
    </div>
  )
}

export default UseContext