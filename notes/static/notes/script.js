
const icon = document.querySelector('button.important');
const divItem = document.querySelector('.container');

const heading = document.querySelector('.card-title');

divItem.addEventListener('click' , function (e) { 
    const t = e.target;
    //console.log(t);

    if ( t.tagName == "BUTTON"){
        const parentOfButton = t.parentNode;
       
        const div =  document.createElement('DIV');
      
        // div.innerHTML = `<i class="fas fa-star icon"></i>`;

        const parentOfParent = parentOfButton.parentNode;
        // console.log('parent of parent ',parentOfParent);

        parentOfParent.classList.add("borderStyle");
        parentOfButton.append(div);

        // console.log(div);
        // console.log(parentOfButton);
    }
});


