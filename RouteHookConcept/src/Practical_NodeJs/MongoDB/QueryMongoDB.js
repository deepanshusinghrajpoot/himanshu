





//🔹 Mongoose CRUD Query Cheat Sheet (User Model)
// --------------------------------------------------


// Assume User model

import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number,
});
const User = mongoose.model("User", UserSchema);






//🟢 Create
//-----------


// 1. Create single user

await User.create({ name: "John", email: "john@mail.com", age: 25 });



// 2. Insert many users

await User.insertMany([
  { name: "Alice", email: "alice@mail.com", age: 22 },
  { name: "Bob", email: "bob@mail.com", age: 30 },
]);









//🔵 Read
//-----------



// 3. Find all users
await User.find();

// 4. Find one user
await User.findOne({ email: "john@mail.com" });

// 5. Find by ID
await User.findById("64f1c29...");

// 6. Select specific fields
await User.find({}, "name email");   // only name & email

// 7. Find with conditions
await User.find({ age: { $gt: 20, $lt: 30 } });

// 8. Sort results
await User.find().sort({ age: -1 });   // descending

// 9. Limit & skip
await User.find().limit(5).skip(10);   // pagination

// 10. Count documents
await User.countDocuments({ age: { $gte: 18 } });












//🟡 Update
//-------------



// 11. Update one (first match)
await User.updateOne({ email: "john@mail.com" }, { $set: { age: 26 } });

// 12. Update many
await User.updateMany({}, { $inc: { age: 1 } }); // increase age by 1

// 13. Find and update (returns updated doc)
await User.findOneAndUpdate(
  { email: "john@mail.com" },
  { $set: { name: "Johnny" } },
  { new: true }
);

// 14. Update by ID
await User.findByIdAndUpdate("64f1c29...", { $set: { age: 28 } }, { new: true });














// 🔴 Delete
// -------------



// 15. Delete one
await User.deleteOne({ email: "john@mail.com" });

// 16. Delete many
await User.deleteMany({ age: { $lt: 18 } });

// 17. Find and delete
await User.findOneAndDelete({ email: "alice@mail.com" });

// 18. Delete by ID
await User.findByIdAndDelete("64f1c29...");











//⚡ Aggregation & Extra Queries
// --------------------------------




// 19. Aggregation example (group by age)
await User.aggregate([
  { $group: { _id: "$age", total: { $sum: 1 } } }
]);

// 20. Distinct values
await User.distinct("age");

// 21. Exists condition
await User.find({ email: { $exists: true } });

// 22. Regex search
await User.find({ name: { $regex: /^J/, $options: "i" } }); // names starting with J






// ✅ This covers 95% of MongoDB/Mongoose queries asked in interviews.















