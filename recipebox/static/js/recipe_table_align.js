console.log('loaded recipe_table_align.js')

var tableAmount = document.getElementById('table-amount')
var tableUnit = document.getElementById('table-unit')
var tableIngredient = document.getElementById('table-ingredient')

tableAmount.style.width = $("#recipe_ingredients_amount").css('width');
tableUnit.style.width = $("#recipe_ingredients_unit").css('width');
tableIngredient.style.width = $("#recipe_ingredients_ingredient").css('width');

var tableStep = document.getElementById('table-step')
var tableProcedure = document.getElementById('table-procedure')

tableStep.style.width = $("#recipe_step_text").css('width');
tableProcedure.style.width = $("#recipe_procedure_text").css('width');