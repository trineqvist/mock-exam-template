# GSM - Assignment

In this assignment you will solve a number of tasks related to genome-scale metabolic models using both the E. coli Core and iML1515 genome-scale model.

In `assignment.py`:

1. Simulate the model. What is the reaction with the largest flux magnitude?
2. What are the exchange reactions in the model that can facilitate the uptake of carbon sources?
3. What are the carbon sources that E. coli can grow on anaerobically?
4. Add the capability to produce 3-Hydroxypropanoate (3HP) to the full genome-scale model of E. coli (iML1515). What is the maximum production rate of 3HP.
5. What is the maximum production rate of 3HP at 20% growth (also using iML1515)?


Hints:
* `assignment.py` contains hints and recommendations both in the beginning and in the comments to each task.
* Remember to undo modifications to the model before continuing with the next task (either make a copy of the model for each task or use the `with model: ...` statement as shown in the exercise).
* If not mentioned otherwise, use the default conditions set in the model.


*The Rules*:
* Every tasks needs to be solved programmatically going from the provided data to the final result, do not use manual steps in between.
* The ideal solution contains code only, is self-explanatory and provides sufficient context for the teacher to follow the solution process.
* Do not replace the placeholders _ with numbers that you took directly out of the test cases, manually calculated or guessed. Ideally placeholders _ should be replaced with the final calculation step or a variable that contains the result of the final calculation step.
* Use human readable variable/function names (avoid cryptic abbreviations and one letter variables). Consider the recommendations laid out in https://www.python.org/dev/peps/pep-0008/
