
This example written to show my codding abilities in python and does not represent all testing that should be done for specific component.
Current solution based on testing dataset that framework user can extend.
1) Data set located in resources folder
1) test_data.yaml file define the data set :
   * picture to run on image recognition framework
   * expected response from the system

1) Current solution has only two picture but it can be extended by adding new

There is only one test in that solution that goes over data set and check if returned results from service are equal to expected.
Solutions ignore order in witch it returned from service , but request that all values will be identical.
For sure, in real world we need to consider some different results each time, also in sytem that learn the world all the time
Real test should check if all expected objects will be found and coordinates of objects will be slightly different

I was requested to use matplotlib, so I solve printing recognition times to the graph

Project was written with TDD approach and all framework classes tested.
In my opinion it super in important to test automation first, to be sure that our framework don't miss defect or create false alarms


Structure:
1) Framework unit tests located in: */unittest*
2) System test */testing.py*

# Important notes
1) Some magic values should be extracted to the config files (didn't do it to make things simple)
1) Installation packages are: tensorflow==1.15.0 (The latest package does not not work with luminoth)
1) utilizing  dataset (checkpoint): e1c2565b51e9 |   Faster R-CNN w/COCO | 
