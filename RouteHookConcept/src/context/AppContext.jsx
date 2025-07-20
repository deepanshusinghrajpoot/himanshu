import {createContext} from 'react'

export const AppContext = createContext();


const ContextProvider = (props) => {
    
   const phone = "+8400332467"
   const owner = "DEEPANSHU SINGH"

   const data = {phone, owner}


    return (
        <AppContext.Provider value={data} >
            {props.children}
        </AppContext.Provider>
    )
}


export default ContextProvider