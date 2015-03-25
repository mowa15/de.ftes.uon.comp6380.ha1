TODO: error curves

# a) Original Dataset

## Steps

1. data obtained from [http://wiki.cs.brynmawr.edu/?page=TwoSpiralsProblem](http://wiki.cs.brynmawr.edu/?page=TwoSpiralsProblem)
    1. version on blackboard did not contain class identifiers
    2. according to the code in the [original paper](http://www.researchgate.net/publication/269337640_Learning_to_Tell_Two_Spirals_Apart), this seems to be the correct format
2. converted spaces to tabs
3. processed with Pybrain ([pybrain-classify.py](pybrain-classify.py))
    1. followed [tutorial](http://pybrain.org/docs/tutorial/fnn.html)
    2. used two binary output neurons (``dataset._convertToOneOfMany(bounds=[0.,1.])``)
    3. used ideas from [Beherey et al.](http://www.hindawi.com/journals/acisc/2009/721370/)
        1. network layout: 2 hidden layers with 77 neurons each
        2. activation: tanh for hidden layers, linear for output
        3. RPROP as training algorithm, because it converges faster than back propagation
 
## Result

- reproduce by running [pybrain-classify.py](pybrain-classify.py)
- visualization of final result not available (plot stopped responding)
    - [intermediate output](original-dataset-intermedidate-output.png)
- training error achieved after 5000 epochs: 0.52% (1 misclassified)


# b) Self-generated dataset

## Steps

1. generated data set using algorithm in blackboard [denser-dataset.png](denser-dataset.png)
    1. far denser spirals
    2. 1920 (10x as many) data points
2. trained feed-forward net with same characteristics as in a) on new data

## Result

- faster conversion