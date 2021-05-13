// const draggables = document.querySelectorAll('.container');
// const draggable_box =  document.querySelectorAll('.box');
// //console.log(draggable_box);

// draggable_box.forEach( (item, index)=>{
//     item.setAttribute('data-index', index);
// } )


// function drag_start(){
//     //console.log('Event: ', 'dragstart');
//     d = +this.closest('div').getAttribute('data-index');
//     console.log(d);
//     // const d = +this.getAttribute('data-index');
//     // console.log(d);
//     //start = +this.getAttribute('data-index');
// }
// function drag_over(e){
//     //console.log('Event: ', 'dragover');
//     // const d = +this.getAttribute('data-index');
//     // console.log(d);
//     e.preventDefault();
// }
// function drag_drop(){
//     //console.log('Event: ', 'drop');
//     const dragItemEnd = +this.getAttribute('data-index');
//    //console.log(d);
//   // swap(start, dragItemEnd);
// }

// function swap(from, to) {
//     //console.log(123);
//     const item1 = draggables[from].querySelector('div');
//     const item2 = draggables[to].querySelector('div');
    

//     console.log(item1, item2);
// }


// function drag_enter(){
//     //console.log('Event: ', 'dragenter');
// }
// function drag_leave(){
//     //console.log('Event: ', 'dragleave');
    
// }


// draggables.forEach(drag=>{
//     drag.addEventListener('dragstart', drag_start);    
// });

// draggable_box.forEach(dragItem=>{
//     dragItem.addEventListener('dragover', drag_over);
//     dragItem.addEventListener('drop', drag_drop);
//     dragItem.addEventListener('dragenter', drag_enter);
//     dragItem.addEventListener('dragleave', drag_leave);

// });