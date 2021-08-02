function addIngredientToTable() {
  var ingredientsTable = document.getElementById('ingredientsTable').getElementsByTagName('tbody')[0]

  var newIngredient = document.getElementById('ingredients')
  var newAmount = document.getElementById('amount')
  var newUnit = document.getElementById('unit')

  var newRow = ingredientsTable.insertRow()

  var ingredientCell = newRow.insertCell()
  var ingredientText = document.createTextNode(newIngredient.options[newIngredient.selectedIndex].text)
  ingredientCell.setAttribute("value", newIngredient.options[newIngredient.selectedIndex].value)
  ingredientCell.appendChild(ingredientText)

  var amountCell = newRow.insertCell(-1)
  var amountText = document.createTextNode(newAmount.value)
  amountCell.setAttribute("value", newAmount.value)
  amountCell.appendChild(amountText)

  var unitCell = newRow.insertCell(-1)
  var unitText = document.createTextNode(newUnit.options[newUnit.selectedIndex].text)
  unitCell.setAttribute("value", newUnit.options[newUnit.selectedIndex].value)
  unitCell.appendChild(unitText)


  console.log('add ingredient')
}

function submitForm(){
  console.log('post form')
}

console.log('loaded js')

var addButton = document.getElementById('add_ingredient')
addButton.setAttribute("onclick", "addIngredientToTable();")

var submitButton = document.getElementById('submit')
submitButton.setAttribute("onclick", "submitForm();")
