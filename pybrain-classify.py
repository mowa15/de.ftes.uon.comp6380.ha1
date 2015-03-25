__author__ = 'Fredrik'

in_file = 'data-with-headers-tabs.txt'
margins = 0., 1.
#in_file = 'denser-data-with-headers-tabs.txt'
#margins = -1., 1.

from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer, RPropMinusTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.structure.modules import TanhLayer, LinearLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where

# http://stackoverflow.com/questions/10133386/pybrain-loading-data-with-numpy-loadtxt
import numpy
array = numpy.loadtxt(in_file, delimiter='\t', skiprows=1)
number_of_columns = array.shape[1]
dataset = ClassificationDataSet(number_of_columns - 1, target=1, nb_classes=2)
for row in array:
    dataset.addSample(row[:-1], row[-1:])

dataset._convertToOneOfMany(bounds=[0.,1.])

print "Number of training patterns: ", len(dataset)
print "Input and output dimensions: ", dataset.indim, dataset.outdim

fnn = buildNetwork( dataset.indim, 77, 77, dataset.outdim, hiddenclass=TanhLayer
                    , outclass=LinearLayer
    )


#trainer = BackpropTrainer( fnn, dataset=dataset, momentum=0.5, learningrate=0.005, verbose=True)
trainer = RPropMinusTrainer(fnn, dataset=dataset)

step = 0.05
ticks = arange(margins[0], margins[1] + step, step)
#ticks = arange(-1.05,1.05,0.05)
X, Y = meshgrid(ticks, ticks)
# need column vectors in dataset, not arrays
griddata = ClassificationDataSet(2,1, nb_classes=2)
for i in xrange(X.size):
    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
griddata._convertToOneOfMany()  # this is still needed to make the fnn feel comfy

for i in range(2000):
    trainer.trainEpochs( 10 )

    trnresult = percentError( trainer.testOnClassData(),
                              dataset['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult

    out = fnn.activateOnDataset(griddata)
    out = out.argmax(axis=1)  # the highest output activation gives the class
    out = out.reshape(X.shape)

    figure(1)
    ioff()  # interactive graphics off
    clf()   # clear the plot
    hold(True) # overplot on
    for c in [0,1]:
        here, _ = where(dataset['class']==c)
        plot(dataset['input'][here,0],dataset['input'][here,1],'o')
    if out.max()!=out.min():  # safety check against flat field
        contourf(X, Y, out)   # plot the contour
    ion()   # interactive graphics on
    draw()  # update the plot

ioff()
show()