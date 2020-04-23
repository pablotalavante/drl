## **Project details:**
    
This project trains an agent in a Unity environment to move a robotic arm to reach a green ball that is circling around it. There are 4 possible continuous acitions that apply a torque to the joints to control the final position of the hand along time:
    
A reward of +0.1 is given if the hand of the robot is close to the objective.

The whole state is complex, but the state we observe is made of 33 different signals that the agent takes as inputs. With that inputs the agent must learn a policy to act to maximize reward.

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
