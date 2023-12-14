# Habit-at
# Project Overview: 
This project’s goal is to help users build and upkeep the healthy habits they want to achieve. The target audience is students who have a hard time focusing on tasks and keeping up with positive habits due to overwhelming coursework and/or poor mental health. However, the user’s goals are customizable to fit their specific needs making the user base expandable. It is good to have a reminder to maintain healthy habits and stay productive while using a device frequently. As users achieve their habit goals consistently, they will receive rewards and encouragement from their pets in the app environment. This application can offer a fun, engaging, and supportive environment for users wanting to build and maintain positive habits. It leverages psychological principles such as companionship, gamification, and positive reinforcement to make behavior change more enjoyable and sustainable.

# Installation and Setup Instructions: 
Download the entire Habit-at program file from Github, including the images.
From here you can simply run the application from within the Pycharm environment.
You will be asked to input your desired pet name and tasks to complete.

# Usage Guide: 
Once you hit play, you will be asked to input a name for your pet and a list of tasks you want to complete.
You will be brought to a second page where you can check off the tasks you have successfully completed.
With each completion, you will gain 1 coin and some happiness.
You can spend these coins with the interactive buttons at the bottom of the page that allow you to give your pet a treat, give them fresh water, or play with them. Each of these activities will also increase the overall happiness.
Happiness naturally decreases at a rate of -1 every minute.

# Testing Procedures: 
To test this application, you would just go through the sequence of inputting and completing tasks as assumed. You will notice there are error cases put in place. For example, if you try to play with the pet when you have 0 coins, you will get an error message. Happiness also has a cap and a lower bound, it cannot go above 100 or below 0. The pet images change to match happiness status below happiness 30 or above happiness 70. To test the images easily you can manually input the intial happiness level in the Virual Pet class. Naturally, this would occur from >20 minutes passing with no task completion as a result of the gradual decrease set in place or from completing enough tasks that would increase happiness enough. 

# Contributions and Acknowledgments:
I got inspiration from a few other projects I found while researching my topic: https://devpost.com/software/docktor-kitty, https://gamedevacademy.org/pygame-virtual-pet-tutorial/, https://thecleverprogrammer.com/2021/01/24/screen-pet-with-python/
