/*



************************** Difference between Link & NavLink **************************

lll When we use the Link tag, it renders as an anchor (<a>) tag in the DOM
    but it does NOT add any extra class after clicking.

<Link to='/'><li>Home</li></Link>

Console Output:
<a href="/" data-discover="true"><li>Home</li></a>


lll When we use the NavLink tag, it also renders as an anchor (<a>) tag
    but it add an "active" extra class after clicking.


<NavLink to='/'><li>Home</li></NavLink>

Console Output:
<a href="/" class="active" data-discover="true"><li>Home</li></a>
















************************** Routing with useNavigate Hook **************************

lll When we use Link or NavLink, navigation happens in a forward direction.
lll When we use useNavigate React Hook, navigation happens in both direction forword and backword.


But sometimes we need to navigate programmatically, such as:
- Redirecting after form submission
- Navigating based on user action
- Implementing back or forward navigation
- Passing state between routes

In these cases, we use the useNavigate hook.











First: Import useNavigate from react-router-dom where it is needed

import { useNavigate } from 'react-router-dom';

const Navbar = () => {

    const navigate = useNavigate();

    return (
        <button onClick={() => navigate('/useState')}>
            Get Started
        </button>
    );
};





 */