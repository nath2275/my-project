// speak //////////////////////////////////////////////////////////////////////////
var voiceList = document.querySelector('#voiceList');
var synth = window.speechSynthesis;
var voices = [];

PopulateVoices();
if(speechSynthesis !== undefined){
    speechSynthesis.onvoiceschanged = PopulateVoices;
}
function speak(text){
    var toSpeak = new SpeechSynthesisUtterance(text);
    var selectedVoiceName = voiceList.selectedOptions[0].getAttribute('data-name');
    voices.forEach((voice)=>{
        
        if(voice.name === selectedVoiceName){
            toSpeak.voice = voice;
        }
    });
    synth.speak(toSpeak);
}


function PopulateVoices(){
    voices = synth.getVoices();
    var selectedIndex = voiceList.selectedIndex < 0 ? 0 : voiceList.selectedIndex;
    voiceList.innerHTML = '';
    voices.forEach((voice,i)=>{
        //console.log(i,voice.name);//81 //82
        if (i === 0 || i===1 || i===81 || i===82){
            var listItem = document.createElement('option');
            listItem.textContent = voice.name;
            listItem.setAttribute('data-lang', voice.lang);
            listItem.setAttribute('data-name', voice.name);
            voiceList.appendChild(listItem);
        }
    });

    voiceList.selectedIndex = selectedIndex;
}
// speak //////////////////////////////////////////////////////////////////////////


// function speakThai(){
//     let msg = new SpeechSynthesisUtterance('สวัสดีครับ วันนี้ผมมีเรื่องจะมาเล่าให้ท่านฟังครับ');
//     msg.voiceURI = 'native'; //ตัวนี้บอกว่ามันจะใช้ตัวสังเคาะห์ภายใน (แปลว่าอะไรไม่รู้แต่มันจะสามารถใช้ได้โดยไม่มีการเชื่อมต่อเน็ตก็ตาม)
//     msg.volume = 1; // 0 ถึง1 เป็นระดับความดัง
//     msg.rate = 1.2; // 0.1 ถึง 10 อัตราเร็วของการพูด
//     msg.pitch = 1; //0 ถึง 2 // ลักษณะระดับเสียงสูงต่ำ
//     msg.lang = 'th-TH';
//     speechSynthesis.speak(msg)
// }
