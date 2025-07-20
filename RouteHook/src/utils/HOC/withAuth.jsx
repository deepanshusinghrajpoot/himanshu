

/*
   Here:- is a fuction which take a component as a argument and return a component inside other function.
   functional Component:- is nothing but it is a javaScript function.
*/
const withAuth = (Component) => {

    const isAuthenticated = true;
     
    return function(props){
        
        if(isAuthenticated){
            
            return <Component {...props} />

        } else {

            return <p>Please login to access this component</p>

        }
    }
}



export { withAuth, }