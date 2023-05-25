//stetusDropdown
let tabMenu = document.querySelector('.tab-menu')
let iconMenu = document.querySelector('.icon-tabmenu')
let dropDown = document.querySelector('.drop-down')

// content
let save = document.querySelector('.mysave')
let savePage = document.querySelector('.pageSave_word')
let learnword = document.querySelector('.learnword')
let wordPage = document.querySelector('.word1000-page')
let saveWord = document.querySelectorAll('.save-word')
let mysetting = document.querySelector('.mysetting')
let settingPage = document.querySelector('.setting-page')
let table = document.querySelector('.table')



//show save
let word1000_page_save = document.querySelector('.word1000-page-save')



//stetusDropdown
function clickDropdown(){
    if(stetusDropdown === 'open'){
        tabMenu.style.width = '150px'
        tabMenu.style.border = 'none'
        dropDown.style.display = 'none'
        stetusDropdown = 'close'
    }else{
        tabMenu.style.width = '260px'
        tabMenu.style.borderRight = '.5px solid rgba(0, 0, 0, 0.25)'
        setTimeout(()=> dropDown.style.display = 'block',200)
        stetusDropdown = 'open'
    }
}


function openWord(){
    wordPage.style.display = 'block'
    saveWord[0].style.background = '#77777710'
    saveWord[0].style.color = '#756ef6'
    checkStatusSave()
}
function closeWord(){
    wordPage.style.display = 'none'
    saveWord[0].style.color = 'black'
    saveWord[0].style.background = 'none'
}

function openSave(){
    savePage.style.display = 'block'
    saveWord[1].style.background = '#77777710'
    saveWord[1].style.color = '#756ef6'
}
function closeSave(){
    savePage.style.display = 'none'
    saveWord[1].style.background = 'none'
    saveWord[1].style.color = 'black'
    word1000_page_save.style.display = 'none'
}
function openSetting(){
    settingPage.style.display = 'block'
    saveWord[2].style.background = '#77777710'
    saveWord[2].style.color = '#756ef6'
}
function closeSetting(){
    settingPage.style.display = 'none'
    saveWord[2].style.background = 'none'
    saveWord[2].style.color = 'black'
}


// main
function statusWord(){
    Mode_check = 'statusWord'
    openWord()
    closeSave()
    closeSetting()
}
function statusSave(){
    openSave()
    createTable()

    closeWord()
    closeSetting()
    
    let number = data.filter(e => e.save === 'yes')
    console.log(number.length);
    if(number.length < 3 ){
        document.querySelector('.repeat').style.display = 'none'
        setTimeout(()=>{
            alert(`บันทึกคำศัพท์ เพิ่มอีก ${3 - number.length}ข้อ เพื่อทำแบบทดสอบ`)
        },500)
    }else{
        document.querySelector('.repeat').style.display = 'block'
    }
}
function statusSetting(){
    openSetting()

    closeSave()
    closeWord()
}

let HtmlTable = `
    <p class="table-head column0">ลำดับ</p>
    <p class="table-head line-left">TH</p>
    <p class="table-head line-left">EN</p>
    <p class="table-head line-left center">ลบ</p>
`

function dataAll_save(){
    const saveEnglish = data.filter((item,idex)=>{
        return item.save === 'yes'
    })
    return saveEnglish
}

function createTable(){
    const saveEnglish = dataAll_save()
    saveEnglish.forEach((item,index)=>{
        HtmlTable += `
        <p class="table-child column0">${index +1}</p>
        <p class="table-child line-left">${item.thai}</p>
        <p class="table-child line-left">${item.eng}</p>
        <p><i class="fa-solid fa-circle-xmark IconDelete" onclick="deleteIconXmark(${index})" ></i></p>
        `
    })

    table.innerHTML = HtmlTable
    HtmlTable = `
    <p class="table-head column0">ลำดับ</p>
    <p class="table-head line-left">TH</p>
    <p class="table-head line-left">EN</p>
    <p class="table-head line-left center">ลบ</p>
`
}

function deleteIconXmark(index){
    const saveEnglish = dataAll_save()
    let findIndex = data.findIndex(item => item.eng === saveEnglish[index].eng)
    data[findIndex].save = 'no'
    // console.log(findIndex);
    // console.log(data[findIndex].eng);
    createTable()
}






//stetusDropdown
let stetusDropdown = 'open' // 5-17




//stetusDropdown
iconMenu.addEventListener('click',()=>{
    clickDropdown()
})

save.addEventListener('click',statusSave)
learnword.addEventListener('click',statusWord)
mysetting.addEventListener('click',statusSetting)

statusWord()