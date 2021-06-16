# :checkered_flag: End assignments

In the next few weeks of the module you are going to work on the end assignments. There are two assignments that each work with an AI. The assignments are very similar, in both cases the drone Has to follow a set of <span style="color:orangered">orange</span> traffic cones to the finish. The difference is what the drone does when it detects the <span style="color:orangered">orange</span> traffic cones. 

## :golf: Follow the traffic cones


In the first end assignment the drone has to follow the traffic cones to the finish, while following the rules below:

1. A set of traffic cones will be placed at random. The cones will be colored <span style="color:orangered">orange</span>, this is important because the AI can only detect orange cones.
2. If the drone encounters an <span style="color:orangered">orange</span> traffic cone, it should move towards it.
3. If the drone encounters two <span style="color:orangered">orange</span> traffic cones, it should prioritize the left cone.
4. If the drone does not see any <span style="color:orangered">orange</span> cones, it should do a front flip and land.

This is an example of a course and how the drone should follow it:

<img src="/Media/EndEX1.png" width="800"/>

## :construction: Obstacle course 
In the second assignment the drone will have to traverse an obstacle course. This time however, it should detect the <span style="color:orangered">orange</span> traffic cones and follow a different set of rules when it detects them.

1. In the defined area, a set of traffic cones will be placed at random, the cones will be <span style="color:orangered">orange</span> so the AI can detect them
2. If the drone encounters an <span style="color:orangered">orange</span> traffic cone, it should avoid it and pass it on the left side.
3. If the drone encounters two <span style="color:orangered">orange</span> cones, it should move in between them
4. If the drone encounters three or more <span style="color:orangered">orange</span> cones, it should move in between the most left ones.
5. If the drone does not see any <span style="color:orangered">orange</span> cones, it should do a back flip and land.

This is an example of an obstacle course and how the drone should follow it:

<img src="/Media/EndEX2.png" width="800" />

