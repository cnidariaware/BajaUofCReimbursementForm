//import fs from 'fs';

const submitButton = document.getElementById("submitButton");
const inputBoxes = document.getElementsByTagName("input");


const buttonClick = async (event) => {
    submitButton.disabled = true;
    submitButton.innerText = "Working...";
    submitButton.style.backgroundColor = 'grey';
    submitButton.classList.add('disabled');
    submitButton.style.cursor = 'not-allowed';

    var inputValues = [];
    for (let key in inputBoxes) {
        if (inputBoxes[key].value == undefined) {
            break;
        }
        inputValues.push(inputBoxes[key].value);
    }

    let date = new Date();
    var month = (date.getMonth() + 1).toString();
    var day = date.getDate().toString();
    var year = date.getFullYear().toString();
    var currentDate = month + day + year;
    let fileWrite = inputValues[0] + currentDate;
    let fileExt = getFileExtension(inputValues[3]);
    fileWrite += "." + fileExt;
    inputValues.push(fileWrite);
    console.log( inputValues)
    
    //fake delay

    await Fakedelay(5000)
    console.log("fake delay");
    submitButton.disabled = false;
    submitButton.innerText = "Submit";
    submitButton.style.backgroundColor = 'green';
    submitButton.style.cursor = '';
    isButtonDisabled = false;
    // Need to send to the synology server through the back end...
};



function getFileExtension(fileName) {
    const lastDotIndex = fileName.lastIndexOf(".");
    if (lastDotIndex === -1 || lastDotIndex === fileName.length - 1) {
      return "bad"; // No extension found or the dot is at the end of the filename
    }
    return fileName.slice(lastDotIndex + 1);
  }

const sendForm = async (toSend) => {
    if (1) {
        return 1;
    }
    else {
    const res = await fetch("http://jsonplaceholder.typicode.com/todos", {
        method: "POST",
        body: JSON.stringify({
            stuff: 1,
            lots:  "of stuff"
        }),
        headers: {
            "Optional": "no"
        }
    });
    }
    //to do finish this off so that it works
}

function Fakedelay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }