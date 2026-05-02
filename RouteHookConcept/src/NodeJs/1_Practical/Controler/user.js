

// Create a new user and save it to the database and save in cookie
const newUser = tryCatch(async(req, res, next) => {

    const { name, username, password, bio } = req.body;

    const file = req.file;

    if(!file) return next(new ErrorHandler("Please upload file", 400));


    const result = await uploadFileToCloudinary([file]);


    const avatar = {
         public_id: result[0].public_id,
         url: result[0].url,
    }
    


    const user = await User.create({ name, username, password, bio, avatar });

    
    sendToken(res, user, 201, "User Created");

})
