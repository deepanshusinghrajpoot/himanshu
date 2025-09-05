import React, { lazy } from 'react'
import Navebar from './Navebar'
import { Route, Routes } from 'react-router-dom'





//import UseEffect from './components/WhatIsReactHooks/useEffect/UseEffect'
//import UseState from './components/WhatIsReactHooks/useState/UseState'
//import UseRef from './components/WhatIsReactHooks/useRef/UseRef'
//import UseMemo from './components/WhatIsReactHooks/useMemo/UseMemo'
//import UseCallback from './components/WhatIsReactHooks/useCallback.jsx/useCallback'
//import UseContext from './components/WhatIsReactHooks/useContext/UseContext'
//import UseReducer from './components/WhatIsReactHooks/useReducer/UseReducer'
//import UseLayoutEffect from './components/WhatIsReactHooks/useLayoutEffect/UseLayoutEffect'
//import CustomHook from './components/WhatIsReactHooks/CustomHook/CustomHook'
//import Products from './components/ReactRouting/pages/Products'
//import About from './components/ReactRouting/pages/About'
//import Contact from './components/ReactRouting/pages/Contact'




// Lazy loading
const Home = lazy(()=> wait(5000).then(()=> import('./React/ReactRouting/pages/Home')));
const About = lazy(()=> wait(5000).then(()=> import('./React/ReactRouting/pages/About').then((module)=>{return {default:module.About}})));
const Contact = lazy(()=> wait(5000).then(()=> import('./React/ReactRouting/pages/Contact')));
const Products = lazy(()=> wait(5000).then(()=> import('./React/ReactRouting/pages/Products')));


const LifeCycleMethodOfComponent = lazy(()=> wait(5000).then(()=> import('./React/LifecycleMethod/LifeCycleOfComponent')));



const UseState = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useState/UseState')));
const UseEffect  = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useEffect/UseEffect')));
const UseContext = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useContext/UseContext')));
const UseReducer = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useReducer/UseReducer')));
const UseMemo = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useMemo/UseMemo')));
const UseRef = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useRef/UseRef')));
const UseCallback = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useCallback.jsx/UseCallback')));
const UseLayoutEffect = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/useLayoutEffect/UseLayoutEffect')));
const CustomHook = lazy(()=> wait(5000).then(()=> import('./React/WhatIsReactHooks/CustomHook/CustomHook')));



const LazyComponent = lazy(()=> wait(5000).then(()=> import('./React/lazyLoading/LazyComponent')));
const Props = lazy(()=> wait(5000).then(()=> import('./React/Props/Props')));
const ReactComponent = lazy(()=> wait(5000).then(()=> import('./React/ClsaaAndFunctionalComponent/ReactComponent')));
const State = lazy(()=> wait(5000).then(()=> import('./React/State/State')));
const Event = lazy(()=> wait(5000).then(()=> import('./React/EventHandling/Event')));
const HOC = lazy(()=> wait(5000).then(()=> import('./React/HOC/utils/HOC')));
const SyntheticEvent = lazy(()=> wait(5000).then(()=> import('./React/SyntheticEvent/SyntheticEvent')));
const SSR = lazy(()=> wait(5000).then(()=> import('./React/SSR&CSR/SSR')));
const CSR = lazy(()=> wait(5000).then(()=> import('./React/SSR&CSR/CSR')));







const CollStack = lazy(()=> wait(2000).then(()=> import('./JavaScript/EventLoop/callStack/CollStack')));
const This = lazy(()=> wait(2000).then(()=> import('./JavaScript/This/This')));
const Prototype = lazy(()=> wait(2000).then(()=> import('./JavaScript/Prototype/Prototype')));
const PolyfilMapFilterReduce = lazy(()=> wait(2000).then(()=> import('./JavaScript/Prototype/PolyfillOfMapFillterReduce')));
const PolyfillOfCallApplyBind = lazy(()=> wait(2000).then(()=> import('./JavaScript/Prototype/PolyfillOfCalApplyBind')));
const PolyfillOfPromise = lazy(()=> wait(2000).then(()=> import('./JavaScript/Prototype/PolyfillOfPromis')));
const PolyfillOfPromiseAll = lazy(()=> wait(2000).then(()=> import('./JavaScript/Prototype/PolyfillOfPromis_all')));

const Promis = lazy(()=> wait(2000).then(()=> import('./JavaScript/Promiss/Concept')));
const CallBackHell = lazy(()=> wait(2000).then(()=> import('./JavaScript/Promiss/CallbackHell')));
const AsyncAwait = lazy(()=> wait(2000).then(()=> import('./JavaScript/AsyncAwait/AsyncAwait')))

const Hoisting = lazy(()=> wait(2000).then(()=> import('./JavaScript/Hoisting&letConstVar/Hoisting')));
const LetConstHoisted = lazy(()=> wait(2000).then(()=> import('./JavaScript/Hoisting&letConstVar/LetConstHoisted')));
const AllConceptScope = lazy(()=> wait(2000).then(()=> import('./JavaScript/Scope/AllConceptScope')));
const Closure = lazy(()=> wait(2000).then(()=> import('./JavaScript/Closure/Closure')));

const BasicOfFunction = lazy(()=> wait(2000).then(()=> import('./JavaScript/Function/BasicOfFunction')));
const Currying = lazy(()=> wait(2000).then(()=> import('./JavaScript/Function/Currying')));
const HOF = lazy(()=> wait(2000).then(()=> import('./JavaScript/Function/HOF')));
const PureAndImpureFunction = lazy(()=> wait(2000).then(()=> import('./JavaScript/Function/PureImpureFunction')));
const ShallowAndDeepCopy = lazy(()=> wait(2000).then(()=> import('./JavaScript/ShallowAndDeepCopy/ShallowAndDeepCopy')));
const MapFilterReduce = lazy(()=> wait(2000).then(()=> import('./JavaScript/Function/MapFillterReduce')));

const Debouncing = lazy(()=> wait(2000).then(()=> import('./JavaScript/DebouncingThrottling/Debouncing')));
const ThrottlingVsDebouncing = lazy(()=> wait(2000).then(()=> import('./JavaScript/DebouncingThrottling/ThrottlingVsDebouncing')));
const Throttling = lazy(()=> wait(2000).then(()=> import('./JavaScript/DebouncingThrottling/Throttling')));

const Bubbling = lazy(()=> wait(2000).then(()=> import('./JavaScript/Bubbling&Capturing/Bubbling')));
const Capturing = lazy(()=> wait(2000).then(()=> import('./JavaScript/Bubbling&Capturing/Capturing')));
const Delegation = lazy(()=> wait(2000).then(()=> import('./JavaScript/Bubbling&Capturing/Delegation')));


const PrimitiveAndNonPrimitiveDataType = lazy(()=> wait(2000).then(()=> import('./JavaScript/BasicJavaScript/PrimitiveAndNonPrimitiveDataType')));
const LocalStorage = lazy(()=> wait(2000).then(()=> import('./JavaScript/BasicJavaScript/LocalStorage')));
const Operator = lazy(()=> wait(2000).then(()=> import('./JavaScript/BasicJavaScript/Operator/Operator')));
const SpradAndRest = lazy(()=> wait(2000).then(()=> import('./JavaScript/BasicJavaScript/Operator/SpradAndRest')));














const wait = (time) => {
  return new Promise(resolve=> {
      setTimeout(()=>{
           resolve()
      }, time)
  })
}




const App = () => {

  // In this frontend folder not use nested route but nested route is ude inside the frontends folder

  return (
    <> 
      <Navebar />
      <div className='container'>
         <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/products' element={<Products />} />
            <Route path='/about' element={<About />} />
            <Route path='/contact' element={<Contact />}/>
            
        




            <Route path='/lifeCyleMethodOfComponent' element={<LifeCycleMethodOfComponent />} />

            <Route path='/useState' element={<UseState />} />
            <Route path='/useEffect' element={<UseEffect />} />
            <Route path='/useRef' element={<UseRef />} />
            <Route path='/useMemo' element={<UseMemo />} />
            <Route path='/useCallback' element={<UseCallback />} />
            <Route path='/useContext' element={<UseContext />} />
            <Route path='/useReducer' element={<UseReducer />} />
            <Route path='/useLayoutEffect' element={<UseLayoutEffect />} />
            <Route path='/customHook' element={<CustomHook />} />

            <Route path='/lazyComponent' element={<LazyComponent />} />
            <Route path='/props' element={<Props />} />
            <Route path='/reactComponent' element={<ReactComponent />} />
            <Route path='/state' element={<State />} />
            <Route path='/event' element={<Event />} />
            <Route path='/hoc' element={<HOC />} />
            <Route path='/syntheticEvent' element={<SyntheticEvent />} />
            <Route path='/SSR' element={<SSR />} />
            <Route path='/CSR' element={<CSR />} />


        
          











            <Route path='/eventLoop' element={<CollStack/>} />
            <Route path='/this' element={<This/>} />

            <Route path='/prototype' element={<Prototype/>} />\
            <Route path='/polyfillMapFilterReduce' element={<PolyfilMapFilterReduce />} />
            <Route path='/polyfillCallApplyBind' element={<PolyfillOfCallApplyBind />} />
            <Route path='/polyfillPromise' element={<PolyfillOfPromise />} />
            <Route path='/polyfillPromise.all' element={<PolyfillOfPromiseAll />} />



            <Route path='/callBackHell' element={<CallBackHell />} />
            <Route path='/promis' element={<Promis />} />
            <Route path='/async_await' element={<AsyncAwait />} />

            <Route path='/hoisting' element={<Hoisting />} />
            <Route path='/scoping' element={<AllConceptScope />} />
            <Route path='/let_var_const' element={<LetConstHoisted />} />
            <Route path='/closure'  element={<Closure />} />

            
            <Route path='/basicOfFunction'   element={<BasicOfFunction />} />
            <Route path='/hof' element={<HOF />} />
            <Route path='/pureAndImpure' element={<PureAndImpureFunction />} />
            <Route path='/currying'   element={<Currying />} />
            <Route path='/shallow_deep_copy'   element={<ShallowAndDeepCopy />} />
            <Route path='/map_filter_reduce'   element={<MapFilterReduce />} />


            <Route path='/debouncing'   element={<Debouncing />} />
            <Route path='/throttlingVsDebouncing'   element={<ThrottlingVsDebouncing />} />
            <Route path='/throttling'   element={<Throttling />} />

            <Route path='/bubbling'  element={<Bubbling />} />
            <Route path='/capturing' element={<Capturing />} />
            <Route path='/eventDelegation' element={<Delegation />} />


          
            <Route path='/primitiveAndNonPrimitive' element={<PrimitiveAndNonPrimitiveDataType />} />
            <Route path='/localStorage' element={<LocalStorage />} />
            <Route path='/operator' element={<Operator />} />
            <Route path='/spradAndRest' element={<SpradAndRest />} />



















            

         </Routes>
      </div>
    </>
  )
}

export default App