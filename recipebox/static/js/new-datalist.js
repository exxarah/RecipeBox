var inputs = document.getElementsByClassName('datalist-input')
var datalists = document.getElementsByClassName('datalist-list')
var keepListOpen = false;

for (let input of inputs) {
  for (let datalist of datalists){

    input.onfocus = function () {
      datalist.style.display = 'block';
      input.style.borderRadius = "5px 5px 0 0";
    };

    input.onblur = function () {
      if (!keepListOpen)
        datalist.style.display = 'none';
    }

    input.oninput = function() {
      let text = input.value.toUpperCase();
      for (let option of datalist.options) {
        if(option.value.toUpperCase().indexOf(text) > -1){
          option.style.display = "block";
        }else{
          option.style.display = "none";
        }
      }
    }

    for (let option of datalist.options) {
      option.onmousedown = function() {
        keepListOpen = true;
      }
      option.onclick = function () {
        input.value = option.innerHTML
        datalist.style.display = 'none';
        input.style.borderRadius = "5px";
      }
    }


    window.onmouseup = function () {
      if (keepListOpen) {
          datalist.style.display = 'none';
          keepListOpen = false;
      }
    }

  }
}