import React from 'react'
import Account from '../Components/Account'
import Bonus from '../Components/Bonus'
import { useSelector } from 'react-redux'

const Home = () => {
  
 
  const amount = useSelector((state)=> state.account.amount)      // state is global state mean :- store.getState()
  const points = useSelector((state)=> state.bonus.points)
  const account = useSelector((state)=> state.account)


  return (
    <div>
        <h1>Home</h1>
        {
           account.pending ?  
           (<p>Loading......</p>)
           : 
           account.error ? 
           (<p>{account.error}</p>)
           : 
           (<h2>Current Amount : {amount}</h2>)
        }
        
        <h2>Total Bonus : {points}</h2>
        <Account />
        <Bonus />
    </div>
  )
}

export default Home