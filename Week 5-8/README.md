# :checkered_flag: End assignments

In the next few weeks of the module you are going to work on the end assignments. There are two assignments that each work with an AI. The assignments are very similar, in both cases the drone Has to follow a set of colored traffic cones to the finish. The difference is what the drone does when it detects the colored traffic cones. 

## :golf: Follow the traffic cones

In the first end assignment the drone has to follow the traffic cones to the finish, while following the rules below:

1. A set of traffic cones will be placed at random. All but one of the cones will be <span style="color:orangered">orange</span>, and the other cone will be <span style="color:mediumpurple">purple</span>.
2. If the drone encounters an <span style="color:orangered">orange</span> traffic cone, it should move towards it.
3. If the drone encounters two <span style="color:orangered">orange</span> traffic cones, it should prioritize the left cone.
4. If the drone encounters a <span style="color:mediumpurple">purple</span> traffic cone, it should move towards it and land next to it.

This is an example of a course and how the drone should follow it:

<img src="/Media/EndEX1.png" width="300" float="right"/>

## :construction: Obstacle course 

In the second assignment the drone will have to traverse an obstacle course This time however, it should detect the different colored traffic cones and follow a different set of rules when it detects them.

1. In the defined area, a set of traffic cones will be placed at random, with different colors 
  The first type of cone will be <span style="color:orangered">orange</span>, the second type will be <span style="color:deepskyblue">blue</span>, the third type will be <span style="color:red">red</span> and there will be one will be <span style="color:mediumpurple">purple</span> cone.
2. If the drone encounters an <span style="color:orangered">orange</span> traffic cone, it should avoid it and pass it on the left side.
3. If the drone encounters a  <span style="color:red">red</span> or <span style="color:deepskyblue">blue </span>cone, it should avoid them and pass them on the right side.
4. If the drone encounters either an <span style="color:orangered">orange </span>and a <span style="color:red">red</span> or an <span style="color:orangered">orange</span> and a <span style="color:deepskyblue">blue</span> cone, it should prioritize the <span style="color:orangered">orange</span> one.
5. If the drone encounters a <span style="color:mediumpurple">purple</span> traffic cone, it should move towards it and land next to it.

This is an example of an obstacle course and how the drone should follow it:

<img src="/Media/EndEX2.png" width="300"/>

