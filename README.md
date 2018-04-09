# Programming-for-Spatial-Analysts-Assessment-2
The final code for Assessment 2 in the module: Programming for Spatial Analysis: Advanced Skills. This Agent-Based Model simulates the movement of drunk people attempting to get home.

### Key Model Notes

* The provided town plan (town.plan.txt) file is used to set the model environment and is read into the model row by row. 
* A new environment is created using the same layout as the town plan, this time with each cell being 0. This is used to create a density map. 
* Using the x and y coordinates, each agent is commanded to identify the location of the pub, and start off there when the model is initiated. 
* Agents are then allocated an ID number and house number (calculated as (ID#+1)*10). 
* Each agent is instructed to navigate the town in random directions until it has reached its home. 
* Each step taken is recorded on the new environment output, each step on a cell increases its value by one. 
* If an agent has not reached its home, it will continue to wander until it has, taking as many model iterations as required. 
* Once all agents have arrived home, the new environment file is saved and printed, producting a density map. 
* When an agent has reached home, it will call out "What a journey! WHERE'S MY BED!!", letting the user knowits arrival. 
* The intial map will reopen at the end of the model run, displaying each agent at their home. 
* Finally, a new window will open displaying the new environment map, coloured to show the density of each map cell. 
* The new environment will also be saved as a .csv, so the number of steps can be viewed. 
