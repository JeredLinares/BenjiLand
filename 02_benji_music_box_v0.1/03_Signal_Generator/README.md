# Signal Generator
Generate data to test that speaker works.
- Components to Test: 
  - Data
  - Code
  - Circuit

## Author 
JD Linares   
2025 01 23   

## Data
Creates a .raw file to emulate what the music will look like.  
Contains a middle C tone wave form sampled at 44.1kHz with 16bit unsigned integers  
Period of middle C is 0.00383 seconds  
Sampled at a rate of 44.1 kHz, you need 169 samples before you can loop  

Middle C: 261 cycles/sec  
16 bit unsigned integer   
- max: 65,535 
- min: 0

## Generator Equation
__V = 65535 * sin((2 * pi/0.00383) * t)__  
For 169 data points in increments of 1/44100 seconds





