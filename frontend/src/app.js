const multimeterGetBtn = document.getElementById('multimeterGetBtn');
const wfgGetBtn = document.getElementById('wfgGetBtn');
const display_multimeter = document.getElementById('display-multimeter');
const display_wfg = document.getElementById('display-wfg');
const { ipcRenderer } = require('electron');


multimeterGetBtn.addEventListener('click', ()=>{

    ipcRenderer.on('fetch-multimeter-data-response', (event, data) => {
        display_multimeter.innerHTML = JSON.stringify(data);
    });
    ipcRenderer.send('fetch-multimeter-data');
});

wfgGetBtn.addEventListener('click', () => {
    ipcRenderer.on('fetch-wfg-data-response', (event, data) => {
        display_wfg.innerHTML = JSON.stringify(data);
    });
    ipcRenderer.send('fetch-wfg-data');
});