import React, {useState} from 'react'
import { useAddAccountMutation, useDeleteAccountMutation, useGetAccountsQuery, useUpdateAccountMutation } from '../api/adminSlice'

const Admin = () => {
    

      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()

      // react-redux merge the state of react and redux

      // react-redux do only three things:-  (first:- use Provider, second:- use:- useDispatch(), useSelector() )
      

      const [value, setValue] = useState(0);
      const [amount, setAmount] = useState(0);
      
      
      const {data, error, isLoading} =  useGetAccountsQuery()   // this is query so get data from server
      const [addAccount, addResponse] = useAddAccountMutation();   // addAccount(this is variable according to you) is use to run the hook (mutation hook)
                                                                // response is similar to this {data, error, isLoading}
      const [deleteAccount, deleteResponse] = useDeleteAccountMutation();
      const [updateAccount, updateResponse] = useUpdateAccountMutation();

      console.log("addResponse:-", addResponse);        // addResponse:- {requestId: 'gZW5Jv3HUtkh6Nz8LoEfx', status: 'pending', endpointName: 'addAccount', startedTimeStamp: 1744019838284, isUninitialized: false, …}
      console.log("deleteResponse:-", deleteResponse);  // deleteResponse:- {requestId: 'vNoM5SqVVT11LoYs5ADP3', status: 'fulfilled', endpointName: 'deleteAccount', startedTimeStamp: 1744019827474, data: {…}, …}


      return (
        <div>
            <div>
                 <h1>Admin Component</h1>
                 <input type="number" placeholder="Enter number and update..."  value={value}  onChange={(e)=> setValue(e.target.value)} />
                 {
                  data && data.map((account, index) =>
                     <div key={index} >
                           <span>{account.id}  : {account.amount}</span>
                           <button onClick={()=> deleteAccount({userId:account.id})} >Delete Account</button> 
                           <button onClick={()=>{ updateAccount({userId:account.id,amount:value}); setValue()}} >Update Account</button>
                     </div>)
                 }
                 <div>
                        <input type='number' placeholder='Enter amount and add...' value={amount} onChange={(e)=> setAmount(e.target.value)} />
                        <button onClick={()=>{addAccount({userId:data.length + 1, amount}); setAmount() }} >Add Account</button>
                 </div>
                 
            </div>
        </div>
      )
}

export default Admin



