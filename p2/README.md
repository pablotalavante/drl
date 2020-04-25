## **Project details:**
    
This project trains an agent in a Unity environment to move a robotic arm to reach a green ball that is circling around it. There are **4 possible continuous acitions** that apply a torque to the joints to control the final position of the hand along time:
    
A reward of +0.1 is given if the hand of the robot is close to the objective.

The whole state is complex, but the state we observe is made of **33 different signals** that the agent takes as inputs. With that inputs the agent must learn a policy to act to maximize reward.

There are 2 versions of the environment. The version 1 consist on just one agent. The version 2 consists on 20 pararell agents, but the problem is the same. A environment is considered solved when:

 - [version 1] the agent receives an average reward (over 100 episodes) of at least +30, or
 - [version 2] the agent is able to receive an average reward (over 100 episodes, and over all 20 agents) of at least +30.
 
The problem chosen here was the **version 1**.

## **Getting started:**

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux : [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
	- MAC OSX : [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
	- Windows : [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)


2. Place the file in this folder

3. Install the requirements with:
```
pip install requirements.txt
``` 


## **Instructions**:

The notebook training_.ipynb constains the script to train the agent. 

Once the agent is trained, the notebook acting_.ipynb takes the trained agent and uses it to see a working agent, with a policy without noise.

The report is on Report.ipynb
