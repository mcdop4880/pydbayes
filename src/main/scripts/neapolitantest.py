import math

import pandas as pan
import pydbayes.scoring


##########################################################################
# Test out the scoring systems Neapolitan p446

testData = {'x': pan.Series([1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0]),
            'y': pan.Series([1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0])}
testData = pan.DataFrame(testData)
prior = pan.Series([2.0, 2.0])
testData = testData - 1
independentScore = pydbayes.scoring.MSR(testData[testData.columns[0]], prior) + pydbayes.scoring.MSR(
    testData[testData.columns[1]], prior)
print(math.exp(independentScore))

dataMatrix = pan.crosstab(testData[testData.columns[0]], testData[testData.columns[1]])
priorMatrix = {'x': pan.Series([1.0, 1.0]), 'y': pan.Series([1.0, 1.0])}
priorMatrix = pan.DataFrame(priorMatrix)

dependentScore = pydbayes.scoring.MSR(testData[testData.columns[0]], prior) + pydbayes.scoring.MCR(testData,
                                                                                                   priorMatrix, 0, 1)
print(math.exp(dependentScore))
print(math.exp(dependentScore) / (math.exp(dependentScore) + math.exp(independentScore)))

# Test symmetrical scoring
dependentScore2 = pydbayes.scoring.MSR(testData[testData.columns[0]], prior) + pydbayes.scoring.MCR(testData,
                                                                                                    priorMatrix, 1, 0)
print(dependentScore == dependentScore2)
print(math.exp(dependentScore) / (math.exp(dependentScore) + math.exp(independentScore)))

##########################################################################
