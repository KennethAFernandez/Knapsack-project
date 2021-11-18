            __  __                  ______  
            _ \/ /_____________________  /__
            __  /__  __ \_  __ \  _ \_  //_/
            _  / _  / / /  / / /  __/  ,<   
            /_/  /_/ /_//_/ /_/\___//_/|_|  



# Solution Methods

Exhaustive Apprach:
```
  Let powerSet = all subsets
  knapsack = { } 
  bestValue = 0
  for each subset in powerSet do
    subsetValue = 0
    subsetWeight = 0
    for each item in subset do
      subsetValue += item.value
      subsetWeight += item.weight
    if subsetWeight < WEIGHT_CAPACITY AND subsetValue > bestValue then
      bestValue = subsetValue
      knapsack = subset
  return knapsack
```

Value to Weight Heuristic:
```
  knapsack = { }
  currentW = WEIGHT_CAPACITY
  // Sort items decreasing order of (value / weight), if tie sort decreasing order by value
  for each item in items do
    if item.weight < currentW then
      knapsack.add(item)
      currentW = currentW - item.weight
  return knapsack
```
