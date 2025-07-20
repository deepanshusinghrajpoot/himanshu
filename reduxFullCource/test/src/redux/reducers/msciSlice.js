import { createSlice } from "@reduxjs/toolkit"



const initialState = {
    isRam:false,
    isShayam:false,
    isRohan:false,
    isHero:false,
    isDeepanshu:false,
    isHimanshu:false,
}



const miscSlice = createSlice({
       
     name:"misc",
     initialState,
     reducers:{

        setIsRam:(state, action)=>{
            state.isRam = action.payload;
        },
        setIsShayam:(state, action)=>{
            state.isShayam = action.payload;
        },
        setIsRohan:(state, action)=>{
            state.isRohan = action.payload;
        },
        setIsHero:(state, action)=>{
            state.isHero = action.payload;
        },
        setIsDeepanshu:(state, action)=>{
            state.isDeepanshu = action.payload;
        },
        setIsHimanshu:(state, action)=>{
            state.isHimanshu = action.payload;
        }

     }

})


export default miscSlice

export const {
                    setIsRam,
                    setIsShayam,
                    setIsRohan,
                    setIsHero,
                    setIsDeepanshu,
                    setIsHimanshu,
                                            } = miscSlice.actions




