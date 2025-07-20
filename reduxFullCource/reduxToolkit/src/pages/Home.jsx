import React from 'react'
import Account from '../Components/Account'
import Bonus from '../Components/Bonus'
import { useSelector } from 'react-redux'
import Reward from '../Components/Reward'
import Admin from '../Components/Admin'

const Home = () => {
  
 
  const amount = useSelector((state)=> state.account.amount)      // state is global state mean :- store.getState()
  const points = useSelector((state)=> state.bonus.points)
  


  return (
    <div>
        <h1>Home</h1>
        <h2>Current Amount: {amount}</h2>
        <h2>Total Bonus : {points}</h2>
        <Account />
        <Bonus />
        <Reward />
        <Admin />
    </div>
  )
}

export default Home