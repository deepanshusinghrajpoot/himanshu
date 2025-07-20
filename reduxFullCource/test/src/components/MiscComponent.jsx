import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {} from '../redux/reducers/bonusSlice'
import { setIsDeepanshu, setIsHero, setIsHimanshu, setIsRam, setIsRohan, setIsShayam } from '../redux/reducers/msciSlice'






const MiscComponent = () => {


    
    
     const miscData = useSelector((state)=> state.misc)
     const { isRam, isShayam, isRohan, isDeepanshu, isHimanshu, isHero } = miscData;


     const dispatch = useDispatch()


     console.log(miscData)


    return (
         
         <div>
               <h1>This is a the misc page</h1>
               <div>Ram:{isRam ? <span>True</span> : <span>False</span> } <button  onClick={()=> dispatch(setIsRam(!isRam))} >{isRam? <span>Make Ram is a false</span> : <span>Make ram is a true</span> }</button> </div>
               <br/>
               <div>Shayam:{isShayam ? <span>True</span> : <span>False</span> } <button onClick={()=> dispatch(setIsShayam(!isShayam))} >{isShayam? <span> Make Shayam is a False</span> : <span>Make Shayam is a True</span> }</button></div>
               <br/>
               <div>Rohan:{isRohan ? <span>True</span> : <span>False</span> } <button  onClick={()=> dispatch(setIsRohan(!isRohan))} >{isRohan? <span>Make Rohan is a False</span> : <span> Make Rohan is a True</span> }</button></div>
               <br/>
               <div>Rohan:{isHero ? <span>True</span> : <span>False</span> } <button  onClick={()=> dispatch(setIsHero(!isHero))} >{isRohan? <span>Make Hero is a False</span> : <span> Make Hero is a True</span> }</button></div>
               <br/>
               <div>Deepanshu:{isDeepanshu ? <span>True</span> : <span>False</span> } <button onClick={()=> dispatch(setIsDeepanshu(!isDeepanshu))} >{isDeepanshu? <span> Make Deepanshu is a False</span> : <span> Make Deepanshu is a True</span> }</button></div>
               <br/>
               <div>Himanshu:{isHimanshu ? <span>True</span> : <span>False</span> }  <button onClick={()=> dispatch(setIsHimanshu(!isHimanshu))}>{isHimanshu? <span>Make Himanshu is a False</span> : <span>Make Himanshu is a True</span> }</button></div>
         </div>
    )

}



export default MiscComponent