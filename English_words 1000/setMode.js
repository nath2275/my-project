let sw3 = document.querySelector('.sw3')
let sw5 = document.querySelector('.sw5')
// set หน้าตอบ
let Mode_check = 'statusWord'
// ode_check = 'statusWord'


function setNumberGroupWord3(){
    groupSet = 3
    sw3.style.color= '#fff';
    sw3.style.background= '#7F96E7';

    //close
    sw5.style.color= '#7F96E7';
    sw5.style.background= '#fff';
}
function setNumberGroupWord5(){
    groupSet = 5
    sw5.style.color= '#fff';
    sw5.style.background= '#7F96E7';

    //close
    sw3.style.color= '#7F96E7';
    sw3.style.background= '#fff';
}


// icon repeat
function repeatClick(){
    let wordSet = List_word()
    let count = wordSet[wordOrder].thai.length
    let findIndex = wordSet[wordOrder].thai.findIndex(item => item === wordList.innerHTML)
    // console.log(wordSet[wordOrder].thai);
    // console.log(count); // 2 2
    // console.log(findIndex); // 0 1
    if(findIndex >= count - 1){  wordList.innerHTML = wordSet[wordOrder].thai[0]  }
    else{  wordList.innerHTML = wordSet[wordOrder].thai[findIndex + 1]  }
}
function repeatClickSave(){
    let wordSet = setOptionSave()
    let count = wordSet[wordOrderSave].thai.length
    let findIndex = wordSet[wordOrderSave].thai.findIndex(item => item === wordListSave.innerHTML)
    if(findIndex >= count - 1){  wordListSave.innerHTML = wordSet[wordOrderSave].thai[0]  }
    else{  wordListSave.innerHTML = wordSet[wordOrderSave].thai[findIndex + 1]  }
}
