# Youmu-Bot-Rewrite
A rewrite of the original Youmu Bot, removing all things that have ties to databases, organizing code better, and using slash commands. 
Also uses pipenv now.

# Commands 
(Not including shorthands for character commands)
```
/c [character] optional: [args] -> Searches for artwork of that character (case insensitive)

/ship [thing1] optional: [thing2] -> tests love compatibility between the 2 things. If [thing2] is omitted, tests love compatibility between your user and thing. 

/char_list -> Sends a dm containing a list of characters that the bot has

/rate [thing] -> Same as last time, but with an optimized prng that isn't process-dependent

/percent [thing] -> Same as last time, but with an optimized prng that isn't process dependent

/ping -> Check ping and get an awesome message

/tag [tags] optional: [args] -> Search for artwork with the given tags and args. Note: you can separate tags with a space, just as you do with gelbooru. 

/inspire -> Gives an (un)inspirational quote using inspirobot's api

/ttt [player] -> Challenge someone to TicTacToe (Naughts and Crosses)

/spellcard -> Creates a random name for a spellcard using a Markov chain
```

# Tags Info:
Use [gelbooru](https://gelbooru.com/) to see available tags

# Args for the art searching commands
You probably noticed the `[args]` part of the `/c`, `/tag`, and aliases for `/c [name]` commands. Args can be stacked together by separating them with a space. 

Here's the list of args so far. Combining mutually exclusive arguments will send an embed saying there is a compatibility issue. 
```
--desc -> Sends a description of the character. Overrides all other tags.

--solo -> Only artworks with the character by themselves allowed. Mutually exclusive with --multi.

--multi -> Only artworks with more than one character, along with the character allowed. Mutually exclusive with --solo. 

--gif -> Only animated artworks are allowed.

--ns -> Only artworks that are not rated safe are allowed (questionable and explicit ones). Mutually exclusive with --q and --e.

--q -> Only artworks that are rated questionable are allowed. Mutally exclusive with --e and --ns

--e -> Only artworks that are rated explicit are allowed. Mutally exclusive with --q and --ns
```
More args will be added in the future.


# Overview of changes from original
- Removed leveling
- Removed bot channels
- Removed prefix database because everything is now slash
- Removed `cut` command because of new focus for the bot (And to make it more likely that no issues would be caused)
- Removed now redundant dependencies
- Add `/ship`
- All commands are slash commands 
- `;char` changed to `/tag` for more clarity
- All art searchin commands can now take
- Added all of the characters that [Tenshi Bot](https://github.com/KawashiroDev/TenshiBot) added by parsing its code
- New method of forming commands that only takes in a tuple of data
- Probably some stuff I'll forget to put here
- Made the documentation less verbose
-
# TODO
- Add more character descriptions
- Add more fun stuff
- Add more args for art searching
- Do more testing
