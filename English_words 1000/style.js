


//language
let bt_en = document.querySelector('.bt_en')
let bt_th = document.querySelector('.bt_th')

//icon translate
let boxSave = document.querySelector('.box-save')
let iconSave = document.querySelector('.icon-save')
let boxSpeaker = document.querySelector('.box-speaker')
let iconSpeaker = document.querySelector('.icon-speaker')
let boxRepeat = document.querySelector('.box-repeat')

//learn english words 1,000 page
let count_range = document.querySelector('.count_range')

//input
const wordList = document.querySelector('.wordList')
const input_translate = document.querySelector('.input_translate')
// หมวดที่ a ศัพท์ที่ 1
const bt_type = document.querySelector('.bt_type')
const bt_at_word = document.querySelector('.bt_at_word')
//answer
const real_answer = document.querySelector('.real_answer')
const check_word = document.querySelector('.check_word')
//point
const check_user_true = document.querySelector('.check_user_true')
const check_user_wrong = document.querySelector('.check_user_wrong')

// const Continue = document.querySelector('.continue')


//language
function ModeLanguage(){
    if(language === 'EN'){
        bt_en.style.background = 'none'
        bt_en.style.color = '#FF7C7C'
        bt_th.style.color = '#fff'
        bt_th.style.background = '#7F96E7'
        bt_th.style.border = '1.5px solid #7F96E7'
        language = 'TH'
        if(Mode_check === 'statusWord'){
            question()
        }else if(Mode_check === 'statusSaveWord1000'){
            questionSave()
        }
        
    }else{
        bt_th.style.background = 'none'
        bt_th.style.color = '#7F96E7'
        bt_en.style.color = '#FFf'
        bt_en.style.background = '#FF7C7C'
        bt_en.style.border = '1.5px solid #FF7C7C'
        language = 'EN'
        if(Mode_check === 'statusWord'){
            question()
        }else if(Mode_check === 'statusSaveWord1000'){
            questionSave()
        }
    }
}

//icon translate 
// check save
function checkStatusSave(){
    let wordSet = List_word()
    wordSet[wordOrder].save
    if (wordSet[wordOrder].save === 'no'){
        boxSave.innerHTML = '<i class="fa-regular fa-bookmark icon-save"></i>'
    }else{

        boxSave.innerHTML = '<i class="fa-solid fa-bookmark icon-save"></i>'
    }
}

function styleCheckSave(){
    let wordSet = List_word()
    wordSet[wordOrder].save
    if (wordSet[wordOrder].save === 'no'){
        boxSave.innerHTML = '<i class="fa-solid fa-bookmark icon-save"></i>'
        wordSet[wordOrder].save = 'yes'
    }else{
        boxSave.innerHTML = '<i class="fa-regular fa-bookmark icon-save"></i>'
        wordSet[wordOrder].save = 'no'
    }
    // if (checkSave === 'no'){
    //     boxSave.innerHTML = '<i class="fa-solid fa-bookmark icon-save"></i>'
    //     checkSave = 'yes'
    // }else{
    //     boxSave.innerHTML = '<i class="fa-regular fa-bookmark icon-save"></i>'
    //     checkSave = 'no'
    // }
}
// check Speaker ลำโพงเปิด - ปิด
/*
function styleCheckSpeaker(){
    if (checkSpeaker === 'no'){
        boxSpeaker.innerHTML = '<i class="fa-solid fa-volume-high icon-speaker"></i>'
        checkSpeaker = 'yes'
    }else{
        boxSpeaker.innerHTML = '<i class="fa-solid fa-volume-xmark icon-speaker"></i>'
        checkSpeaker = 'no'
    }
}
*/

//learn english words 1,000 page
function ChangeSetValue(){
    wordOrder = 0
    document.querySelector('.setNumber').innerHTML = `set ${count_range.value}`
    question()
}
function reduceSetValue(){
    count_range.value = `${Number(count_range.value) - 1}`
    ChangeSetValue()
    
}
function addSetValue(){
    count_range.value = `${Number(count_range.value) +1}`
    ChangeSetValue()
}

function List_word(){
    //learn english words 1,000 page
    count_range.max = Math.ceil(data.length / groupSet)
    let set = Number(count_range.value)
    let min = (set - 1) * groupSet
    let max = set * groupSet

    bt_at_word.innerHTML = `ศัพท์ที่ ${min + wordOrder+1}`

    let wordSet = data.filter((item,index)=>{
        return index >= min && index < max
    })
    return wordSet

}

function question(){
    checkStatusSave()
    let wordSet = List_word()
    bt_type.innerHTML = `หมวด ${wordSet[wordOrder].eng[0]}`
    if(language === 'EN'){
        if(typeof(wordSet[wordOrder].thai) === typeof([])){
            boxRepeat.style.display = 'block'
            wordList.innerHTML = wordSet[wordOrder].thai[0]
        }else{
            boxRepeat.style.display = 'none'
            wordList.innerHTML = wordSet[wordOrder].thai
        }
        
    }else{
        boxRepeat.style.display = 'none'
        wordList.innerHTML = wordSet[wordOrder].eng
        speak(wordSet[wordOrder].eng)
    }

}
function checkEnd(){
    let setMax = Math.ceil(data.length / groupSet) 
    return [setMax,data.length]
}

function answerTrue(){
    let setMax = checkEnd()
    let set = Number(count_range.value)
    if(pointTrue< 1000){pointTrue += 1}
    else{pointTrue = '1,000'}

    check_user_true.innerHTML = pointTrue
    input_translate.value = ''
    check_word.innerHTML = `
    <i class="fa-solid fa-circle-check green"></i>
    <p class="real_answer" id="green">
        เยี่ยม
    </p>`
    incessant += 1
    setTimeout(()=>{
        wordOrder += 1
        // console.log('wordOrder =',wordOrder);
        // console.log('incessant =',incessant);
        if(incessant >= groupSet && wordOrder >= groupSet){
            addSetValue()
            incessant = 0
            wordOrder = 0
            console.log('success');
        }
        else if(wordOrder >= groupSet){
            // addSetValue()
            wordOrder = 0
        }
        else if(setMax[0] * groupSet > setMax[1] && set >= setMax[0] && wordOrder >= groupSet - ((setMax[0] * groupSet) - setMax[1]) ){
            count_range.value = '0'
            console.log(count_range.value);
            ChangeSetValue()
        }
        check_word.innerHTML = ''
        question()
    },1200)
}


function submit(){
    let wordSet = List_word()
    if(language === 'EN'){
        if(input_translate.value.toUpperCase() ===  wordSet[wordOrder].eng.toUpperCase()){
            answerTrue()
        }else{
            if(pointFalse< 1000){pointFalse += 1}
            else{pointFalse = '1,000'}
            check_user_wrong.innerHTML = pointFalse
            incessant = 0
            input_translate.value = ''
            check_word.innerHTML = `
            <i class="fa-solid fa-circle-xmark"></i>
            <p class="real_answer">
                ${wordSet[wordOrder].eng}
            </p> `
            speak(wordSet[wordOrder].eng)
            setTimeout(()=>{check_word.innerHTML = ''},3000)
        }
    }else{
        if(typeof(wordSet[wordOrder].thai) === typeof([])){
            if(wordSet[wordOrder].thai.includes(input_translate.value)){
                answerTrue()
            }else{
                if(pointFalse< 1000){pointFalse += 1}
                else{pointFalse = '1,000'}
                check_user_wrong.innerHTML = pointFalse
                incessant = 0
    
                input_translate.value = ''
                check_word.innerHTML = `
                <i class="fa-solid fa-circle-xmark"></i>
                <p class="real_answer">
                    ${wordSet[wordOrder].thai}
                </p> `
                setTimeout(()=>{check_word.innerHTML = ''},3000)
            }
        }
        else if(input_translate.value === wordSet[wordOrder].thai){
            answerTrue()
        }else{
            if(pointFalse< 1000){pointFalse += 1}
            else{pointFalse = '1,000'}
            check_user_wrong.innerHTML = pointFalse
            incessant = 0

            input_translate.value = ''
            check_word.innerHTML = `
            <i class="fa-solid fa-circle-xmark"></i>
            <p class="real_answer">
                ${wordSet[wordOrder].thai}
            </p> `
            setTimeout(()=>{check_word.innerHTML = ''},3000)
        }
    }
    
}



input_translate.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        submit()
    }
});







//language
let language = 'EN'

//icon translate // check save
let checkSave = 'no'
let checkSpeaker = 'yes'

//learn english words 1,000 page
let groupSet = 3
count_range.max = Math.ceil(data.length / groupSet)
let wordOrder = 0
// ความถูกต่อเนื่องของคำ
let incessant = 0
//point
let pointTrue = 0
let pointFalse = 0

//language
bt_en.addEventListener('click',ModeLanguage)
bt_th.addEventListener('click',ModeLanguage)

//icon translate 
// check save
boxSave.addEventListener('click',styleCheckSave)
// boxSpeaker.addEventListener('click',styleCheckSpeaker)
// boxSpeaker.addEventListener('click',question)



//learn english words 1,000 page
question()