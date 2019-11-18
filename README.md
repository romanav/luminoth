# Intoduction

This example written to show my codding abilities in python and does not represent all testing that should be done for specific component.
Current solution based on testing dataset that framework user can extend.
1) Data set located in resources folder
1) test_data.yaml file define the data set (as list):
   * picture to run on image recognition framework
   * expected response from the system
1) Current solution has only two picture but to check sistem we must add big set of different situation

There is only one test in that solution that goes over data set and check if returned results from service are equal to expected. We check that all object returned with correct name and coordinates.

Solution ignore order in witch it returned from service , but all values will be identical in the responce list to expected set. For sure, in real world, we need to consider that in the sytem that learn the world all the time recognition will provide slightly different results each time, in that reason trivial check can be not stable here.


I was requested to use matplotlib, so I solve printing recognition times to the graph

Project was written with TDD approach and all framework classes tested.
In my opinion it super important to test automation first (specialy if we write in python). We must be sure that our framework don't miss defect or create false alarms


Structure:
1) Framework unit tests located in: */unittest*
1) System test */testing.py*
1) Framework classes in files 

# Important notes
1) Some magic values should be extracted to the config files (didn't do it to make things simple)
1) Installation packages are: tensorflow==1.15.0 (The latest package does not not work with luminoth)
1) utilizing  dataset (checkpoint): e1c2565b51e9 |   Faster R-CNN w/COCO | 
