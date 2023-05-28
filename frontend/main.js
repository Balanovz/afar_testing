const { app, BrowserWindow, Menu, ipcMain } = require('electron')
require('electron-reload')(__dirname)
const axios = require('axios');


function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile('./src/index.html');
    mainWindow.webContents.openDevTools();

    let menu = Menu.buildFromTemplate([]);
    Menu.setApplicationMenu(menu);

    ipcMain.on('fetch-multimeter-data', async (event, args) => {
        try {
            const response_mult = await axios.get('http://127.0.0.1:8000/multimeter/');
            event.reply('fetch-multimeter-data-response', response_mult.data);
        } catch (error) {
            console.error(error);
        }
    });

    ipcMain.on('fetch-wfg-data', async (event, args) => {
        try{
            const response = await axios.get('http://127.0.0.1:8000/wfg/');
            event.reply('fetch-wfg-data-response', response.data);
        } catch (error) {
            console.error(error);
        }
    });
}

app.whenReady().then(createWindow);
