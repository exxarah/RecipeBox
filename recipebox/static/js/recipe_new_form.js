function addIngredient() {
    let recipeIngredients = document.getElementsByClassName("recipe-ingredients")[0]
    let clone = recipeIngredients.cloneNode(true)
    document.getElementsByClassName('ingredients-parent')[0].appendChild(clone)
}

function removeIngredient(element){
    let recipeIngredients = document.getElementsByClassName("recipe-ingredients")
    if (recipeIngredients.length <= 1){
        alert("Your recipe must include at least 1 ingredient")
        return
    }
    element.parentElement.parentElement.remove()
}

function addProcedure() {
    let recipeProcedures = document.getElementsByClassName("recipe-procedures")[0]
    let clone = recipeProcedures.cloneNode(true)
    document.getElementsByClassName('procedures-parent')[0].appendChild(clone)
}

function removeProcedure(element) {
    let recipeProcedures = document.getElementsByClassName("recipe-procedures")
    if (recipeProcedures.length <= 1){
        alert("Your recipe must include at least 1 step")
        return
    }
    element.parentElement.parentElement.remove()
}

let ingredientButton = document.getElementById('add-ingredient-btn')
ingredientButton.setAttribute("onclick", "addIngredient();")

ingredientButton = document.getElementById('remove-ingredient-btn')
ingredientButton.setAttribute("onclick", "removeIngredient(this);")

let procedureButton = document.getElementById('add-procedure-btn')
procedureButton.setAttribute("onclick", "addProcedure();")

procedureButton = document.getElementById('remove-procedure-btn')
procedureButton.setAttribute("onclick", "removeProcedure(this);")

