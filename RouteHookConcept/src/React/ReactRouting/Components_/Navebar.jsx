import React from 'react'
import { assets } from '../../../assets/assets'
import { Link, NavLink, useNavigate } from 'react-router-dom'


const Navebar = () => {

  const navigate = useNavigate();


  return (
    <div>
        <div className='navbar' >
          <img src={assets.logo} alt='' style={{width:'2.5rem'}} />
          <ul>
            <NavLink to='/' ><li>Home</li></NavLink>
            <NavLink to='/products' ><li>Products</li></NavLink>
            <NavLink to='/about' ><li>About</li></NavLink>
            <NavLink to='/contact' ><li>Contact</li></NavLink>   
          </ul>

          <button onClick={()=> navigate('/contact', {replace: true})} >Get Started</button>

        </div>

        <div className='navbar'>
            <ul>
                <li><h1>JavaScript all interview question</h1></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='/eventLoop' ><li>(1). 1. What is JavaScript </li></Link>
                <Link to='/eventLoop' ><li>2. GEC, Queue, Event Loop all question</li></Link>
            </ul>
            <ul>
                <Link to='/this' ><li>(2). this concept</li></Link>
            </ul>
            <ul>
                <Link to='/prototype' ><li>(3). 1. Prototype Inheritence (Prototype, Inheritance, Prototype chain)</li></Link>
                <Link to='/polyfillMapFilterReduce' ><li>2. Polyfill of map, filter, reduce method</li></Link>
                <Link to='/polyfillCallApplyBind' ><li>3. Polyfill of coll, apply, bind method</li></Link>
                <Link to='/polyfillPromise' ><li>4. Polyfill of Promise</li></Link>
                <Link to='/polyfillPromise.all' ><li>4. V.Imp Polyfill of Promise.all method</li></Link>
            </ul>
            <ul>
                <Link to='/callBackHell'><li>(4).  1. CallbackHell , Inversion of control</li></Link>
                <Link to='/promis' ><li>2. Promis and All api</li></Link>
                <Link to='/async_await' ><li>3. async & await</li></Link>
            </ul>
            <ul>
                <Link to='/hoisting'><li>(5) 1. Hoisting(explain using GEC)</li></Link>
                <Link to='/let_const_var'><li> 2. All concept of let_const_var( TDZ,  SyntaxError vs ReferenceError vs TypeError, Additional Restrictions of let and const)</li> </Link>
            </ul>
            <ul>
                <Link to='/scoping'><li>(6). All concept of scope(Scope, Lexical environment, Lexical Context, Scope Chaining) </li></Link>
            </ul>
            <ul>
                <Link to='/closure'><li>(7). Closure</li></Link>
            </ul>
            <ul>
                <Link to='/basicOfFunction'><li>(8). 1. Bsic Of Function((statement or declaration), expression, anonymous, first class citizens)</li></Link>
                <Link to='/hof'><li>2. Cllback, HOF</li></Link>
                <Link to='/pureAndImpure'><li>3. Pure and Impure</li></Link>
                <Link to='/currying'><li>4. Currying</li></Link>
                <Link to='/shallow_deep_copy'><li>5. Shallow & Deep Copy</li></Link>
                <Link to='/map_filter_reduce'><li>6. map & filter & reduce</li></Link>
            </ul>
            <ul>
                <Link to='/debouncing'><li>(9). 1. Debouncing</li></Link>
                <Link to='/throttlingVsDebouncing'><li>2. Throttling V/S Debouncing</li></Link>
                <Link to='/throttling'><li>3. Throttling</li></Link>
            </ul>
            <ul>
                <Link to='/bubbling'><li>(10). 1. Bubbling</li></Link>
                <Link to='/capturing'><li>2. Capturing</li></Link>
                <Link to='/eventDelegation'><li>3. Delegation</li></Link>
            </ul>

            <ul>
                <Link><li><h4>...............................................................................Basic all interview question of JavaScript.................................................................................</h4></li></Link>
            </ul>
            <ul>
                <Link to='/localStorage'><li>(1) Local Storage</li></Link>
            </ul>
            <ul>
                <Link to='/primitiveAndNonPrimitive'><li>(1) Primitive and Non-primitive</li></Link>
            </ul>
            <ul>
                <Link to='/operator'><li>(1) 1. Operator</li></Link>
                <Link to='/spradAndRest'><li>2. Imp Sprad and Rest Operator</li></Link>
            </ul>
        </div>



        <div className='navbar'>
            <ul>
                <li><h1>ReactJs all interview question</h1></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='/lifeCyleMethodOfComponent' ><li>(1). Life Cycle Methode of Component (mounting, updating, unmounting)</li></Link>
            </ul>
            <ul>
                <Link to='/useState' ><li>(1). 1. useState</li></Link>
                <Link to='/useEffect' ><li>2. useEffect</li></Link>
                <Link to='/useRef' ><li>3. useRef</li></Link>
                <Link to='/useMemo' ><li>4. useMemo</li></Link>
                <Link to='/useCallback' ><li>5. useCallback</li></Link>
                <Link to='/useContext' ><li>6. useContext</li></Link>
                <Link to='/useReducer' ><li>7. useReducer</li></Link>
                <Link to='/useLayoutEffect' ><li>8. useLayoutEffect</li></Link>
                <Link to='/customHook' ><li>9. customHook</li></Link>    
            </ul>
            <ul>
                <Link to='/lazyComponent' ><li>(2). 1. LazyLoding</li></Link>
            </ul>
            <ul>
                <Link to='/props' ><li>(3). Props</li></Link>
            </ul>
            <ul>
                <Link to='/reactComponent' ><li>(4). ReactComponent</li></Link>
            </ul>
            <ul>
                <Link to='/state'><li>(5). State</li></Link>
            </ul>
            <ul>
                <Link to='/hoc'><li>(6). HOC</li></Link>
            </ul>
            <ul>
                <Link to='/syntheticEvent'><li>(7). Synthetic Event</li></Link>
            </ul>
        </div>

        <div className='navbar'>
            <ul>
                <li><h1>NodeJs all interview question</h1></li>
            </ul>
        </div>



        <div className='navbar'>
            <ul>
                <li><h1>SQL</h1></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='/AnkiBansal2hourComponent' ><li>(1). Ankit Bansal 2 hour concept.</li></Link>
            </ul>
        </div>
    </div>
  )
}

export default Navebar