# Feedback notes and processing

## Julia

### Points of critique
#### Critique 1:
Point: The claim that your smart textile approach can learn from scratch is too strong because your setup is too simple:
(1) dynamics of cloth without instrumentation are more complex (less stiff)
(2) you don't know whether it can cope with complexer shirts or tasks, requiring more complex trajectories

Answer: transfer to non-instrumented cloth is essential and a research topic on its own. More complex shirts and less influence on deformability is covered in followup work Proesmans. 
Everything in our setup was cheap DIY so this method should transfer to more expensive robots. 

#### Critique 2
Point: More structure in SOTA via tables. 

Answer: 

#### Critique 3
Point: Simulator is used in only 1 chapter. 

Answer: developing simulators is indeed very complex and expensive. We instead decided to exploit the strengths of our lab and went for the hardware route with instrumentation, dataset collection and RL.
We see it being useful in a next step where we redo our ch6 work on reward functions in simulation and then 

#### Critique 4
Point: 

Answer: 

### Requested rework
Add more structure and summaries (via tables) in SOTA chapter. 


### Questions
#### Chapter 3:

Q:
Developing	a cloth	simulator is a very	difficult task.	What	do	you	think	you	have learned in	this chapter	that was	useful	for	the	rest	of	the	thesis	or	for	working	on	cloth	manipulation	research?

A: 
Meta: As dataset requirements for DL methods remain high, simulators will remain important as a tool for experimentation and data collection.  

Context:
I did this part of my research in 2016 when the go-to robotics simulator was Gazebo which has no soft body support at all. There were some researchers also lookign at robotic cloth manipulation in simulatoin but also stranded on limited funcitonality of for example Bullet simulator (Matas2018). 

Answer: what have we learned or how use it?
- It gave us early insights that training on the real platform alleviates sim2real problems.
- If learning to fold cloth takes 1M rollouts on a simulated robot, then you will never learn it from scratch on the real platform. 
- Use high fideilty simulation or(and!) with domain randomization. High fidelty cloth simulation is difficult so try to use existing simulation build by teams specialized in this. Alternatively, make one of your own with specific features you need. It will be less realistic so adapt your method to it. This is what we did by running it on GPU so we can just train on many cloth instances (diffferent material props). (domain randomization)
- This is a testbed for our ch6 on learning reward functions.
-  

-------------------------
#### Chapter 4:

Q: ch4 instrumentation: does it affect the dynamics of cloth?
A: yes, it becomes a little bit stiffer (not quantified) so we have follow-up work that reduces this impact. 

Q: What are you suggestions concerning ch4: instrumentation?
A: Multiple points:

- Staging the environment to accelerate learning by having a stronger learning signal.
- Collecting multimodal inputs for
  - supervised learning dataset 
  - RL way like we did in ch4: reward function
- NOT all cloths should be made of this. Infeasible and not the point.
  
-------------------------

Q: Can	results	learned	from	an	instrumented	cloth	be	applied	to	general	cloth?

A: Generalizing towards arbitrary cloths requires addressing (1) effect on **stiffness** by adding electronics and (2) instrumented-to-real transfer.

Considering stiffness:
1. Effects on deformability: We have follow-up work that scales down the components
2. We have published followup work that makes it work for state estimation of shorts 
3. we instrument only crucial areas instead of the whole textile piece

Considering instrumented-to-real transfer:
1. Research topic on its own
2. Our reward functions embedding is uni-modal but we hypothesize we can learn invariance towards input modality.
3. use it as a supervised classifier to estimate the state of the cloth. Input = images, output = tactile sensing. for example.

-------------------------

Q: In	the	text,	it	seems	that	you	still	need	to	hand	label	the	states	of	the	cloth	according	to	the	contact	pattern	of	the	matrix.	Can	you	discuss	what	are	the	advantages	of	using	instrumented	cloth	if	data labeling	is	still	required	to	learn	to	recognize	the	state?

A: There is indeed hand-labelling involved but not at a level at which you seem to imply. We do not label each frame individually, instead we label **keyframes** and the in-between frames receive the same label as the prev keyframe. 

Alternatives are to use **unsupervised methods** to extract states. We have experimented with this in ch6 where we used agglomerative clustering to detect subtasks when folding shirts on the learned embedding. 
We also experimented (but not publisehd) with hidden markov models but found the transitions to hidden states to be hard to interpret.  

To answer the question directly: the benefit of hand-labeling is data quality if a protocol is followed.

-------------------------

Q:
How	many different states could	be	identified with	the	method.	Are	they contact sensors? that	is,	can	they identify contact with the	table	or	the	grippers? If	so,	can	you	discuss	how	this could be used?

Our smart textile is piezoresitive material: the resitivity will change when you exert pressure on it. 

Our textile can detect contact with the gripper and can detect multiple folds. 

Concerning contact detection with the table: it probably can. It is important to note that our sensor is not calibrated. Absolute values are not meaningful so we work with a delta compared to baseline, which is the cloth being in a neutral, taut position. Our baseline for our experiments was holding the cloth in the air with two grippers. So it would work, but we have not explicitely tested for this. 

How to use contact detection with table and grippers:
- Contact detection: tell robot cloth was grasped and where
- table: important to use table to fold. Example: lower bottom of a rectangular cloth. 

How many different states:
    we have experiemntal results up to 4 states but only required two for the experiment. 

-------------------------

Q: how does your state detection based on instrumentation react if a completely new manipulation is executed

A: our robot had limited wokring space because inexpensive DIY but easy to recollect new data and retrain system as we don't use expensive neural networks. 


-------------------------

**A main takeaway here is that vision-only is dangerous because the system would attend movement of the end-effectors and corners of the cloth. In addition, cloth state space is large and pixel space is large -> reduce with sensor instrumentation. + easy to retrain**

Having (visually) unseen cloth states can be problematic while with tactile sensors on the cloth, you don't need viewpoint invariance. 

-------------------------

#### Chapter 5:

Q: How	do	you	think	we	could collect	real	data	to	bridge	the	gap	between	the	semantic	state	(what	you	
identify	in	ch.	6) and	the	low	level	state	of	deformation	of	the	cloth?

A:

Supervised Dataset: keyframing between semantic states while collection instrumented cloth data. 

Unsupervised dataset: perform manipulation with instrumented cloth and run unsupervised methods on it to extract semantic states. 

Main problem with purely vision based is that you are also recording the actions and trajectories of the entity manipulating the cloth. This might lead to the system using that signal instead of looking at the cloth only. This is why instrumentation is interesting. 

-------------------------

Q: Is your dataset usable for action recognition or cloth state estimation?

A: both

Action recognition: we have hand trajectories

Cloth state estimation: we labelled the state of the cloth. However, an extra camera providing a zoom-in view on the cloth woudl have been useful in this scene. 

-------------------------

#### Chapter 6:

Q: Do	you	think	it	could	be	used	to	progress	monitor	of	a	robot	executing	the	task?	Have	you	tried	it?

A: 

We have shown that our embedding contains invariance towards the executor. So we believe it to work for robots.
We did not try it on a robot given the dfficulty of manipulating cloth with robots.

-------------------------


Q: Does	it	classify	every	state	independently	or	used	time	consistency?	If	no,	have	you	tried	to	identify scene	states	of	other	tasks	that	may	look	similar	but	are	not	in	your	dataset?	

A: 
The system does not need temporal information so it would be possible but:
1. Would need dataset of 3 viewpoints. The embedding itself doesn't need it, but the reward system uses it for voting mechanism for extra performance (we have the data anyway). 
2. I believe we only have viewpoint invariance towards these three viewpoints with some margin but not radical different viewpoints.

-------------------------

Q: What	do	you	think	is	missing	to	achieve	a	full	state	estimation	of	the	scene	from	what	you	achieved in	this	chapter?

A: 
1. Close-up camera on cloth
2. Instrumented cloth

-------------------------

#### Chapter 7:

-------------------------



<!-- --------------------------- -->
## Stijn

### Points of critique

### Requested rework

### Questions
Q: Digital twins are mentioned in section 3.1. According to https://www.cadmatic.com/en/resources/blog/digital-model-digital-shadow-or-digital-twin/. Digital twins require automated input data flow to the digital twin and automated data flow out of the digital twin. Is this the case in this research and can we justify the use of the term digital twin?

A: The robot and cloth simulator built in CH3 are not transferred to the real platform. However, we use Unity that has ROS integration so it can communicate with the real platform. The term digital twin is justified, as the input data flow to the digital twin is the physical robot state en the data output flow from digital twin is motor commands. This is possible. We did not yet use it in this manner however. But it was most certaintly a requirement for our research. 

-------------------------

Q: 
How is the tuning of the spring parameters in figure 3.5 done in practice? Are the spring constants identical over the whole cloth? What is the possible potential for a certain probability on these parameters?

A:
Trial and error to make the virtual cloth visually appear to be realistic. We did not do any system identification to make the cloth behave like for example a jeans textile material because other methods would be more suited for that.
The spring constants differ per spring type but are constant among the whole cloth. 

also: new mesh resolution -> have to compeltly retune because collective spring behavior changes completely.

The Mass spring system also has no physical reality. There is no method to translate the energy in those springs to physical properties of the cloth.

About probability -> put a distribution on spring parameters -> allows to sample for randomization or bayensian inference based on real data. 

-------------------------

• Is there a certain randomness in the cloth behaviour simulations to challenge the learning?
No, because it already took long training times.
Sources of randomness could be:
  - initial state
  - a range of stable spring constants to sample from
  - small perturbations
  - 

-------------------------

• It would be convenient to have an overview of all parameters that need user tuning and justify how this tuning is done for each of those parameters.

Concerning ch3 -> the most difficult part was tuning the cloth simulation parameters to find stable and cloth-looking behavior. WE summarized these in appendix A. 

Tuning process was manually and labor intensive.

-------------------------

• What are the candidates’ views on possible novel actuator designs for cloth handling? A typical 6DOF robotic arm is not necessarily the best configuration?

1) Arm:
context: dealing with uncertainty -> cobots -> active or passive compliant robots
dynamics can matter, precision. UR3 vs Baxter.

e2e RL: can deal with inherent imprecisions and limitations of robot
SL + trajectories: robust robot is more desired.

6 DOF robot is ok. 

2) Gripper 

Depends on task -> flattening  vs pickandplace
Depends on strategy -> air vs traditional 
Depends on env -> can we use extrinsin contact (e.g. a table)?

Towards anthropomorphism -> oppossable thumb for grasping
Beyond  anthropomorphism -> two thumbs for rotations

Simple designs: De taartschep cfr our own designs based on http://www.joace.org/uploadfile/2013/0514/20130514021735577.pdf.

Cfr paper Borras https://upcommons.upc.edu/bitstream/handle/2117/330928/2334-A-Grasping-Centered-Analysis-for-Cloth-Manipulation.pdf?sequence=1.

Also depends on folding strategy that is used. Using the table to fold can be done with parallel gripper. Air folding could use a third finger that pushes sleeves inwards. If going towards folding style that is popularized in media as Japanese style folding, then two possable fingers are enough but the arm needs to be able to sufficient dynamic behavior to fold the shirt. 
 y component.

Because the nature of cloth introduces 

-------------------------

<!-- --------------------------- -->
## Naveen

### Points of critique

### Requested rework

### Questions

<!-- --------------------------- -->
## Tony

### Points of critique

ch2 SOTA is too long.
  It is 22% of the thesis and contains background information and literature study for all subsequent chapters. 

ch2 is not novel
  It takes a different approach compared to other cloth manipulation literature study. We take a historic perspective from engineered pipelines to e2e RL and maintain a cloth-based focus.

ch3
  why use unity?
    ROS integration, high-fidelity cloth, robotics physics simulation (featherstone algorithm), ease of access

  why dont use unity cloth?
    unstable, not all features: cannot query and modify individual vertices

  Why 42 DOF for Baxter?
    6 directions
    7 joints 

  What is 114 state space dimension?
    14 joint states
    10x10 cloth relative positions 

  show me a video 

ch 4
  Is this sensor signal from the smart cloth really useful or necessary?
    Letting gravity do the hard work is very common in cloth folding. 
    The sensor signal is encoded to a cloth state which is used as reward function.

  Harder tasks for smart cloth:
    reduce footprint of sensing path by changing copper wires and tape by conductive thread + embed on wellchosen locations
    contact detection
    train for multiple state detection (fold 1, fold 2 etc) -> embed in dataset of ch5
    transfer towards non-instrumented cloth via modality invariant embedding idea 

ch5
  how do you see your dataset being used in the future?

    learning actions from demonstrations
    learning reward functions from demonstrations
    supervised learning on the annotations
      Folding quality
      Folding method  (action recognition)
      Folding substep -> semantic understanding of cloth state
    representation learning like we did in reward function chapter

ch6
  potential beyond cloth folding 
    we claim that understands task intent, to some extent. 
    prepare videos and discuss that 

High-level
  What is the contribution of a data-driven pipeline? Do we go e2e or settle for smaller , dedicatd modules?
    Sample efficiency through
      decouple e2e learning
        learning submodules 
        Embed priors, do not learn every submodule
      Curriculum learning
      LfD

    we advocate there is a spectrum to be leveraged between programming and data.
      This residual part appears in every part of the pipeline:
          Modeling physics - we have white box modelled but lets leave the unmodelled effects to ML

  What does solving robot-cloth manipulation mean for robotics and AI at large?
    Cloth manipulation as a testbed for general-purpose robotics. From software to hardware. 
    
  What is your dream dataset?
    multi modalities: vision, tactile sensing
    contains actions indicating cloth semantic state and underlying low-level cloth sensing states
    high quality, high volume 
    contains simulated counterpart that is calibrated. Use for simulation exps.
    Multiple clothing types and textile types.


### Requested rework

### Questions

<!-- --------------------------- -->
## Pieter Simoens

### Points of critique

### Requested rework

### Questions

ch6 tcn:
  Q:  Does you reasoning about Euclidean distance not working for embeddings still hold for larger dimensions?
  A:  Yes, start and end can be semantically for most dimensions similar. E.g. baseball bat hitting. 

