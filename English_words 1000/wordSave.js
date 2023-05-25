let setNumberSave = document.querySelector('.setNumber-save')
let downSetSave = document.querySelector('.downSet-save')
//input
let count_rangeSave = document.querySelector('.count_range-save')

let upSetSave = document.querySelector('.upSet-save')
let bt_typeSave = document.querySelector('.bt_type-save')
let bt_at_wordSave = document.querySelector('.bt_at_word-save')

//translate
let wordListSave = document.querySelector('.wordList-save')
// change
let box_repeat_save = document.querySelector('.box-repeat-save')
//ลำโพง
let box_speaker_save = document.querySelector('.box-speaker-save')
//input
let input_translate_save = document.querySelector('.input_translate-save')
let check_word_save = document.querySelector('.check_word-save')





function openSaveWord(){
    savePage.style.display = 'none'
    word1000_page_save.style.display = 'block'
    // const saveEnglish = dataAll_save()
}

//learn english words 1,000 page
function ChangeSetValueSave(){
    wordOrderSave = 0
    setNumberSave.innerHTML = `set ${count_rangeSave.value}`
    questionSave()
}
function reduceSetValueSave(){
    count_rangeSave.value = `${Number(count_rangeSave.value) - 1}`
    ChangeSetValueSave()
    
}
function addSetValueSave(){
    count_rangeSave.value = `${Number(count_rangeSave.value) +1}`
    ChangeSetValueSave()
}

function questionSave(){
    let wordSet = setOptionSave()
    bt_typeSave.innerHTML = `หมวด ${wordSet[wordOrderSave].eng[0]}`
    if(language === 'EN'){
        if(typeof(wordSet[wordOrderSave].thai) === typeof([])){
            box_repeat_save.style.display = 'block'
            wordListSave.innerHTML = wordSet[wordOrderSave].thai[0]
        }else{
            box_repeat_save.style.display = 'none'
            wordListSave.innerHTML = wordSet[wordOrderSave].thai
        }
    }else{
        box_repeat_save.style.display = 'none'
        wordListSave.innerHTML = wordSet[wordOrderSave].eng
        speak(wordSet[wordOrderSave].eng)
    }
}

function setOptionSave(){
    //learn english words 1,000 page
    const saveEnglish = dataAll_save()
    count_rangeSave.max = Math.ceil(saveEnglish.length / groupSet) 

    let set = Number(count_rangeSave.value)
    let min = (set - 1) * groupSet
    let max = set * groupSet
    
    bt_at_wordSave.innerHTML = `ศัพท์ที่ ${min + wordOrderSave+1}`
    let wordSet = saveEnglish.filter((item,index)=>{
        return index >= min && index < max
    })
    bt_typeSave.innerHTML = `หมวด ${wordSet[wordOrderSave].eng[0]}`
    return wordSet
}

function checkEndSave(){
    const saveEnglish = dataAll_save()
    let setMax = Math.ceil(saveEnglish.length / groupSet) 
    return [setMax,saveEnglish.length]
}

function answerTrueSave(){
    let Setmax = checkEndSave()
    input_translate_save.value = ''
    check_word_save.innerHTML = `
    <i class="fa-solid fa-circle-check green"></i>
    <p class="real_answer" id="green">
        เยี่ยม
    </p>`
    setTimeout(()=>{
        let set = Number(count_rangeSave.value)
        wordOrderSave += 1
        console.log('set =',set);
        console.log('if set =',set* groupSet);
        console.log('Setmax[0] =',Setmax[0]);
        console.log('Setmax[1] =',Setmax[1]);
        console.log('groupSet =',groupSet);
        console.log('wordOrderSave =',wordOrderSave);
        console.log('end =',groupSet - ((Setmax[0] * groupSet) - Setmax[1]));
        if(wordOrderSave >= groupSet){
            addSetValueSave()
            wordOrderSave = 0
        }else if(Setmax[0] * groupSet > Setmax[1] && set >= Setmax[0] && wordOrderSave >= groupSet - ((Setmax[0] * groupSet) - Setmax[1]) ){
            count_rangeSave.value = '0'
            console.log(count_rangeSave.value);
            ChangeSetValueSave()
        }
        check_word_save.innerHTML = ''
        questionSave()
    },1200)
}


function submitSave1(){
    let wordSet = setOptionSave()
    if(language === 'EN'){
        if(input_translate_save.value.toUpperCase() ===  wordSet[wordOrderSave].eng.toUpperCase()){
            answerTrueSave()
        }else{
            input_translate_save.value = ''
            check_word_save.innerHTML = `
            <i class="fa-solid fa-circle-xmark"></i>
            <p class="real_answer">
                ${wordSet[wordOrderSave].eng}
            </p> `
            speak(wordSet[wordOrderSave].eng)
            setTimeout(()=>{check_word_save.innerHTML = ''},3000)
        }
    }else{
        if(typeof(wordSet[wordOrderSave].thai) === typeof([])){
            if(wordSet[wordOrderSave].thai.includes(input_translate_save.value)){
                answerTrueSave()
            }else{
                input_translate_save.value = ''
                check_word_save.innerHTML = `
                <i class="fa-solid fa-circle-xmark"></i>
                <p class="real_answer">
                    ${wordSet[wordOrderSave].thai}
                </p> `
                setTimeout(()=>{check_word_save.innerHTML = ''},3000)
            }
        }
        else if(input_translate_save.value === wordSet[wordOrderSave].thai){
            answerTrueSave()
        }else{
            input_translate_save.value = ''
            check_word_save.innerHTML = `
            <i class="fa-solid fa-circle-xmark"></i>
            <p class="real_answer">
                ${wordSet[wordOrderSave].thai}
            </p> `
            setTimeout(()=>{check_word_save.innerHTML = ''},3000)
        }
    }
}




function showSaveWord(){
    Mode_check = 'statusSaveWord1000'
    openSaveWord()
    setOptionSave()
    questionSave()
}

input_translate_save.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        submitSave1()
    }
});


function submitSave(){}


let wordOrderSave = 0