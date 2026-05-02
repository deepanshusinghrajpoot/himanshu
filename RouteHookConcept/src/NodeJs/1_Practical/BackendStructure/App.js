import express from "express";
import "dotenv/config";
import cookieParser from "cookie-parser";
import { connectDB } from "../MongoDB/ConnectDB.js";


import userRouter from "./routes/user.js";
import adminRoute from "./routes/admin.js";
import chatRouter from "./routes/chat.js";



const app = express();




dotenv.config({
    path: "./.env",
});





const mongoURI = process.env.MONGO_URI;
const PORT = process.env.PORT || 3000;



connectDB(mongoURI);
               




// use here middleware 
app.use(express.json());          // this use to get JSON(raw) data from body
app.use(cookieParser());          // this is use to get cookie from local machine 



app.use("/api/v1/user", userRouter);




app.get("/",(req, res)=>{
    res.send("Hellow you are in home page");
})







app.listen(PORT, ()=>{
    console.log(`Server is runing on port ${PORT} in ${envMode} mode`);
})


