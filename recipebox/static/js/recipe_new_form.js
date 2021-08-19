function addIngredientToTable() {
    let ingredientsTable = document.getElementById('ingredientsTable').getElementsByTagName('tbody')[0];
    let newRow = ingredientsTable.insertRow()

    let newAmount = document.getElementById('recipe_ingredients_amount')
    let amountCell = newRow.insertCell()
    let amountText = document.createTextNode(newAmount.value)
    amountCell.setAttribute("data-value", newAmount.value)
    amountCell.appendChild(amountText)

    let newUnit = document.getElementById('recipe_ingredients_unit')
    let unitCell = newRow.insertCell(-1)
    let unitText = document.createTextNode(newUnit.value)
    unitCell.setAttribute("data-value", newUnit.value)
    unitCell.appendChild(unitText)

    let newIngredient = document.getElementById('recipe_ingredients_ingredient');
    let ingredientCell = newRow.insertCell(-1)
    let ingredientText = document.createTextNode(newIngredient.options[newIngredient.selectedIndex].text)
    ingredientCell.setAttribute("data-value", newIngredient.options[newIngredient.selectedIndex].value)
    ingredientCell.appendChild(ingredientText)

    console.log("added item")
}

function addProcedureToTable() {
    let procedureTable = document.getElementById('procedureTable').getElementsByTagName('tbody')[0];
    let newRow = procedureTable.insertRow()

    let newStep = document.getElementById('recipe_step_text')
    let stepCell = newRow.insertCell(-1)
    let stepText = document.createTextNode(newStep.innerText)
    stepCell.setAttribute("data-value", newStep.innerText)
    stepCell.appendChild(stepText)

    newStep.innerText = (parseInt(newStep.innerText) + 1).toString();

    let newProcedure = document.getElementById('recipe_procedure_text')
    let procedureCell = newRow.insertCell(-1)
    let procedureText = document.createTextNode(newProcedure.value)
    procedureCell.setAttribute("data-value", newProcedure.value)
    procedureCell.appendChild(procedureText)
}

function submitForm(){
    let recipeAmount = document.getElementById('recipe_amount')
    let recipeUnit = document.getElementById('recipe_unit')
    let recipeIngredients = document.getElementById('recipe_ingredients')
    let ingredientsTable = document.getElementById('ingredientsTable')

    for (let i = 1; i < ingredientsTable.rows.length; i++) {
        recipeAmount.value += ingredientsTable.rows.item(i).cells.item(0).dataset.value + ','
        recipeUnit.value += ingredientsTable.rows.item(i).cells.item(1).dataset.value + ','
        recipeIngredients.value += ingredientsTable.rows.item(i).cells.item(2).dataset.value + ','
    }

    let recipeStep = document.getElementById('recipe_step')
    let recipeProcedure = document.getElementById('recipe_procedure')
    let procedureTable = document.getElementById('procedureTable')

    for (let i = 1; i < procedureTable.rows.length; i++) {
        recipeStep.value += procedureTable.rows.item(i).cells.item(0).dataset.value + ','
    }
}

console.log('loaded js')

let ingredientButton = document.getElementById('add-ingredient-btn')
ingredientButton.setAttribute("onclick", "addIngredientToTable();")

let procedureButton = document.getElementById('add-procedure-btn')
procedureButton.setAttribute("onclick", "addProcedureToTable();")

let submitButton = document.getElementById('submit')
submitButton.setAttribute("onclick", "submitForm();")
