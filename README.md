# Plazma-Burst-2-Randomizer
A value randomizer for Plazma Burst 2

I don't know how to introduce so let's just skip on how to use it instead.

## Randomly Selecting Alive Players
Yes, exactly alive players. You can do this by querying the website link:\
`https://plazma-burst-2-randomizer.herokuapp.com/player?players=1,2,3,4,5,6,7,8,9,10,11,12`\
The query string is a list of `players` that must have the values of the players alive, then the script would simply return a randomly selected number from that list.

## Generate A Random Integer
You can do this by using `https://plazma-burst-2-randomizer.herokuapp.com/randomize?start=1&stop=4`. On default, the `start` value is `0` and `stop` value is `256` if it is not provided. This would then return a random value from `start` to `stop` minus 1. Example values above, the randomized values would only return from `0` to `3`.
