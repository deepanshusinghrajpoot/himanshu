 /*

    import mongoose from "mongoose";

*/


const connectDB = (url) => {

    mongoose.connect(url,{dbName: 'chat-app'})
    .then((data)=>{ console.log(`Connect to DB: ${data.connection.host}`)})
    .catch((error)=> { throw error });

}



export  {  connectDB,  }

  












