# Mechanical Keyboard

I designed a 60% Mechanical Keyboard featuring 60+ push-button switches, a rotary encoder, and keystabilizers for larger keycaps. It features an EC11 rotary encoder,  the Raspberry Pi Pico microcontroller, which was chosen for its small form factor and support for KMK firmware. The parts are populated on a custom PCB for tidy arrangement and good performance. The case is fully 3D printable, making the design easy to reproduce and customize. This keyboard provides a programmable  interface to enhance game control and portability rather than a larger keyboard. 



# Project Goal
This is my second official project, and the reason I wanted to implement this is that I wanted to work more in-depth with complex PCBs. Thus, I decided that a keyboard with a key matrix would be best, and routing all the switches would require using a lot more of the front-end and back-end copper layers, as well as vias. The purpose as a whole was not to try to follow any guides too much and just research a lot more in order to understand things. I felt like this would build a stronger sense of passion and understanding for the subject rather than blindly following a DIY guide. 




# BOM : 
*Shipping is included in the cost

*You may notice that I use Amazon a lot. I have Amazon Prime, and when comparing that to buying from somewhere with high shipping costs and potentially lower quality, I chose Amazon Prime.
| Name  | Vendor | Cost | Link |
| ------------- | ------------- | ------------- | ------------- |
| 1N4148WT Diodes x 100  | DigiKey  | ~$14.56  | [Link](https://www.digikey.com/en/products/detail/onsemi/1N4148WT/2094398?gad_source=1&gad_campaignid=20228387720&gbraid=0AAAAADrbLljx--os3Oc-ERVDq4RA6mW2A&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJaR7fGtX2-klAVP3bMztAKNuhO9PWpQEzcAYNcuLx_19G9B_UClEchoC3voQAvD_BwE&gclsrc=aw.ds) |
| Keycaps ( Purple and Black)  | Amazon  | $14.59 |[Link](https://www.amazon.com/gp/product/B0C1BLFFKJ/ref=ewc_pr_img_1?smid=A2X78RSRFYCZMR&th=1)|
| PLA 1.75mm 3D Printer Filament  | Amazon  | $9.99  | [Link](https://www.amazon.com/Filament-Dimensional-Accuracy-Clogging-Cardboard/dp/B0DCJR8JTG/ref=sr_1_7?dib=eyJ2IjoiMSJ9.SPz8Xg0t9pBHW5vzHC0hcrOoBcMg9tsOwIfYVbRVdq2ehkdGSJNIpnLfy-G6GQ386npSm8NKU2eVOB5lDs9fM5SP3BwNw4DneEFMYhiqj9ARZiM8VilUR0xDQeslmXf7QOampqty_90bjSue5upWMHlNu01QlYdR9fPvTke6ssTXEpueHXChgBcv-6XMi5C7ikbnbpweuy44VwVD9MQ54rEdYbO8RnUJGZE0x8X4jw87FPFn10WNIHPx8eS0kNnTs_qJJx6g4uEozHVpQCTFo04w7rRJaRNAy-MbtuTK-ns.JQQ1MoJ_n79QH0eVFcw0CVfC-Xj4-dKdjL8ozW3CjK8&dib_tag=se&keywords=pla%2Bfilament%2B1.75mm%2Bblack&qid=1750881112&s=industrial&sr=1-7&th=1) |
| Rotary Encoder + Cap  | Amazon  | $8.88  | [Link](https://www.adafruit.com/product/5454?srsltid=AfmBOorYPqeBmuc5MZ6s_MCTYFLaZhHhOz2tPLmYjFdNPAYrPFRNpYgzi4o&gQT=2) |
| Gateron PCB Mounted Stabilizer  | Gateron  | $10.99  |[Link](https://www.gateron.com/products/gateron-pcb-mounted-stabilizer?VariantsId=10538&gad_source=1&gad_campaignid=22307967329&gbraid=0AAAAA97B41r4u1jlMcNYsYIA4WSFWE40U&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJYqdNxVkPkeaBVAqQ8hNKb8qgmINa21uSZfjtv5JoNzrLA4rcxZpuhoCk9QQAvD_BwE) |
| Cherry MX Key Switches x 65 | Amazon  | $39.99  |[Link](https://www.amazon.com/Switches-Mechanical-Keyboards-Mounted-MX1AE1NN/dp/B09ZST8WMF?th=1) |
| Rasberry Pi Pico  | Amazon  | $8.99 | [Link](https://www.amazon.com/Raspberry-Pi-Pico/dp/B09KVB8LVR?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3FPRP7I8FTOOJ&gQT=2) |
| M2.5 Screws   | Amazon  | $3.78 | [Link](https://www.amazon.com/Stainless-Electrical-Attaching-Connectors-Furniture/dp/B0F1TX35J1/ref=sr_1_3?dib=eyJ2IjoiMSJ9.JTABbbPI4c84bvAyFdR4QAuyl-zvLu0fcJk5cXvI7CgP3PrnFfs1Y5-tGvIDeWtB2-1FXimYR_6tWbYc7l1Yl75981KrnOtSW7BK_mkXe-KHN3JKPEqmflJlMbz0sP5a1YoZXgVWCERNChIxjkHuQOriRZKJPfTJImp-mY7FlTiTPr8vP3QAtC0O0UXKuSoqTSKWbbI68CFg5M05HuokIzPbcaEjR5B-uYtZjY1wSyU9kXgomI_tM-oYrlB5bJTbmkOtBr_AUfUpnt7zL0WXS9AVvfKmu5PKEjocyukiYc8.IYtoqxmfqz2vQdNwSSBZ0ralFLwOOfUYzNbiWcVSgDY&dib_tag=se&keywords=M2.5+Screws+and+Nuts&qid=1751160641&s=industrial&sr=1-3) |
| PCB   | JLPCB  | $28.94 | [Link](https://cart.jlcpcb.com/quote?spm=Jlcpcb.Homepage.1006&spm=Jlcpcb.Homepage.1006) |


Approximate Total Cost:  $140.71

Rounded Total Cost (To Take Tax Into Account): $145




# PCB and Schematics Design

![Screenshot 2025-06-20 154312](https://github.com/user-attachments/assets/f9341538-364d-473b-a71c-cffc13529c5b)
![Screenshot 2025-06-24 005438](https://github.com/user-attachments/assets/a2023eba-bac7-4035-835a-229de0a0691b)

# CAD Model

Top Plate

![Screenshot 2025-06-24 132848](https://github.com/user-attachments/assets/dc55301d-fbc1-400d-b455-939b98517084)


Bottom Plate

![Screenshot 2025-06-25 140403](https://github.com/user-attachments/assets/b15d69f8-a5aa-4d34-b139-4c2dee2451e4)



# Firmware Overview

![Screenshot 2025-06-25 141201](https://github.com/user-attachments/assets/f9ca5d95-2545-4322-960d-a2e0a100da36)





