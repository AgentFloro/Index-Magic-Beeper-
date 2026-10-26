from pyscript import display, document
import math, random
from pyodide.ffi import to_js
def Index(e):
    input_name = document.getElementById('input1').value
    sound = document.getElementById("player")
    Among = document.getElementById("Super")
    SweetNumber = math.floor(random.random() * 17)
    
    Index_Prescript = ""
    if SweetNumber == 0:
        Index_Prescript = (f"[To: {input_name}]: Cheat in the Ict exam")
    elif SweetNumber == 1:
        Index_Prescript = (f"[To: {input_name}]: Go to the convinience store near 7-11 and go buy a pack of gun")
    elif SweetNumber == 2:
        Index_Prescript = (f"[To: {input_name}]: Larp as Roland")
    elif SweetNumber == 3:
        Index_Prescript = (f"[To: {input_name}]: Go to the park and do a backflip")
    elif SweetNumber == 4:
        Index_Prescript = (f"[To: {input_name}]: Go to Mcdonalds and Spill the drink of a kid under 7 years old.")
    elif SweetNumber == 5:
        Index_Prescript = (f"[To: {input_name}]: Drink Cheriffer")
    elif SweetNumber == 6:
        Index_Prescript = (f"[To: {input_name}]: Hack The IAD and put spinning seal radio in the wallpapaer and make sure its not mutable.")
    elif SweetNumber == 7:
        Index_Prescript = (f"[To: {input_name}]: Go to The Same Gym Prince and Neo go to. And start doing 20 jumping jacks. Drink Coffee, and Throw your ball straight at them.")
    elif SweetNumber == 8:
        Index_Prescript = (f"[To: {input_name}]: Break Ykat's latop ")
    elif SweetNumber == 9:
         Index_Prescript = (f"[To: {input_name}]: Bake 100 cookies and send them to the concept incinerator") 
    elif SweetNumber == 10:
         Index_Prescript = (f"[To: {input_name}]: Vouch Pio for the President of the Universe")
    elif SweetNumber == 11:
         Index_Prescript = (f"[To: {input_name}]: Go to Sir Velasco. Ask him about the secrets of the universe. If he says no, then go to the next person and ask them.")
    elif SweetNumber == 12:
         Index_Prescript = (f"[To: {input_name}]: Call your mom and tell her you love her")
    elif SweetNumber == 13:
         Index_Prescript = (f"[To: {input_name}]: Write a letter to your future self")
    elif SweetNumber == 14:
         Index_Prescript = (f"[To: {input_name}]: Convert into BVScode")
    elif SweetNumber == 15:
         Index_Prescript = (f"[To: {input_name}]: Hack Kurt's roblox account and change his password into ILoveSoftPillows")
    elif SweetNumber == 16:
        Index_Prescript = '<img src="https://media.tenor.com/KoY_nSwZIEAAAAAM/super-idol-super-idol-meme.gif" alt="Super Idol" />'
        Among.play()

    
    sound.play()
    document.getElementById('output1').innerHTML = (Index_Prescript)
