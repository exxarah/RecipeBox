var input = document.getElementById('ingredients-input')
var ingredients = document.getElementById('ingredients')
var keepListOpen = false;

input.onfocus = function () {
  ingredients.style.display = 'block';
  input.style.borderRadius = "5px 5px 0 0";
};

input.onblur = function () {
  if (!keepListOpen)
    ingredients.style.display = 'none';
}

input.oninput = function() {
  let text = input.value.toUpperCase();
  for (let option of ingredients.options) {
    if(option.value.toUpperCase().indexOf(text) > -1){
      option.style.display = "block";
    }else{
      option.style.display = "none";
    }
  }
}

for (let option of ingredients.options) {
  option.onmousedown = function() {
    keepListOpen = true;
  }
  option.onclick = function () {
    input.value = option.innerHTML
    ingredients.style.display = 'none';
    input.style.borderRadius = "5px";
  }
}


window.onmouseup = function () {
  if (keepListOpen) {
      ingredients.style.display = 'none';
      keepListOpen = false;
  }
}