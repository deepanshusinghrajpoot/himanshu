/*

============================= Phase of Component ======================================

lll (1) Mounting - Mounting is the process of creating an element and inserting it in a DOM tree.
lll (2) Updating - Updating is the process of changing state or props of component and update changes to nodes already in the DOM.
              (3) Error Handling - These are used when there is error during rendering, in lifecycle method or in the constructor of any child component.
lll (4) Unmounting - Unmounting is the process of removing components from the DOM.


lll 
    These lifecycle method are use in class based component. 
    These are not use in function based component.

============================= Lifecycle Method =======================================

Each component has several "Lifecycle methods" that (you or we) can override to run code at particular times in the process.

Life cycle of component have different phase.
  1. Mounting 
  2. Updating
                    3. Error Handling (according to documentation error handling is not contain in Life cycle phase)
  4. Unmounting

         
                              React mainting Virtual DOM in memory
 .............                             .
 .  Header   .  -------------->    ................                        
 .           .                     .              .      (1) Mounting
 .  Content  .  -------------->    . Virtual DOM  . ---------------------> body
 .           .                     .              .      (2) Updating    
 .  Footer   .  -------------->    ................      (3) Unmounting
 .............

   


   .....................      .........................................   ............................
   .     Mounting      .      .            Updating                   .   .       Unmountin          .
   .        .          .      .                                       .   .                          .
   .    constructor    .      .  NewProps  setState()  forceUpdate()  .   .                          .
   .        .          .      .     .         .             .         .   .                          .
   .        >          .      .     >         >             >         .   .                          .   
   ....................................................................   .                          .
   .           getDerivedStateFromProps                               .   .                          .
   ....................................................................   .                          .
   .                   .      .     .         .                .      .   .                          .
   .                   .      .     >         >                .      .   .                          .
   .                   .      .  ..........................    .      .   .                          .
   .                   .      .  .  shouldComponentUpdate .    .      .   .                          .
   .                   .      .  ..........................    .      .   .                          .
   .                   >      .           >                    >      .   .                          .   
   ....................................................................   .                          .
   .                              render                              .   .                          .
   ....................................................................   .                          .
   .                   .      .  ..........................           .   .                          .
   .                   .      .  .getSnapSortBeforeUpdate .           .   .                          .
   .                   .      .  ..........................           .   .                          .
   .                   >      .           >                           .   .                          .   
   ....................................................................   .                          .
   .               React update DOM and refs                          .   .                          .
   ....................................................................   .                          .
   .                   .      .               .                .      .   .                          .
   . componentDidMount .      .       ComponentDidUpdate       .      .   .     ComponentWillMount   .     
   .                   .      .                                .      .   .                          .
   ...................................................................................................



   
*/


























