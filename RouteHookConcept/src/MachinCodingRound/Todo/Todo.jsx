import React, { useState } from 'react'
import "./Todo.css"

const App = () => {

  const [input, setInput] = useState();

  const [todoList, setTodoList] = useState([]);


  const addTodoItem = () => {
      
     if(input.trim() == "") return;

     const item = {
         id: todoList.length + 1,
         text: input.trim(),
         completed: false,
     }

     setTodoList(prev => [...prev, item]);

     setInput("");
  }



  const toggleCompleted = (id) => {
      
     setTodoList(todoList.map((row) => {
         if(row.id == id){
            return {
                ...row,
                completed: !row.completed,
            }
         }
         else{
            return row;
         }
     }));


  }


  const handleDleteItem = (id) => {
      setTodoList(todoList.filter((row)=> row.id !== id));
  }





  return (
    <div>
         <input 
           type="text"
           placeholder="Enter todo"
           value={input} 
           onChange={(e)=> setInput(e.target.value)}
         />
         <button onClick={()=> addTodoItem()}>Add</button>

         <ul>
            {
                todoList.map((row)=>(
                    <li key={row.item}>
                        <input type="checkbox" checked={row.completed}  onChange={()=> toggleCompleted(row.id)} />
                        <span className={ row.completed ? "strikeThrough" : ""}>{row.text}</span>
                        <button onClick={()=> handleDleteItem(row.id)}>Delete</button>
                    </li>
                ))
            }
         </ul>
    </div>
  )
}

export default App