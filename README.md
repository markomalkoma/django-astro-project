### ASTRO PROJECT

### Python/Django/HTML/CSS/JS

### https://astroaspects.herokuapp.com/

#### Astro-project is aimed at discovering probabilities of astrological aspect's rates of certain people categories that can be hardly explained by pure chance.

### About

 A few years ago, I decided to go through famous lectures on physics by Richard Feynman. 
 Probably no one ever did a better job with an effort to explain this complicated subject from the start. 
 The scientific content is associated with intellect, but what came to my mind while going through demanding calculations, 
 was that this was not just a common sense but a specific type of intelligence. 
 The scientific mind is not just about getting general mechanism, but one that is colored by skepticism, 
 concentrated on details, and often requires enduring work for results to come. To know does something work, generality and hints are not enough. 
 A theory should be completely approved by mathematics and evidence. I realized that this approach would be painful for many people that rely much on their minds. 
 Grasping “Big picture” and hints, are most often enough in real-life decision making and in generating approaches toward challenging situations, 
 but not enough for scientific methodology.

 During my studies of physical chemistry, I was going through a period of self-evaluation, comparison with others, and who I thought I was and where I should be. 
 I started being interested in Astrology. Of course, Astrology is appealing, and most often reading it makes one feels good about oneself, 
 but I always wondered is something there? What came to my mind doing these calculations was that those two types of intelligence described above have their markers in astrology. 
 They are both mapped by certain astrological aspects. It is considered that two planets are in aspect when they are placed in certain directions 
 concerning Earth (with small deviations). A skeptical mind is related to the Mercury-Saturn aspect, and general intelligence by the Mercury-Jupiter aspect. 
 Jupiter symbolizes luck, intuition, and something that comes on its own, without effort. Saturn symbolizes austerity, skepticism, fear, doubt, lack of intuition, and effort. 
 An equal share of both aspects in natal charts of greatest physicists, chemists, and mathematicians would simply mean that story that was connecting myself and astrology ended. 
 As much as the first aspect would help someone to do scientific work, second would be tremendous hinder, I thought. 
 So I gathered birth data of all most famous physicists, chemists, and mathematicians, searched for those aspects, and calculated their dominance.

 Out of 67 scientists, 27 didn’t have any of these two aspects or had both aspects with the same strength. 
 Major aspects – conjunction, square, trine, and opposition were calculated with deviance up to 10 degrees. 
 It is considered that a person has a sextile if deviance is not more than 5 degrees. 
 In a case that a scientist has both aspects, one would be dominant if the deviation was lower by at least 4 degrees to the other aspect. 
 In my study, 40 scientists had some sort of dominance. 28 times this was a dominance of the Mercury-Saturn aspect, and 12 times this was a dominance of the Mercury-Jupiter aspect.
 The probability that the share of the first aspect would be so large (from 28/40 up to 40/40) was 0.0087, lower than 1%. 
 Something like drawing a coin 40 times and winning in 70% cases.
 
 The results were intriguing, so I decided to make a more serious study. I made a code that would check aspects that included 14 celestial bodies, commonly used in astrology. 
 The results were again very interesting. The presence of a Mercury-Saturn aspect was 46.3% concerning a 29.7% natural ratio. 
 The probability for such a ratio or more was about 0.3%. Among 91 possible aspects, this was by far the least probable one. 
 The analysis also revealed some aspects whose ratio was much lower than naturally recorded. 
 Sun-Venus aspect, which is commonly related to artistic inclinations and leisured life, Sun-Mars, connected to combative nature and tendencies for physical expression, 
 and Moon-Neptune, linked with the inability of discerning illusion from reality were ones rarely found in charts of greatest scientists. 
 Respective probabilities for such aspects to be present in calculated ratios or lower were: 0.0067, 0.0083, and 0.0001. 
 Mercury-Jupiter aspect had a moderate ratio with a probability of 0.5231 to happen by chance. 
 As we said, it would give intelligence, but it would be helpful, as much as a hindrance, and very often it would be (if present) outweighed by Mercury-Saturn aspect.
 
 Calculating dominance for Mercury-Saturn and Moon-Neptune aspects one receives a fascinating result. 
 Out of 25 scientists that have one aspect dominant, in 24 cases this was Mercury-Saturn. 
 Imagine drawing a coin 25 times and making head in 24! The only scientist who broke the astrological prediction was Paul Dirac, 
 one of the pioneers in a field of Quantum mechanics. The low number of scientist in this calculation (the total number was 67) was since 
 precise times of birth was often not known. This is usually not a big deal, as planets move fastest 1 degree by day, except for a moon that covers 1 degrees fo just 2 hours. 
 So, in this comparison, which involved Moon, objects with unknown time of birth were ignored.
 
 To make calculations, swiss astrology tables for the period 1400 – 2050 were used. This is how the average aspect ratios were calculated. 
 Data for objects with a time of birth not known are populated with time 12:00 AM to make possible deviations lowest. 
 Each object was given a certain number of categories (fields of science here). Major aspects: conjunction, square, trine, and opposition are tolerated with deviations 
 (orbit is an astrological term) of 8 degrees, except for calculating dominance, where 10-degree fluctuations were accepted. 
 For sextile, corresponding deviations were 4 and 5 degrees.
 
 Along with the complete aspect table and comparison of the dominance of two aspects, there is an option that enables one to allow the program to search for the least probable 
 combinations of aspects for chosen Astro objects. One should be cautious here. First, the number of possible combinations exponentially grows with the number of celestial bodies.
 For 3 Astro objects, there are 20 combinations. 3 different pairs of aspects where each can be present or absent (3x4), 
 and all 3 aspects with 8 present-absent possibilities. The total number of combinations is in a case of three Astro objects 12+8=20. 
 In a case of four planets, the number of combinations is 728, for five planets, the number is 56,252, and for six 14,381,674. 
 Especially in a case of small groups, one in the abundance of low probable combinations would appear. Along with putting pressure on server running time, 
 this was one of the reasons for limiting the number of Astro objects to five in this type of investigation. 
 It has to be taken into account that some aspects are generational and stay there for years or decades. 
 Most of the people included in the study would be ones born in 19. or 20. century, 
 so some more distant planets (Neptune, Uranus, Pluto) aspects would decrease probabilities just by this fact.
 
 
 
