import React from "react";



const CallBackHell = () => {


    const cart = {

        cartId:10,
        totalCart:2,

    }

    const createOrder = (cart, callBack)=>{

        console.log("Cart available");
        setTimeout(()=>{
            const orderId = 1203;
            callBack(orderId);
        }, 2000);

    }

    const proceedToPayment = (orderId,  callBack) => {
        console.log("Order id get for proceed to payment");

        setTimeout(()=>{
            const paymentInfo = {
                orderId:orderId,
                status:"Success",
                method:"Razorpay",
            }
            callBack(paymentInfo);
        }, 1000);
    }
    
    const showOrderSummury = (paymentInfo, callBack)=>{
        console.log("order summury show", paymentInfo);
        setTimeout(()=>{
            callBack(paymentInfo)
        }, 500);
    }

    const updateWalletBallence = () => {
        console.log("Wallet balance updated after purchase.");
    }



    createOrder(cart, (orderId)=>{
        proceedToPayment(orderId, (paymentInfo)=>{
             showOrderSummury(paymentInfo, ()=>{
                updateWalletBallence();
             })   
        })
    })




    return (
        <div>
            <h1>CallBackHell Problem</h1>
        </div>
    )
}



export default CallBackHell;