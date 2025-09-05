import React from 'react'
import { assets } from './assets/assets'
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
                <Link to='/eventLoop' >
                        <li>(1). 1. What is JavaScript </li>
                        <li>2. What is web API and Libuv</li>
                </Link>
                <Link to='/eventLoop' >
                        <li>2. Global  Execution Context (GEC) :- There are two phase in GEC (1). Memory Creation Phase (2). Code Execution Phase</li>
                        <li>3. Event Loop and Call Stack</li>
                        <li>4. Queue :- There are two type of Queue in JS (1).  Macro Task Queue (Callback Queue) (2). Micro Task Queue</li>
                </Link>
            </ul>
            <ul>
                <Link to='/this' >
                         <li>(2). this concept</li>
                         <li>1. What is value of this in global space</li>
                         <li>2. What is value of this inside Regular function for Static & Non-Static Mode</li>
                         <li>3. The value of this depend on how we call a function</li>
                         <li>3. Call, Apply, Bind</li>
                         <li>4. What is value of this inside arrow function</li>
                </Link>
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
                <Link to='/promis' >
                       <li>2. Promise</li>
                       <li>(i). Promise have some API to handle multiple promise:- (1). Promise.all([p1,p2,p3,...])  (2). Promise.allSettled([p1,p2,p3,...]) (3). Promise.Race([p1,p2,p3,...]) (4). Promise.any([p1,p2,p3,...])</li>
                       <li>(ii). There are two way handling promise in JS (1). using dot_then dot_catch  (2). using async & await</li>
                </Link>
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
                <Link to='/closure'><li>(7). Closure :- Famouse Example (1).Famous setTimeout Closure Interview Question (2). Nested Function </li></Link>
            </ul>
            <ul>
                <Link to='/basicOfFunction'><li>(8). 1. Bsic Of Function((statement or declaration), expression, anonymous, first class citizens)</li></Link>
                <Link to='/hof'><li>2. Cllback, HOF</li></Link>
                <Link to='/pureAndImpure'><li>3. Pure and Impure</li></Link>
                <Link to='/currying'><li>4. Currying :- There are two way implement function curring (1). Using Bind method (2). Using Closure</li></Link>
                <Link to='/map_filter_reduce'><li>6. map & filter & reduce</li></Link>
            </ul>
            <ul>
                <Link to='/shallow_deep_copy'>
                              <li>(9) Shallow & Deep Copy</li>
                              <li>There are two way creating Shallow Copy (1). Sprade operator  (2). using Object.assign() method</li>
                              <li>There are two way creating Deep Copy (1). using JSON.stringify() and JSON.parse() methods (2). Recursive way to create Deep Copy</li>
                </Link>
            </ul>
            <ul>
                <Link to='/debouncing'><li>(10). 1. Debouncing</li></Link>
                <Link to='/throttlingVsDebouncing'><li>2. Throttling V/S Debouncing</li></Link>
                <Link to='/throttling'><li>3. Throttling</li></Link>
            </ul>
            <ul>
                <Link to='/bubbling'><li>(11). 1. Bubbling</li></Link>
                <Link to='/capturing'><li>2. Capturing</li></Link>
                <Link to='/eventDelegation'><li>3. Delegation</li></Link>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <li><h4>Basic all interview question of JavaScript</h4></li>
            </ul>
        </div>
        <div className='navbar'>
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
                <Link to='' ><li>(1). 1. What Is React and its feature</li></Link>
                <Link to='' ><li>2. What Is Virtual DOM</li></Link>
                <Link to='' ><li>3. What Is Diffing Algorithum</li></Link>
                <Link to='' ><li>4. What Is Reconciliation</li></Link>
                <Link to='' ><li>5. What Is React fiber</li></Link>
                <Link to='/lifeCyleMethodOfComponent' >
                        <li>2. Life Cycle Methode of Component :- </li>
                        <li>(i). mounting</li>
                        <li>(ii). updating</li>
                        <li>(iii). unmounting</li>
                </Link>
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
            <ul>
                <Link to='/SSR'><li>(8). SSR:- Hydration</li></Link>
                <Link to='/CSR'><li>(8). CSR</li></Link>
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
                <li><h4>SQL Theoretical Question</h4></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='' ><li>(1). keys (Super key, Candidate key, Alternative key, Primary key, Foriegn key, Composite key)</li></Link>
            </ul>
            <ul>
                <Link to='' ><li>(2). 1. Normal Form </li></Link>
                <Link to='' ><li>2. Type of Normal Form :- (i) 1NF , (ii) 2NF , (iii) 3NF , (iV) BCNF </li></Link>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <li><h4>SQL Ankit Bansal</h4></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='' ><li>(1). Core Concept </li></Link>
                <Link to='' ><li>1. Engine executes in logical order</li></Link>
                <Link to='' ><li>2. SQL syntax order</li></Link>

            </ul>
            <ul>
                <Link to='' ><li>(2). Operator :- </li></Link>
                <Link to='' ><li>1. Comparison, 2. Logical, 3. Set&Range, 4. Patter match, 5. Arithmatic, 6. String, 7. join  </li></Link>
            </ul>
            <ul>
                <Link to='' ><li>(3). Functionality of key ward :- </li></Link>
                <Link to='' ><li>1. SELECT, 2. FROM, 3. WHERE, 4. GROUP BY, 5. HAVING, 6. ORDER BY, 7. LIMIT </li></Link>
            </ul>
            <ul>
                <Link to='' ><li>(4).1 CASE Statement </li></Link>
                <Link to='' ><li>2. String Functions </li></Link>
                <Link to='' ><li>3. Date Functions </li></Link>
            </ul>
        </div>
















        <div className='navbar'>
            <ul>
                <li><h1>OOP C++</h1></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='/OopC++' ><li>(1). 1. Class </li></Link>
                <Link to=''><li>2. Object </li></Link>
                <Link to='' ><li>3. Acess Modifire </li></Link>
                <Link to='' ><li>4. Seter & Getter Function  </li></Link>
            </ul>
            <ul>
                <Link to='/ConstructorC++' ><li>(2). 1. !Constructor (Properties) !Destructor</li></Link>
                <Link to='' ><li>2. Type of constructor(non-parametarise, parametarise, Copy)</li></Link>
                <Link to='' ><li>3. Copy Constructor(Shallow Copy, Deep Copy)</li></Link>
            </ul>
            <ul>
                <Link to='/EncapsulationC++' ><li>(3). 1. Encapsulation </li></Link>
                <Link to='' ><li>2. Data hiding  </li></Link>

            </ul>
            <ul>
                <Link to='/InheritanceC++' ><li>(4). 1. Inheritance (In Inheritace which called first Constructor & Destructor ) </li></Link>
                <Link to='' ><li>2. base class - Private member, base class - Protect member, base class - Public member </li></Link>
                <Link to='' ><li>3. Type of inheritance(Single level, Multiple, Multi level, Hierarchical, Hybrid)   </li></Link>
            </ul>
            <ul>
                <Link to='/PolymorphismC++' ><li>(5). 1. Polymorphism </li></Link>
                <Link to='' ><li>2. Type of polymorphism (i) Compile time polymorphism (eg:- Constructor overloading,  Function overloading, Operator Overloading) (ii) Run time polymorphism (eg:- Function overriding with overtual function) </li></Link>
            </ul>
            <ul>
                <Link to='/AbstractionC++' ><li>(5). 1. Abstraction </li></Link>
                <Link to='' ><li>2. There are two way of performing abstraction (i) using access modifire (ii) Abstract classes </li></Link>
                <Link to=''><li>Abstract classes</li></Link>
            </ul>
        </div>











        <div className='navbar'>
            <ul>
                <li><h1>DSA C++</h1></li>
            </ul>
        </div>
         <div className='navbar'>
            <ul>
                <li><h4>Number-based Problems</h4></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='' ><li>1. Print Fibonacci Series</li></Link>
                <Link to='' ><li>2. Find Nth Fibonacci Number (loop + recursion)</li></Link>
                <Link to='' ><li>3. Factorial (loop + recursion)</li></Link>
                <Link to='' ><li>4. Prime Number check (loop + loop using diviser)</li></Link>
                <Link to='' ><li>5. Print all primes up to N (Sieve of Eratosthenes – bonus)</li></Link>
                <Link to='' ><li>6. GCD & LCM (Euclidean Algorithm):- pending</li></Link>
                <Link to='' ><li>7. Reverse a Number (optimal)</li></Link>
                <Link to='' ><li>8. Palindrome Number (1. using reverse)(2. diviser & reverse :- Optimal)</li></Link>
                <Link to='' ><li>9. Armstrong Number (Optimal)</li></Link>
                <Link to='' ><li>10. Strong Number (sum of factorial of digits = number)</li></Link>
                <Link to='' ><li>11. Perfect Number (sum of divisors = number) (iterative + divisor)</li></Link>
                <Link to='' ><li>12. Sum of digits of a number (iterative + recusive + string)</li></Link>
                <Link to='' ><li>13. Count digits of a number (iterative + recusive)</li></Link>
                <Link to='' ><li>14. Swap two numbers without using 3rd variable ('+', '^')</li></Link>
                <Link to='' ><li>15. Power of a number (a^b)</li></Link>                
                <Link to='' ><li>16. Convert decimal ↔ binary</li></Link>                
                <Link to='' ><li>17. Convert decimal ↔ binary</li></Link>                
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <li><h4>5. Pattern Printing</h4></li>
            </ul>
        </div>
        <div className='navbar'>
            <ul>
                <Link to='' ><li>1. Right-angled triangle</li></Link>
                <Link to='' ><li>2. Inverted triangle</li></Link>
                <Link to='' ><li>3. Full pyramid</li></Link>  
                <Link to='' ><li>4. Diamond</li></Link>        
                <Link to='' ><li>5. Number pyramid</li></Link>        
                <Link to='' ><li>6. Floyd’s Triangle</li></Link>        
                <Link to='' ><li>7. Pascal’s Triangle</li></Link>        
                <Link to='' ><li>8. Butterfly pattern</li></Link>        
            </ul>
        </div>

    </div>
  )
}

export default Navebar









/*



🔹 5. Pattern Printing
-----------------------
Most common:

1. Right-angled triangle
2. Inverted triangle
3. Full pyramid
4. Diamond
5. Number pyramid
6. Floyd’s Triangle
7. Pascal’s Triangle
8. Butterfly pattern




*/