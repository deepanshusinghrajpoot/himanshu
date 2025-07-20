import React from "react";



const CallbackHell = () => {


  // Mock cart data
  const cart = {
    items: [
      { name: "Medicine A", price: 50 },
      { name: "Test B", price: 100 }
    ],
    total: 150
  };
  
  // Step 1: Create Order
  function createOrder(cart, callback) {
    console.log("Creating order...");
    setTimeout(() => {
      const orderId = "ORD" + Math.floor(Math.random() * 10000);
      console.log(`Order created with ID: ${orderId}`);
      callback(orderId);
    }, 1000);
  }
  
  // Step 2: Proceed to Payment
  function proceedToPayment(orderId, callback) {
    console.log(`Processing payment for order ${orderId}...`);
    setTimeout(() => {
      const paymentInformation = {
        orderId: orderId,
        status: "Success",
        amountPaid: cart.total,
        paymentMethod: "Razorpay"
      };
      console.log("Payment successful.");
      callback(paymentInformation);
    }, 1000);
  }
  
  // Step 3: Show Order Summary
  function showOrderSummary(paymentInfo, callback) {
    console.log("Order Summary:");
    console.log(paymentInfo);
    setTimeout(() => {
      callback();
    }, 500);
  }
  
  // Step 4: Update Wallet
  function updateWalletBalance() {
    console.log("Wallet balance updated after purchase.");
  }
  
  // Running the full flow
  createOrder(cart, function (orderId) {
    proceedToPayment(orderId, function (paymentInformation) {
      showOrderSummary(paymentInformation, function () {
        updateWalletBalance();
      });
    });
  });
  

    return (
        <div>
            <h1>CallBackHell Problem</h1>
        </div>
    )
}



export default CallbackHell;