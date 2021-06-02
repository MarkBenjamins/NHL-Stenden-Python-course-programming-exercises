# :checkered_flag: End assignments

In the next few weeks of the module you are going to work on the end assignments. There are two assignments that each work with an AI. The assignments are very similar, in both cases the drone traverses a 5 by 5 area with colored traffic cones. The difference is what the drone does when it detects the colored traffic cones. 

## :golf: Follow the traffic cones

In the first end assignment the drone has to traverse in an area that is 5 meters wide and 5 meter longs. In this area the drone should detect the different colored traffic cone's and follow a set of rules when it does detect them.

- The drone is not allowed to exit the area, your code should prevent it from leaving.
- In the defined area, a set of four traffic cones will be placed at random. Three of the cones will be <span style="color:orangered">orange</span>, and the other cone will be <span style="color:mediumpurple">purple</span>.
- If the drone encounters a <span style="color:orangered">orange</span> traffic cone, it should move towards it.
- If the drone encounters two <span style="color:orangered">orange</span> traffic cones, it should prioritize the left cone.
- If the drone encounters a <span style="color:mediumpurple">purple</span> traffic cone, it should move towards it, and land next to it.

## :construction: Obstacle course 

In the second assignment the drone will have to travers in an area that is 5 meters long and 5 meters wide again. This time, it should detect the different colored traffic cone's and follow a different set of rules when it detects them.

- The drone is not allowed to exit the area, your code should prevent it from leaving.
- In the defined area, a set of four traffic cones will be placed at random. 
  One cone will be <span style="color:orangered">orange</span>, one will be <span style="color:mediumpurple">purple</span>, one will be <span style="color:deepskyblue">blue</span> and the last cone will be <span style="color:red">red</span>.
- If the drone encounters a <span style="color:orangered">orange</span> traffic cone, it should avoid it and pass it on the left side.
- If the drone encounters a  <span style="color:red">red</span> or <span style="color:deepskyblue">blue </span>cone, it should avoid them and pass them on the right side.
- If the drone encounters both a <span style="color:orangered">orange </span>and a <span style="color:red">red</span> or <span style="color:deepskyblue">blue</span> cone, it should prioritize the <span style="color:orangered">orange</span> one.
- If the drone encounters a <span style="color:mediumpurple">purple</span> traffic cone, it should move towards it, and land next to it.

