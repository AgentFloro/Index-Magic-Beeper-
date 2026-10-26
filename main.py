from pyscript import display, document
import math, random
from pyodide.ffi import to_js

sound = document.getElementById("player")

def Saikai(e):
    Saikai = document.getElementById("Saikai")
    Saikai.play()
    Index_Prescript = '<img src="https://i.pinimg.com/originals/73/56/6b/73566baa9541941de51b7875b73f5fea.gif" alt="Super Idol" style="width: 100%; height: auto;" />'
    sound.play()
    document.getElementById('output2').innerHTML = (Index_Prescript)
def Index(e):
    input_name = document.getElementById('input1').value
    
    Among = document.getElementById("Super")
    SweetNumber = math.floor(random.random() * 30)
    
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
    elif SweetNumber == 17:
        Index_Prescript = (f"[To: {input_name}]: Drink 3 tumblers of Water. And then Do the floss.")
    elif SweetNumber == 18:
        Index_Prescript = (f"[To: {input_name}]: Go to Mcdonalds. And Wait for a familiar person to arrive.")
    elif SweetNumber == 19:
        Index_Prescript = (f"[To: {input_name}]: Send a message to a loved one that you will have to go to dagestan. Make a memorable goodbye message and stay in OB's basement for a day.")
    elif SweetNumber == 20:
        Index_Prescript = (f"[To: {input_name}]: Swim in a pool. And jog. Sink deep into the water slowly. Then Drown. Once you see a rubber ducky, Float up for air.")
    elif SweetNumber == 21:
        Index_Prescript = (f"[To: {input_name}]: Do 2 push-ups")
    elif SweetNumber == 22:
        Index_Prescript = (f"[To: {input_name}]: Make 10 sand castles. Watch each one get swallowed by the waves. And write what you fetl when doing it.")
    elif SweetNumber == 23:
        Index_Prescript = (f"[To: {input_name}]: Walk through a wall. Find a person to relay the massive secret room to. And live in the secret room for the rest of your life.")
    elif SweetNumber == 24:
        Index_Prescript = (f"[To: {input_name}]: Take a walk in nature and appreciate the surroundings")
    elif SweetNumber == 25:
        Index_Prescript = (f"[To: {input_name}]: Play Animal Crossing.")
    elif SweetNumber == 26:
        Index_Prescript = (f"[To: {input_name}]: Ask Rocky Saludes for a hug and tell him you love him")
    elif SweetNumber == 27:
        Index_Prescript = (f"[To: {input_name}]: AI generate an apple")
    elif SweetNumber == 28:
        Index_Prescript = (f"[To: {input_name}]: Eat an apple.")
    elif SweetNumber == 29:
        Index_Prescript = (f"[To: {input_name}]: Set a goal for yourself and work towards it")

    
    sound.play()
    document.getElementById('output1').innerHTML = (Index_Prescript)
