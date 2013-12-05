# @drakeomatic

What is this?

[@drakeomatic](http://twitter.com/drakeomatic) is one of the most common styles of twitter bot: A Markov text generator. [@drakeomatic](http://twitter.com/drakeomatic) analyzes Drake lyrics that were pulled from rapgenius.com and then constructs tweets that are sometimes insightful, sometimes funny, sometimes quotes, and ~~sometimes~~ often complete gibberish.

While the bot is called Drake-o-matic, it is based on the wonderful [markov-text](https://github.com/codebox/markov-text) by [Code Box](http://http://codebox.org.uk) and can learn to construct sentences after studying any body of text. So, have fun! Make your own bot! Just know that I called dibs on a Taylor Swift bot (and a Taylor Swift + Drake bot).

Requirements:
 * [Twitter for Python](https://pypi.python.org/pypi/twitter)

How To Use:
 * Clone this repo and edit the settings in `keys.rb.example`.
 * Assemble a corpus of text and save it in the drakeomatic directory as a plaintext file.
 * Tell the bot to analyze your corpus of data using the following command: `python drakeomatic.py parse <name> <depth> <file>`
 * Setup cron jobs to tweet at regular intervals using the following command: `python drakeomatic.py gen <name> <count>`
 * Remember: NO TAYLOR SWIFT BOTS. Those are mine.

Thanks:
 * To [Rob Dawson](https://github.com/codebox).