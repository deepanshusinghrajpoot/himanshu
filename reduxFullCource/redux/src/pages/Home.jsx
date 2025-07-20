import React from 'react'
import Account from '../Components/Account'
import Bonus from '../Components/Bonus'

const Home = ({store}) => {
  
  console.log(store);

  return (
    <div>
        <h1>Home</h1>
        <h2>Current Amount : {store.getState().account.amount}</h2>
        <h2>Total Bonus : {store.getState().bonus.points}</h2>
        <Account />
        <Bonus store={store} />
    </div>
  )
}

export default Home