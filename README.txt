VFPGA V2.0


Usage:
To run, ensure you have installed python3 (https://www.python.org/downloads/). Install version 3.7.6 (scroll down after selecting OS).
Ensure you have made a constraints file (.ucf) as per lab03. It must have the same prefix (ie lab4.sch, lab4.ucf)
Ensure that in XILINX ISE you have Synthesized, Implemented and Generated the Programming File with NO errors or serious warnings. VFPGA will most likely freeze if you give it a non-functional schematic.
Additionally ensure that ALL inputs to your logic blocks are NOT floating i.e. they are all connected to something. If you are not using an input tie it to VCC or GND as appropriate.
Navigate to where you extracted the folder and double click VFPGA.py. A terminal will come up, and you will have to wait 10-20 seconds for it to load. When it has loaded you will see a replica FPGA board appear.
Click File->Open and navigate to your schematic, open it
Your design should now be loaded and you can click buttons and toggle switches as you need. If the FPGA appears frozen, double check your schematic and if it seems fine, email me the schematic, constraints file, and a snapshot of the terminal (it will contain an error message). It is likely you are using a gate I haven't implemented yet, and is a quick fix.
To load a new design, simply click File->Open again, and select the new schematic (the .ucf file is found automatically).
To exit, click File->Exit

Change log:
V1.1: Added nand3b3, nand4b4, nand5b5, nand2, nand3, nand4, nand5, nand6, nand7, or16, nor2, nor3, nor4, nor5
V1.2: Added nor6, nor7
V1.3: Added m4_1e, xor2
V1.4: Added and4, and5, and6
V1.5: Added and7, and8, and9
V1.6: Fixed xor2
V1.7: Added and3b1
V1.8: Added and3b2

V2.0: Added better error handling including bug fixes when cancelling opening a file, added a clock source of 125Hz, and added cd4ce, cb2ce, cb16ce, d2_4e, bcdtoseg