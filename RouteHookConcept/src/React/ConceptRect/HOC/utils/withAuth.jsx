

/*
   Here:- is a fuction which take a component as a argument and return a component inside other function.
   functional Component:- is nothing but it is a javaScript function.
*/



const withAuth = (Component) => {

  return function WrappedComponent(props) {
    const isAuthenticated = props.isAuthenticated; // Coming from parent

    if (isAuthenticated) {
      return <Component {...props} />;
    } else {
      return <p>Hello {props.username || "User"}, please login to access!</p>;
    }
  };
  
};


export { withAuth };
