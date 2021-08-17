function addIngredientToTable() {
  var ingredientsTable = document.getElementById('ingredientsTable').getElementsByTagName('tbody')[0]

  var newIngredient = document.getElementById('recipe_ingredients_ingredient')
  var newAmount = document.getElementById('recipe_ingredients_amount')
  var newUnit = document.getElementById('recipe_ingredients_unit')

  var newRow = ingredientsTable.insertRow()

  var amountCell = newRow.insertCell()
  var amountText = document.createTextNode(newAmount.value)
  amountCell.setAttribute("value", newAmount.value)
  amountCell.appendChild(amountText)

  var unitCell = newRow.insertCell(-1)
  var unitText = document.createTextNode(newUnit.value)
  unitCell.setAttribute("value", newUnit.value)
  unitCell.appendChild(unitText)

  var ingredientCell = newRow.insertCell(-1)
  var ingredientText = document.createTextNode(newIngredient.options[newIngredient.selectedIndex].text)
  ingredientCell.setAttribute("value", newIngredient.options[newIngredient.selectedIndex].text)
  ingredientCell.appendChild(ingredientText)

  console.log("added item")
}

function submitForm(){
  var recipeAmount = document.getElementById('recipe_amount')
  var recipeUnit = document.getElementById('recipe_unit')
  var recipeIngredients = document.getElementById('recipe_ingredients')
  var ingredientsTable = document.getElementById('ingredientsTable')

  for (var i = 1; i < ingredientsTable.rows.length; i++) {
    recipeAmount.value += ingredientsTable.rows.item(i).cells.item(0).value + ','
    console.log(recipeAmount.value)
  }
}

console.log('loaded js')

var addButton = document.getElementById('add-ingredient-btn')
addButton.setAttribute("onclick", "addIngredientToTable();")


var submitButton = document.getElementById('submit')
submitButton.setAttribute("onclick", "submitForm();")
