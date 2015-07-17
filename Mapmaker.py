import numpy as np
import healpy as hp
import math
import os
import matplotlib
import matplotlib.pyplot as plt
from Source.Specifications import Specifications
from Source.PrimaryBeams import PrimaryBeams
from Source.VisibilitySimulator import VisibilitySimulator
from Source import Geometry
from Source.PointSourceCatalog import PointSourceCatalog
import scipy.constants as const
plt.close("all")

freq = 150
#TODO: the frequency should be passed as a command line parameter

#Load in everything we need, figure out which LSTs to work with
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
s = Specifications(scriptDirectory, "/configuration.txt",freq)
Geometry.CutOutUnusedLSTs(s)
coords = Geometry.Coordinates(s)
PBs = PrimaryBeams(s)
ps = PointSourceCatalog(s,PBs)

#Simulate or load visibilities
if s.simulateVisibilitiesWithGSM or s.simulateVisibilitiesWithPointSources:
    visibilities = VisibilitySimulator(s,PBs,ps)
else:
    print "Visibility loading functions are not done."    
    #visibilties = mmh.LoadVisibilities(s)
visibilities *= s.convertJyToKFactor



#PSUEDO CODE:
#-assign LSTs to snapshots
#-Noise inverse variance weight
#-rephase visibilities
#-loop over snapshots:
#    -calculate Ninv
#    -Calculate Ninv*y
#    -Calculate KAtranspose
#    -add snapshot map
#    -add snapshot PSF
#Normalize the final output
#Save data products    



#plt.figure()
#plt.plot(np.real(visibilities))



#hp.mollview(pixelAzs, title="Pixel Azimuths at LST=0")
#hp.mollview(PBs.beamSquared("X","x",s.pointings[0]), title="PrimaryBeam")

plt.show()    

    
