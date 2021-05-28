
const icon = document.querySelector('button.important');
const divItem = document.querySelector('.container');

//console.log(icon);
//const icodNode = document.innerHTML('<i class="fas fa-star icon"></i>');
const heading = document.querySelector('.card-title');

divItem.addEventListener('click' , function (e) { 
    const t = e.target;
    if(t.tagName == "BUTTON"){
        const parentOfButton = t.parentNode;
        //const i = document.createElement("I");
        const div =  document.createElement('DIV');
        div.innerHTML = `<i class="fas fa-star icon"></i>`;
        div.className = 'myIcon';
       
        console.log(div);
       
        const parentOfParent = parentOfButton.parentNode;
        parentOfParent.classList.add("borderStyle");
        parentOfParent.append(div);
        
    }
});
