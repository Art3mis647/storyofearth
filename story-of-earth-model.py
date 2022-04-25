'''
By: Tony Shu 09B2

Made for Y9 PBL Science

Story of Earth Model

pretty low quality code
'''

#dependencies

import time
import sys
import os
from datetime import datetime,  timedelta, date

#some functions


def datenumber(date):
    date = str(date)
    date.rjust(3+len(date), '0')
    year = "2022"
    res = datetime.strptime(year + "-" + date, "%Y-%j").strftime("%m-%d")
    return res

#defining clear function
def clear():
    os.system('clear')


#defining slowprint function
def slowprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.03)
  print()

#defining mediumprint function
def mediumprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.01)
  print()

#defining fastprint function
def fastprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.001)
  print()

  

def help():
    fastprint(" __    __   _______  __      .______   ")
    fastprint("|  |  |  | |   ____||  |     |   _  \  ")
    fastprint("|  |__|  | |  |__   |  |     |  |_)  | ")
    fastprint("|   __   | |   __|  |  |     |   ___/  ")
    fastprint("|  |  |  | |  |____ |  `----.|  |      ")
    fastprint("|__|  |__| |_______||_______|| _|      ")
    mediumprint("========================================")
    slowprint("The format of the commands is given as follows:\n")
    slowprint("'input': description\n")
    slowprint("In order to use the command, simply type in 'input', and press enter, and it will do what is listed in the description.\n")
    slowprint("If you have any further questions, just track me down in real life and I'll help you.\n")
    slowprint("This model is actually 2 different models, both of a Gregorian Year. One for the Pre-Cambrian, Paleozoic, and Mesozoic eras, in which a day is equal to 12602739 years, and one for the Cenozoic era, in which a day is 178082 years.\n")
    slowprint("To get out of this screen, press enter.")
    input('')
    clear()

def credits():
    slowprint("As I am not particularly talented at art, I decided to code my project instead. For that I thank the following people, without whom this project would not have been possible:")
    slowprint("========================================")
    slowprint("Tony Shu, for coding this. (thanks me!)")
    slowprint("Moses Lai, for giving his name to this time machine.")
    slowprint("Jason Lo, for me to bounce ideas off.")
    slowprint("The Internet, for teaching me how to code.")
    slowprint("The Beatles, whos music kept me sane while coding this.\n")
    slowprint("Additionally, all of the following people helped in some way or another.")
    slowprint("Juby, Celine, Maxwell, Theo, Urvi, Carissa, Otis, Ms. Nahar, Ms. Momeni, Mama G, PBL 9, the PBL 9 teachers, my dog, my parents, my extended family, Jesus Christ, that clerk at the 7-11, the Candy-Man, George Washington, Ibn Battuta, the country of Equatorial Guinea, and (ok i'm just making stuff up at this point)\n")
    slowprint("Press enter to leave this menu.")
    input('')
    clear()

def formation():
    slowprint("It's New Year's day today, or 4.6 Bya, coincidentally the day earth formed! It's cold on this day in our world, but when Earth formed the temperature was very hot with temperatures averaging around 80°C.\n")
    slowprint("The earth was at this time additionally very toxic for humans (radiation), and the atmosphere consisted of bits of water vapour and carbon dioxide, with the notable exception of oxygen.\n")
    slowprint("The earth was formed by gravity gradually pulling clumps of matter (dust and rocks) into a ball. Scientists believe there used to be around 100 planets in our solar system, but now there only exist 8, as all planets were formed this way.\n")
    slowprint("However, there are people who believe that the Earth was formed by God through creation over the course of 7 days, which was quite the debate a few decades ago (although I wasn't alive then so I don't really know).\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    exit()
    return
def thea():
    slowprint("On January 8th, or 4.5 Bya, and the moon formed today!\n")
    slowprint("A mars sized planet, dubbed Theia, crashed into the earth at a speed of 10 miles/second, splitting off the moon.\n")
    slowprint("The moon is currently 240k miles away from the earth, but at the time of the collision it was a mere 14k miles away.\n")
    slowprint("Another side effect of this was that the earth started spinning faster, and a day was just around 6 hours!\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    exit()
    return
def layers():
    slowprint("From January 8th to February 18th, or 4.5-4 Bya, the layers of the earth started forming.\n")
    slowprint("These layers are known as the Crust, Mantle, and Inner/Outer Core.\n")
    slowprint("These layers formed as the the building blocks of earth known as the planetesimals collided and collapsed under their own gravity.\n")
    slowprint("At the time, the heaviest elements (eg: Iron and Nickel) sunk to the core, whilst the lighter elements (eg: Silicon, Oxygen and Carbon) rose to form the mantel and crust.\n")
    slowprint("As the magnetic core coalesced together at this time, earth also started to have a magnetic field.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()

    return
def meteorites():
    slowprint("From February 24th to March 12th, or 3.9-3.7 Bya, meteorites strike the earth.\n")
    slowprint("These meteorites, coming from the leftovers of the Solar System when it formed, brought with them water, in the form of ice, as well as salt.")
    slowprint("Thus, every drop of water on earth is billions of years old, originating from these meteorites that struck!\n")
    slowprint("These meteorites also brought with them minerals (such as Carbon), chemicals (such as Amino Acids), and also destruction (duh).\n")
    slowprint("You may notice that around this time, the earth starts to look more like our earth, a trend that will continue.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def oceans():
    slowprint("On March 12th, or 3.8 Bya, oceans started to cover the earth.\n")
    slowprint("Additionally, as volcanoes erupt, molten rock bursts, and as it cools, it forms a volcanic island\n")
    slowprint("In the future, these islands will come together to form the first continents.\n")
    slowprint("Note that during this time, there were huge storms on earth due to its quick rotation, and the tides were huge due to the proximity of the moon.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def soup():
    slowprint("From March 12th to March 28th, or 3.7-3.5 Bya, something started happening deep in the oceans!\n")
    slowprint("Underwater chimneys in the ocean start spewing out hot liquid, and seawater seeps into the crust collecting minerals and chemicals along the way.\n")
    slowprint("Over time, this becomes a 'Chemical Soup', and something is forming in this soup.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def life():
    slowprint("On March 28th, or 3.5 Bya, the chemical soup in the ocean, formed life!\n")
    slowprint("It turns out that the chemicals in the ocean just happened to be the building blocks for life, and somehow single-cell bacterial life formed!\n")
    slowprint("The 4 theories for how this happened are as follows:\n")
    slowprint("1. Meteorites, bearing life crashed into tiny little ponds, bringing life to earth from outer space.\n")
    slowprint("2. Chemical reactions occured in deep seafloor vents, bringing life to earth deep beneath the oceans.\n")
    slowprint("3. Chemical reactions spurred by lightning alongside mixing by waves occured in intertidal zones, bringing life to earth on the beaches.\n")
    slowprint("4. Chemical reactions occured in areas with high levels of radiation and heat, bringing life to earth through radiation.\n")
    slowprint("2 people called Miller and Urey at the University of Chicago in 1952 did an experiment (called the 'Miller-Urey Experiment'(duh)) on this. If you want you can check it out!\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def oxygen():
    slowprint("From March 28th to July 1st (wow that's a long time!), or 3.5-2.3 Bya, oxygen starts to form!\n")
    slowprint("Stramatolites, or colonies mainly comprised of limestone formed by bacteria, start to form underwater.\n")
    slowprint("And as these stramatolites form, they start to add oxygen to the earth through photosynthesis.\n")
    slowprint("This also helps us understand why deforestation is so devastating. As photosynthesis is the process of converting carbon into oxygen, cutting down trees decreases our oxygen levels and adds to the carbon in the atmosphere.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def blue_sky():
    slowprint("From July 1st to September 2nd (also a long time), or 2.3-1.5 Bya, the sky gradually turns blue due to the influx of oxygen from stramatolites.\n")
    slowprint("This is due to a phenomena called Raleigh Scattering caused by oxygen particles. What happens is that as blue light travels in shorter wavelengths, it gets scattered around more than other light. You can google this up for more info.\n")
    slowprint("However, it will take billions of years for oxygen levels to reach what they are today.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def nothing():
    slowprint("From September 2nd to October 28th, or 1500-800 Mya, nothing major happens.\n")
    slowprint("Throughout this time period, the trends that we have been establishing continue. A day gets longer (now 18 hours), the moon gets farther away from the earth, the temperature drops (now 85 degrees), and the sky gets more and more blue.")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
def loadofstuff1():
    slowprint("From October 28th to November 18th, or 800-540 Mya, a ton of stuff happens!\n")
    slowprint("From October 28th to October 31st (free candy day), or 800-750 Mya, a force causes the crust of the earth to break up into plates (which still exist). This force is the core of the earth.\n")
    slowprint("On Halloween, or 750 Mya, these plates gradually drift together to form a supercontinent (one big continent), christened Rodinia, from the russian word родина, meaning birthplace.\n")
    slowprint("However, the very next day (November 1st), or 740 Mya, Rodinia splits into 2, like you and your middle school crush (ok that was probably mean sorry to whoever is reading this). If you're interested in this type of thing, there are loads of interesting YouTube videos showing the gradual shift of the continent over the years.\n")
    slowprint("From November 1st to November 2nd, or 740-720 Mya, Volcanoes pump huge amounts of CO2 into the Atmosphere causing temperatures to drop. This is due to CO2 causing Acid Rain (also a modern day issue) through a chemical reaction, which causes the rocks to absorb all the CO2. Now without CO2 to trap air in the atmosphere (through the Greenhouse Effect, also a modern day problem), the temperature drops to -60 Degrees. The chemical equation for acid rain is CO2 + H2O (Carbon + Water) = H2CO3 (Carbonic Acid).\n")
    slowprint("From November 2nd to November 4th, or 720-700 Mya, the Earth begins to freeze over due to the temperature loss. This begins a process called the Snowball Earth. What's bad about this, is that the increase of ice on earth is exponential, as the more ice that forms, the more sunlight is deflected from the sun, meaning that the earth gets colder forming more ice to restart this cyclical effect. The ice that covers the earth during this time is roughly 10,000 feet thick, leaving all life in earth deep below the ice, under the sea.\n")
    slowprint("From November 6th to November 10th, or 700-650 Mya, the ice recedes. This is due to the hot core underneath all that ice gradually melting it. Additionally, the carbon during this time was unable to be absorbed by the rocks, as the rocks were smothered with ice.\n")
    slowprint("From Nobember 10th to November 14th, or 650-600 Mya, the ozone layer starts to form. As Ozone is comprised of 3 oxygen atoms, ultraviolet radiation from the sun caused a chemical reaction creating ozone from the leftover oxygen not used during photosynthesis. Ozone is important as it helps filter out radiation from the sun. Gradually, this ozone starts to form a layer called the ozone layer. If you are old enough (which I'm not), you may remember the ozone gap, in which scientists discovered a gap in our ozone layer. This gap still exists over antarctica, albeit seasonally, closing up every summer do to stratospheric air from lower altitudes.\n")
    slowprint("On November 18th, or 540 Mya, the crustal plates come together to form a new supercontinent. This continent is christened Gondwana after the Gondwana region of central India.\n")
    slowprint("At this time, a day is 22 hours, and the temperature is equatable to that of a summer day.\n")
    slowprint("The formation of Gondwana marks the end of the Pre-Cambrian era. We will now be traveling through time to the Paleozoic Era.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
def loadofstuff2():
    slowprint("From November 18th to November 25th, or 540-444 Mya, life begins to evolve.\n")
    slowprint("From November 18th to November 19th, or 540-530 Mya, the amount of species explodes in an event known as the Cambrian Explosion, named after the Latin name for wales, Cambria. We know this happened due to the sudden burst in the amount of fossils found. Thus, it is possible that perhaps it wasn't the amount of species that exploded, but rather something happened to make the preservation of fossils much easier.\n")
    slowprint("On November 21st, or 500 Mya, we see the first land plants, in the forms of bryophytes, like moss.\n")
    slowprint("On November 22nd, or 480 Mya, we see the first insects, such as dragonflies.\n")
    slowprint("On November 24th, or 450 Mya, we see the first sharks, meaning that sharks are incredibly old!\n")
    slowprint("Also on November 24th, or 450 Mya, we see the first big extinction event, out of 5 total. We don't know what caused it, but 85% of all species went extinct.")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def loadofstuff3():
    slowprint("From November 26th to December 2nd, or 420-359 Mya, life continues to evolve.\n")
    slowprint("On November 26th, or 420 Mya, we see the first vascular plants (plants with tubes to transport water), such as ferns.\n")
    slowprint("On November 28th, or 380 Mya, we see the first forests starting to form, as vascular plants start to develop into more tree-like organisms.\n")
    slowprint("On November 29th, or 375 Mya, the first fish start to emerge on land, in particular one species, Tiktaalik (derived from an Inuktitut word meaning 'Large Freshwater Fish'), of which its has many features that indicate the moment fish starting turning into tetrapods, a group consisting of all current land vertebrates. Of course, it will take many more years until Tiktaalik evolves into species similar to humans.\n")
    slowprint("Additionally on November 29th, or 366 Mya, the first amphibians emerge.\n")
    slowprint("On December 2nd, or 360 Mya, the the first seed bearing plants start to emerge, a trait that almost all plants have today. The advantages of a seed over a spore is that a seed requires a lot less water to grow than a spore.\n ")
    slowprint("Additionally on December 2nd, or 359 Mya, the second mass extinction event occurs, wiping out 75% of all species.")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def loadofstuff4():
    slowprint("From December 5th to December 11th, or 315-252 Mya, life still continues to evolve.\n")
    slowprint("On December 5th, or 315 Mya, Hylonomous, the first reptile (there is debate over this) evolves. This is notable as it is the first time life forms evolved to lay amniotic (shelled) eggs, which has a plethora of benefits, most notably allowing for more mobility (as you're not weighed down by a baby).\n")
    slowprint("On December 6th, or 305 Mya, oxygen levels increase by 30%, or 50% more than present day levels. This allows for life forms to have huge respiratory systems, allowing for huge insects and huge life forms, most notably arthropods.\n")
    slowprint("On December 6th, or 300 Mya, giant reptiles, such as Therapsids evolved. Their absence would allow for a group of reptiles known as the dinosaurs to take control.\n")
    slowprint("On December 6th, or 299 Mya, supercontinent Pangaea (derived from greek word Pangaia) forms. This is probably the most famous, and most recent supercontinent.\n")
    slowprint("On December 10th, or 260 Mya, the first turtles develop.\n")
    slowprint("Additionally around this time, the plant material that rots begins a million year process of turning into coal, which we now use for fuel and electricity. Thus, the places where there are huge coal mines are the former swamps (as more plants rotting = more coal).")
    slowprint("On December 11th, or 252 Mya, a chain of volcanoes known as the Siberian Trap in what is now Siberia erupts, spewing lava in the air, erupting the landscape. This causes the third mass extinction event, wiping out 95% of all species. This is also known as the Permian Extinction. CO2 levels rose, it started to rain more, and the earth became hotter (40 degrees C). Vegetation died out, the oceans turned pink and bubbles of methane gas emerged from the ocean floor causing the temperature to go haywire. The earth was almost entirely covered by lava at this time.\n")
    slowprint("This marks the end of the Paleozoic Era. We will now be traveling through time to the Mesozoic Era.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('')
    clear()
    return
def loadofstuff5():
    slowprint("From December 12th to December 15th, or 230-201 Mya, a few changes that have major consequences occur.\n")
    slowprint("On December 12th, or 230 Mya, the first dinosaurs, both on land and underwater evolve. This faction of reptiles will go on to dominate the land and seas for a long period of time, and their mere existance has inspired loads of pop culture such as Jurassic Park.\n")
    slowprint("On December 14th, or 210 Mya, the first mammals evolve. This is notable as mammals (humans) now dominate the world in lieu of reptiles (dinosaurs). But how did these new upshot humans come to be? That is what we will see next.\n")
    slowprint("On December 15th, or 201 Mya, the fourth mass extinction event occurs, wiping out 50% of all species. However, new research shows that this lack of diversification was actually caused by a decrease in speciation, rather than an increase in extinction. Thus, the extinction moniker is slightly innacturate.\n")
    slowprint("To continue your journey through time, please press enter!")
    input('') 
    clear()   
    return
def loadofstuff6():
    slowprint("From December 16th to Christmas (December 25th), or 180-65 Mya, we enter the last stretch of this journey, and the Mesozoic Era.\n")
    slowprint("On December 16th, or 180 Mya, Pangaea breaks up. The continents will now gradually drift apart until they take the positions that we know them in today.\n")
    slowprint("On December 18th, or 150 Mya, the first birds (Archaeopteryx) emerge. However, it is safe to note that these birds are still similar to dinosaurs in many ways, and were by no means the first to achieve flight, that honor going to the insects.\n")
    slowprint("On December 19th, or 140 Mya, the Atlantic Ocean starts to open up, as the European and American plates drift apart.\n")
    slowprint("As the oceans open up, fish and plankton population skyrocket, and as they die they coat the ocean floor to be buried and to be turned into oil, another source of fuel and electricity. Thus, our 2 giggest sources of fuel and energy all came from millions of years ago.\n")
    slowprint("On December 20th, or 130 Mya, the first flowering plants start to form. The advantages of flowers is that they help to attract pollen.\n")
    slowprint("On December 21st, or 112 Mya, the first snakes form.")
    slowprint("On December 22nd, or 100 Mya, the first placental mammals (completing embryotic development within the placenta) form, such as us humans, whales and elephants. The advantage of being placental is that you give birth to a relatively mature and large fetus, as the placenta nourishes and protects the fetus.\n")
    slowprint("On Christmas day, of 65 Mya, the final mass extinction occurs. An asteroid from the Oort Cloud, later known as the Chicxulub (after a Yucatec Mayan word) lands in the Gulf of Mexico killing 76% of all species and all of the dinosaurs. Debris flew everywhere, earthquakes shook the earth, tsunamis battered the coast, dust and magma spread across the planet, and the temperature reached 500 degrees, and sunlight was blocked from reaching the earth.\n") 
    slowprint("Interestingly enough, this had such a large impact that we can see where it happened within the geologic record. Indeed, the dinosaurs who had come to dominate the earth for so long, were wiped out not by anyone from our planet, but an asteroid from far out in space.\n")
    slowprint("To embark on another journey through time, please press enter for the last time. It's been a wonderful experience traveling with you through time. Farewell!")
    input('')
    clear()
    return
def loadofstuff7():
    slowprint("On January 1st, or 65 Mya, mammals start to evolve to dominate the earth. The mighty reptiles, dinosaurs, are now gone, replaced by the mighty mammals, rhinos, lions, woolly mammoths, humans. This is a process that will continue until our present day.")
    slowprint("Throughout this time, there are frequent ice ages roughly every 10,000 years, as the earth shifts from an age of ice to an age of warmth. Interestingly enough, using past data, an ice age should have started 2000 years ago, or at around the birth of christ. However, for some reason it hasn't started yet, and instead we're warming up the planet.\n")
    slowprint("This trend continues until an event occured starting from April 11th to September 9th, or 47-20 Mya. The Indian plate smashes into Asia forming the Himalayan mountains. Half of all humans now rely on the watershed of this mountain range for survival, with it feeding the Yangtze, Mekong, Yellow, Ganges, Indus, Yamuna, Irrawady and Brahmaputra rivers.\n")
    slowprint("Earth right now's average temperature is the same as it is today, and a day lasts just under 24 hours. The environment is very similar to what it is right now.\n")
    slowprint("Next, we'll explore how we, humans got here.\n")
    slowprint("To continue your journey through time, please press enter!")
    return
def loadofstuff8():
    slowprint("Starting on November 27th, and ending at the end of the year, or 6 Mya-now, humans start to form and develop.\n")
    slowprint("On November 27th, or 6 Mya, we see the first hominids in Africa, the family of humans. However, it is safe to assume that these hominids look nothing like humans today, and probably have more in common with gorillas than they do with us.\n")
    slowprint("However, the biggest shift comes on December 11th, or 3.5 Mya, when the African Rift Valley stretching 4000 miles opens up in East Africa.\n")
    slowprint("Living in its rain shadow are a bunch of hominids, great apes, who, after having to live in a hotter and drier environment after the rift opened up, adapted in evolutionary ways.\n")
    slowprint("As these apes had to travel farther for food and carry it back, they decided to go bipedal, rather than quadrupedal, allowing for their arms to be kept free in order to carry food around. These are truly the early ancestors of humans.\n")
    slowprint("These apes gradually evolve to become humans, until many major things happen on the last day of the year, or starting at 7 Kya.")
    slowprint("As these apes evolve slowly into humans, a species of human in Africa known as Homo Sapiens, start to move into Arabia at around 70 Kya. These Homo Sapiens are what we are. They gradually grow to enhabit the earth, killing off all other species of humans and many predatory animals. They brave an Ice Age at around 40 Kya, and at around 6 Kya they develop civilization.\n")
    slowprint("From here on its a breeze, as they learn to make Bronze from Tin and Copper, learn to Write, create Religion, centralized States, and slowly but surely advance technology.")
    slowprint("Indeed, all of what we as humans have done has happened on the last hour of the last day of the last month of the year symbolizing the most recent era. Everyone, me, you, Confucius, Stalin, Buddha, Caesar, Washington, Jesus, have all but made up a tiny fraction of the story of earth. And as we look forward to future we must keep this in perspective. As the sun sets on New Year's Eve of our year, we start a new year, a new age, a new dawn for humanity. As we look onto our new year, the future, we must conclude the Story of Earth. It has been a joy having you along on this ride, and I hope you join us in our travels through time again!")
    slowprint("For the very last time, press enter to leave this journey!")
    input('')
    clear()
    exit()


def precambrian():
    clear()
    formation()
    thea()
    layers()
    meteorites()
    oceans()
    soup()
    life()
    oxygen()
    blue_sky()
    nothing()
    loadofstuff1()
    return
def paleozoic():
    loadofstuff2()
    loadofstuff3()
    loadofstuff4()
def mesozoic():
    loadofstuff5()
    loadofstuff6()
def cenozoic():
    loadofstuff7()
    loadofstuff8()
def early():
    clear()
    formation()
    thea()
    layers()
    meteorites()
    oceans()
    soup()
    life()
    oxygen()
    blue_sky()
    nothing()
    loadofstuff1()    
    loadofstuff2()
    loadofstuff3()
    loadofstuff4()
    loadofstuff5()
    loadofstuff6()
    return


def start():
    clear()
    #include eras you idiot
    yes = True
    while yes:
        mediumprint("If you would like a comprehensive journey:")
        mediumprint("'one': from formation to extinction")
        mediumprint("'two': from extinction to a new beginning")
        mediumprint("========================================")
        mediumprint("If you would journey through a single era:")
        mediumprint("'precambrian': pre-cambrian: from a ball of lava to life!")
        mediumprint("'paleozoic': paleozoic: from bacteria to dinosaurs!")
        mediumprint("'mesozoic': mesozoic: the rise and fall of dinosaurs!")
        mediumprint("'cenozoic': cenozoic: from extinction to civilization!")
        mediumprint("'exit': exit this menu")
        choice = input('')
        if choice == 'one'.lower():
            clear()
            early()
        elif choice == 'two'.lower():
            clear()
            cenozoic()
        elif choice == 'precambrian'.lower():
            clear()
            precambrian()
        elif choice == 'paleozoic'.lower():
            clear()
            paleozoic()
        elif choice == 'mesozoic'.lower():
            clear()
            mesozoic()
        elif choice == 'cenozoic'.lower():
            clear()
            cenozoic()
        elif choice == 'exit'.lower():
            clear()
            break
        else: 
            mediumprint('Invalid Input')
            time.sleep(2)
            clear()
            
    return
def era():
    clear()
    slowprint("Eras:")
    slowprint("========================================")
    slowprint("Pre-Cambrian: 4.6-.541 Bya")
    slowprint("Paleozoic: 541-252 Mya")
    slowprint("Mesozoic: 252-65 Mya")
    slowprint("Cenozoic: 65-0 Mya")
    slowprint("Periods:")
    slowprint("========================================")
    slowprint("Hadean: 4.6-4 Bya")
    slowprint("Archea: 4-2.5 Bya")
    slowprint("Proterozoic: 2.5-.541 Bya")
    slowprint("Cambrian: 541-485 Mya")
    slowprint("Ordovician: 485-444 Mya")
    slowprint("Silurian: 444-419 Mya")
    slowprint("Devonian: 419-359 Mya")
    slowprint("Carboniferous: 359-299 Mya")
    slowprint("Permian: 299-252 Mya")
    slowprint("Triassic: 252-201 Mya")
    slowprint("Jurassic: 201-145")
    slowprint("Cretacous: 145-65 Mya")
    slowprint("Tertitiary: 65-2.6 Mya")
    slowprint("Quarternary: 2.6-0 Mya.")
    clear()
    return
def menu():
    amisane = False
    while amisane == False:
        #there's probably a better way of doing this
        clear()
        mediumprint('For the ASCII to load properly, make sure your console is as wide as possible.')
        time.sleep(5)
        clear()
        fastprint(".___________. __    __   _______         _______.___________.  ______   .______     ____    ____      ______    _______     _______     ___      .______     .___________. __    __ ") 
        fastprint("|           ||  |  |  | |   ____|       /       |           | /  __  \  |   _  \    \   \  /   /     /  __  \  |   ____|   |   ____|   /   \     |   _  \    |           ||  |  |  | ")
        fastprint("`---|  |----`|  |__|  | |  |__         |   (----`---|  |----`|  |  |  | |  |_)  |    \   \/   /     |  |  |  | |  |__      |  |__     /  ^  \    |  |_)  |   `---|  |----`|  |__|  | ")
        fastprint("    |  |     |   __   | |   __|         \   \       |  |     |  |  |  | |      /      \_    _/      |  |  |  | |   __|     |   __|   /  /_\  \   |      /        |  |     |   __   | ")
        fastprint("    |  |     |  |  |  | |  |____    .----)   |      |  |     |  `--  |  |  |\  \----.   |  |        |  `--  | |  |         |  |____ /  _____  \  |  |\  \----.   |  |     |  |  |  | ")
        fastprint("    |__|     |__|  |__| |_______|   |_______/       |__|      \______/  | _| `._____|   |__|         \______/  |__|        |_______/__/     \__\ | _| `._____|   |__|     |__|  |__| ")

        mediumprint("Commands:")
        mediumprint("=========================================================")
        mediumprint("'start': start screen")
        mediumprint("'help': help manual")     
        mediumprint("'credits': credit screen")
        mediumprint("'reference': reference sheet (era/period times)")
        mediumprint("'exit': exit program")
        startinginput = input('')

        if startinginput == 'exit'.lower():
            clear()
            exit()
        elif startinginput == 'help'.lower():
            clear()
            help()
        elif startinginput == 'start'.lower():
            clear()
            start()
        elif startinginput == 'credits'.lower():
            clear()
            credits()
        elif startinginput == 'reference'.lower():
            era()
        else:
            slowprint('Invalid Command')
            time.sleep(3)
            clear()

def name():
    clear()
    gradesnihilism = True
    while gradesnihilism:
        slowprint("Hello Earthling, I am 'Angry Moses', a time machine from outer space. What is your name?")
        name = input('')
        clear()
        slowprint(f"Well, {name}, would you like to travel through time and see the Story of Earth?")
        selection = input('')
        clear()
        if selection == 'yes'.lower():
            slowprint("Great! Now lets start!")
            time.sleep(2)
            clear()
            menu()
        elif selection == 'no'.lower():
            slowprint("uhh...\n")
            time.sleep(2)
            slowprint("wasn't expecting that one\n")
            time.sleep(2)
            slowprint("why don't we try that out again, but you say yes this time?")
            time.sleep(2)
            clear()
        else:
            slowprint("Invalid Input")
            clear()

    return
name()
