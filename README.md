# Knapsack-project
The Knapsack Problem is defined as follows:  A thief robbing a store findsnitems.  Theith item isworthvidollars and weighswipounds, whereviandwiare positive integers.  The thief wants totake as valuable a load as possible, but can carry at mostWpounds in his/her knapsack, for someintegerW.  Which items should the thief steal?

# Solution Methods
Exhaustive Apprach
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
