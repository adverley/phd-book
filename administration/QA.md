SIMULATION
Why choose MSD above FEM?
    MSD: easy to implement, fast and stable with PBD.
    FAM: we experimented with FEM but found no fast enough linear solver in csharp. Linear FEM leads to large errors in case of high deformations. 

    In the end, it depends on the application. We were not intersted in small wrinkles but in performing high-level folds.
    physics randomization on high-performance cloth in simulation to learn handle various types of cloth. It is about suspension of disbelief. 

REWARD FUNCTIONS CH: 

How does your work compare to prior work. What is the novelty?

Application-wise: 
    1. first app to express progress cloth folding. 
    2. in-depth analysis 
    3. reward function from videos without labels

Architectural wise:
    prior work disadv:
        Kinesthetic teach-in: move the robot arm, hard with cloth
        Visually remove robot from scene: we cannot pause folding in between
        Requires human intervention
        Uses Euclidean distance in embedding space but not always useful

Q: how does step 3 work from your reward extraction?
Each query frame is aligned to each of the experts frames. 


