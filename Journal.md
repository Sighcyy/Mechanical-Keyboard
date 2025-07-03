# June 20th, 2025
Time = ~4 hours

Today, I took the first step to advance to the next level in my keyboard journey. I started with a MacPad, but I did not use a matrix since I only had a few keys. Thus, my next project was going to be a Mechanical Keyboard.

Today, I conducted research and completed some overall planning for my project. With the matrix design, I had to take into account "ghosting", which I could easily avoid with some diodes. 

I did a couple of whiteboard drawings just to understand how many columns and rows I would need. Then I created my schematic based on my whiteboard drawing reference. 

<img width="709" alt="D1_Schematics" src="https://github.com/user-attachments/assets/753b6ddc-71cd-40f3-bc8c-fdfaba43a062" />

I then went into what each key would represent so that I could get a better understanding of what the keyboard key layout would be like.

By doing this, I was able to remove some extra columns so that my keyboard would be much more portable.

![Screenshot 2025-06-20 154312](https://github.com/user-attachments/assets/4d5bfdb6-1e10-486a-80fa-9d4704626020)


Afterwards, I spent the rest of my time choosing the right footprints and placing all my parts properly on the PCB


![Screenshot 2025-06-20 192159](https://github.com/user-attachments/assets/2b8595ca-d0da-415c-9701-bff9e6d7eb78)


# June 21th, 2025
Time = ~4 hours

Today, I focused on figuring out how to properly route all the key inputs on my PCB, which turned out to be more challenging than expected due to limited space and overlapping traces. I spent a lot of time experimenting with using the bottom copper layer and strategically placing vias to reduce congestion and avoid trace conflicts. This approach significantly streamlined the routing process and helped me finish the layout more efficiently. Along the way, I also picked up several helpful workflow shortcuts in KiCad, like quick via placement, net highlighting, and optimized trace routing, which should speed up my future designs and make the overall process smoother.

![Screenshot 2025-06-24 005438](https://github.com/user-attachments/assets/3ded05ee-60ca-4a6b-9f2e-0eeefa13afa1)


# June 22nd, 2025
Time = ~4 hours

Today was a productive day on the 3D modeling front, as I completed the main structure of the CAD model by designing both the top and bottom plates, following a similar approach to my earlier Macropad build. I used a keyboard layout editor to customize the key arrangement, then exported it as a DXF file to precisely cut switch holes into the top plate. While the design is still pretty minimal in terms of aesthetics, I decided to hold off on cosmetic features until later in the process. Instead, I shifted gears and began researching the firmware side—specifically how keymaps, layers, and matrix scanning are handled in microcontroller code—so I can better integrate the hardware and software components once the physical build is done.

![Screenshot 2025-06-24 132848](https://github.com/user-attachments/assets/530ba73e-e083-4c96-be5e-964affe50b20)
![Screenshot 2025-06-24 132908](https://github.com/user-attachments/assets/feaa8121-55bc-4ec2-b769-3ab3c2f4ea51)


# June 23rd, 2025
Time = ~4 hours

Today, I wrapped up writing the firmware for my keyboard using Python with the KMK framework. Thanks to the research I did yesterday on implementing diode-based matrix scanning and integrating a rotary encoder, the coding process went smoothly and efficiently. My prior experience with key assignments from my Macropad project also helped me set up the keymap and layers quickly. With the core functionality complete, I decided to spend some extra time refining the keyboard case design by adding custom inscriptions and decorative linings to give it a more polished and personalized look—details I believe will help the final product stand out both functionally and visually.
![Screenshot 2025-06-25 140403](https://github.com/user-attachments/assets/7a3564c9-32cb-4950-8cda-f16ca27bc3fd)

![Screenshot 2025-06-25 141201](https://github.com/user-attachments/assets/6ef3f3dc-db00-47ed-b0a4-fb0b11b23701)


# June 24th, 2025
Time = ~4 hours

Since today was planned to be my final work session, I focused on wrapping up all remaining tasks to prepare for the build phase. I started by creating a complete Bill of Materials (BOM), which took some time due to the various key sizes and layout adjustments I had made—several non-standard key sizes required finding the right switch kit that could accommodate everything. I also researched PCB-mount stabilizers to match the layout and ensure proper key feel. In addition, I finalized my component list by selecting a compatible PCB, PLA filament for 3D printing the case, and a set of small screws and nuts to secure the top and bottom plates together. Most of the sourcing was done through Amazon, after comparing product specs and reviews to ensure everything matched my design needs. To finish off the day, I carefully reviewed the CAD model, double-checking all key dimensions and mounting points to catch any potential issues before manufacturing.


# July 7th, 2025
Big things, I wanted to do some quick changes. The keyboard itself was a little bland. Thus, I thought I would spend time today adding a little more uniqueness to it. I gave the edges of the keyboard a column-like aesthetic. The bottom had 3 large X's. Finally, for the actual top, I added the word 'PRIDE' in text. I thought it looked nice. 
![Screenshot 2025-07-02 205211](https://github.com/user-attachments/assets/04515da5-88ea-45cf-898d-39b2029edb16)
![Screenshot 2025-07-02 205138](https://github.com/user-attachments/assets/2ba43a6d-dfc0-4362-aa68-58e8a01c0d13)
![Screenshot 2025-07-02 205131](https://github.com/user-attachments/assets/18d006f4-b8a0-483c-ba5f-4641c171dce6)


Also, I wanted to make sure that if I painted it, I knew how it would loo,k so I added that into the design as well and finished up my design

![Screenshot 2025-07-02 211341](https://github.com/user-attachments/assets/f76c3267-a021-42f1-b533-2285cbc6a14d)
![Screenshot 2025-07-02 211335](https://github.com/user-attachments/assets/c581495d-d0af-4ac0-9795-173254fdd514)
![Screenshot 2025-07-02 211326](https://github.com/user-attachments/assets/bc0e10da-ba95-4553-8ee9-3ff53c478f34)


