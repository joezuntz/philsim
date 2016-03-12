# PhilSim

There are many simulation tools used in DESC - OpSim, CatSim, GalSim, PhoSim - but what does the collaboration really need?

The answer: *PhilSim*.

![alt tag](https://raw.githubusercontent.com/joezuntz/philsim/master/phil.png)

Sometimes, Phil is asleep or out of the country.  At those times you can generate a stream of GitHub issues using PhilSim.  PhilSim uses a Markov Chain trained from all the issues Phil has ever opened on GitHub, and can either just print out a suggested issue, or file it directly on a repo of your choice.

Please use this with care.

#Usage

You will need a github API token, which you can generate on your github profile page.

Put this token in token.txt in the philsim directory.

Then you can do:

    python philsim.py  
    # prints out a new issue, like this one:
    What form of output will enable the desired analyses
    ----------------------------------------------------
    This is primarily for the names of the sky.  md files to document other aspects of the 3rd paragraph as well as sky positions.  Let's make a nice little paper for the histograms and for the extra 238 candidates.


Or:

    python philsim.py --repo philsim
    #to open an issue on a specific repo automatically.

