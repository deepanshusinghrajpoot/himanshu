/*

================================= Redux Toolkit ===================================
Redux Toolkit is a library that provides a set of tools and best practices for managing state in JavaScript applications, particularly those built with React. It simplifies the process of writing Redux logic and helps developers avoid common pitfalls associated with Redux.

---------------------- Chapter ----------------

1. Redux Concepts/term
2. Redux with react 
3. Redux ToolKit(RTK) with React
4. RTK Query with React
5. Project with RTK Async Thunk



---------------------- Why use Redux -----------------------------

1. Predictable State Management: Redux provides a predictable way to manage application state, making it easier to understand how data flows through the app.
2. Centralized Store: Redux maintains a single source of truth for the application state, which helps in debugging and tracking changes over time.

                                 APP
                                  .
         ......................................................                
         .                        .                           .
       Search                   Sidebar                     Content
                                                              .
                                    ............................................................
                                    .                         .                                .
                                 Cover                      Intro                            video

        
    if required to send state from video component to cover component the it is difficult
    this problem is solved by using :- lifting State



----------------------- When to use Redux -----------------------------

. Big Applications
. High frequency of state changes



----------------------- Redux -----------------------------------

store have contain :- (State, Reducer, dispatch)

action have :- {type:"deposit", payload:100}

state is a object as nested tree :- {"amount": 777, "id": 5}

getState() :- is use to get data of state

if we required to change the state then required to call :- dispatch(action)
And in dispatch we send action which is gone to the reducer and inside reduser create a new state using prev state and action 









// for create fack API server
// npm install -g json-server
// json-server db.json 

                                
*/